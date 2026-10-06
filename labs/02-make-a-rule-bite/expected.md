# Lab 02 · Answer key

**After step 2** (prose only, a `print` added): every CI step is green. Nothing reads `AGENTS.md`
except the agent, and only when it chooses to.

**After step 3** (`"T20"` added to the ruff rules): the **Lint and format** step fails:

```
T201 `print` found
 --> shop/service.py:<line>:9
```

The other checks (Architecture, Tests) still pass. With the ruleset on, the PR shows **Merging is
blocked**.

**After step 5** (`print` removed): all green, and the PR only changes `pyproject.toml`:

```toml
[tool.ruff.lint]
select = ["E", "F", "I", "B", "UP", "SIM", "T20"]
```

**The three strengths of the same rule:**

| Strength | Where it lives | What happens when it's broken |
|---|---|---|
| Prose | a line in `AGENTS.md` | nothing |
| Executable | `"T20"` in `pyproject.toml`, run by CI | the Lint step fails |
| Required | the `hygiene` check in a ruleset | the merge is blocked |

`main` already has no `print` calls, so turning the rule on costs nothing today. In an older
codebase it might find dozens. Then you'd switch it on with a baseline (ignore today's, fail on
new ones) and shrink the list over time.
