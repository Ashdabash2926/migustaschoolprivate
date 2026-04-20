# Me Gusta Spanish — registration worker

Cloudflare Worker that powers `register.html`:

1. Receives the registration + 5 open-ended answers
2. Grades the test with Claude (CEFR A1–C2 + one-line teacher note)
3. Picks a suggested class + weekly price
4. Emails staff a pre-filled WhatsApp reply
5. Emails the student a confirmation

Runs on the free Cloudflare tier. Expected cost: ~$0.002 per submission (Claude Haiku) + email (Resend free tier covers 3,000/month).

## One-time setup

```bash
cd register-worker
npm install
npx wrangler login
```

### 1. Configure the public settings

Edit `wrangler.toml` `[vars]` — email addresses, WhatsApp number, PayPal username, allowed origin (the site that can POST). No restart needed; vars ship on deploy.

### 2. Add the secrets

```bash
# Your Claude key for now — swap to the school's later.
npx wrangler secret put ANTHROPIC_API_KEY

# Sign up at https://resend.com (free tier 3k emails/mo), verify the sending domain.
npx wrangler secret put RESEND_API_KEY
```

### 3. Deploy

```bash
npm run deploy
```

Note the deployed URL (e.g. `https://migusta-register.YOURNAME.workers.dev`).

### 4. Wire up the frontend

Open `../register.html`, find the CONFIG block near the bottom:

```js
const REGISTER_ENDPOINT = '';  // ← put the worker URL here
```

Commit + push → GitHub Pages serves the updated form. Done.

## Testing locally

```bash
npm run dev
```

Spins up the worker at `http://localhost:8787`. Temporarily point `REGISTER_ENDPOINT` at `http://localhost:8787` in `register.html`, open the page, submit.

## Swapping to the school's Claude key later

```bash
npx wrangler secret put ANTHROPIC_API_KEY  # paste the school's key
```

Zero code change, zero downtime.

## Editing the price table

Open `src/index.js`, edit the `PRICE_TABLE` object at the top. Redeploy with `npm run deploy`.

## Watching live logs

```bash
npm run tail
```

Useful for debugging — you'll see every request + any Claude / Resend errors.
