---
name: perlead-reply-triage
description: Use twice per weekday and whenever the owner asks "who replied". Reads new replies, classifies them, stops sequences, updates dossiers and drafts the answer.
version: 0.1.0
---
# Reply triage

A human reply always beats the sequence. The moment someone answers, automatic follow-ups stop for that person.

## Steps

1. Read new messages in the owner's inbox since the last run, only in threads that belong to tracked leads (and new inbound from tracked companies).
2. Ignore and do not count as replies: out-of-office, auto-replies, ticket systems, bounces. Log bounces and mark the address.
3. Classify each human reply:

| Class | What happens |
| --- | --- |
| `positive` | Stop sequence, status `replied`, draft a fast answer with a concrete next step |
| `info_request` | Stop sequence, draft an answer to exactly what they asked, then one ask |
| `redirect` | Stop for this person, create a dossier for the named person, draft a short note to them referencing the redirect |
| `not_now` | Stop, set `next_step` to the date they gave (or 90 days), draft a short thank-you |
| `no` | Stop, status `lost` with their reason, draft a one-line acknowledgment, never re-pitch |
| `unsubscribe` | Stop, status `do_not_contact`, no reply needed unless the law where they are requires confirmation |
| `question_about_us` | Draft an answer using only allowed proof; flag anything you cannot answer |

4. Update the dossier: `last_reply`, `objections`, `status`, `next_step`.
5. Run every reply draft through `06-pre-send-judge`.

## Output to the owner

Replies first, ordered by value (positive, info request, redirect, then the rest), each with the class, one line on what they said, and the draft ready to send. Speed matters: positive replies and info requests at the top.

## Never

- Send. The human sends.
- Argue with a no, or keep writing to someone who asked to stop.
