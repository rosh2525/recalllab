# AWS support request — submitted

Subject: Account cannot invoke first-party Amazon Nova Lite in Bedrock

Hello AWS Support,

I am building an educational prototype and cannot invoke Amazon Nova Lite using my active AWS account. Please review whether account verification or another account-level Bedrock restriction is pending, and advise a resolution compatible with my current Free account plan.

Observed on 23 October 2026:

- Region: eu-north-1 (Europe / Stockholm).
- Model: amazon.nova-lite-v1:0.
- Temporary AWS CLI browser login and STS GetCallerIdentity succeed. The Python SDK can also authenticate.
- GetFoundationModelAvailability reports agreement AVAILABLE, entitlement AVAILABLE, region AVAILABLE, but authorizationStatus NOT_AUTHORIZED.
- The initial minimal Converse request failed with AccessDeniedException stating that my account is currently being verified, normally taking under two hours.
- A subsequent minimal Converse request failed with ValidationException: Operation not allowed.
- The Bedrock console says the Model access page has been retired and models are enabled automatically on first invocation.
- No successful inference response or token usage has been received.

Please confirm the specific restriction, whether verification needs action from me, and whether this model can be used on my current account plan. Please do not upgrade my plan or create paid resources.

Thank you.

---
Submitted with explicit user authorization on 23 October 2026 through AWS Support Center, Basic Support, Account and billing → Account Activation → Bedrock Allowlisting, severity General question, Web response. Submission was verified on the case details page with status Work in progress. No plan change or payment details were entered. The private case receipt is kept under data/ and excluded from the source package.
