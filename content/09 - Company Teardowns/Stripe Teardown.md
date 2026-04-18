---
title: Stripe Teardown
tags: [teardown, payments, infrastructure, stripe]
domain: Company Teardowns
layer: application
source: primary research & public docs
last_reviewed: 2026-04-18
confidence: high
connections: [Card Network Economics, Embedded Finance Stack, BaaS Licensing Models]
---

# Stripe Teardown

Stripe is the canonical example of a "developer-first" fintech. It succeeded not by inventing a new payment rail, but by building a "Global Payments and Treasury Network" (GPTN) that abstracts the incredible complexity of the legacy [[Card Network Economics|card world]] into a few lines of code.

## The Foundation: Decoupling Complexity

### 1. The Gateway + Processor
When Stripe started, a merchant needed a **Gateway** (the "terminal" that sends data) and a **Merchant Account** (the bank relationship). Stripe bundled these. By acting as a **Payment Facilitator (PayFac)**, Stripe could onboard thousands of sub-merchants under its own master merchant account, eliminating the weeks-long approval process traditional banks required.

### 2. High-Fidelity Data
Most traditional processors lose data as it travels through the [[Four-Party Payment Model]]. Stripe built its own "issuer-side" integrations to keep data fidelity high. This allowed them to build higher-value products like **Radar** (fraud detection) and **Adaptive Acceptance** (retrying declined transactions in ways that are more likely to succeed).

## The Revenue Model

Stripe's core model is a classic "Take Rate":
- **Payments**: Typically 2.9% + $0.30. They pay out the interchange and network fees (often ~2.2%) and keep the remaining spread (~0.7%).
- **Software as a Service (SaaS)**: Products like **Billing**, **Tax**, and **Revenue Recognition** are charged as a percentage of volume (e.g., 0.5%) or per-active-user. These are significantly higher margin than the payments leg.
- **Financial Services**: Products like **Stripe Capital** (lending) and **Stripe Treasury** (BaaS) represent the next frontier, where they capture interest margin and banking fees.

## The Strategic Moats

### The API as the Brand
Stripe's greatest moat was its focus on the developer. By winning the "integration" battle at the startup level, they ensured that as those startups (like Shopify, Lyft, and DoorDash) grew into giants, Stripe's infrastructure grew with them.

### Vertical Integration
Stripe is slowly becoming its own bank without actually having a bank charter. Through products like **Stripe Issuing** and **Stripe Treasury**, they provide the full [[Embedded Finance Stack]] to their customers. They partner with banks (Goldman Sachs, Evolve) for the license but own the ledger and the developer experience.

## Why This Matters for Fintech Builders

### The "Stripe-ification" of Everything
Every modern fintech is essentially trying to "Stripe-ify" a different legacy rail.
- **Unit/Treasury Prime** are "Stripe for Bank Accounts."
- **Bond/Canopy** are "Stripe for Credit Cards."
- **Lithic** is "Stripe for Card Issuing."

### Lesson: Start as a Wedge, Grow into an OS
Stripe started as a simple "Pay" button. They used that wedge to capture transactional data, which they then used to build a "Financial Operating System." This is the blueprint for the [[Embedded Finance Stack]]: capture the flow of money first, then provide the tools to manage and grow that money.

### The Aggregator Risk
For builders, relying on Stripe is a double-edged sword. It is the fastest way to market, but as a PayFac, Stripe has total control over your business. If your business model is deemed "high risk," Stripe can freeze your funds instantly. This is why many "Scale-ups" eventually move to a direct-to-acquirer model to reduce "platform risk."
