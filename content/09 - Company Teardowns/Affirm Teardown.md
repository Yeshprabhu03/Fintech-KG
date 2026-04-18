---
title: Affirm Teardown
tags: [teardown, bnpl, lending, consumer-credit]
domain: company-teardown
layer: application
source: Affirm investor relations, S-1 filing
last_reviewed: 2026-04-18
confidence: high
connections: [Credit Scoring Models, Embedded Finance Stack, Buy Now Pay Later, Securitization Basics]
---

# Affirm Teardown: Building a Better Credit Card

> ⚠️ Draft — needs verification against primary sources

Affirm (NASDAQ: AFRM) is the leading US-based "Buy Now, Pay Later" (BNPL) provider, founded in 2012 by Max Levchin (a PayPal co-founder). While BNPL is often criticized for encouraging consumer debt, Affirm has positioned itself as the "honest" alternative to credit cards. By rejecting late fees and using a transparent, simple-interest model, Affirm has built a premium brand that attracted massive partnerships with players like **Amazon, Shopify, and Peloton**.

## 1. The Model: Simple Interest vs. Late Fees
The core of Affirm’s value proposition is transparency. Unlike traditional credit cards or competitors like **Klarna** and **Afterpay** (which have historically relied on late fees for a significant portion of their revenue), Affirm famously **does not charge late fees**.

Instead, Affirm uses a **Simple Interest** model. When a user chooses Affirm at checkout:
- They are shown the exact total amount they will pay over the life of the loan.
- The interest is fixed and never "compounds" like a credit card.
- If a user misses a payment, the interest doesn't spike, and they are never charged a fee, though their ability to use Affirm in the future is suspended.

This "no surprises" approach is what allows Affirm to charge higher APRs (sometimes up to 30%+) while still maintaining high customer satisfaction scores (NPS).

## 2. Revenue Model: The Three-Legged Stool
Affirm’s income comes from three primary sources:
1. **Merchant Development Rate (MDR)**: Merchants pay Affirm a percentage of each transaction (typically 3-6%) to offer BNPL. Merchants are willing to pay this "subsidy" because BNPL dramatically increases "Average Order Value" (AOV) and conversion rates.
2. **Interest Income**: Revenue from the consumer loans that Affirm keeps on its balance sheet.
3. **Interchange (Affirm Card)**: As Affirm expands into the **Affirm Card** (a debit/credit hybrid), it captures standard interchange revenue when users use the card for non-BNPL purchases.

## 3. Funding & Securitization: The Lending Machine
Affirm is not a bank; it is a "balance sheet" lender that relies on capital markets to fund its growth. To avoid keeping all the risk of billions in loans, Affirm uses a complex **Securitization** model:
- **Warehouse Lines**: Affirm uses large credit lines from banks (like Goldman Sachs or Morgan Stanley) to fund the initial loan at the point of sale.
- **ABS (Asset-Backed Securities)**: Periodically, Affirm "bundles" thousands of its loans into a security and sells them to institutional investors. This allows Affirm to "recycle" its capital and move the credit risk off its balance sheet.
- **Whole Loan Sales**: Some partners (like Cross River Bank) originate the loans and keep them on their own books, with Affirm acting as the servicer and technology provider.

## 4. The Power of Partnerships: Amazon & Shopify
Two massive partnerships define Affirm’s market dominance:
- **Shopify (Shop Pay Installments)**: Affirm is the exclusive provider of BNPL for Shopify’s "Shop Pay" product. This gives Affirm instant access to millions of small and medium merchants.
- **Amazon**: Affirm became the first BNPL integration on Amazon in 2021. This partnership provided a massive boost to Affirm's **GMV (Gross Merchandise Volume)** and cemented its status as the "enterprise" choice for BNPL.

## 5. Unit Economics: The "RLTC" Metric
To understand Affirm, you must look at **Revenue Less Transaction Costs (RLTC)**. Because Affirm’s business involves expensive "Transaction Costs" (funding costs, processing fees, and the **Provision for Credit Losses**), "Total Revenue" is a misleading figure.
- **Provision for Losses**: Affirm must set aside money for every loan it expects will go unpaid. In 2023/2024, as inflation and rates rose, this provision became a key focus for analysts.
- **Funding Costs**: As interest rates (Fed Funds Rate) increased, the cost for Affirm to borrow money for its warehouse lines also increased, squeezing its "take rate."

## 6. Interest Rate Sensitivity & Regulatory Risk
Affirm is more sensitive to interest rates than many other fintechs. 
- **The "Squeeze"**: When rates rise, Affirm's funding costs go up instantly, but it cannot always raise the APRs it charges consumers (due to state-level usury caps). 
- **Credit Performance**: Higher rates often correlate with consumer stress. Affirm’s proprietary underwriting (which looks at SKU-level data—i.e., what exactly you are buying) is its primary defense against a "credit cycle" downturn.
- **CFPB Oversight**: In 2024, the CFPB issued guidance stating that BNPL providers should be treated more like credit card issuers, requiring them to follow similar dispute and disclosure rules. Affirm has generally welcomed this, as they already followed many of these practices.

## 7. The Affirm Card: Beyond Checkout
Affirm is currently in a "Stage 2" transition. The goal is to move from being a "Checkout Button" to an "Everyday Wallet." The **Affirm Card** allows users to pay for anything immediately (digital or physical) or "thin-file" it into a BNPL loan after the fact. This move into the "debit-card" space is a direct attempt to capture a greater share of customer wallet and compete with traditional banks for daily spending.

> ⚠️ Verify all figures against https://investors.affirm.com before publishing

## Connections
- Related: [[Credit Scoring Models]], [[Embedded Finance Stack]], [[Buy Now Pay Later mechanics]], [[Securitization basics]]
