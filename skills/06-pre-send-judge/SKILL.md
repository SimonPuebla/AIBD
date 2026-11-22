---
name: perlead-pre-send-judge
description: Use on every draft Perlead produces (follow-ups, recaps, LinkedIn and X drafts, reply drafts) before showing it to the owner as ready. A second pass that looks for the reason a careful person would stop the draft.
version: 0.1.0
---
# Pre-send judge

A separate pass. Do not reuse the writer's reasoning. Read only: the draft, the thread, the dossier and the evidence list.

Your job is to find the reason the owner would stop this message. If you cannot find one, say so.

## Questions (yes or no, one line of why each)

1. **Grounded.** Every claim about the person or company is in the evidence list with a source. A claim without a source is a no.
2. **Continuity.** It fits the thread: does not repeat what was said, does not ignore their question, does not contradict their answer, does not restart the relationship.
3. **Timing.** Nothing in the thread or dossier makes this badly timed: a meeting coming up, a request to wait, bad news, a no.
4. **Promises.** No guaranteed results, deadlines, prices or capabilities outside the owner's allowed proof.
5. **One thing.** It asks for one easy action.
6. **Right person.** By role and thread, it makes sense to write to this person about this.
7. **Tone.** It reads like one person writing to another, in the owner's voice, without flattery or filler.

## Verdict

- `pass`: all yes. Show to the owner as ready.
- `revise`: one or two fixable no's. Return to the writer once with the reason. If it fails again, show to the owner marked "needs your eye" with the reason.
- `block`: grounded, timing or promises is a no and cannot be fixed. Do not show as a draft; show the reason.

Return a short JSON: `{"verdict": "...", "answers": {...}, "reason": "..."}`.

## Learning

Log every `revise` and `block` reason. `09-weekly-review` turns repeated reasons into proposed rules.
