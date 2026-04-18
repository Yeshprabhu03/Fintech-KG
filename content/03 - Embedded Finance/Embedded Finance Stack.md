---
title: Embedded Finance Stack
tags: [embedded-finance, baas, stack, middleware]
domain: Embedded Finance
layer: infrastructure
source: industry research
last_reviewed: 2026-04-18
confidence: high
connections: [BaaS Licensing Models, Card Network Economics, Open Banking Global Comparison]
---

# Embedded Finance Stack

Embedded Finance is the integration of financial services into non-financial environments. This allows companies like Shopify, Uber, or Toast to offer bank accounts, cards, and loans to their customers at the exact moment of need. To build or understand these products, one must view them through the lens of a **three-layer technical and regulatory stack**.

## The Architecture: Three Layers

Every embedded finance product involves three structural layers: Infrastructure, Middleware, and Distribution.

### 1. Infrastructure (The Balance Sheet & License)
This is the bottom layer that holds the "charter" and the funds. Without this layer, no financial activity can legally occur.
- **Sponsor Banks**: These are the licensed entities (e.g., Evolve, Coastal Community, Cross River) that provide the regulatory umbrella and FDIC insurance. They handle the "heavy lifting" of capital requirements and regulatory reporting.
- **Card Networks**: Visa and Mastercard provide the rails for transactions.
- **Ledger Systems**: Traditional core banking systems (like Jack Henry or FIS) or modern cloud-native ledgers (like Lithic or Unit's internal ledger).

### 2. Middleware (The API Abstraction)
This layer acts as the bridge. It abstracts the "legacy" systems of the banks into modern, developer-friendly APIs. 
- **BaaS Providers**: Companies like **Unit, Treasury Prime, and Bond** (though many are shifting models). They bundle the bank relationship, KYC (Know Your Customer) systems, and transaction monitoring into a single integration.
- **Specialized Infrastructure**: 
    - **Issue/Processing**: Marqeta, Lithic, and Stripe Issuing.
    - **Data Aggregation**: Plaid, MX (see [[Open Banking Global Comparison]]).
    - **Lending-as-a-Service**: Canopy, Peach.

### 3. Distribution (The Platform)
This is the "consumer-facing" layer where the financial product actually lives. 
- **The Platform**: This is a non-fintech company with a high-trust, high-frequency relationship with its users. For example, Shopify uses embedded finance to offer "Shopify Balance" (bank accounts) and "Shopify Capital" (loans) to its merchants.
- **The Advantage**: Because the platform already has the user's data (sales history, customer behavior), they can underwrite credit and offer services more accurately and cheaper than a traditional bank.

## Value Capture: Who Makes Money?

The economics of the stack follow a "cascading" model:
1. **The Merchant/Consumer** pays a fee (e.g., MDR) or interest.
2. **The Platform (Distribution)** takes the largest cut as the "owner" of the customer.
3. **The Middleware** takes a software SaaS fee or a slice of the transaction basis points.
4. **The Bank (Infrastructure)** takes a small cut (bps) of the volume and keeps the "net interest margin" on the deposits held.

## Why This Matters for Fintech Builders

### The "Context over Product" Shift
Builders must realize that in embedded finance, the *context* of the transaction is more valuable than the *product* itself. A loan offered at the checkout of a Shopify store has a higher conversion and lower acquisition cost than a loan offered by a traditional bank via mail.

### Build vs. Buy in the Middleware Layer
As the [[BaaS Licensing Models|regulatory environment shifts]], many large platforms are moving away from all-in-one middleware providers and choosing to integrate "directly" with banks while using specialized vendors for specific parts of the stack (e.g., using Marqeta for cards only). This "unbundling" reduces dependency on a single vendor but increases the complexity of the internal engineering team. A canonical example of this transition is explored in the [[Stripe Teardown]].

### Data as the Moat
The true competitive advantage in the embedded finance stack is data. Platforms that can ingest data via [[Open Banking Global Comparison|Open Banking]] or internal sales data can offer "pre-approved" financial products, fundamentally changing the risk profile of the business. This becomes especially profitable when capturing [[Card Network Economics|Interchange Revenue]].

