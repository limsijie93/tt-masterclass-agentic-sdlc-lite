Closes #<!-- issue number -->

Spec: `specs/<issue>.md`

## What and why
<!-- Two lines. What changed, and which acceptance criterion it serves. -->

## Machine-checked: skip these in review
- **CI (`hygiene`)**: lint, format, layering, tests, coverage. Blocks the merge on its own.
- **Agent review (`/review-pr`)**: does the diff match the spec, and is it overbuilt? Comments only.

## Human judgement: only you can tick these
<!-- `/pr-focus` lists where to look. These boxes are for the reviewer, not the author. -->
- [ ] It solves the problem the ticket was actually about.
- [ ] The business rules are right (money, limits, edge cases a customer would hit).
- [ ] Nothing here should not exist.
- [ ] I would be happy to own this code at 3am.
