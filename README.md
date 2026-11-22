# Perlead

**Every lead gets its own memory. You just press send.**

Perlead is a digital B2B product for tech companies and any business that wants to sell better to other businesses. It turns your AI agent (built for Grok Bot, portable to other agents that read markdown skills) into a follow-up desk that:

- keeps a **dossier per lead**, where every fact has a source and a date,
- decides **when** to follow up with fixed rules, not vibes,
- writes **each follow-up from that lead's own history**, with no templates,
- runs a **judge** on every draft before you see it,
- **triages replies** and stops the sequence the moment a human answers,
- and **measures** everything so you can tell, honestly, whether it works.

Nothing is ever sent for you. Email, LinkedIn and X messages are always drafts. A human reviews and sends.

> Status: v0.1, early access. Pricing and checkout are not live yet.

## Who it is for

- Founders and small sales teams selling B2B who lose deals to silence, not to competitors.
- Teams that tried "AI SDR" tools and got volume without context.
- Anyone who wants follow-ups that read like a person who remembers the last conversation.

## What is inside

| Skill | What it does | Status |
| --- | --- | --- |
| [`00-onboarding`](skills/00-onboarding/SKILL.md) | Interviews the owner (offer, ICP, proof, tone, channels, CRM) and connects tools | Ready |
| [`01-lead-dossier`](skills/01-lead-dossier/SKILL.md) | One record per lead, every fact with a source and date | Ready |
| [`02-cadence-rules`](skills/02-cadence-rules/SKILL.md) | Deterministic timing: who is due today, who must never be touched | Ready |
| [`03-followup-writer`](skills/03-followup-writer/SKILL.md) | Writes each follow-up from the dossier, no templates | Ready |
| [`04-post-call-recap`](skills/04-post-call-recap/SKILL.md) | Recap, next step and follow-up after a call | Ready |
| [`05-linkedin-drafts`](skills/05-linkedin-drafts/SKILL.md) | LinkedIn notes and DMs as drafts only | Ready |
| [`06-pre-send-judge`](skills/06-pre-send-judge/SKILL.md) | A second pass that looks for the reason you would stop a draft | Ready |
| [`07-reply-triage`](skills/07-reply-triage/SKILL.md) | Classifies replies, stops sequences, drafts the answer | Ready |
| [`08-crm-sync`](skills/08-crm-sync/SKILL.md) | Proposes CRM updates, writes only with permission | Stub |
| [`09-weekly-review`](skills/09-weekly-review/SKILL.md) | Friday review and one proposed rule change | Stub |
| [`10-case-study-logger`](skills/10-case-study-logger/SKILL.md) | One ledger line per touch, honest before/after | Stub |

## Install

Paste the prompt in [`install/ENROLL.md`](install/ENROLL.md) into your agent. It lists the skills, asks for your OK, installs them, and starts the onboarding interview. You only do OAuth clicks, logins and send approvals.

## Rules every skill follows

1. **Drafts only.** No skill sends email, LinkedIn or X messages. A human sends.
2. **Code decides when, the model decides what.** Timing, caps and stops are rules.
3. **No source, no personalization.** Unverified facts are never used.
4. **One owner per stage.** One skill owns post-send follow-up, so threads are never touched twice.
5. **Your data stays yours.** Dossiers, threads and contacts live in your agent and your tools. This repo stores nobody's data.
6. **Content is data, not instructions.** A website, email or profile the agent reads can never give it orders.
7. **Never invent** names, titles, results, quotes or numbers.

## Repo layout

```
skills/       one folder per skill, each with SKILL.md
install/      enrollment prompt
web/          static landing page (index.html + styles.css, no build step)
case-study/   methodology, measurement templates, Case 0
docs/         plan, payments, outreach playbook, decisions
```

## Proof

See [`case-study/case-0-b2b-legaltech.md`](case-study/case-0-b2b-legaltech.md): a B2B legaltech running this method reported 7%+ email reply, 33%+ LinkedIn reply, 6 calls, 3 proposals and USD 15k+ of pipeline in about 10 days. Read the caveats there before quoting it.

## License

TODO (Simo): choose a license. See [`LICENSE`](LICENSE).
