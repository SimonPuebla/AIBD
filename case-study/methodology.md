# Measurement methodology

How Perlead results are measured and reported. The goal is numbers a skeptical buyer would accept.

## Rules

1. **Only human replies count.** Out-of-office, auto-replies, ticket systems, bounces and unsent drafts are excluded.
2. **Always show the sample.** Every rate comes with `n` (messages sent) and the period. Small samples are labeled small.
3. **Same window before and after.** Baseline = the 30 days before day 0. After = days 1 to 14, plus 7 days of waiting for late replies.
4. **Pipeline only if it exists.** Pipeline value counts only deals created in the CRM with an amount, not estimates.
5. **Publish what did not work too.**
6. **The owner approves** the final text and the anonymization.

## Metrics

| Metric | How it is measured | Before | After |
| --- | --- | --- | --- |
| Leads with a dated next step | % of open leads with a date in the dossier or CRM | Day 0 snapshot | Day 14 |
| Follow-ups on time | % of due follow-ups sent on their due day | Last 30 days, from Sent | Days 1 to 14 |
| Reply rate by touch | Human replies / sent, for first touch, FU1, FU2, FU3 | Last 30 days | Days 1 to 14 + 7 |
| Meetings and proposals | Calendar events and proposals sent | Last 30 days | Days 1 to 14 |
| Drafts approved without edits | % approved as written | n/a | Week 1 vs week 2 |
| Owner minutes per day | Daily self-report | Owner estimate | Average of 14 days |
| Errors stopped by the judge | Count and type of revise and block verdicts | n/a | Days 1 to 14 |

## Files

- `ledger-template.csv`: one line per event.
- `before-after-template.md`: the report shape.
- Real ledgers stay in the owner's private storage, never in this repo.
