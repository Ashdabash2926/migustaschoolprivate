#!/usr/bin/env python3
"""Add data-fr attributes to all translatable elements across all pages."""
import re, os, html

BASE = '/Users/ash/Projects/migusta'
PAGES = ['index.html', 'classes.html', 'methodology.html', 'teachers.html',
         'activities.html', 'cafe.html', 'about.html', 'accommodation.html',
         'faqs.html', 'blog.html', 'contact.html']

# ── Comprehensive EN → FR dictionary ──
FR = {
    # Nav
    'Classes': 'Cours',
    'Teachers': 'Professeurs',
    'Activities': 'Activités',
    'About': 'À propos',
    'Contact': 'Contact',
    'More': 'Plus',
    'Home': 'Accueil',
    'Methodology': 'Méthodologie',
    'Accommodation': 'Hébergement',
    'FAQs': 'FAQ',
    'Blog': 'Blog',
    'Register Now': "S'inscrire",
    'Café': 'Café',
    'About Us': 'À propos de nous',

    # Common
    'Learn': 'Apprendre',
    'Discover': 'Découvrir',
    'Find Us': 'Nous trouver',
    'Contact': 'Contact',
    'Sucre, Bolivia 🇧🇴': 'Sucre, Bolivie 🇧🇴',
    '© 2025 Me Gusta Spanish. All rights reserved.': '© 2025 Me Gusta Spanish. Tous droits réservés.',
    'A Spanish school with heart, based in the heart of South America. Come for the language. Stay for Bolivia.': "Une école d'espagnol avec du cœur, au cœur de l'Amérique du Sud. Venez pour la langue. Restez pour la Bolivie.",

    # Index page
    'Learn Spanish in <em>Sucre, Bolivia</em>': "Apprenez l'espagnol à <em>Sucre, Bolivie</em>",
    ' in sucre, bolivia': ' à sucre, bolivie',
    'Small classes. Real conversations. A city that feels like home.': 'Petits groupes. Vraies conversations. Une ville qui ressemble à chez soi.',
    'Start your journey →': 'Commencez votre aventure →',
    'See our classes': 'Voir nos cours',
    'Face to face, online, or both — find the class that fits.': 'En présentiel, en ligne, ou les deux — trouvez le cours qui vous convient.',
    'Explore classes →': 'Découvrir les cours →',
    'our classes': 'nos cours',
    'meet the team': 'rencontrez l\'équipe',
    'Meet the <em>Teachers</em>': 'Rencontrez les <em>professeurs</em>',
    'Seven passionate teachers who live and breathe this city. Each one trained personally by our founders.': "Sept professeurs passionnés qui vivent et respirent cette ville. Chacun formé personnellement par nos fondateurs.",
    'Meet our teachers →': 'Rencontrez nos professeurs →',
    'what our students say': 'ce que disent nos étudiants',
    'Real <em>stories</em>': 'Vraies <em>histoires</em>',
    'latest post': 'dernier article',
    'from our blog': 'de notre blog',
    'Read the blog →': 'Lire le blog →',
    'read more': 'lire la suite',
    'have a question?': 'une question ?',
    'We reply to every message — usually the same day.': 'Nous répondons à chaque message — généralement le jour même.',
    'Get in touch →': 'Contactez-nous →',
    'Get in <em>touch</em>': 'Prenez <em>contact</em>',
    'our story': 'notre histoire',
    'our café': 'notre café',
    'Visit <em>Me Gusta Café</em>': 'Visitez <em>Me Gusta Café</em>',
    'Open to everyone — students and non-students alike. Specialty Bolivian coffee, fresh pastries, and a courtyard that makes you forget about time.': "Ouvert à tous — étudiants et non-étudiants. Café bolivien de spécialité, pâtisseries fraîches, et une cour qui fait oublier le temps.",
    'See the café →': 'Voir le café →',
    'Ready to <em>begin?</em>': 'Prêt à <em>commencer ?</em>',
    'Join hundreds of students who chose Sucre. Classes start every Monday.': "Rejoignez des centaines d'étudiants qui ont choisi Sucre. Les cours commencent chaque lundi.",
    'Register now →': "S'inscrire maintenant →",
    'Browse classes first →': "Voir les cours d'abord →",
    '756 students &amp; counting': '756 étudiants &amp; plus',
    '17 years of learning what works': "17 ans d'apprentissage de ce qui fonctionne",
    ' learn from anywhere': ' apprenez de partout',
    'Online classes available': 'Cours en ligne disponibles',

    # Classes page
    'find your level': 'trouvez votre niveau',
    'Classes built around <em>you</em>': 'Des cours conçus pour <em>vous</em>',
    'Every student is different. We build your programme around your level, your goals, and how you actually learn — not a one-size-fits-all textbook.': "Chaque étudiant est différent. Nous construisons votre programme autour de votre niveau, vos objectifs, et votre façon d'apprendre — pas un manuel universel.",
    'our programmes': 'nos programmes',
    'Choose your <em>programme</em>': 'Choisissez votre <em>programme</em>',
    'Face-to-Face Classes': 'Cours en présentiel',
    'Online Classes': 'Cours en ligne',
    'Intensive Programme': 'Programme intensif',
    'DELE Exam Prep': 'Préparation DELE',
    'Group Classes': 'Cours en groupe',
    'Private Tutoring': 'Cours particuliers',
    'face to face': 'en présentiel',
    'online': 'en ligne',
    'intensive': 'intensif',
    'exam prep': 'préparation examen',
    'group': 'groupe',
    'private': 'privé',
    'per hour': 'par heure',
    'per week': 'par semaine',
    'Most popular': 'Le plus populaire',
    'Register →': "S'inscrire →",
    'from': 'à partir de',
    'All levels': 'Tous niveaux',
    'Beginner friendly': 'Adapté aux débutants',
    'Flexible schedule': 'Horaires flexibles',
    'how it works': 'comment ça marche',
    'How it <em>works</em>': 'Comment ça <em>marche</em>',
    'Start here →': 'Commencez ici →',
    'pricing': 'tarifs',
    'Simple, transparent <em>pricing</em>': 'Tarifs simples et <em>transparents</em>',
    'No hidden fees. No contracts. Pay weekly or monthly.': "Pas de frais cachés. Pas de contrats. Payez à la semaine ou au mois.",
    'Book a free trial': 'Réserver un essai gratuit',
    'Ready to start <em>learning?</em>': 'Prêt à commencer à <em>apprendre ?</em>',

    # Teachers page
    'the team': "l'équipe",
    'Meet Our <em>Teachers</em>': 'Rencontrez nos <em>professeurs</em>',
    'Seven teachers who love what they do. Each one handpicked and trained by Elizabeth — because the right teacher changes everything.': "Sept professeurs passionnés par leur métier. Chacun sélectionné et formé par Elizabeth — parce que le bon professeur change tout.",
    'Face to Face &amp; Online': 'Présentiel &amp; en ligne',
    'Face to Face': 'En présentiel',
    'Online Specialist': 'Spécialiste en ligne',
    'Beginners': 'Débutants',
    'Conversation': 'Conversation',
    'Intermediate': 'Intermédiaire',
    'Culture &amp; History': 'Culture &amp; histoire',
    'All levels': 'Tous niveaux',
    'Exam Prep': 'Préparation examen',
    'Pronunciation': 'Prononciation',
    'Grammar': 'Grammaire',
    'Advanced': 'Avancé',
    'Travel Spanish': 'Espagnol voyage',
    'The <em>founders</em> still teach': 'Les <em>fondateurs</em> enseignent encore',
    'Co-founder &amp; Academic Director': 'Co-fondatrice &amp; directrice académique',
    'Co-founder &amp; School Director': 'Co-fondateur &amp; directeur de l\'école',
    "Abbie brings warmth and patience to every session. Known for putting nervous beginners at ease, her classes are lively, structured, and full of real conversation from day one. Students describe her as the teacher who made them finally believe they could do this.": "Abbie apporte chaleur et patience à chaque session. Connue pour mettre à l'aise les débutants nerveux, ses cours sont vivants, structurés et pleins de vraie conversation dès le premier jour.",
    "Angel weaves Bolivian culture and history into every lesson — his students leave not just knowing the language but understanding the world it belongs to. He's the kind of teacher who makes you want to keep learning long after the class is over.": "Angel intègre la culture et l'histoire boliviennes dans chaque leçon — ses étudiants repartent non seulement en connaissant la langue, mais en comprenant le monde auquel elle appartient.",
    "Anna is Me Gusta's online specialist — her virtual sessions are packed with interactive activities and real-world tasks. She also runs the school's DELE exam preparation programme and has helped dozens of students pass with flying colours.": "Anna est la spécialiste en ligne de Me Gusta — ses sessions virtuelles regorgent d'activités interactives. Elle dirige aussi le programme de préparation au DELE et a aidé des dizaines d'étudiants à réussir haut la main.",
    "Belén has a gift for pronunciation — she helps students move past the self-conscious stumbling that holds so many back and find a rhythm that feels natural. Her calm, encouraging manner makes even the most nervous learner feel completely at ease.": "Belén a un don pour la prononciation — elle aide les étudiants à dépasser les hésitations et à trouver un rythme naturel. Sa manière calme et encourageante met même les plus nerveux parfaitement à l'aise.",
    "Claudia is the team's grammar specialist — not in the dry, textbook sense, but through storytelling and real conversation. She makes even the subjunctive feel logical. Her advanced students consistently say her classes were the point where Spanish finally clicked.": "Claudia est la spécialiste en grammaire de l'équipe — pas de manière sèche, mais à travers la narration et la vraie conversation. Elle rend même le subjonctif logique. Ses étudiants avancés disent que ses cours sont le moment où l'espagnol a enfin fait clic.",
    "Erik understands exactly what it feels like to learn a language as an adult — and that empathy is the foundation of every class he teaches. His sessions are practical, immersive, and built around real situations, making him a favourite with travellers.": "Erik comprend exactement ce que c'est d'apprendre une langue à l'âge adulte — et cette empathie est la base de chaque cours. Ses sessions sont pratiques, immersives, et construites autour de situations réelles.",
    'Elizabeth teaches advanced conversation and writing classes. Her sessions focus on fluency, nuance, and helping students move from functional Spanish to something that feels truly natural.': "Elizabeth enseigne des cours avancés de conversation et d'écriture. Ses sessions se concentrent sur la fluidité et aident les étudiants à passer d'un espagnol fonctionnel à quelque chose de vraiment naturel.",
    "Fernando covers classes across all levels and is especially popular with travellers on short intensive stays. His deep knowledge of Bolivian culture brings an authenticity to lessons that students find hard to find elsewhere.": "Fernando assure des cours à tous les niveaux et est particulièrement apprécié des voyageurs en séjour intensif. Sa connaissance profonde de la culture bolivienne apporte une authenticité difficile à trouver ailleurs.",
    "Elizabeth and Fernando don't just run the school — they still teach, every week. It's important to them that they stay close to the classroom, know every student by name, and keep refining what they do.": "Elizabeth et Fernando ne dirigent pas seulement l'école — ils enseignent encore, chaque semaine. Il leur tient à cœur de rester proches de la salle de classe et de connaître chaque étudiant par son nom.",

    # Activities page
    'life beyond the classroom': 'la vie au-delà de la salle de classe',
    'Learn Spanish.<br><em>Live Bolivia.</em>': "Apprenez l'espagnol.<br><em>Vivez la Bolivie.</em>",
    'The best way to learn a language is to live it. Our activities immerse you in Bolivian culture, food, music, and conversation — all in Spanish, all with your teachers by your side.': "La meilleure façon d'apprendre une langue est de la vivre. Nos activités vous immergent dans la culture, la cuisine, la musique et la conversation boliviennes — tout en espagnol.",
    'Bolivian Cooking Class': 'Cours de cuisine bolivienne',
    'Market Morning': 'Matinée au marché',
    'Sucre City Walk': 'Visite de Sucre',
    'Salsa &amp; Cumbia Night': 'Soirée Salsa &amp; Cumbia',
    'Cinema &amp; Conversation': 'Cinéma &amp; Conversation',
    'Conversation Evening': 'Soirée conversation',
    'Tarabuco Day Trip': 'Excursion à Tarabuco',
    'Photography Walk': 'Promenade photo',
    'Every 2 weeks': 'Toutes les 2 semaines',
    'Weekly': 'Hebdomadaire',
    'Monthly': 'Mensuel',
    'Seasonal': 'Saisonnier',
    '2 hours': '2 heures',
    '2–3 hours': '2–3 heures',
    '3 hours': '3 heures',
    'Full day': 'Journée entière',
    'Included': 'Inclus',
    'Free': 'Gratuit',
    'how activities work': 'comment fonctionnent les activités',
    'Step': 'Étape',
    'good to know': 'bon à savoir',
    'All activities are conducted entirely in Spanish — but don\'t worry, your teachers adapt to your level. Beginners are always welcome. Activities are included with your course or available separately.': "Toutes les activités se déroulent entièrement en espagnol — mais ne vous inquiétez pas, vos professeurs s'adaptent à votre niveau. Les débutants sont toujours les bienvenus.",
    'ready to experience Bolivia?': 'prêt à découvrir la Bolivie ?',
    'Your adventure starts with a <em>conversation</em>': 'Votre aventure commence par une <em>conversation</em>',
    'Chat with us →': 'Contactez-nous →',

    # Café page
    'our café': 'notre café',
    ' fresh': ' frais',
    'Café': 'Café',

    # About page
    'our story': 'notre histoire',
    'A school born from <em>passion</em>': 'Une école née de la <em>passion</em>',
    "We're Elizabeth and Fernando — a Bolivian couple who fell in love with languages, with Sucre, and with the idea that anyone can learn to speak Spanish. Me Gusta is our home, and we'd love it to become yours too.": "Nous sommes Elizabeth et Fernando — un couple bolivien passionné par les langues, par Sucre, et par l'idée que tout le monde peut apprendre l'espagnol. Me Gusta est notre maison, et nous aimerions qu'elle devienne la vôtre aussi.",
    'Meet us in Sucre →': 'Rencontrez-nous à Sucre →',
    'Elizabeth &amp; Fernando, Sucre 2011 ✨': 'Elizabeth &amp; Fernando, Sucre 2011 ✨',
    'the people behind the school': "les personnes derrière l'école",
    'Meet the <em>Founders</em>': 'Rencontrez les <em>fondateurs</em>',
    "Me Gusta Spanish was built on a simple belief: that learning a language should feel personal, joyful, and deeply human. Elizabeth and Fernando are both from Sucre, and their deep love for their city, its culture, and its beautifully clear Spanish shines through in every part of the school.": "Me Gusta Spanish est fondé sur une conviction simple : apprendre une langue doit être personnel, joyeux et profondément humain. Elizabeth et Fernando sont tous deux de Sucre, et leur amour profond pour leur ville transparaît dans chaque aspect de l'école.",
    'Elizabeth, Co-founder ✨': 'Elizabeth, co-fondatrice ✨',
    'Fernando, Co-founder ✨': 'Fernando, co-fondateur ✨',
    "Elizabeth grew up in Sucre and discovered her passion for teaching languages while studying at university. Her natural gift for connecting with people from all over the world, combined with her deep knowledge of Bolivian culture, makes her the heart of Me Gusta's academic programme.": "Elizabeth a grandi à Sucre et a découvert sa passion pour l'enseignement des langues à l'université. Son don naturel pour connecter avec des personnes du monde entier fait d'elle le cœur du programme académique de Me Gusta.",
    "As Academic Director, she designs the curriculum, trains every teacher personally, and ensures that every student leaves having genuinely improved. She believes the most powerful thing a teacher can do is make you feel capable — and that conviction shapes everything about how Me Gusta teaches.": "En tant que directrice académique, elle conçoit le programme, forme chaque professeur personnellement, et s'assure que chaque étudiant progresse vraiment.",
    "Fernando was born and raised in Sucre, and has spent his entire adult life sharing his city — and its language — with the world. He studied linguistics in Buenos Aires before returning home with a clear mission: to show foreigners that Bolivian Spanish, spoken clearly and purely here in Sucre, is the very best in Latin America to learn.": "Fernando est né et a grandi à Sucre, et a passé toute sa vie adulte à partager sa ville — et sa langue — avec le monde. Il a étudié la linguistique à Buenos Aires avant de rentrer avec une mission claire : montrer que l'espagnol bolivien de Sucre est le meilleur d'Amérique latine.",
    "As School Director, Fernando runs the day-to-day life of Me Gusta with warmth, humour, and an infectious energy that makes the school feel like a second home from day one. He's the reason students come back year after year.": "En tant que directeur de l'école, Fernando gère le quotidien de Me Gusta avec chaleur, humour et une énergie contagieuse qui fait de l'école un second foyer dès le premier jour.",
    'how we got here': 'comment nous en sommes arrivés là',
    'Our <em>story</em>': 'Notre <em>histoire</em>',
    'what drives us': 'ce qui nous anime',
    'Our <em>values</em>': 'Nos <em>valeurs</em>',
    "We're not a factory. Every student is treated as an individual, every teacher is trained by us personally, and every decision comes back to one question: does this help our students learn?": "Nous ne sommes pas une usine. Chaque étudiant est traité individuellement, chaque professeur est formé par nous, et chaque décision revient à une question : cela aide-t-il nos étudiants à apprendre ?",
    'People first': "Les personnes d'abord",
    'Continuous improvement': 'Amélioration continue',
    'Honest progress': 'Progrès honnête',
    'Immersion in everything': 'Immersion en tout',
    'Warmth &amp; welcome': 'Chaleur &amp; accueil',
    'Love of Bolivia': 'Amour de la Bolivie',
    "Languages exist to connect people. We never lose sight of that. Our classes are conversations, not lectures — warm, relaxed, and completely focused on you.": "Les langues existent pour connecter les gens. Nous ne l'oublions jamais. Nos cours sont des conversations, pas des conférences — chaleureux, détendus et entièrement centrés sur vous.",
    "We never stop refining how we teach. Elizabeth reviews every teacher's performance regularly, attends classes, and updates the curriculum as the language — and our students' needs — evolve.": "Nous ne cessons jamais de perfectionner notre enseignement. Elizabeth évalue régulièrement chaque professeur et met à jour le programme selon l'évolution des besoins.",
    "We'll tell you the truth about where you are and what you need to do to improve. We'd rather give you honest feedback than make you feel good for a week and see no change.": "Nous vous dirons la vérité sur votre niveau et ce que vous devez faire pour progresser. Nous préférons des retours honnêtes plutôt que de vous faire plaisir sans résultat.",
    "Class is just the beginning. We recommend host families, organise activities, and encourage you to get out into Sucre. The whole city is your classroom.": "Le cours n'est que le début. Nous recommandons des familles d'accueil, organisons des activités et vous encourageons à explorer Sucre. Toute la ville est votre salle de classe.",
    "Moving to a new country, even for a few weeks, can be daunting. From the moment you arrive, we want you to feel like you belong here. Fernando's door is always open.": "S'installer dans un nouveau pays, même pour quelques semaines, peut être intimidant. Dès votre arrivée, nous voulons que vous vous sentiez chez vous. La porte de Fernando est toujours ouverte.",
    "We're proud to be based in Sucre. Bolivia doesn't get the attention it deserves — its culture, history, food, and people are extraordinary. Part of our mission is to share that with the world.": "Nous sommes fiers d'être à Sucre. La Bolivie ne reçoit pas l'attention qu'elle mérite — sa culture, son histoire, sa cuisine et ses gens sont extraordinaires. Notre mission est de partager cela avec le monde.",
    'from us, to you ✨': 'de nous, à vous ✨',
    'Welcome to our family — and welcome to our school.': 'Bienvenue dans notre famille — et bienvenue dans notre école.',
    "Whether you've just started thinking about learning Spanish or you've been at it for years, there's a place for you here. Come and find us in Sucre — we'll put the kettle on.": "Que vous commenciez tout juste à penser à apprendre l'espagnol ou que vous le fassiez depuis des années, il y a une place pour vous ici. Venez nous trouver à Sucre.",
    'Elizabeth &amp; Fernando meet': 'Elizabeth &amp; Fernando se rencontrent',
    "Both born and raised in Sucre, Elizabeth and Fernando meet through a shared love of languages. They begin dreaming of a school that could share their city — and its beautifully clear Spanish — with the world.": "Tous deux nés et élevés à Sucre, Elizabeth et Fernando se rencontrent grâce à leur amour commun des langues. Ils commencent à rêver d'une école qui partagerait leur ville avec le monde.",
    'The methodology is born': 'La méthodologie naît',
    "Teaching friends and travellers from their living room, Elizabeth and Fernando begin developing what will become the Me Gusta method — practical, conversation-first, and built around real situations.": "En enseignant à des amis et voyageurs depuis leur salon, Elizabeth et Fernando développent ce qui deviendra la méthode Me Gusta — pratique, conversationnelle, basée sur des situations réelles.",
    'Me Gusta Spanish opens': 'Me Gusta Spanish ouvre ses portes',
    "The school opens its doors in the historic centre of Sucre with four teachers, a handful of classrooms, and an enormous amount of heart. In the first year alone, students from 28 countries pass through.": "L'école ouvre ses portes dans le centre historique de Sucre avec quatre professeurs et une quantité énorme de cœur. Dès la première année, des étudiants de 28 pays y passent.",
    'Me Gusta Café opens': 'Me Gusta Café ouvre',
    'Online classes launch': 'Lancement des cours en ligne',
    'Today': "Aujourd'hui",

    # Contact page
    "we'd love to hear from you": 'nous aimerions avoir de vos nouvelles',
    "Whether you have a question, want to book a class, or just want to say hola — we're here. We reply to every single message.": "Que vous ayez une question, vouliez réserver un cours, ou simplement dire hola — nous sommes là. Nous répondons à chaque message.",
    'WhatsApp': 'WhatsApp',
    'Email': 'Email',
    'Landline': 'Téléphone fixe',
    'send us a message': 'envoyez-nous un message',
    'Tell us about <em>yourself</em>': 'Parlez-nous de <em>vous</em>',
    'Fill in the details below and we\'ll get back to you personally.': 'Remplissez les informations ci-dessous et nous vous répondrons personnellement.',
    'First name': 'Prénom',
    'Last name': 'Nom',
    'Email address': 'Adresse email',
    "I'm interested in...": 'Je suis intéressé(e) par...',
    'Face-to-face classes': 'Cours en présentiel',
    'Both': 'Les deux',
    'Just asking a question': 'Juste une question',
    'My level': 'Mon niveau',
    'Complete beginner': 'Débutant complet',
    'Elementary (A1–A2)': 'Élémentaire (A1–A2)',
    'Intermediate (B1–B2)': 'Intermédiaire (B1–B2)',
    'Advanced (C1–C2)': 'Avancé (C1–C2)',
    'Your message': 'Votre message',
    'Send message →': 'Envoyer le message →',
    'We reply within 24 hours, usually much sooner.': 'Nous répondons sous 24 heures, généralement bien plus vite.',
    'find us': 'nous trouver',
    'Visit our <em>school</em>': 'Visitez notre <em>école</em>',
    'Address': 'Adresse',
    'Open hours': 'Horaires',
    'Monday – Friday, 9am – 6pm': 'Lundi – Vendredi, 9h – 18h',
    'Me Gusta Café': 'Me Gusta Café',
    'Open to everyone — come say hola': 'Ouvert à tous — venez dire hola',
    'Open in Maps': 'Ouvrir dans Maps',
    'ready to start?': 'prêt à commencer ?',
    'Your Spanish adventure <em>begins here</em>': "Votre aventure en espagnol <em>commence ici</em>",
    'Chat on WhatsApp': 'Discuter sur WhatsApp',
    'Dirección': 'Adresse',

    # Methodology page
    'our approach': 'notre approche',
    'The <em>Me Gusta</em> Method': 'La méthode <em>Me Gusta</em>',
    'methodology': 'méthodologie',

    # Accommodation page
    ' budget-friendly': ' économique',
    ' most comfortable': ' le plus confortable',
    'A place to <em>stay a while</em>': 'Un endroit où <em>séjourner</em>',
    'Host Family': 'Famille d\'accueil',
    'Shared Apartment': 'Appartement partagé',
    'Private Apartment': 'Appartement privé',
    'Hostel': 'Auberge',
    '/ person / night': '/ personne / nuit',

    # FAQs page
    'Questions &amp; <em>Answers</em>': 'Questions &amp; <em>réponses</em>',
    'frequently asked': 'questions fréquentes',
    ' Classes &amp; Scheduling': ' Cours &amp; horaires',
    ' Activities &amp; Life in Sucre': ' Activités &amp; vie à Sucre',
    ' Getting Here &amp; Practical Info': ' Venir ici &amp; infos pratiques',

    # Blog page
    'Read more →': 'Lire la suite →',
    '4 min': '4 min',
    '5 min': '5 min',
    '5 min read': '5 min de lecture',
    '6 min': '6 min',
    '7 min': '7 min',
    '8 min': '8 min',
    'All': 'Tout',
    'Culture': 'Culture',
    'Language': 'Langue',
    'Travel': 'Voyage',
    'School Life': 'Vie scolaire',
    'Bolivia': 'Bolivie',

    # Common buttons/labels
    'Calle Dalence 146, Sucre, Bolivia': 'Calle Dalence 146, Sucre, Bolivie',
    'Sucre, Bolivia': 'Sucre, Bolivie',
    ' Junín 333, Sucre · In-person &amp; Online': ' Junín 333, Sucre · Présentiel &amp; en ligne',
    'Phone': 'Téléphone',
    'Email &amp; Social': 'Email &amp; réseaux sociaux',
    'Email us any time': 'Écrivez-nous à tout moment',
    'Mobile / WhatsApp': 'Mobile / WhatsApp',
}

