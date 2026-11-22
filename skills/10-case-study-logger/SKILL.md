---
name: perlead-case-study-logger
description: Use on every touch, reply, call and proposal to append one ledger line, and at day 0 and day 14 to snapshot the before and after. Builds an honest, anonymized case study.
version: 0.1.0-stub
---
# Case study logger (stub)

Status: stub in v0.1. Use `case-study/ledger-template.csv` and `case-study/methodology.md` from the Perlead repo.

- Day 0: snapshot the baseline (last 30 days) as described in the methodology.
- Every event: one ledger line (date, lead id hash, channel, touch number, draft or sent, reply class, meeting, proposal, pipeline value only if a deal with an amount exists in the CRM).
- Day 14: compute the after numbers with sample sizes and a 7-day wait for late replies.
- Anonymize: no names, emails, company names or quotes unless the owner explicitly approves each one.
- The ledger stays in the owner's private storage, never in a public repo.
