# Product feedback and friction log

These are development observations from this project. No Fire TV, Bee, Ring, Kiro or native Alexa+ tests are claimed.

## Tools and services used

| Tool / API | Use and what worked | Improvement and onboarding | Use again? |
| --- | --- | --- | --- |
| MCP Python SDK / FastMCP | Four synchronous study tools served through stateless Streamable HTTP. Official clients discover and invoke them. | Make the distinction between protocol sessions and durable app sessions more prominent in examples. We kept learner state in SQLite. | Yes |
| MCP TypeScript SDK | The React interface performs actual tool calls, including retries using stable request IDs. | Provide a compact example handling both structuredContent and JSON text tool results, plus transport error recovery. | Yes |
| Amazon Bedrock Converse / Nova Lite | A bounded conceptual-assessment adapter is implemented; model and region appear available. | Authentication succeeds but invocation is denied. Surface account eligibility and verification reasons beside the model action, with one route to the correct support category. No successful inference is claimed. | Reassess after access clears |
| AWS CLI browser login / boto3 | Named short-lived profile works in CLI and Python without permanent access keys. | The SDK initially needed botocore[crt]; mention this alongside CLI login examples. Root login inherits broad permissions; a scoped development identity remains necessary for sustained cloud use. | Yes, with scoped access |
| Browser SpeechRecognition / speechSynthesis | Optional editable input and read-aloud are implemented alongside typing. | Availability varies; microphone trial has not been performed. Explain provider processing before use and preserve typed text when recognition cannot start. | Yes, with fallback |
| FastAPI / SQLite / SymPy / React / Vite | Local hosting, transactional persistence, deterministic checking and a production interface work together. | Restrict learner maths syntax before constructing symbolic expressions. Build output and tests are reproducible through the release script. | Yes |

## Friction log

| Task and reproduction | Expected | Observed | Severity | Workaround | Actionable request |
| --- | --- | --- | --- | --- | --- |
| Reuse an old AWS identity; inspect closure notices after failed sign-in | Clear account state | A prior account was permanently closed; a separate active account was needed | Blocking for that identity | Verify account status before registration | Show a direct, non-ambiguous account-closure explanation in sign-in recovery |
| Sign in using an older console redirect | Normal root sign-in | Request error in the older flow | Important | Start from the current console sign-in flow | Preserve a recovery link when redirect state is invalid |
| Use CLI browser login from Python boto3 | Same temporary provider works in both | MissingDependencyException until botocore[crt] was installed | Important | Add the official dependency and verify STS | Document the dependency next to browser-login setup |
| Inspect Nova Lite, run a five-token Converse request | Either usable model or explicit prerequisite | Availability NOT_AUTHORIZED; initial account-verification denial; later generic Operation not allowed | Blocking | Submitted Basic Support case under Account Activation → Bedrock Allowlisting; AWS declined access; keep local maths available | Expose the remaining verification state and support route in the catalog; preserve the specific error across retries |
| Consume official MCP tool results in browser | Discoverable typed payload | This implementation returns JSON text; client also supports structuredContent | Important | Decode both supported forms | Provide a minimal interoperable browser/server example |
| Run native browser setup with Mac locking | Uninterrupted setup while connected to power | Lock screen interrupted interaction | Minor | Temporary keep-awake; user unlock | No AWS defect claimed |

## Feature requests

1. **Critical:** Explain Bedrock account-level denial in the model catalog, with the current verification state and exact remediation route.
2. **Important:** A temporary CLI-login guide that includes boto3 dependencies, identity permissions and credential lifetime together.
3. **Important:** An MCP browser study-workflow sample covering durable application state, idempotent calls and both result formats.
4. **Nice-to-have:** A reference Alexa+ web simulation for keyboard-only and voice-unavailable flows, without requiring partner-gated native access.

No private account IDs, email addresses, authentication data or student responses belong in public feedback attachments.
