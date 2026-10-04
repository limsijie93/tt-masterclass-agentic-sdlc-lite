# Harvest ledger

Append-only. One line per finding that `/harvest` read, **including the ones it did not propose**.
Those are the point: some rules only fire on a second sighting, and one ticket can't see a
repeat. This file is the memory that makes the second sighting countable.

Don't edit or reorder past lines. A ledger someone has tidied can't be counted.

```
<date>      <ticket>  <PR>  <home, or "none">         <finding>
```

---
