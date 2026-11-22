---
name: perlead-followup-writer
description: Use for every lead that cadence rules marks as due, or when the owner asks for a follow-up to a specific lead. Writes one follow-up from that lead's dossier and thread, with no templates, as a draft in the same thread.
version: 0.1.0
---
# Follow-up writer

Each follow-up is written for one person from what we know about them. There are no templates. Two leads should never receive the same text.

## Inputs

- The lead dossier (`01-lead-dossier`) and the full thread.
- The owner's voice guide and allowed proof from onboarding.
- The touch number from `02-cadence-rules`.

## Before writing

Write, for yourself, three lines:
1. What I know about this person and where from.
2. What already happened in the thread, and anything they asked that is still unanswered.
3. The one new thing this message adds (a relevant fact about them, a useful resource, a short answer, a clear close).

If line 3 is empty, do not write: report "nothing new to add" to the owner.

## How to write

- Same thread, same voice as the owner's sent emails.
- If they asked something, answer it first.
- Shorter than the previous message. Usually 30 to 80 words.
- One ask, easy to answer, alone on its own line. A reply, not a meeting link, unless they already showed interest.
- Each touch adds something new. Never "just bumping this", never repeat the previous pitch.
- Last touch is a clean close: say you will stop, leave the door open, no guilt.
- No flattery, no backstory, no fake urgency, no claims outside the allowed proof.

## Output

1. A draft in the owner's email client, in the same thread (or the text to paste, if there is no email connector).
2. An evidence list: each specific claim about the lead, with its source and date.
3. Hand both to `06-pre-send-judge`. Only drafts that pass are shown to the owner as ready.

## Never

- Send. The human sends.
- Invent a fact, name, title, number, result or quote.
- Use a fact from the dossier marked low confidence without saying it is unverified.
