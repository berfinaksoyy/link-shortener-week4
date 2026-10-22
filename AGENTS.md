# AGENTS.md — Link Shortener

## What this is
A tiny FastAPI + SQLite service that turns a long URL into a short code and redirects to it.
- `POST /shorten` with `{"url": "https://..."}` → `{"code": "b", "short_url": "/b"}`
- `GET /{code}` → `307` redirect to the stored URL, or `404` for an unknown code

## Where things are
| Path | Purpose |
|---|---|
| `main.py` | The whole app: DB setup (`init_db`), base62 `encode`, request models, routes |
| `test_main.py` | Behavioral tests through FastAPI's `TestClient` |
| `docs/TASKS.md` | The list of features that may be implemented |
| `links.db` | Local SQLite file created at startup — never commit it |
| `.agents/rules/` | Scoped rules (e.g. extra rules for test files) |
| `.agents/skills/` | Reusable workflows (e.g. `implement-feature`) |

## Commands (run from the repo root, venv active)
```bash
python3.12 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest -q                     # must pass before and after every change
uvicorn main:app --reload     # http://localhost:8000 (docs at /docs)
```

## Product boundaries
In scope: shortening URLs, redirecting, and the small features listed in `docs/TASKS.md`.
Out of scope — do not add unless the task explicitly asks:
- user accounts, authentication, or a web UI
- a different database, an ORM, or new runtime dependencies
- splitting `main.py` into packages or other architecture changes

## Conventions
- Keep the existing API backward compatible: current requests and responses must keep working.
- Validate input and return clear HTTP errors (`400` bad input, `404` not found, `409` conflict, `410` gone).
- Schema changes must also work when an older `links.db` already exists.
- Keep changes small and focused on the selected task.

## Change workflow
1. **Understand** — read the task in `docs/TASKS.md`, `main.py`, and `test_main.py`.
2. **Test** — add a failing behavioral test for the new behavior (success and failure cases).
3. **Implement** — make the smallest change in `main.py` that makes the test pass.
4. **Verify** — run `pytest -q`; all old and new tests must pass. Summarize what changed.
