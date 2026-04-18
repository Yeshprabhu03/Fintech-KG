---
title: Adyen Teardown
tags: [teardown, payments, enterprise, acquiring]
domain: company-teardown
layer: infrastructure
source: Adyen investor relations, public filings
last_reviewed: 2026-04-18
confidence: high
connections: [Card Network Economics, Four-Party Payment Model, Stripe Teardown, Acquiring Economics]
---

# Adyen Teardown: The Single Platform Powerhouse

> ⚠️ Draft — needs verification against primary sources

Adyen (AMS: ADYEN) is often described as the "most efficient machine in payments." Founded in Amsterdam in 2006 by Pieter van der Does and Arnout Schuijff, the company was built to solve the fragmentation of the global payment landscape. While companies like Stripe focused on developer accessibility for small businesses, Adyen focused on the complex plumbing required by the world’s largest enterprises. Today, Adyen processes hundreds of billions of euros in volume for global giants, maintaining a technical architecture that is widely considered the gold standard of the industry.

## 1. The Single Platform Architecture
Adyen’s core competitive advantage is its "Single Platform" philosophy. In the traditional payments world, a merchant typically has to deal with a web of intermediaries: a gateway (the digital checkout), a processor (the switch that routes data), and an acquirer (the bank that settles the funds). These systems often sit on legacy stacks, connected by brittle APIs and batch files.

Adyen replaced this entire chain with a single, modern tech stack. By building its own gateway, processor, and acquirer from the ground up, Adyen eliminated the technical debt and "latency tax" inherent in multi-vendor setups.
- **Improved Authorization Rates**: Because Adyen has a direct feedback loop from the networks to the gateway, it can optimize transactions in real-time to maximize successful payments.
- **Lower Maintenance**: A single integration gives a merchant access to hundreds of global payment methods and dozens of currencies.

## 2. Direct Network Connectivity & Bypassing Acquirers
Unlike many fintechs that sit on top of legacy banks, Adyen is a **licensed bank** in Europe and holds direct acquiring licenses in major markets like the US, Brazil, and Hong Kong. This allows them to connect directly to the card networks (Visa, Mastercard, etc.) without a "sponsor bank" intermediary.

By "owning the rail," Adyen gains deeper visibility into কেন transitions fail. They can provide granular data back to merchants—such as specific "decline codes" or "partial authorizations"—that traditional processors often lose in translation. This direct connectivity is what allows Adyen to offer its **RevenueProtect** suite, using cross-network data to differentiate between legitimate high-value customers and professional fraudsters.

## 3. Revenue Model: Interchange++, Fees, and Float
Adyen’s revenue model is designed for transparency and enterprise scale:
- **Interchange++ Pricing**: Unlike "flat-rate" models (e.g., Stripe’s 2.9% + 30c), Adyen typically uses Interchange++. The merchant pays the exact interchange rate set by the networks, the scheme fees, and a small Adyen-specific markup. This is highly attractive to high-volume merchants where basis points (0.01%) matter.
- **Processing Fees**: A fixed fee for every transaction processed, regardless of the outcome.
- **Settlement Float**: As a licensed bank, Adyen holds merchant funds for a short period before settling them. In a high-interest-rate environment, the interest earned on this "float" becomes a significant secondary revenue stream (often contributing 10-15% of EBITDA).

## 4. The Enterprise Focus: Why Not SMBs?
Adyen is famously disciplined about its customer base. They rarely serve small-to-medium businesses (SMBs) directly. The reason is simple: **Operational Efficiency**. 
Serving 10,000 small merchants requires a massive support and fraud-monitoring organization. Serving 100 global enterprises (like **Microsoft, Uber, or Spotify**) allows Adyen to maintain a lean headcount and high margins. This focus is reflected in their metrics: Adyen has some of the highest revenue-per-employee ratios in the entire tech sector.

## 5. Unified Commerce: The Offline-Online Bridge
One of Adyen’s biggest growth drivers is **Unified Commerce**. For a merchant like **Victoria's Secret** or **eBay**, having separate systems for "Online Sales" and "In-Store Terminals" is a nightmare for data reconciliation. 
Adyen provides a single system for both. A customer can buy something online and return it in-store, and Adyen’s system recognizes the transaction instantly. By late 2024, Adyen's in-person payment volume grew significantly, proving that their "single platform" thesis extends effectively into the physical world.

## 6. Adyen vs. Stripe: Technical & Philosophical Differences
While often compared, Adyen and Stripe move in different directions:
- **Stripe** is a "Platform for Platforms." It excels at ease-of-use, documentation, and the "long tail" of the internet. Stripe is an aggregator of thousands of small merchants.
- **Adyen** is a "Direct Infrastructure Player." It is for the CFO and the Head of Payments at a Fortune 500 company who wants to squeeze every basis point of margin out of their global processing.
- **Banking Status**: Adyen is a bank; Stripe is (primarily) a software layer that partners with banks (Wells Fargo, Goldman Sachs). This gives Adyen more control over the funds and a lower cost of capital.

## 7. Public Financials & The Amsterdam Listing
Adyen went public on the **Euronext Amsterdam** in 2018. Since then, it has been a favorite of European tech investors due to its consistent 20-30% growth and massive EBITDA margins (often exceeding 45%). However, the company faced a significant stock "crash" in 2023 following a period of slower growth and increased US competition, leading to a renewed focus on hiring and infrastructure to regain its competitive edge.

> ⚠️ Verify all figures against https://ir.adyen.com before publishing

## Connections
- Related: [[Card Network Economics]], [[Four-Party Payment Model]], [[Stripe Teardown]], [[Acquiring Economics]]
