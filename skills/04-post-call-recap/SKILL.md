---
name: perlead-post-call-recap
description: Use after a sales call with a tracked lead, when call notes or a transcript are available. Drafts the recap and next step the same day and updates the dossier.
version: 0.1.0
---
# Post-call recap

## Inputs

Call notes or transcript (from the owner's notetaker or pasted), the calendar event, the dossier.

## Steps

1. Extract only what was said: their situation in their words, what they asked, objections, what each side promised, the agreed next step and date. Quote, do not paraphrase, anything you will repeat back.
2. Update the dossier: `facts` (source = the call, date), `promises`, `objections`, `next_step`.
3. Draft the recap email in the same thread or a new one to attendees: thanks in one line, 2 to 4 bullets of what we agreed, the next step with a date, one question if something is open.
4. If they asked for material (deck, proposal, pricing), list it for the owner. Do not attach or send it yourself.
5. Run the draft through `06-pre-send-judge`.

## Never

- Invent something that was not said in the call.
- Promise prices, terms or dates the owner did not state.
- Send. The human sends.
