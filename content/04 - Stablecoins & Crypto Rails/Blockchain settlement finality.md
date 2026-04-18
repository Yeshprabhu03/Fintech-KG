---
title: Blockchain settlement finality
tags: [blockchain, settlement, latency]
domain: stablecoins
layer: infrastructure
source: needs verification
last_reviewed: 2026-04-18
confidence: stub
connections: []
---

# Blockchain settlement finality

> ⚠️ Draft — needs verification against primary sources

## Summary
The point at which a blockchain transaction is considered irreversible, comparing the "probabilistic" finality of Proof-of-Work to the "deterministic" finality of BFT-based systems.

## Key Concepts
- **Probabilistic Finality**: Why Bitcoin typically requires 6 confirmations (~60 minutes) to be considered settled.
- **Deterministic Finality**: Why modern Layer 1s (like Solana, Avalanche, or Ethereum post-Merge) can achieve settlement in seconds.
- **Block Reorganizations (Reorgs)**: The risk of a network switching to a longer chain, which could orphan and revert previously "confirmed" blocks.
- **Fintech Implications**: Why payment apps must balance the speed of "confirming" a user's transaction with the technical risk of the transaction being reverted.

## Connections
- Parent: [[Stablecoins & Crypto Rails]]
- Related: [[Clearing and Settlement]], [[Real-Time Rails]]
