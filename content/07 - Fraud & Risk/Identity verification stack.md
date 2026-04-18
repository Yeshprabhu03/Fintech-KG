---
title: Identity verification stack
tags: [fraud, risk, kyc, idv]
domain: fraud-risk
layer: infrastructure
source: needs verification
last_reviewed: 2026-04-18
confidence: stub
connections: []
---

# Identity verification stack

> ⚠️ Draft — needs verification against primary sources

## Summary
The combination of vendors and data sources used by fintechs to confirm that a person is who they claim to be during onboarding.

## Key Concepts
- **Document Verification**: Matching a user's selfie to an image of their government-issued ID (e.g., Jumio, Onfido).
- **Bureau & PII Matching**: Verifying Social Security Numbers, names, and addresses against credit bureau or utility data (e.g., LexisNexis, Alloy).
- **Liveness Detection**: Ensuring the user is a real person and not a photo, video, or deepfake during the selfie process.
- **Continuous IDV**: The movement toward re-verifying identity when a user performs a high-risk action, rather than just at onboarding.

## Connections
- Parent: [[Fraud & Risk]]
- Related: [[AML and KYC Infrastructure]], [[Synthetic identity fraud]]
