import streamlit as st

st.set_page_config(
    page_title="MediScan AI | About",
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

st.markdown('<div class="page-title">About MediScan AI</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">End-to-end drug interaction prediction and analytics project.</div>',
    unsafe_allow_html=True
)

st.markdown("## Project Summary")

st.write(
    """
    MediScan AI is a Data Science and Machine Learning project built to predict
    drug-drug interaction types using the DrugBank DDI dataset.
    
    The project covers the complete machine learning lifecycle, including data understanding,
    cleaning, exploratory data analysis, feature engineering, model training, model evaluation,
    hyperparameter tuning, explainability, and web application deployment.
    """
)

st.markdown("## Technologies Used")

st.write(
    """
    - Python
    - Pandas
    - NumPy
    - Scikit-learn
    - XGBoost
    - Plotly
    - Streamlit
    - ReportLab
    - Joblib
    - Git and GitHub
    """
)

st.markdown("## Machine Learning Workflow")

st.write(
    """
    1. Load DrugBank DDI dataset
    2. Clean missing and duplicate values
    3. Perform EDA
    4. Encode drug names and interaction labels
    5. Train multiple models
    6. Compare performance
    7. Tune Random Forest
    8. Deploy best model in Streamlit
    """
)

st.markdown("## Limitation")

st.warning(
    """
    This model uses only drug names as input features. It does not include chemical structures,
    dosage, patient health data, clinical history, or molecular fingerprints.
    
    Therefore, MediScan AI is suitable for educational and research demonstration only.
    It must not be used for real medical decisions.
    """
)

st.markdown("## Future Improvements")

st.write(
    """
    - Add molecular fingerprint features
    - Include drug class and therapeutic category
    - Add SHAP explainability
    - Improve rare class prediction
    - Add clinical risk severity levels
    - Improve UI with authentication and history tracking
    """
)