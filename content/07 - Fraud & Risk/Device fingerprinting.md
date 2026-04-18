---
title: Device fingerprinting
tags: [fraud, security, risk]
domain: fraud-risk
layer: infrastructure
source: needs verification
last_reviewed: 2026-04-18
confidence: stub
connections: []
---

# Device fingerprinting

> ⚠️ Draft — needs verification against primary sources

## Summary
The process of gathering specific hardware and software attributes of a user's device (browser version, OS, IP address, screen resolution) to create a unique identifier for fraud detection.

## Key Concepts
- **Velocity Checks**: Detecting when many different accounts are accessed from the exact same physical device in a short time.
- **Bot Detection**: Identifying non-human browsing patterns and "headless" browsers used for mass account creation.
- **Signal Quality**: The trade-off between privacy-preserving identifiers (like Apple's IDFA) and the high-fidelity signals needed to stop fraud.
- **Network Effects**: Cross-platform fraud detection where a device flagged on one fintech app is automatically blocked on others.

## Connections
- Parent: [[Fraud & Risk]]
- Related: [[Account takeover patterns]], [[Synthetic identity fraud]]
