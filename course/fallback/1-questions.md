<!-- Fallback for beat 1, phase 1. A known-good `/refine-ticket` comment on Issue #2.
     Use it if the live run misbehaves, or to check the live run against.
     Next step: the Product Owner's answers are in 1-answers.md. -->

## Questions before this can be built

1. What kinds of deal does the first campaign actually need?
   - blocks: the discount data model
   - assumes: percentage off, fixed amount off, buy-one-get-one and free shipping, all at once

2. Can a customer use more than one code on the same order?
   - blocks: whether discounts stack, and in what order
   - assumes: yes, codes stack

3. Do codes expire or have usage limits?
   - blocks: extra stored fields, a clock dependency, per-customer tracking
   - assumes: every code has an expiry date and a per-customer limit

4. What happens when a customer enters a code that does not exist?
   - blocks: the error path in checkout
   - assumes: the code is silently ignored and the order goes through at full price

5. Who creates new codes, and how often?
   - blocks: whether we build an admin endpoint
   - assumes: Marketing creates codes themselves through an admin API

Touches: `shop/api.py:6` entry point · `shop/service.py:6` total calculation · `shop/repo.py:3` storage

_Waiting for answers. Reply on this issue, or in the session._
