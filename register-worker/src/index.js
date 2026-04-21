// Me Gusta Spanish — registration + placement test worker.
//
// POST  → { contact info, 5 open-ended answers, class preferences }
// 1. Claude grades the answers → CEFR level + teacher note
// 2. Look up suggested class + weekly price
// 3. Email staff a pre-filled WhatsApp reply
// 4. Email the student a confirmation
// 5. Respond with { ok: true, level }

const PRICE_TABLE = {
  // Weekly prices in USD. Edit to match the school's actual pricing.
  group:   { '1w': 150, '2w': 280, '1m': 520, longer: 520 },
  private: { '1w': 350, '2w': 660, '1m': 1200, longer: 1200 },
  online:  { '1w': 180, '2w': 340, '1m': 620, longer: 620 },
  undecided: { '1w': 150, '2w': 280, '1m': 520, longer: 520 },
};

const LEVEL_COPY = {
  BEGINNER: 'absolute beginner — perfect starting point',
  A1: 'A1 — basic phrases and self-introduction',
  A2: 'A2 — elementary, ready to build on what you know',
  B1: 'B1 — intermediate, working toward real fluency',
  'B2+': 'B2+ — upper-intermediate and above',
};

export default {
  async fetch(request, env) {
    const origin = request.headers.get('origin') || '';
    const cors = corsHeaders(origin, env.ALLOWED_ORIGIN);

    if (request.method === 'OPTIONS') return new Response(null, { headers: cors });
    if (request.method !== 'POST') return json({ error: 'method not allowed' }, 405, cors);

    let payload;
    try { payload = await request.json(); }
    catch { return json({ error: 'invalid json' }, 400, cors); }

    const err = validate(payload);
    if (err) return json({ error: err }, 400, cors);

    try {
      const grade = await gradeWithClaude(payload.answers, env);
      const plan  = suggestPlan(grade.level, payload.classType, payload.duration);

      await Promise.all([
        emailStaff({ payload, grade, plan, env }),
        emailStudent({ payload, grade, plan, env }),
      ]);

      return json({ ok: true, level: grade.level }, 200, cors);
    } catch (e) {
      console.error('register error', e);
      return json({ error: 'server error' }, 500, cors);
    }
  },
};

function corsHeaders(origin, allowed) {
  // Allow the configured origin + any *.pages.dev preview + local dev.
  const ok = origin === allowed
    || /^http:\/\/localhost(:\d+)?$/.test(origin)
    || /\.pages\.dev$/.test(origin)
    || /\.github\.io$/.test(origin);
  return {
    'Access-Control-Allow-Origin': ok ? origin : allowed,
    'Access-Control-Allow-Methods': 'POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '86400',
    Vary: 'Origin',
  };
}

function json(body, status, extraHeaders = {}) {
  return new Response(JSON.stringify(body), {
    status,
    headers: { 'Content-Type': 'application/json', ...extraHeaders },
  });
}

function validate(p) {
  if (!p || typeof p !== 'object') return 'missing body';
  if (!p.firstName || !p.email || !p.whatsapp || !p.country) return 'missing contact fields';
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(p.email)) return 'invalid email';
  if (!p.answers || typeof p.answers !== 'object') return 'missing answers';
  return null;
}

