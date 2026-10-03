<!-- Body for PR #3: branch demo/promo-codes into main. Title: "Add promo codes at checkout".
     Written the way an implementing agent writes it: confident, and listing extras as features. -->

Closes #2

Spec: `specs/2.md`

## What and why
Adds promo codes at checkout, as specced in #2. Built as a pluggable discount engine so
Marketing can run any kind of deal without code changes later: percentage and fixed-amount
rules, a rule registry for new deal types, stackable codes, and optional expiry dates.

## Machine-checked: skip these in review
- **CI (`hygiene`)**: lint, format, layering, tests, coverage. Blocks the merge on its own.
- **Agent review (`/review-pr`)**: does the diff match the spec, and is it overbuilt? Comments only.

## Human judgement: only you can tick these
- [ ] It solves the problem the ticket was actually about.
- [ ] The business rules are right (money, limits, edge cases a customer would hit).
- [ ] Nothing here should not exist.
- [ ] I would be happy to own this code at 3am.
