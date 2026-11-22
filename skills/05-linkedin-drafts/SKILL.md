---
name: perlead-linkedin-drafts
description: Use when a lead's best channel is LinkedIn, or after a LinkedIn connection is accepted. Drafts connection notes and DMs for the owner to paste and send. Never clicks, connects or sends on LinkedIn.
version: 0.1.0
---
# LinkedIn drafts

LinkedIn is draft-only. The agent never sends invites, messages or follows from the owner's account. It may read public profiles to verify a person.

## Before drafting

- Confirm the exact profile URL and that the current role and company match the dossier. No verified profile, no draft. Never guess a profile from a name.
- Check the dossier and cadence stops: no LinkedIn touch if the same person got an email in the last 3 days.

## Shapes

- **Connection note** (under 300 characters): one real, specific reason to connect, no pitch, no link.
- **First DM after accepting**: thanks, plus genuine curiosity about one verified fact about them. No pitch, no link.
- **Later DMs**: answer what they said, ask about their challenges, mention what the owner does only when they ask or a matching pain shows up. One ask per message.
- At most 2 DMs without a reply, at least 7 days apart, then stop.

## Output

The text to copy, the profile URL, and the evidence list. Run through `06-pre-send-judge`. The owner pastes and sends.
