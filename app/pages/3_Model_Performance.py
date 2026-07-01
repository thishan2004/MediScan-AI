import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="MediScan AI | Model Performance",
    page_icon="M",
    layout="wide"
)

st.markdown(
    """
    <style>
    .stApp { background-color: #0B1117; color: #F8FAFC; }
    .page-title { font-size: 42px; font-weight: 800; color: #F8FAFC; margin-bottom: 10px; }
    .subtitle { font-size: 17px; color: #CBD5E1; margin-bottom: 30px; }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="page-title">Model Performance</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Evaluation results of machine learning models trained for drug interaction prediction.</div>',
    unsafe_allow_html=True
)

results_df = pd.read_csv("reports/model_comparison.csv")
final_metrics = pd.read_csv("reports/final_model_metrics.csv")
feature_importance = pd.read_csv("reports/feature_importance.csv")

st.markdown("## Final Selected Model")

col1, col2, col3 = st.columns(3)

col1.metric("Accuracy", f"{final_metrics.loc[0, 'Accuracy'] * 100:.2f}%")
col2.metric("Macro F1", f"{final_metrics.loc[0, 'Macro F1'] * 100:.2f}%")
col3.metric("Weighted F1", f"{final_metrics.loc[0, 'Weighted F1'] * 100:.2f}%")

st.markdown("## Model Comparison")

st.dataframe(results_df, use_container_width=True)

fig1 = px.bar(
    results_df,
    x="Model",
    y="Accuracy",
    color="Accuracy",
    color_continuous_scale="Tealgrn",
    title="Accuracy Comparison"
)
fig1.update_layout(title_x=0.5)
st.plotly_chart(fig1, use_container_width=True)

fig2 = px.bar(
    results_df,
    x="Model",
    y="Weighted F1",
    color="Weighted F1",
    color_continuous_scale="Tealgrn",
    title="Weighted F1 Comparison"
)
fig2.update_layout(title_x=0.5)
st.plotly_chart(fig2, use_container_width=True)

st.markdown("## Feature Importance")

fig3 = px.bar(
    feature_importance,
    x="Importance",
    y="Feature",
    orientation="h",
    color="Importance",
    color_continuous_scale="Tealgrn",
    title="Feature Importance"
)
fig3.update_layout(title_x=0.5)
st.plotly_chart(fig3, use_container_width=True)

st.info(
    "Random Forest was selected as the final model because it achieved the best overall performance after comparison and tuning."
)