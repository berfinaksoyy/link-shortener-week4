---
trigger: glob
globs: "test_*.py"
description: "Rules for writing and editing pytest tests in this repository"
---
# Test rules

- Test through the public HTTP API with FastAPI's `TestClient` (`client.get`, `client.post`). Do not call internal helpers such as `encode` or `get_db` directly.
- For every feature, cover the success case and at least one failure or edge case (for example `400`, `404`, `409`, `410`).
- Tests must be independent: each test creates the data it needs (for example, its own `POST /shorten`) and never relies on another test's data or on execution order.
- Do not hard-code generated short codes such as `"b"`; read the code from the response.
- Assert on behavior that a client can see (status code, JSON body, `location` header), not on private implementation details or database rows.
- Use `follow_redirects=False` when checking a redirect.
- Keep one behavior per test and give it a descriptive name (`test_<feature>_<case>`).
