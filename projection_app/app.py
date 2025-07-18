
import streamlit as st
import pandas as pd
from models import project_5x200, project_fly30, project_split400, project_asr, combined_projection

st.set_page_config(page_title="400 m Projection Dashboard", layout="centered")

st.title("AI‑Assisted 400 m Projection Dashboard")

@st.cache_data
def load_data():
    return pd.read_csv("data/sample_data.csv")

df = load_data()

athletes = df['athlete'].unique()
athlete_sel = st.sidebar.selectbox("Select athlete", athletes)
date_sel = st.sidebar.selectbox("Select session date", df[df['athlete']==athlete_sel]['date'].unique())

row = df[(df['athlete']==athlete_sel) & (df['date']==date_sel)].iloc[0]

st.subheader(f"Projections for {athlete_sel} ({date_sel})")

proj_5x200 = project_5x200(row['avg_200'])
proj_fly30 = project_fly30(row['fly30'])
proj_split = project_split400(row['split400_total'])
proj_asr = project_asr(row['asr_proj'])
proj_combined = combined_projection(row)

data = {
    'Model': ['5×200 m', 'Fly 30 m', 'Split 400 m', 'ASR', 'Combined'],
    'Projection (s)': [proj_5x200, proj_fly30, proj_split, proj_asr, proj_combined]
}
proj_df = pd.DataFrame(data)
st.table(proj_df)

actual = row['actual_400']
if not pd.isna(actual):
    st.metric("Actual race time", f"{actual} s", delta=f"{round(actual - proj_combined,2)} s vs combined")
else:
    st.info("No actual race time recorded for this date.")

st.markdown("---")
st.caption("Formulas are illustrative. Update coefficients in models.py as your calibration evolves.")
