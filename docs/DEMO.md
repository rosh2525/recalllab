# Demo and submission draft

## Pitch

RecallLab helps students find the gap between recognising an explanation and being able to produce one. It combines an attempt-first learning loop, reviewed hints, deterministic mathematical verification and independent follow-up checks.

## Under-three-minute demo

- **0:00–0:20:** Show the dashboard and the misconception: “A zero derivative always means a maximum.” Explain the learner's problem.
- **0:20–1:05:** Start the optimisation path, submit an explanation, open a graduated hint and a source citation. If Bedrock is disabled, explicitly explain that the answer is saved for self-review; do not pretend live AI assessment occurred.
- **1:05–1:35:** Show a numerical practice question and symbolic verification, including a wrong answer and a corrected one.
- **1:35–2:05:** Start an independent check. Show that hints and feedback are withheld until completion and that progress distinguishes assisted work.
- **2:05–2:35:** Show real MCP activity, persisted progress and the local/cloud mode boundary.
- **2:35–2:55:** State measured results, present limitations and describe the next student pilot.

## Submission package

- Primary track: Alexa+ web simulated experience, subject to current event rules and timing eligibility.
- Repository: source, MIT licence, locked dependencies and reproducible instructions.
- Public English demo video under three minutes: record/upload separately after the demonstration is ready; no video has been uploaded by this implementation.
- Actual product feedback: official Python MCP server and TypeScript client interoperate with Streamable HTTP; application sessions are stored independently from transport sessions. Report the exact versions in the lockfiles.
- AWS Builder: claim a live service integration only after account setup and actual inference are verified; currently the Bedrock adapter is implemented but disabled.
- Open-source mini-challenge: requires a qualifying additional contribution; no upstream contribution is claimed here.
- Friction log: account sign-in returned a request error in an older flow; old account closure prevented reuse; macOS lock interrupted native browser automation. Describe these accurately without publishing emails, account IDs or authentication data.
