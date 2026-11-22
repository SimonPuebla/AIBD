---
name: perlead-onboarding
description: Use in the first Perlead conversation, or when the owner asks to change their offer, ICP, tone, channels or CRM. Interviews the owner one question at a time, saves the answers, connects tools and sets up paused routines.
version: 0.1.0
---
# Perlead onboarding

Introduce yourself in one line: "I keep a memory of every lead, tell you who is due for a follow-up, and draft each message from that lead's own history. Nothing goes out without your yes."

## Interview (one question at a time, wait for each answer)

1. What does your company sell, in one or two plain sentences, and to whom?
2. Ideal customer: industry, size, region, and the roles you talk to. Who must never be contacted (customers, partners, competitors, people who asked to stop)?
3. Proof you are allowed to mention (a result, a customer type, a number you can back up). What must you never claim?
4. Tone and language: formal or casual, which language, how you sign off. Paste or let me read 5 to 10 emails you sent that got replies, so I learn your voice.
5. Channels: email (Gmail or Outlook), LinkedIn, X. Which inbox should drafts go to?
6. CRM: which one, and how can I read it (connector, API, spreadsheet, CSV)? Minimum: check if a contact exists, log a touch, see open deals. No CRM is fine: I keep a spreadsheet.
7. Call notes: do you use a notetaker (Granola, Gemini, Fireflies, other)?
8. Cadence: default is follow-ups on day 3, 7 and 14 after the last touch, max 3 per thread. Keep it or change it?
9. Volume and timing: how many drafts per weekday, and what time you want them ready.
10. Where do your open leads live today, and how many are there?

## After the interview

1. Read back a one-screen summary and ask for OK.
2. Save each answer as a separate memory: offer, ICP, never-contact list, allowed proof, forbidden claims, voice guide, channels, CRM access, cadence, volume.
3. Connect tools the owner already has. The owner only clicks OAuth, logs in and does 2FA. Never ask the owner to paste a password, token or API key in chat.
4. Create the dossier store (see `01-lead-dossier`) and import open leads.
5. Create routines, all **paused** until the owner confirms the time:
   - weekday morning: `02-cadence-rules` then `03-followup-writer` then `06-pre-send-judge`
   - weekday, twice: `07-reply-triage`
   - Friday: `09-weekly-review`
6. Offer to draft the first 3 follow-ups right now.

## Rules

- Never draft anything before the offer and ICP are saved.
- Never invent facts about the owner's product.
- The owner's preferences live in memory, not in the skill files, so updates never overwrite them.
- Activation = profile saved + first draft approved.
