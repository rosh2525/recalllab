# Validation record

## Completed checks

- Backend suite: 79 tests passed on Python 3.14, 23 October 2026.
- Production TypeScript/Vite build passed.
- Local HTTP health endpoint and application page returned 200.
- Browser verified dashboard rendering, a real MCP practice session, correct maths assessment, original source dialog and returning to the saved session, and a full five-question independent check with grades withheld until completion.
- The official Python MCP client independently negotiated protocol 2025-11-25, discovered all four tools and read progress successfully.
- Both narrow and wide responsive layouts were visually inspected during browser use.

The suite covers 26 reviewed mathematical questions (21 practice + five check), wrong/equivalent expressions, unsafe syntax, pre-operation intermediate size/degree bounds for nested powers, hidden answer keys, closed-book assessment state, duplicate and concurrent retries, SQLite restart recovery, invalid model output, model failures, host/origin checks, MCP initialization, discovery and tool calls.

## Remaining evidence, not claimed as complete

- Temporary AWS developer login succeeded. Nova Lite availability was inspected and authorized minimal Converse smoke tests were attempted in Stockholm. AWS rejected it because account verification is pending; no successful live inference, token usage or cost measurement is claimed.
- Conceptual assessment has schema/failure tests but no live-model accuracy benchmark yet. The planned ≥90% agreement threshold is a target, not an achieved result.
- A 60-case developer-authored conceptual evaluation set is included at `evaluation/conceptual.json`. Its labels need independent educator review, and the live benchmark must run before reporting that accuracy result.
- No student interviews, usability pilot, delayed independent-test results or learning-effect claims are fabricated.
- Speech recognition depends on browser support and microphone permission. Typed interaction was verified; live microphone recognition is not yet verified.
- Keyboard labels, source-dialog focus restoration and reduced-motion styles are implemented; representative keyboard flows are checked. A full assistive-technology audit and real screen-reader trial remain outstanding.

## Suggested pilot

Recruit five consenting students without uploading private course or identifying data. Observe completion of a practice path. Ask parallel questions immediately and one day later, recording assistance separately. Record confusing feedback and voluntary return use. Treat this as exploratory product feedback, not a causal effectiveness study.
