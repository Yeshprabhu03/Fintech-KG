---
title: Account takeover patterns
tags: [fraud, security, ato]
domain: fraud-risk
layer: infrastructure
source: needs verification
last_reviewed: 2026-04-18
confidence: stub
connections: []
---

# Account takeover patterns

> ⚠️ Draft — needs verification against primary sources

## Summary
The methods and signals used by malicious actors to gain unauthorized access to an existing customer's financial account.

## Key Concepts
- **Credential Stuffing**: Using leaked usernames and passwords from other data breaches to try and access the target fintech app.
- **SIM Swapping**: Social engineering a mobile carrier to move a user's phone number to a new card to intercept SMS-based MFA.
- **Anomalous Behavior**: Detecting access from a new device, a new IP address, or a sudden change in transaction patterns (e.g., changing the email address or password immediately before a large withdrawal).
- **MFA Bypass**: Using phishing sites or "push fatigue" (spamming a user with MFA push notifications until they approve one) to bypass multi-factor authentication.

## Connections
- Parent: [[Fraud & Risk]]
- Related: [[Device fingerprinting]], [[Identity verification stack]]
