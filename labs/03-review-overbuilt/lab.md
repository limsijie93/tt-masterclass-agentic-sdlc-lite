# Lab 03 · Review an overbuilt PR

**Practises:** judging a PR against its spec (not just its tests), then pointing a human at what
only they can decide. **Time:** about 20 minutes.

An agent implemented lab 01's spec (`specs/qty-limit.md`) on the branch
`labs/03-qty-limit-overbuilt`. Every CI check is green, at 100% coverage. Your job: decide whether
it built the right thing.

## Steps

1. **Open the PR.** In your copy, open a pull request from `labs/03-qty-limit-overbuilt` into
   `main`. In the description, write `Spec: specs/qty-limit.md`. Wait for CI: it should be green.
2. **Review it yourself first, five minutes, before any agent.** Read `specs/qty-limit.md`, then
   *Files changed*. Write down anything that isn't in the spec. Do this first: once you've read the
   agent's review you can't un-read it.
3. **Run** `/review-pr <your PR URL>` in a **new** session (never the one you used for anything
   else on this PR). Let it post.
4. **Compare.** What did it find that you missed? What did you find that it missed? Did it get
   anything wrong?
5. **Run** `/pr-focus <your PR URL>`. Let it post.
6. **Decide, as the human.** Answer its "You decide" questions in a review: *Review changes →
   Request changes*, one line per decision. Lab 04 harvests your decisions, so keep this review.

## Check yourself

- [ ] CI was green, and the review still found at least three things beyond the spec
- [ ] Each finding quoted the spec line it breaks, and named a simpler version
- [ ] The review flagged that criterion 3 ("the same limit for every product") has **no test**
- [ ] `/pr-focus` asked about silently charging for less than the customer ordered, and didn't
      answer it for you
- [ ] Your own five-minute review: you can name one thing you caught that it didn't, or the
      reverse

## Answer key

- [`expected-review.md`](expected-review.md) and [`expected-focus.md`](expected-focus.md): real
  outputs of the two skills on this branch. Yours will be worded differently.
- **Model solution:** the branch `labs/03-qty-limit-solution`, which is what this PR should have
  been. [Compare it with the overbuilt version](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/compare/labs/03-qty-limit-overbuilt...labs/03-qty-limit-solution):
  61 lines of code and tests become 29, the missing criterion-3 test is added, and one review
  decision is applied (an unknown product is reported before the limit). In your copy, open a PR
  from it and run `/review-pr`: expect no findings.

## Why it matters

Green CI says the code is clean. It can't say whether it's the code anyone asked for. Here, about
two thirds of the change is something the spec cut.
