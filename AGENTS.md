# shop

Tiny checkout service used to demo the agentic SDLC. Python 3.12, stdlib only.

## Layout

- `shop/api.py`: entry point. Validates the request and calls `service`. **Never imports `repo`.**
- `shop/service.py`: business rules.
- `shop/repo.py`: storage (in-memory dicts). Prices are integer cents.

## Commands (CI runs exactly these)

```
ruff check . && ruff format --check .
lint-imports
pytest -q --cov=shop        # fails under 90% coverage
```

## Rules

- Build what the spec asks for and nothing else. If a spec exists in `specs/`, every change
  must trace to an acceptance criterion.
- No abstraction without a second real use: no base class with one subclass, no registry,
  no config for a value that never changes.
- Every behaviour change ships with a test.
- Never edit a test just to make it pass.
