---
name: implement-feature
description: Implement one feature from docs/TASKS.md in this link shortener using a test-first workflow. Use when asked to build, add, or implement a task from docs/TASKS.md.
---
# Implement a feature

Follow these steps in order. Do not skip a step.

1. **Read the task and guidance.** Read the selected task in `docs/TASKS.md` and the root `AGENTS.md`.
2. **Inspect the code and tests.** Read `main.py` and `test_main.py`. Note how the database table, the request model, and the routes work today.
3. **State the plan before editing.** Write down:
   - the expected behavior, including status codes for success and failure cases,
   - which files you will change,
   - any risk (for example, a database schema change on an existing `links.db`, or a new route that clashes with `GET /{code}`).
4. **Add a failing behavioral test.** Add tests to `test_main.py` for the success case and at least one failure or edge case. Run `pytest -q` and confirm the new tests fail for the expected reason.
5. **Implement the smallest change.** Edit `main.py` only as much as needed. Keep existing requests and responses working. Do not add dependencies.
6. **Run the tests.** Run `pytest -q`. All original and new tests must pass. If something fails, fix the code, not the expected behavior.
7. **Summarize.** Report the files changed, the tests added, the final `pytest` result, and any remaining risks or limitations.