async function gradeWithClaude(answers, env) {
  const a = (k) => (answers[k] || '').trim() || '(blank)';
  const prompt = `You are a Spanish placement examiner for a language school in Sucre, Bolivia.
Assess the student's Spanish level from their free-text answers to a 5-question placement test.

Questions and answers (each question targets a specific level):
1. (beginner) "¿Cómo te llamas y de dónde eres?"
   → ${a('q1')}
2. (A1) "¿Qué haces un día normal? Mañana, tarde y noche."
   → ${a('q2')}
3. (A2) "¿Qué hiciste el fin de semana pasado? ¿Qué te gustó más y por qué?"
   → ${a('q3')}
4. (B1) "Si pudieras vivir un año en otro país, ¿cuál elegirías y cómo cambiaría tu vida?"
   → ${a('q4')}
5. (B2+) "¿Qué ventajas y desventajas tiene el trabajo remoto? Opinión con ejemplos."
   → ${a('q5')}

Rubric — pick the single best-fit level from: BEGINNER, A1, A2, B1, B2+.
Students at upper-intermediate level or above are rare, so bucket everyone at B2 and higher into B2+.
- BEGINNER: can barely handle Q1, writes in English, or leaves most answers blank.
- A1: handles Q1 and parts of Q2. Present tense only, simple vocabulary, frequent errors.
- A2: Q2 clean in present tense. Q3 attempted with basic preterite, some mixed/broken tenses.
- B1: Q3 coherent narrative with preterite/imperfect mostly correct. Q4 attempted with conditional, limited complexity.
- B2+: Q4 handled naturally — conditional + some subjunctive. Q5 gives a clear, well-structured opinion with connectors. Covers B2, C1, and C2 since these are uncommon.
If the student wrote in English, left everything blank, or only wrote "I don't know any Spanish" → return level "BEGINNER".

Return ONLY a JSON object, no prose, in exactly this shape:
{"level":"BEGINNER|A1|A2|B1|B2+","note":"one sentence teacher-facing observation about strengths and gaps"}`;

  const res = await fetch('https://api.anthropic.com/v1/messages', {
    method: 'POST',
    headers: {
      'x-api-key': env.ANTHROPIC_API_KEY,
      'anthropic-version': '2023-06-01',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      model: env.MODEL || 'claude-haiku-4-5-20251001',
      max_tokens: 200,
      messages: [{ role: 'user', content: prompt }],
    }),
  });

  if (!res.ok) {
    const text = await res.text();
    throw new Error(`anthropic ${res.status}: ${text}`);
  }

  const data = await res.json();
  const raw = (data.content?.[0]?.text || '').trim();
  // Claude sometimes wraps JSON in prose or fences; extract the first {...} block.
  const match = raw.match(/\{[\s\S]*\}/);
  if (!match) throw new Error('no json in model response: ' + raw);
  const parsed = JSON.parse(match[0]);
  const level = String(parsed.level || 'BEGINNER').toUpperCase();
  const note  = String(parsed.note || '').slice(0, 400);
  if (!/^(BEGINNER|A1|A2|B1|B2\+)$/.test(level)) throw new Error('bad level: ' + level);
  return { level, note };
}

function suggestPlan(level, classType, duration) {
  const type = PRICE_TABLE[classType] ? classType : 'group';
  const dur  = PRICE_TABLE[type][duration] ? duration : '2w';
  const price = PRICE_TABLE[type][dur];
  return { classType: type, duration: dur, priceUSD: price };
}

