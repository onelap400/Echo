
# 400 m Projection App

A lightweight Streamlit dashboard that combines four projection models
(5×200 m, Fly 30 m, Split 400 m workout, and Anaerobic Speed Reserve)
into a single view. The underlying formulas were co‑developed with generative‑AI
(ChatGPT & Claude) during high‑performance planning for NCAA All‑American and
Olympic‑Trials athletes.

## Quick start (local)

```bash
pip install streamlit pandas
streamlit run app.py
```

## Deploy to Streamlit Cloud

1. Push this folder to a public GitHub repo.
2. Go to share.streamlit.io, select *New app* ➞ point to your repo ➞ *Deploy*.
3. Share the generated URL (e.g., `https://400m-projection.streamlit.app`) with reviewers.

## Data

Replace `data/sample_data.csv` with your real workout & race log.
Expected columns:

| column | example | description |
|--------|---------|-------------|
| athlete | George Franks | Athlete name |
| date | 2025-03-28 | Session date YYYY-MM-DD |
| fly30 | 2.72 | Fly‑30 time (s) |
| avg_200 | 23.38 | Average of 5×200 m reps (s) |
| split400_total | 44.80 | Total time of 2×200 m split‑400 workout (s) |
| asr_proj | 45.06 | Projection from Anaerobic Speed Reserve model (s) |
| actual_400 | 46.15 | Official race result, if available (s) |
