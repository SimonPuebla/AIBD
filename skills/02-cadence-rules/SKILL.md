---
name: perlead-cadence-rules
description: Use every weekday morning before drafting, or when the owner asks who is due for a follow-up. Decides with fixed rules which leads are due today and which must not be touched.
version: 0.1.0
---
# Cadence rules

The model does not decide timing. These rules do. Output is a list; this skill writes no message.

## Defaults (the owner can change them in onboarding)

- Follow-up 1: 3 days after the last touch. Follow-up 2: 7 days. Follow-up 3 (last, a clean close): 14 days.
- Maximum 3 follow-ups in the same thread after the first message.
- Never two touches to the same person on the same day, never less than 3 days apart.
- Weekdays only, in the lead's time zone when known.
- After a call: the recap is due the same day (the Pack's `perlead-post-call-recap` drafts it).

## Hard stops (any one means: not due, ever, until a human changes it)

- Any human reply in the thread (it goes to the owner, or to `perlead-reply-triage` if the Pack is installed).
- Bounce, unsubscribe, "stop", "not interested", or on the never-contact list.
- Open deal or meeting already scheduled with this person, owned by someone else.
- Another touch to this person from any channel in the last 3 days.
- Status `won`, `lost` or `do_not_contact`.
- Missing data is not permission: if you cannot check a stop, the lead is not due.

## Steps

1. Read all dossiers with status `active` or `waiting`.
2. For each, re-read the latest message in the actual thread (not only the dossier). If anything new is there, update the dossier first.
3. Apply hard stops, then the timing rules.
4. Respect the daily draft cap from onboarding. If more are due, keep the oldest `next_step` first and report the rest.

## Output

A table: lead, company, touch number due, days since last touch, channel, why it is due. Plus a short list of leads due tomorrow and leads that were stopped today with the reason.

## Idempotency

A lead plus touch number produces at most one draft. If a draft for that touch already exists, report it instead of creating another.