async function emailStaff({ payload, grade, plan, env }) {
  const paypalUrl = `https://paypal.me/${env.PAYPAL_USERNAME}/${plan.priceUSD}`;
  const reply = buildStaffReply({ payload, grade, plan, paypalUrl });

  const subject = `New registration · ${payload.firstName} ${payload.lastName || ''} · ${grade.level}`;
  const html = `
    <div style="font-family:system-ui,-apple-system,sans-serif;color:#1C1410;max-width:640px;">
      <h2 style="font-family:Georgia,serif;font-weight:400;color:#C8572D;margin:0 0 6px;">
        New registration · ${escapeHtml(payload.firstName)} ${escapeHtml(payload.lastName || '')}
      </h2>
      <p style="color:#4A3A2C;margin:0 0 18px;">Auto-graded level: <b>${grade.level}</b> — ${escapeHtml(LEVEL_COPY[grade.level] || '')}</p>

      <h3 style="margin:18px 0 6px;">Contact</h3>
      <table cellpadding="4" style="font-size:14px;border-collapse:collapse;">
        <tr><td><b>Email</b></td><td>${escapeHtml(payload.email)}</td></tr>
        <tr><td><b>WhatsApp</b></td><td>${escapeHtml(payload.whatsapp)}</td></tr>
        <tr><td><b>Country</b></td><td>${escapeHtml(payload.country)}</td></tr>
        <tr><td><b>Age</b></td><td>${escapeHtml(payload.age || '—')}</td></tr>
        <tr><td><b>Language</b></td><td>${escapeHtml(payload.language || 'en')}</td></tr>
      </table>

      <h3 style="margin:18px 0 6px;">Plan requested</h3>
      <table cellpadding="4" style="font-size:14px;border-collapse:collapse;">
        <tr><td><b>Class type</b></td><td>${escapeHtml(plan.classType)}</td></tr>
        <tr><td><b>Duration</b></td><td>${escapeHtml(plan.duration)}</td></tr>
        <tr><td><b>Accommodation</b></td><td>${escapeHtml(payload.accommodation || '—')}</td></tr>
        <tr><td><b>Start date</b></td><td>${escapeHtml(payload.startDate || '—')}</td></tr>
        <tr><td><b>Suggested price</b></td><td><b>$${plan.priceUSD} USD</b> (edit before sending)</td></tr>
      </table>

      <h3 style="margin:18px 0 6px;">Teacher note</h3>
      <p style="background:#FAF3E4;border-left:3px solid #C4913A;padding:10px 14px;margin:0 0 18px;font-style:italic;">
        ${escapeHtml(grade.note)}
      </p>

      <h3 style="margin:18px 0 6px;">Student's answers</h3>
      ${renderAnswers(payload.answers)}

      ${payload.notes ? `<h3 style="margin:18px 0 6px;">Notes from student</h3><p style="white-space:pre-wrap;">${escapeHtml(payload.notes)}</p>` : ''}

      <h3 style="margin:22px 0 6px;">Reply template — copy, edit, send</h3>
      <div style="background:#FFF9F4;border:1px dashed #C8572D;border-radius:10px;padding:14px 16px;font-family:system-ui;font-size:14px;white-space:pre-wrap;line-height:1.5;">${escapeHtml(reply)}</div>
      <p style="margin-top:8px;"><a href="https://wa.me/${onlyDigits(payload.whatsapp)}" style="display:inline-block;background:#25D366;color:#fff;text-decoration:none;padding:8px 14px;border-radius:50px;font-weight:600;">Open WhatsApp chat →</a></p>
    </div>
  `;

  return sendEmail({
    env,
    to: env.STAFF_EMAIL,
    replyTo: payload.email,
    subject,
    html,
  });
}

function buildStaffReply({ payload, grade, plan, paypalUrl }) {
  const name = payload.firstName;
  const levelCopy = LEVEL_COPY[grade.level] || '';
  const classLabel = {
    group: 'group class (Mon–Fri mornings)',
    private: 'private one-on-one (flexible hours)',
    online: 'online class',
    undecided: 'group class (Mon–Fri mornings) — happy to switch if you prefer private',
  }[plan.classType];
  const durLabel = {
    '1w': 'one week', '2w': 'two weeks', '1m': 'one month', longer: 'an extended stay',
  }[plan.duration];

  return `Hi ${name}! Thanks for registering with Me Gusta Spanish — we've had a look at your placement test.

Based on your answers we'd place you at ${grade.level} (${levelCopy}).

For a ${classLabel} over ${durLabel}, the price is $${plan.priceUSD} USD.

To confirm your spot: ${paypalUrl}

Reply here with any questions, or let us know your preferred start date. ¡Nos vemos pronto!
— The Me Gusta Spanish team`;
}

