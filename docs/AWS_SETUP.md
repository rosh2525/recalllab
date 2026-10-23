# AWS setup status and safe next steps

## Status, 23 October 2026

- Browser sessions and the relevant AWS emails were inspected.
- A previous account associated with the student's institutional email was permanently closed on 15 May 2026. AWS's earlier notice says its Free Plan credits had run out. The closed account cannot be reopened.
- The user subsequently signed into a separate AWS account in Firefox and the in-app browser. The console confirmed an active Free Plan with $100 credits and 183 days remaining. The user approved temporary CLI/SDK developer sign-in and Nova Lite model terms. The named `recalllab` profile authenticated successfully in both AWS CLI and boto3 after installing the official `botocore[crt]` dependency; no long-term access keys were created.
- No payment method, bank account, card information or UPI details have been entered. No paid plan is authorized.
- Nova Lite (`amazon.nova-lite-v1:0`) is region-available in Stockholm (`eu-north-1`), but its availability API returned `authorizationStatus: NOT_AUTHORIZED`. One minimal Converse request (five output tokens maximum) failed with `AccessDeniedException`: the account is currently being verified. AWS says verification normally takes under two hours; if the same error persists longer, contact `aws-verification@amazon.com`. No model response or token usage was returned.
- A subsequent retry still returned `NOT_AUTHORIZED`; the minimal Converse retry returned `ValidationException: Operation not allowed`. The console states that the Model access activation page is retired and serverless models are automatically enabled on first invocation. There is no manual enablement action offered there. The latest generic error does not prove whether verification has finished or a separate account restriction remains.
- With explicit user authorization, an AWS Support case was submitted under Account Activation → Bedrock Allowlisting. The case details page confirmed Work in progress; replies are delivered through email and Support Center. No support-plan upgrade was selected.
- AWS Support replied on 23 October 2026 that it cannot approve Bedrock access at this time and that access may change automatically later. A subsequent five-token retry still returned Operation not allowed. The application remains in local mode with Bedrock disabled; no plan change or payment details were entered. A paid-plan upgrade is not established as necessary by this error and was not attempted.

Personal emails, account IDs, OTPs and identity documents are not stored in this repository.

## Setup sequence

1. Check the existing-account path before registering a duplicate. A different email does not reset Free Tier eligibility.
2. If registration is appropriate, use the user's requested personal address. Verify email using the requested inbox. User creates and submits any new password.
3. Review the plan actually offered. Do not select a paid plan or enter payment information. Account terms require the user's acceptance at the relevant step.
4. If payment or identity-document verification is mandatory, stop that step. There is no need to block local development.
5. The active account is now verified. A named `recalllab` AWS CLI browser-login flow has been started in Stockholm (`eu-north-1`). Its final credential permission was explicitly approved by the user and sign-in succeeded. This session inherits the selected identity’s permissions; the current selection is root. No root access keys are created. Prefer a restricted development identity for sustained use. Verify Nova access before choosing the inference model/region.
6. After account verification completes, retry the small smoke test. Set a low app request limit, verify account credits/billing controls, then explicitly enable `RECALLLAB_ENABLE_BEDROCK=1` and perform one conceptual assessment.

AWS Educate offers free learning/labs; institutional email alone does not guarantee personal AWS credits. Do not promise Free Tier access or cloud inference costs without inspecting the actual account.

References:
- https://aws.amazon.com/free/free-tier-faqs/
- https://aws.amazon.com/education/awseducate/
- https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html
