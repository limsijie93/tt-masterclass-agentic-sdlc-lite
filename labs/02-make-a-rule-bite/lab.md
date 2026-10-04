# Lab 02 · Make a rule bite

**Practises:** turning a rule written in prose into a check that blocks the merge.
**Time:** about 15 minutes, all in GitHub's web editor. No terminal.

Your team has an unwritten rule: *no `print()` left in the app code*. Debug prints end up in
production logs. Today that rule lives in people's heads, which means it lives nowhere.

## Steps

1. **Write it as prose first.** In your copy, edit `AGENTS.md` (pencil icon) and add under
   **Rules**:
   ```
   - No print() in shop/. Use the return value or raise; don't log to stdout.
   ```
   Commit straight to `main`. This is the "prose" strength: the agent can read it, nothing
   enforces it.
2. **Break it, and watch nothing happen.** Create a branch `lab/print`, edit `shop/service.py`,
   and add `print("total", total)` just before `return total` in `order_total`. Open a PR into
   `main`. CI runs on its own, and it's **green**. The prose rule didn't catch anything.
3. **Make it executable.** On the same branch, edit `pyproject.toml`: add `"T20"` to the ruff rule
   list (`select = [..., "SIM", "T20"]`). `T20` is ruff's rule set for `print` statements. Commit.
4. **Watch it bite.** CI runs again on its own. **Lint and format** fails with
   `T201 print found` at `shop/service.py`. If you set up the ruleset, the merge button says
   **Merging is blocked**.
5. **Fix it.** Remove the `print` and commit. CI goes green.
6. **Keep the rule, lose the print.** The PR now changes only `pyproject.toml`. Merge it: from now
   on every PR is checked.

## Check yourself

- [ ] Step 2 was green: the prose rule caught nothing
- [ ] Step 4 failed on `T201`, on the **Lint and format** step, without anyone running anything
- [ ] After merging, `pyproject.toml` on `main` includes `"T20"`
- [ ] You can say which of the three strengths each step was: prose (step 1), executable (step 3),
      required (the ruleset)

## Answer key

[`expected.md`](expected.md)

## Go further

Run the same check earlier: [`course/resources/hygiene/`](../../course/resources/hygiene/) has a
pre-commit config and a Claude Code agent hook. Ruff reads `pyproject.toml`, so both pick up
`T20` automatically. Same rule, three places.