const STUDENT_COPY = {
  en: {
    subject: "We've got your Me Gusta Spanish registration",
    greeting: "Gracias",
    lead: "We've received your placement test and all your details. A teacher will look through your answers and message you on WhatsApp within 24 hours with your class, schedule and price.",
    levelLabel: "Your provisional level:",
    levelNote: "This is our first read — your teacher will confirm the level on day one. No payment needed yet; we'll send a secure link when you're ready.",
    whatsappPrompt: "Any questions in the meantime? WhatsApp us directly:",
    sign: "— Me Gusta Spanish, Sucre, Bolivia",
    reminderSubject: "See you tomorrow at Me Gusta Spanish!",
    reminderHeader: "¡Nos vemos mañana!",
    reminderLead: "A friendly reminder — you told us you'd like to start your Spanish classes tomorrow. Here's what to expect on day one:",
    reminderPoints: [
      "Arrive about 10 minutes early — your teacher will meet you and show you around.",
      "Check your WhatsApp if you haven't — we sent the address and exact time there.",
      "Bring a notebook and pen, and maybe a snack for the break.",
      "Don't worry about your level — day one is all about getting comfortable.",
    ],
    reminderOutro: "If anything changed on your side, just reply here or send us a WhatsApp. ¡Hasta mañana!",
  },
  es: {
    subject: "Recibimos tu registro — Me Gusta Spanish",
    greeting: "Gracias",
    lead: "Ya tenemos tu prueba de nivel y todos tus datos. Un profesor revisará tus respuestas y te escribirá por WhatsApp en menos de 24 horas con tu clase, horario y precio.",
    levelLabel: "Tu nivel provisional:",
    levelNote: "Esto es solo una primera lectura — tu profesor confirmará el nivel el primer día. No hace falta pagar todavía; te enviaremos un enlace seguro cuando estés listo.",
    whatsappPrompt: "¿Tienes alguna duda mientras tanto? Escríbenos por WhatsApp:",
    sign: "— Me Gusta Spanish, Sucre, Bolivia",
    reminderSubject: "¡Nos vemos mañana en Me Gusta Spanish!",
    reminderHeader: "¡Nos vemos mañana!",
    reminderLead: "Un recordatorio amistoso — nos dijiste que querías empezar tus clases mañana. Esto es lo que puedes esperar el primer día:",
    reminderPoints: [
      "Llega unos 10 minutos antes — tu profesor te recibirá y te mostrará la escuela.",
      "Si aún no lo has hecho, revisa tu WhatsApp — te enviamos la dirección y la hora exacta.",
      "Trae un cuaderno y un bolígrafo, y quizás un snack para el descanso.",
      "No te preocupes por tu nivel — el primer día es para sentirte cómodo.",
    ],
    reminderOutro: "Si algo cambió por tu parte, responde aquí o escríbenos por WhatsApp. ¡Hasta mañana!",
  },
  fr: {
    subject: "Nous avons reçu votre inscription — Me Gusta Spanish",
    greeting: "¡Gracias",
    lead: "Nous avons reçu votre test de niveau et toutes vos informations. Un professeur examinera vos réponses et vous écrira sur WhatsApp sous 24 heures avec votre cours, votre horaire et le prix.",
    levelLabel: "Votre niveau provisoire :",
    levelNote: "Ce n'est qu'une première lecture — votre professeur confirmera le niveau le premier jour. Aucun paiement n'est requis pour l'instant ; nous vous enverrons un lien sécurisé lorsque vous serez prêt.",
    whatsappPrompt: "Des questions entre-temps ? Écrivez-nous sur WhatsApp :",
    sign: "— Me Gusta Spanish, Sucre, Bolivie",
    reminderSubject: "¡Nos vemos mañana ! Votre premier cours à Me Gusta Spanish",
    reminderHeader: "À demain !",
    reminderLead: "Un petit rappel amical — vous nous avez dit que vous souhaitiez commencer vos cours demain. Voici à quoi vous attendre le premier jour :",
    reminderPoints: [
      "Arrivez une dizaine de minutes en avance — votre professeur vous accueillera et vous fera visiter.",
      "Si ce n'est pas déjà fait, vérifiez votre WhatsApp — nous y avons envoyé l'adresse et l'heure exacte.",
      "Apportez un carnet et un stylo, et peut-être un en-cas pour la pause.",
      "Ne vous inquiétez pas pour votre niveau — le premier jour sert à prendre vos marques.",
    ],
    reminderOutro: "Si quelque chose a changé de votre côté, répondez ici ou écrivez-nous sur WhatsApp. À demain !",
  },
};

