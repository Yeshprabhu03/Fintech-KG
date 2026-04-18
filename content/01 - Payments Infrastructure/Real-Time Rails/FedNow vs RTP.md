--- 
title: FedNow vs RTP
tags: [payments]
domain: payments
layer: infrastructure
last_reviewed: 2026-04-18
confidence: high
connections: []
---

# FedNow vs RTP

The United States has historically lagged behind other nations (like India with [[UPI Architecture]]) in real-time payments. This changed with the launch of the **RTP network** by The Clearing House in 2017 and the **FedNow Service** by the Federal Reserve in 2023. While both provide instant clearing and settlement, they serve different segments of the banking ecosystem.

## Key Differences

| Feature | RTP (The Clearing House) | FedNow (Federal Reserve) |
| :--- | :--- | :--- |
| **Launch Year** | 2017 | 2023 |
| **Operator** | Private (Big Banks) | Public (Fed) |
| **Membership** | Open to all US FI's | Open to all US FI's |
| **Limit** | $1 Million per transaction | $500,000 (default) |

## Strategic Importance
1. **Liquidity Management**: Real-time payments require banks to manage liquidity 24/7/365, as settlement is instantaneous.
2. **Account Funding**: Fintechs can use instant rails to allow users to fund their accounts instantly from an external bank, reducing the "time to value" and the risk associated with ACH returns.
3. **The "Check Killing" Use Case**: Real-time rails are the best candidate to finally eliminate paper checks in B2B commerce, where settlement finality is crucial.

Compared to [[Card Network Economics|Legacy Card Loops]], these rails offer significantly lower costs for merchants. They also represent the domestic equivalent of what [[Stablecoin Settlement Mechanics]] aims to achieve globally.

However, moving money instantly requires more robust [[07 - Fraud & Risk/Fraud & Risk|Fraud & Risk]] controls. Unlike ACH, there is no "undo" button once an RTP or FedNow transaction is authorized. Settlement is final and irrevocable. As we have seen in global markets like India's [[UPI Architecture]], instant rails accelerate the velocity of money but also the velocity of social engineering fraud.

## Connections
- Parent: [[Payments Infrastructure]]
- Related: [[UPI Architecture]], [[Stablecoin Settlement Mechanics]]