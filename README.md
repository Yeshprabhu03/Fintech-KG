# Fintech Brain

A freely accessible knowledge vault mapping the infrastructure layer of global finance — payments rails, embedded finance, stablecoins, banking regulation, card networks, and tokenization.

Built for fintech operators, founders, investors, and anyone who wants to understand how money actually moves.

**Live site:** [yeshprabhu03.github.io/Fintech-KG](https://yeshprabhu03.github.io/Fintech-KG)

---

## What's inside

| Domain | Focus |
|--------|-------|
| Payments Infrastructure | Card networks, real-time rails, cross-border |
| Banking & Regulation | Licensing, Basel III, open banking |
| Embedded Finance | BaaS, lending-as-a-service |
| Stablecoins & Crypto Rails | USDC, USDT, settlement mechanics |
| Capital Markets | Clearing, settlement, prime brokerage |
| Fraud & Risk | AML, KYC, fraud scoring |
| Company Teardowns | Stripe, Wise, Plaid, Nubank |
| Frameworks & Models | Mental models for fintech analysis |

---

## How it evolves

- **Weekly auto-ingestion** — Python + Gemini pulls from BIS, Fed, CFPB, and fintech publications. Summarizes into draft notes. Human reviews before publish.
- **Decay scoring** — Every note has a `last_reviewed` date. Notes older than 180 days are flagged in the Needs Review dashboard.
- **Event-triggered updates** — When a regulation passes or a major fintech event happens, existing notes are diffed against new information via `scripts/event_update.py`.

---

## Run locally

```bash
npm install
npx quartz build --serve
```

```bash
pip install -r requirements.txt
cp .env.example .env   # add your GEMINI_API_KEY
python scripts/decay_check.py
python scripts/ingest.py
```

---

## Stack

| Layer | Tool |
|-------|------|
| Authoring | Obsidian (local) |
| Publishing | Quartz 4 |
| Hosting | GitHub Pages |
| Automation | Python + Gemini + GitHub Actions |

---

Built by [Yeshprabhu](https://github.com/Yeshprabhu03) — part of a long-term journey into fintech infrastructure.
