# Lab 01 · Refine a ticket

**Practises:** ask, stop, prune, before any code exists. **Time:** about 15 minutes.

The ticket below is vague in the same way the demo's was, and it hides the same bait: a word
that invites the agent to build more than anyone needs. Your job is to get a spec out of it that
an agent can build and a teammate can disagree with.

## Steps

1. **File the ticket.** In your copy, open a new issue. Use **Feature request** if you want to see
   the issue form, or a blank issue to keep it vague like the demo. Paste the text from
   [`ticket.md`](ticket.md).
2. **Before you run anything, predict.** Write down the three questions you think matter most,
   and the one word in the ticket most likely to make an agent overbuild.
3. **Run** `/refine-ticket <your issue URL>` in a fresh session. Let it post its questions.
4. **Check the stop.** It should stop after the questions and wait. If it answers its own
   questions or drafts a spec, the stop failed: note it, then tell it to wait.
5. **Answer as the Product Owner.** Reply on the issue with the answers in
   [`answers.md`](answers.md), then tell the session *"The answers are on the issue. Continue."*
6. **Read the spec it posts.**

## Check yourself

- [ ] At least one question named the bait word ("configurable"), and its `assumes:` line said
      what the agent would have built
- [ ] It stopped after the questions
- [ ] Every acceptance criterion is something a test could prove (a number, a status, a message)
- [ ] **Out of scope** has at least three lines, each with a reason
- [ ] "Configurable" became either a criterion or an out-of-scope line, not something left vague
- [ ] Your predictions in step 2: how many of your three questions did it ask?

## Answer key

[`expected-spec.md`](expected-spec.md). Lab 03 builds this exact spec, overbuilt.

## Why it matters

The cheapest place to cut scope is before the code exists. In lab 03 you'll see what an agent
builds when it treats "configurable" as an invitation.
