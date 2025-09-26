# 🔍 SEO Keyword AI Agent

## Overview
This project implements an AI-powered SEO Keyword Research Agent.
It accepts a seed keyword and returns keyword suggestions ranked by search volume and competition.

The workflow is built using **n8n** and a simple **Streamlit frontend** for user interaction.
- **Data Source (Demo):** SerpAPI (free tier, returns ~8 related searches)
- **Data Source (Production-ready):** Google Ads Keyword Planner API (requires developer token)

---

## 🚀 Features
- Accepts a seed keyword as input
- Fetches related keywords via SerpAPI
- Mock `search_volume` and `competition` values generated to simulate sorting
- Returns up to 50 suggestions (demo shows ~8–10 real results)
- Results shown via API (n8n webhook) and Streamlit table

---

## 📂 Files
- `app.py` – Streamlit UI (frontend for user input & output table)
- `n8n-workflow.json` – exported workflow (Webhook → SerpAPI → Function → Respond)
- `requirements.txt` – Python dependencies
- `development-plan.pdf` – one-page development plan
- `README.md` – project documentation

---

## ⚡ Demo Flow
1. User enters seed keyword in Streamlit app.
2. Streamlit calls n8n webhook.
3. n8n workflow → fetch keywords from SerpAPI → add mock metrics → sort → return JSON.
4. Streamlit displays results in a clean table.

---
