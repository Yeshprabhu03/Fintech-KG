---
title: Card Network Economics
tags: [payments, economics, cards]
domain: Payments Infrastructure
layer: infrastructure
source: industry analysis
last_reviewed: 2026-04-18
confidence: high
connections: [Four-Party Payment Model, Stripe Teardown, Embedded Finance Stack]
---

# Card Network Economics

The economics of card networks—primarily dominated by Visa and Mastercard—represent one of the most successful and resilient "toll booth" business models in history. To understand how these networks make money, one must first understand the [[Four-Party Payment Model]], which separates the flow of data from the flow of funds.

## The Four-Party Model and the Fee Stack

In a typical card transaction, the "merchant discount rate" (MDR)—the total fee a merchant pays (often 2-3%)—is carved up among several participants. The card networks themselves do not actually "touch" the money in the sense of holding deposits or extending credit; instead, they act as the switch that facilitates the movement of value.

### 1. Interchange Fees
Interchange is the largest component of the MDR, typically accounting for 70-90% of the total fee. Crucially, **this fee is not kept by the card network.** It is paid by the **Acquirer** (the merchant's bank) to the **Issuer** (the cardholder's bank). Interchange is designed to incentivize banks to issue cards and to compensate them for the risk of fraud and the cost of credit. The card networks set the interchange rates, but they do not collect them.

### 2. Assessment Fees
This is the fee that Visa and Mastercard actually keep. It is a small percentage (typically around 0.11% to 0.15%) of the total transaction volume. These fees are charged to the acquirers and issuers for the right to use the network's brand and infrastructure.

### 3. Network Fees (Switching & Processing)
These are per-transaction fixed fees (e.g., $0.01 to $0.05) charged for the technical act of routing the authorization request and the settlement message. This is where the scale of the networks truly shines; with billions of transactions monthly, these fractions of a cent aggregate into massive high-margin revenue.

## Mechanics of Value Capture

Card networks operate as two-sided platforms. They must balance the needs of merchants (who want low fees and high acceptance) with the needs of cardholders and issuers (who want rewards, security, and ubiquity). 

Key players include:
- **Networks**: Visa, Mastercard, American Express (which operates a three-party model), Discover.
- **Issuers**: JPMorgan Chase, Citi, Capital One.
- **Acquirers/Processors**: Fiserv (First Data), FIS (Worldpay), and modern players like [[Stripe Teardown|Stripe]].

## Why This Matters for Fintech Builders

For builders in the [[Embedded Finance Stack]], card economics are the foundation of many revenue models. Neobanks and card-issuing startups often rely entirely on **Interchange Revenue Share**. By partnering with a bank and a processor (like Marqeta or Lithic), a fintech can capture a portion of the interchange fee every time their user swipes a card.

Understanding the "interchange leg" is critical for unit economics. For example, debit card interchange is often capped in the US (Durbin Amendment), while credit card interchange is not, leading to the proliferation of "credit-builder" cards in the fintech space.

Builders must also navigate the complexity of "Total Cost of Payments," which includes not just these network fees but also chargeback costs and PCI compliance. As seen in the [[Stripe Teardown|development of Stripe]], the goal for many modern platforms is to abstract this complexity away while capturing a piece of the pie.