async function emailStudent({ payload, grade, plan, env }) {
  const copy = STUDENT_COPY[payload.language] || STUDENT_COPY.en;
  const waUrl = `https://wa.me/${escapeHtml(env.SCHOOL_WHATSAPP)}`;
  const html = `
    <div style="font-family:Georgia,serif;color:#1C1410;max-width:560px;line-height:1.7;">
      <p style="font-size:18px;font-style:italic;color:#C8572D;margin:0 0 12px;">${copy.greeting}, ${escapeHtml(payload.firstName)}!</p>
      <p>${copy.lead}</p>
      <p style="margin-top:20px;padding:14px 18px;background:#FFF9F4;border-left:3px solid #C4913A;">
        <b>${copy.levelLabel}</b> ${grade.level}<br>
        <span style="font-style:italic;color:#4A3A2C;">${escapeHtml(LEVEL_COPY[grade.level] || '')}</span>
      </p>
      <p>${copy.levelNote}</p>
      <p style="margin-top:24px;">${copy.whatsappPrompt} <a href="${waUrl}">+${escapeHtml(env.SCHOOL_WHATSAPP)}</a></p>
      <p style="margin-top:24px;color:#9A8878;font-size:14px;">${copy.sign}</p>
    </div>
  `;
  await sendEmail({ env, to: payload.email, subject: copy.subject, html });

  // Schedule a T-24h pre-class reminder if they told us a start date at least ~36h away.
  const reminderIso = payload.startDate ? buildReminderIso(payload.startDate) : null;
  if (reminderIso && Date.parse(reminderIso) > Date.now() + 12 * 60 * 60 * 1000) {
    const points = copy.reminderPoints.map(p => `<li style="margin-bottom:6px;">${p}</li>`).join('');
    const reminderHtml = `
      <div style="font-family:Georgia,serif;color:#1C1410;max-width:560px;line-height:1.7;">
        <p style="font-size:20px;font-style:italic;color:#C8572D;margin:0 0 12px;">${copy.reminderHeader}</p>
        <p>${copy.reminderLead}</p>
        <ul style="padding-left:20px;margin:12px 0 18px;">${points}</ul>
        <p>${copy.reminderOutro} <a href="${waUrl}">+${escapeHtml(env.SCHOOL_WHATSAPP)}</a></p>
        <p style="margin-top:24px;color:#9A8878;font-size:14px;">${copy.sign}</p>
      </div>
    `;
    await sendEmail({
      env,
      to: payload.email,
      subject: copy.reminderSubject,
      html: reminderHtml,
      scheduledAt: reminderIso,
    });
  }
}

// Resend's scheduled_at takes an ISO 8601 timestamp. We fire the reminder
// 24h before the student's preferred start date, at 08:30 Bolivia time
// (UTC-4) — i.e. 12:30 UTC the previous day.
function buildReminderIso(startDateString) {
  const [y, m, d] = String(startDateString).split('-').map(Number);
  if (!y || !m || !d) return null;
  const startUtc = Date.UTC(y, m - 1, d, 12, 30, 0); // 08:30 Bolivia time
  const reminderUtc = startUtc - 24 * 60 * 60 * 1000;
  return new Date(reminderUtc).toISOString();
}

async function sendEmail({ env, to, subject, html, replyTo, scheduledAt }) {
  const body = {
    from: `${env.FROM_NAME} <${env.FROM_EMAIL}>`,
    to: [to],
    subject,
    html,
  };
  if (replyTo) body.reply_to = replyTo;
  if (scheduledAt) body.scheduled_at = scheduledAt;

  const res = await fetch('https://api.resend.com/emails', {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${env.RESEND_API_KEY}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(body),
  });
  if (!res.ok) {
    const text = await res.text();
    console.error(`resend ${res.status}: ${text}`);
    // Don't throw — we still want to return success to the student if grading worked.
  }
}

function renderAnswers(a = {}) {
  const prompts = {
    q1: '¿Cómo te llamas y de dónde eres?',
    q2: '¿Qué haces un día normal? Mañana, tarde y noche.',
    q3: '¿Qué hiciste el fin de semana pasado? ¿Qué te gustó más y por qué?',
    q4: 'Si pudieras vivir un año en otro país, ¿cuál elegirías y cómo cambiaría tu vida?',
    q5: '¿Qué ventajas y desventajas tiene el trabajo remoto? Opinión con ejemplos.',
  };
  return Object.keys(prompts).map(k => `
    <div style="margin-bottom:12px;">
      <div style="font-size:12px;color:#9A8878;text-transform:uppercase;letter-spacing:0.08em;">${k.toUpperCase()}</div>
      <div style="font-style:italic;color:#4A3A2C;font-size:13px;margin-bottom:3px;">${prompts[k]}</div>
      <div style="white-space:pre-wrap;">${escapeHtml(a[k] || '—')}</div>
    </div>
  `).join('');
}

function escapeHtml(s) {
  return String(s == null ? '' : s)
    .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;').replace(/'/g, '&#39;');
}

function onlyDigits(s) { return String(s || '').replace(/\D/g, ''); }