def add_data_fr(html):
    """Find all data-en="X" that don't already have data-fr and add data-fr="Y"."""
    def replacer(m):
        full_match = m.group(0)
        en_val = m.group(1)

        # Check if data-fr already exists nearby (within same tag)
        # We look for data-fr right after our match
        after = html[m.end():m.end()+50]
        if 'data-fr="' in after.split('>')[0] if '>' in after else after:
            return full_match

        # Look up translation
        fr_val = FR.get(en_val)
        if fr_val is None:
            return full_match

        return f'{full_match} data-fr="{fr_val}"'

    # Match data-en="..." data-es="..." pattern (with or without data-es)
    # We add data-fr after data-es if it exists, or after data-en
    result = re.sub(r'data-en="([^"]+)" data-es="[^"]*"', replacer, html)

    # Also handle elements that might only have data-en (unlikely but safe)
    def replacer_en_only(m):
        full_match = m.group(0)
        en_val = m.group(1)
        after = html[m.end():m.end()+50]
        if 'data-es=' in (after.split('>')[0] if '>' in after else after):
            return full_match  # has data-es, already handled above
        if 'data-fr="' in (after.split('>')[0] if '>' in after else after):
            return full_match
        fr_val = FR.get(en_val)
        if fr_val is None:
            return full_match
        return f'{full_match} data-fr="{fr_val}"'

    result = re.sub(r'data-en="([^"]+)"', replacer_en_only, result)

    return result

total_added = 0
for page in PAGES:
    path = os.path.join(BASE, page)
    if not os.path.exists(path):
        print(f'  skip {page}')
        continue
    with open(path) as f:
        old = f.read()

    new = add_data_fr(old)
    added = new.count('data-fr=') - old.count('data-fr=')
    total_added += added

    with open(path, 'w') as f:
        f.write(new)
    print(f'✓ {page} (+{added} translations)')

print(f'\nDone. Total: +{total_added} data-fr attributes added.')

# Report missing translations
print('\n--- Strings without French translation ---')
missing = 0
for page in PAGES:
    path = os.path.join(BASE, page)
    if not os.path.exists(path):
        continue
    with open(path) as f:
        content = f.read()
    for m in re.finditer(r'data-en="([^"]+)"', content):
        en = m.group(1)
        # Check if this occurrence has data-fr
        after = content[m.end():m.end()+200]
        tag_rest = after.split('>')[0] if '>' in after else after
        if 'data-fr=' not in tag_rest and en not in FR:
            if missing < 30:
                print(f'  {page}: {en[:80]}...' if len(en) > 80 else f'  {page}: {en}')
            missing += 1

if missing > 30:
    print(f'  ... and {missing - 30} more')
print(f'Total missing: {missing}')
