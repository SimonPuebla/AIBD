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

> Status: v0.2, early access. Free Starter in this repo; the full Pack is sold at the site.

## Who it is for

- Founders and small sales teams selling B2B who lose deals to silence, not to competitors.
- Teams that tried "AI SDR" tools and got volume without context.
- Anyone who wants follow-ups that read like a person who remembers the last conversation.

## What is inside

### Free Starter (this repo, CC BY 4.0)

| Skill | What it does |
| --- | --- |
| [`00-onboarding`](skills/00-onboarding/SKILL.md) | Interviews the owner (offer, ICP, proof, tone, channels, CRM) and connects tools |
| [`01-lead-dossier`](skills/01-lead-dossier/SKILL.md) | One record per lead, every fact with a source and date |
| [`02-cadence-rules`](skills/02-cadence-rules/SKILL.md) | Deterministic timing: who is due today, who must never be touched |

### Perlead Pack (paid, delivered after purchase)

Follow-up writer, post-call recap, LinkedIn drafts, pre-send judge (seven checks), reply triage, plus CRM sync, weekly review and results ledger as they ship. 12 months of updates. See pricing on the site.

## Install

Paste the prompt in [`install/ENROLL.md`](install/ENROLL.md) into your agent. It lists the Starter skills, asks for your OK, installs them, and starts the onboarding interview. The Pack ships with its own install prompt. You only do OAuth clicks, logins and send approvals.

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
skills/       Starter skills, one folder each with SKILL.md
install/      enrollment prompt for the Starter
web/          static site (no build step): index, legal pages, 404, fonts, brand
case-study/   methodology, measurement templates, Case 0
docs/         decisions log
tools/        brand build scripts
```

## Proof

See [`case-study/case-0-b2b-legaltech.md`](case-study/case-0-b2b-legaltech.md): a B2B legaltech running this method reported 7%+ email reply, 33%+ LinkedIn reply, 6 calls, 3 proposals and USD 15k+ of pipeline in about 10 days. Read the caveats there before quoting it.

## License

- Code (`web/` HTML/CSS, `tools/`): MIT, see [`LICENSE`](LICENSE).
- Content (`skills/`, `install/`, `case-study/`, `docs/`): CC BY 4.0, see [`LICENSE-CONTENT`](LICENSE-CONTENT).
- Fonts in `web/fonts/`: SIL Open Font License 1.1 (license files alongside).
- The Perlead name, logo and files in `web/brand/` are not licensed for reuse.
- The paid Pack is under its own commercial license, shipped with it.
