# RecallLab submission copy

## Project name
RecallLab

## Tagline
Explain it. Practise it. Prove you understand it.

## What it does
RecallLab is a voice-and-screen study companion for mathematics for economics. Students make an attempt before opening reviewed hints or solutions. They can check numerical and polynomial answers locally, explain a concept in their own words, revisit source notes, and complete five different questions with feedback withheld until the check ends.

The dashboard separates questions explored, assistance used and independent results. A suggested review queue brings back ideas that needed help. The first module covers 12 concepts, 25 practice questions and five independent check questions.

## Inspiration
A student can recognise a worked solution and still struggle to produce one independently. RecallLab makes that distinction visible. Its central example asks whether a zero derivative necessarily proves a maximum. A graph and reviewed hints help the student examine that claim before trying a different problem without help.

This is a product hypothesis, not a claim that RecallLab improves learning. Student interviews, a small pilot and a next-day follow-up are prepared but have not been conducted.

## How we built it
The interface uses React, Vite and TypeScript. It calls a real MCP server through the official TypeScript SDK and Streamable HTTP. Four tools start or resume a session, submit an attempt, request reviewed help and retrieve progress. FastAPI hosts the interface and FastMCP endpoint together. SQLite stores attempts, assistance, content versions and model usage.

A bounded AST grammar assembles SymPy expressions directly; learner text is never executed as Python. Session updates use SQLite transactions, and request IDs make duplicate submissions idempotent.

The optional Bedrock Converse adapter uses Amazon Nova Lite for conceptual answers. It accepts only a validated rubric assessment and reviewed misconception IDs. The server renders authored feedback and original source references. Unsupported output or service errors abstain. Keys stay in the backend.

## Current working demo
The local learning loop, symbolic maths checks, hints, original source notes, saved sessions, review queue and independent checks work without cloud access. Optional speech input leaves an editable transcript and never submits automatically. Unsupported recognition falls back to typing.

AWS temporary CLI and SDK authentication work, but Bedrock invocation is blocked by an account restriction. AWS Support declined the access request, and the latest retry is still blocked. Conceptual answers are therefore saved explicitly for self-review. No successful live inference, model accuracy or cloud-cost claim is made.

## Challenges and lessons
MCP transport sessions and durable study sessions serve different purposes. Keeping learner state in SQLite allows resume after reconnecting. Another challenge was keeping independent-check results hidden across every endpoint, not just the visible feedback panel. Model outputs also needed a narrow, validated schema: free-form generated feedback would make reviewed content and citations harder to trust.

## What is next
Resolve AWS access, run and inspect the live conceptual benchmark, obtain independent label review, and run the five-person pilot. Then revise misleading feedback and observe next-day independent performance. Public hosting, additional subjects and native Alexa+ integration are later work.

## Built with
React · TypeScript · Vite · Python · FastAPI · SQLite · MCP Python SDK / FastMCP · MCP TypeScript SDK · SymPy · boto3 · Amazon Bedrock Converse adapter

## Tracks and evidence
Primary intended track: Alexa+ web simulation, with real MCP in action. AWS Builder remains pending successful integration evidence. No additional open-source contribution is claimed.

## Required links before submitting
- GitHub repository URL: https://github.com/rosh2525/recalllab
- Public English YouTube or Vimeo demo URL: pending actual recording/upload.
- Product feedback: copy the verified entries in PRODUCT_FEEDBACK.md.

Official requirements checked 23 October 2026: https://amazonappdev2026.devpost.com/. They request source/instructions in GitHub, an English public video under three minutes, and product feedback. Confirm current eligibility and reviewer access at submission time. This file is prepared copy, not a submitted entry.
