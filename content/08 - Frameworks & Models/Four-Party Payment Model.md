--- 
title: Four-Party Payment Model
tags: [model]
domain: frameworks
layer: infrastructure
last_reviewed: 2026-04-18
confidence: high
connections: []
---

# Four-Party Payment Model

The Four-Party Model is the canonical framework for understanding how credit and debit card transactions are processed. It defines the relationships between the consumer, the merchant, and their respective banks, tied together by a central card network.

## The Participants
1. **The Cardholder (Consumer)**: The individual who uses a card to purchase goods or services.
2. **The Merchant**: The business that accepts the card as payment.
3. **The Issuer (Cardholder's Bank)**: The financial institution that provides the card to the consumer and handles the credit or debit processing.
4. **The Acquirer (Merchant's Bank)**: The financial institution that processes payments for the merchant.

*Note: The **Card Network** (e.g., Visa, Mastercard) sits in the center, acting as the switch and rule-maker but not directly holding funds.*

## Relationship to Other Rails
- **Card Economics**: This model is the physical architecture upon which [[Card Network Economics]] are built. 
- **Real-Time Rails**: Systems like [[FedNow vs RTP]] and India's [[UPI Architecture]] often attempt to strip away these intermediate layers to provide faster settlement at lower cost.
- **Risk Management**: Managing [[07 - Fraud & Risk/Fraud & Risk|Fraud & Risk]] on the consumer side.

## Connections
- Parent: [[Frameworks & Models]]
- Related: [[Card Network Economics]], [[Stripe Teardown]]