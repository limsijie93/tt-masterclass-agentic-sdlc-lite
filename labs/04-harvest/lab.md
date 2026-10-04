# Lab 04 · Harvest, second sighting

**Practises:** turning review findings into permanent rules, checks and better skills, and the
restraint that makes it work. **Time:** about 20 minutes.

In the masterclass, `/harvest` **logged** PR #3's overbuilding without proposing anything: it was a
first sighting. Lab 03's PR overbuilt again. This time the ledger can count it.

## Steps

1. **Give your repo a memory.** In your copy, open a pull request from `harvest/2` into `main`
   and merge it. That's the harvest from the demo, the same change as [PR #6](https://github.com/limsijie93/tt-masterclass-agentic-sdlc-lite/pull/6). Your `main` now has:
   - `harvest/ledger.md` with 14 findings from the demo, including *"agent built ABC + registry +
     factory for one percentage rule … [logged: first sighting]"*
   - the **Scope** CI check, the rounding domain rule in `AGENTS.md`, and the sharper
     `refine-ticket`
2. **Check that lab 03 is reviewed.** Your lab 03 PR should have the agent review, the
   `/pr-focus` comment, and your own *Request changes* review with your decisions.
3. **Predict.** Before running anything, write down: which finding from lab 03 is now a
   **second sighting**? Where should it go, given the rule "prefer the machine"? Which of your
   decisions from lab 03 should become a domain rule?
4. **Run** `/harvest <your lab 03 PR URL>` in a fresh session. Read the report it shows you.
5. **Let it open the PR**, then review that PR as you would any other. Merge only what you agree
   with: you can edit the branch or ask it to drop a proposal.
6. **Open `harvest/ledger.md`** on `main` afterwards.

## Check yourself

- [ ] It read the ledger **first**, and its overbuilding proposal **cites the earlier ledger
      line** (`#2 … first sighting`). That citation is what makes it a second sighting.
- [ ] Three proposals at most, each to a different home, each with the exact change
- [ ] Where a machine could check something, it proposed a check, not a sentence in `AGENTS.md`
- [ ] At least one of **your** decisions from lab 03 became a domain rule
- [ ] Nothing CI already catches was proposed, and it didn't propose fixing the feature itself
- [ ] The ledger grew by one line per finding, **including** the ones it didn't propose
- [ ] Your prediction in step 3: did it match?

## Answer key

[`expected.md`](expected.md): what a good harvest of lab 03 contains, with one example.

## Why it matters

Each review finds something. Harvest decides where it lives next, so the next PR is a little
harder to get wrong and a little easier to review. Run it after every ticket: that's the
repeatable process.
