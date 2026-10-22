# Week 4 Writeup — Agent-Ready Link Shortener

**Agent:** Antigravity CLI 1.3.1 (Gemini 3.8 Flash)  
**Feature:** Task 2 — Click counter (`GET /stats/{code}`)

## 1. What is in AGENTS.md, and why is it broadly available?

`AGENTS.md` (43 lines) explains what the service does, where the important files are, and how to install, run, and test the application. It also describes the project boundaries, such as not adding authentication, new databases, unnecessary dependencies, or major architecture changes. I included a four-step workflow: understand → test → implement → verify. These instructions are useful for almost every task, so they belong in the root `AGENTS.md`, which Antigravity loads automatically as general project guidance.

## 2. What instruction did I scope, and when does it load?

I created `.agents/rules/tests.md` for test-specific instructions. It requires testing through the public API using `TestClient`, covering success and failure cases, keeping tests independent, and checking visible behavior instead of internal implementation details. It also tells the agent not to hard-code generated short codes.

The rule uses `trigger: glob` with `globs: "test_*.py"`, so it applies when the agent works with matching files such as `test_main.py`. I used this instead of `tests/AGENTS.md` because the tests are located in the repository root. Keeping these instructions separate avoids loading unnecessary testing details for unrelated tasks.

## 3. What procedure does the reusable workflow encode?

`.agents/skills/implement-feature/SKILL.md` defines a reusable test-first workflow. It tells the agent to read the selected task and `AGENTS.md`, inspect `main.py` and `test_main.py`, and explain the expected behavior, affected files, and possible risks.

Next, the agent adds a failing behavioral test, makes the smallest necessary code change, runs `pytest -q`, and summarizes the results and remaining risks. I used this workflow by calling `/implement-feature` when implementing the click counter.

## 4. How does the agent discover each artifact?

| Artifact | Location | How Antigravity finds it |
|---|---|---|
| Repository guidance | `AGENTS.md` | Loaded as general workspace guidance |
| Scoped instruction | `.agents/rules/tests.md` | `glob` trigger on `test_*.py` |
| Reusable workflow | `.agents/skills/implement-feature/SKILL.md` | Description match or `/implement-feature` |

## 5. What did the agent identify during planning or review?

During planning, the agent noticed that `CREATE TABLE IF NOT EXISTS` would not add a `clicks` column to an existing `links.db`. It suggested using `PRAGMA table_info` to check the columns and `ALTER TABLE` if the new column was missing. This helped maintain compatibility with older databases.

It also suggested using an atomic `UPDATE links SET clicks = clicks + 1` instead of updating the counter in Python. One unnecessary suggestion was placing `/stats/{code}` before `/{code}` to prevent a route collision, even though `/{code}` only matches one path segment.

During review, the agent checked the implementation against `TASKS.md`, `AGENTS.md`, and the testing rules. It returned `ACCEPT`, and all 6 tests passed (3 original and 3 new).

## 6. What did I learn about structuring a repository for coding agents?

I learned that organizing repository instructions helps coding agents understand a project and work more effectively. General information should be in `AGENTS.md`, while specific instructions should only load when needed. I also learned that reusable skills make the development process more consistent.

The most important thing I noticed was that planning before coding can help identify problems early. In this assignment, the agent found a possible database issue before making changes. I also understood why testing and reviewing are important, even when the feature seems to work. Overall, clear instructions and a structured workflow can help agents make smaller and more reliable changes.