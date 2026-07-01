import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="MediScan AI | Analytics",
    page_icon="M",
    layout="wide"
)

st.markdown(
    """
    <style>
    .stApp {
        background-color: #0B1117;
        color: #F8FAFC;
    }
    .page-title {
        font-size: 42px;
        font-weight: 800;
        color: #F8FAFC;
        margin-bottom: 10px;
    }
    .subtitle {
        font-size: 17px;
        color: #CBD5E1;
        margin-bottom: 30px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="page-title">Analytics Dashboard</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Explore DrugBank DDI dataset patterns and interaction insights.</div>',
    unsafe_allow_html=True
)

@st.cache_data
def load_dataset():
    return pd.read_csv("data/processed/cleaned_DDI_data.csv")

df = load_dataset()

col1, col2, col3 = st.columns(3)

col1.metric("Total Records", f"{len(df):,}")
col2.metric("Interaction Classes", df["interaction_type"].nunique())
col3.metric("Unique Drugs", pd.concat([df["drug1_name"], df["drug2_name"]]).nunique())

st.markdown("## Top 20 Interaction Types")

top_interactions = df["interaction_type"].value_counts().head(20)

fig1 = px.bar(
    x=top_interactions.values,
    y=top_interactions.index,
    orientation="h",
    labels={"x": "Number of Records", "y": "Interaction Type"},
    color=top_interactions.values,
    color_continuous_scale="Tealgrn"
)

fig1.update_layout(
    height=700,
    yaxis={"categoryorder": "total ascending"}
)

st.plotly_chart(fig1, use_container_width=True)

st.markdown("## Top 20 Most Frequent Drugs")

all_drugs = pd.concat([df["drug1_name"], df["drug2_name"]])
top_drugs = all_drugs.value_counts().head(20)

fig2 = px.bar(
    x=top_drugs.values,
    y=top_drugs.index,
    orientation="h",
    labels={"x": "Frequency", "y": "Drug Name"},
    color=top_drugs.values,
    color_continuous_scale="Tealgrn"
)

fig2.update_layout(
    height=700,
    yaxis={"categoryorder": "total ascending"}
)

st.plotly_chart(fig2, use_container_width=True)

st.markdown("## Class Imbalance Analysis")

interaction_counts = df["interaction_type"].value_counts()

fig3 = px.bar(
    x=list(range(len(interaction_counts))),
    y=interaction_counts.values,
    labels={
        "x": "Interaction Classes Sorted by Frequency",
        "y": "Number of Records"
    },
    color=interaction_counts.values,
    color_continuous_scale="Tealgrn"
)

st.plotly_chart(fig3, use_container_width=True)

st.info(
    "The dataset is highly imbalanced: a few interaction classes contain many records, while many classes are rare."
)