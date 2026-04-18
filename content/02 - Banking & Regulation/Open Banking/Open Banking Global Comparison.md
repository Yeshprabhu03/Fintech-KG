--- 
title: Open Banking Global Comparison
tags: [banking]
domain: banking
layer: infrastructure
last_reviewed: 2026-04-18
confidence: high
connections: []
---

# Open Banking Global Comparison

Open Banking—the principle that consumers own their financial data and should be able to share it with third parties via APIs—is transforming the competitive landscape of finance. However, different regions have taken radically different paths to implementation. This comparison is vital for understanding the [[Embedded Finance Stack]] on a global scale.

## Comparison of Models

### 1. The UK and EU (Regulatory-Led)
In the UK and EU (under PSD2/PSD3), open banking was mandated by regulators to increase competition. Banks were forced to provide APIs for data sharing and payment initiation. This has led to a robust ecosystem of TPPs (Third Party Providers) but has also been plagued by poor API performance and low consumer adoption.

### 2. The United States (Market-Led)
Until recently, the US was almost entirely market-led, with companies like Plaid and MX using "screen scraping" to access data. This is changing with the CFPB's upcoming rules under **Section 1033**, which will move the US toward a more structured API-first environment.

### 3. India (Infrastructure-Led)
India uses the **Account Aggregator (AA)** framework. Instead of bank-by-bank APIs, India built a centralized digital public infrastructure that allows users to share data across banks, insurers, and investment platforms with a single consent.
- **Relationship to UPI**: While [[UPI Architecture]] focus on *payments*, AA focuses on *data parity* for lending and wealth management.

## Strategic Implications
For builders in lending (the [[05 - Lending Infrastructure/Lending Infrastructure|Lending Infrastructure]]), open banking is a game-changer. It allows for "Cash-flow based underwriting" (using actual income/expense data) rather than just relying on a stagnant credit score.

In the EU/UK, Open Banking allows fintechs to bypass [[Card Network Economics]] by initiating a direct transfer from the customer's bank account at checkout. This "Pay-by-Bank" model is significantly cheaper for merchants but lacks the chargeback protection customers are used to with cards.

## Connections
- [[index|Back to Home]]
