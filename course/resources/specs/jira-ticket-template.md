# Jira ticket template

What a requester fills in before a ticket can be refined. Paste it into your Jira issue type's
description template, and ask your Jira admin to make the fields marked **required** mandatory for
that issue type. The GitHub equivalent is the issue form in
[`.github/ISSUE_TEMPLATE/feature.yml`](../../../.github/ISSUE_TEMPLATE/feature.yml).

A template checks that the fields exist, not that they're good. `/refine-ticket` still reads what's
in them and asks about what's missing.

## The template

```
Summary: <one line, what changes for the user>

Goal (required)
Who needs what, and why? One or two sentences.

Acceptance criteria (required)
How will we know it works? One check per line, each something a test could prove.
-
-

Out of scope (required)
What is this NOT? List the things someone might reasonably assume are included.
-

Decisions already made
Business rules a builder would otherwise guess: money, limits, wording, edge cases.
-

Question owner (required)
Who answers questions about this, and how quickly?
```

## The same ticket, before and after

**Before**: Issue #2 as Dana filed it, with no template:

> Marketing is planning a few campaigns next quarter and wants customers to be able to enter a
> promo code at checkout to get a discount. It should be flexible so we can do all kinds of deals.

**After**: the same request through the template:

```
Summary: Customers can apply a promo code at checkout

Goal
Customers enter a promo code at checkout and get a percentage off the whole order,
for next quarter's campaigns.

Acceptance criteria
- SAVE10 on a $52.00 order makes the total $46.80
- An unknown code is rejected, and the customer is told the code isn't valid
- With no code, the total is unchanged

Out of scope
- More than one code per order
- Fixed-amount, buy-one-get-one, free-shipping deals
- Codes that expire automatically

Decisions already made
- Round discounts in the customer's favour
- Codes are not case-sensitive

Question owner
Dana (Marketing), same day on Slack
```

Most of what `/refine-ticket` had to ask in the demo is answered up front. Its job shrinks to
checking the answers against the code.
