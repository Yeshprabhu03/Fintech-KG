---
title: Payment tokenization
tags: [security, pci, tokens]
domain: payments
layer: infrastructure
source: needs verification
last_reviewed: 2026-04-18
confidence: stub
connections: []
---

# Payment tokenization

> ⚠️ Draft — needs verification against primary sources

## Summary
The process of replacing sensitive data (like a 16-digit Primary Account Number) with a non-sensitive equivalent, referred to as a token.

## Key Concepts
- **Network Tokens**: Tokens issued directly by Visa/Mastercard that remain constant even if the underlying card is reissued.
- **PCI DSS Scope Reduction**: How tokenization allows merchants to avoid storing sensitive PAN data on their own servers.
- **Credential on File (CoF)**: Enhancing recurring payment success rates through lifecycle-managed tokens.
- **Apple Pay & Google Pay**: How mobile wallets use device-specific tokens (DPANs) to authorize transactions without sharing the real card details.

## Connections
- Parent: [[Payments Infrastructure]]
- Related: [[Card Network Economics]], [[The fintech stack layers]]
