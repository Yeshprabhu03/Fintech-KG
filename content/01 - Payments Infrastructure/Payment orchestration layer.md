---
title: Payment orchestration layer
tags: [orchestration, middleware, payments]
domain: payments
layer: infrastructure
source: needs verification
last_reviewed: 2026-04-18
confidence: stub
connections: []
---

# Payment orchestration layer

> ⚠️ Draft — needs verification against primary sources

## Summary
The software layer that connects merchants to multiple payment processors and gateways, allowing for smart routing, redundancy, and unified reporting.

## Key Concepts
- **Dynamic Routing**: Automatically sending a transaction to the processor most likely to authorize it (or the one with the lowest fee).
- **Merchant Independence**: Avoiding vendor lock-in by decoupling the frontend payment UI from the backend processor.
- **Failover & Redundancy**: Automatically switching providers if one gateway goes down during peak traffic.
- **Vaulting**: Storing customer payment tokens in an independent vault so they can be used across multiple processors.

## Connections
- Parent: [[Payments Infrastructure]]
- Related: [[The fintech stack layers]], [[Acquiring economics]]
