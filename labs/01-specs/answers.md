# The Product Owner's answers (lab 01)

`/refine-ticket` stops after its questions and waits for a human. For this lab, that human is Sam
from Ops, who filed the ticket. Give these answers on the issue (or in the session), then say
*"Continue."*

Your agent may word or order its questions differently: match each answer by **topic**. If it
asks something not covered here, answer as you think Sam would.

| Topic | Sam's answer |
|---|---|
| Who is affected, and is it per order or across orders? | It's within a single order. We're not trying to limit customers over time. |
| What's the limit, and does it differ per product? | 10 of any one product. Same number for everything, for now. |
| What happens when someone asks for more? | Reject it and tell them the maximum. Don't change their order behind their back. |
| What does "configurable" mean? | Honestly, just "not hard to change". Engineering can change the number in code; it'll happen maybe once a year. No admin screen, no settings. |
| Any other limits (total items, total value)? | No. Just the per-product count. |

Ready to paste:

```
1. Within a single order only. Not limits across orders or per customer.
2. Max 10 of any one product. Same for every product for now.
3. Reject it and tell them the maximum. Don't silently change the quantity.
4. "Configurable" just means easy to change: engineering edits the number in code, maybe once a year. No admin screen or settings.
5. No other limits. Just the per-product count.
```
