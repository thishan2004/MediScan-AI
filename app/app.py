import streamlit as st

st.set_page_config(
    page_title="MediScan AI",
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

    .hero {
        padding: 55px;
        border-radius: 24px;
        background: linear-gradient(135deg, #0F766E, #2563EB);
        color: white;
        text-align: center;
        margin-bottom: 35px;
    }

    .hero h1 {
        font-size: 56px;
        font-weight: 800;
        margin-bottom: 10px;
    }

    .hero h3 {
        font-size: 26px;
        font-weight: 500;
        margin-bottom: 15px;
    }

    .hero p {
        font-size: 17px;
        color: #E0F2FE;
    }

    .metric-card {
        padding: 28px;
        border-radius: 18px;
        background-color: #FFFFFF;
        box-shadow: 0 8px 20px rgba(0,0,0,0.18);
        text-align: center;
    }

    .metric-title {
        font-size: 17px;
        color: #475569;
        margin-bottom: 8px;
    }

    .metric-value {
        font-size: 34px;
        font-weight: 800;
        color: #0F766E;
    }

    .section-title {
        font-size: 34px;
        font-weight: 800;
        margin-top: 35px;
        margin-bottom: 18px;
        color: #F8FAFC;
    }

    .feature-card {
        padding: 25px;
        border-radius: 18px;
        background-color: #111827;
        border: 1px solid #1E293B;
        min-height: 170px;
    }

    .feature-card h4 {
        color: #38BDF8;
        margin-bottom: 10px;
    }

    .feature-card p {
        color: #CBD5E1;
        font-size: 15px;
    }

    .workflow-box {
        padding: 25px;
        border-radius: 18px;
        background-color: #111827;
        border: 1px solid #1E293B;
        text-align: center;
        color: #E2E8F0;
        font-size: 18px;
        font-weight: 600;
    }

    .disclaimer {
        padding: 18px;
        border-radius: 14px;
        background-color: #132F4C;
        color: #BFDBFE;
        margin-top: 35px;
        font-size: 15px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="hero">
        <h1>MediScan AI</h1>
        <h3>Drug–Drug Interaction Prediction & Clinical Risk Analytics Platform</h3>
        <p>Machine learning powered healthcare intelligence system for drug interaction research and analytics.</p>
    </div>
    """,
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(
        """
        <div class="metric-card">
            <div class="metric-title">Dataset Records</div>
            <div class="metric-value">222K+</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div class="metric-card">
            <div class="metric-title">Interaction Classes</div>
            <div class="metric-value">114</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        """
        <div class="metric-card">
            <div class="metric-title">Best Model</div>
            <div class="metric-value">RF</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col4:
    st.markdown(
        """
        <div class="metric-card">
            <div class="metric-title">Weighted F1</div>
            <div class="metric-value">52.1%</div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown('<div class="section-title">About MediScan AI</div>', unsafe_allow_html=True)

st.write(
    """
    MediScan AI is an end-to-end data science project designed to predict drug-drug
    interaction types using machine learning. The project includes dataset cleaning,
    exploratory data analysis, feature engineering, model comparison, hyperparameter
    tuning, final evaluation, and deployment through a healthcare-themed web application.
    """
)

st.markdown('<div class="section-title">Key Features</div>', unsafe_allow_html=True)

f1, f2, f3, f4 = st.columns(4)

with f1:
    st.markdown(
        """
        <div class="feature-card">
            <h4>Drug Interaction Prediction</h4>
            <p>Select two drugs and predict the possible interaction type using the trained Random Forest model.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with f2:
    st.markdown(
        """
        <div class="feature-card">
            <h4>Analytics Dashboard</h4>
            <p>Explore interaction classes, frequent drugs, class imbalance, and dataset-level patterns.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with f3:
    st.markdown(
        """
        <div class="feature-card">
            <h4>Model Performance</h4>
            <p>Compare Logistic Regression, Decision Tree, Random Forest, and XGBoost using multiple metrics.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with f4:
    st.markdown(
        """
        <div class="feature-card">
            <h4>Report Generation</h4>
            <p>Generate a downloadable prediction report for selected drug combinations.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown('<div class="section-title">Machine Learning Workflow</div>', unsafe_allow_html=True)

w1, w2, w3, w4, w5 = st.columns(5)

with w1:
    st.markdown('<div class="workflow-box">Drug Selection</div>', unsafe_allow_html=True)

with w2:
    st.markdown('<div class="workflow-box">Feature Encoding</div>', unsafe_allow_html=True)

with w3:
    st.markdown('<div class="workflow-box">Random Forest Model</div>', unsafe_allow_html=True)

with w4:
    st.markdown('<div class="workflow-box">Interaction Prediction</div>', unsafe_allow_html=True)

with w5:
    st.markdown('<div class="workflow-box">Clinical Insight</div>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="disclaimer">
        <strong>Disclaimer:</strong> MediScan AI is built for educational and research purposes only.
        It must not be used as a clinical decision-making tool or as a replacement for professional medical advice.
    </div>
    """,
    unsafe_allow_html=True
)