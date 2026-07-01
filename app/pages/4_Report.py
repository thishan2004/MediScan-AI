import streamlit as st
import pandas as pd
import joblib
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

st.set_page_config(
    page_title="MediScan AI | Report",
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

st.markdown('<div class="page-title">Prediction Report Generator</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Generate a downloadable PDF report for a selected drug pair prediction.</div>',
    unsafe_allow_html=True
)

@st.cache_data
def load_dataset():
    return pd.read_csv("data/processed/cleaned_DDI_data.csv")

@st.cache_resource
def load_model_and_encoders():
    model = joblib.load("models/best_model.pkl")
    drug_encoder = joblib.load("models/drug_encoder.pkl")
    target_encoder = joblib.load("models/target_encoder.pkl")
    return model, drug_encoder, target_encoder

def generate_pdf(drug1, drug2, interaction):
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)

    pdf.setTitle("MediScan AI Prediction Report")

    pdf.setFont("Helvetica-Bold", 20)
    pdf.drawString(60, 740, "MediScan AI Prediction Report")

    pdf.setFont("Helvetica", 12)
    pdf.drawString(60, 700, f"Drug 1: {drug1}")
    pdf.drawString(60, 675, f"Drug 2: {drug2}")
    pdf.drawString(60, 650, f"Predicted Interaction Type: {interaction}")

    pdf.drawString(60, 600, "Model: Tuned Random Forest")
    pdf.drawString(60, 575, "Dataset: DrugBank Drug-Drug Interaction Dataset")

    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(60, 520, "Disclaimer")

    pdf.setFont("Helvetica", 10)
    disclaimer = (
        "This report is generated for educational and research purposes only. "
        "It must not be used as medical advice or clinical decision support."
    )

    text = pdf.beginText(60, 500)
    text.setFont("Helvetica", 10)

    for line in disclaimer.split(". "):
        text.textLine(line)

    pdf.drawText(text)

    pdf.save()
    buffer.seek(0)

    return buffer

df = load_dataset()
model, drug_encoder, target_encoder = load_model_and_encoders()

drug_list = sorted(pd.concat([df["drug1_name"], df["drug2_name"]]).unique())

col1, col2 = st.columns(2)

with col1:
    drug1 = st.selectbox("Select First Drug", drug_list)

with col2:
    drug2 = st.selectbox("Select Second Drug", drug_list)

if st.button("Generate Prediction Report", use_container_width=True):

    if drug1 == drug2:
        st.warning("Please select two different drugs.")
    else:
        drug1_encoded = drug_encoder.transform([drug1])[0]
        drug2_encoded = drug_encoder.transform([drug2])[0]

        input_data = pd.DataFrame({
            "drug1_name": [drug1_encoded],
            "drug2_name": [drug2_encoded]
        })

        prediction = model.predict(input_data)[0]
        interaction = target_encoder.inverse_transform([prediction])[0]

        st.success(f"Predicted Interaction: {interaction}")

        pdf_file = generate_pdf(drug1, drug2, interaction)

        st.download_button(
            label="Download PDF Report",
            data=pdf_file,
            file_name="mediscan_ai_prediction_report.pdf",
            mime="application/pdf",
            use_container_width=True
        )