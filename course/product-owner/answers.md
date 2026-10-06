# The Product Owner's answers (Issue #2)

`/refine-ticket` stops after it asks its questions and waits for a human. In this repo, that human
is the Product Owner: Dana from Marketing, who filed the ticket. These are Dana's answers.

**How to use them:**

1. Run `/refine-ticket` on the issue and wait for the questions.
2. Give these answers, either as a reply on the issue (only on your own copy) or in the session.
3. Tell the agent: *"The answers are on the issue. Continue."* (or *"Here are the answers. Continue."*).
4. It writes the spec. Compare it with [`expected-outputs/2-spec.md`](../expected-outputs/2-spec.md).

Your agent may word or order its questions differently, so match each answer by **topic**, not
by number. If it asks something not covered below, answer as you think Dana would, and expect
your spec to differ a little from the expected one.

| Topic | Dana's answer |
|---|---|
| What kinds of deal? | Just "X% off the whole order". That's all the next campaign uses. |
| More than one code per order? | One code per order. |
| Expiry or usage limits? | No expiry for now. We'll ask engineering to remove a code when its campaign ends. |
| A code that doesn't exist? | Reject it and tell the customer the code isn't valid. |
| Who creates codes, and how often? | Engineering adds them. About three a quarter. |
| How to round a fraction of a cent? | No view yet. Leave it open and let whoever reviews the code decide. |

Ready to paste:

```
1. Just "X% off the whole order". That's all the next campaign uses.
2. One code per order.
3. No expiry for now. We'll ask engineering to remove a code when its campaign ends.
4. Reject it and tell the customer the code isn't valid.
5. Engineering adds them. About three a quarter.
6. Rounding a fraction of a cent: no view yet. Leave it open and let whoever reviews the code decide.
```
