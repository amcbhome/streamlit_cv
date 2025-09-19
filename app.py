import streamlit as st
from pathlib import Path

# --- PAGE CONFIG ---
st.set_page_config(page_title="Alastair McBride - CV", page_icon=":briefcase:", layout="wide")

# --- DOWNLOAD CV ---
cv_file = Path("Alastair_McBride_CV.pdf")  # Place your CV PDF in the same folder
with open(cv_file, "rb") as pdf_file:
    CV_BYTES = pdf_file.read()

# --- HEADER ---
st.title("Alastair McBride")
st.subheader("Accounting Graduate | Xero Advisor Certified | Data & Financial Analytics")
st.write("📍 Kilmarnock, Scotland | 📧 amcb.home@gmail.com | 📞 07895 770 953")
st.download_button(
    label="📄 Download CV (PDF)",
    data=CV_BYTES,
    file_name="Alastair_McBride_CV.pdf",
    mime="application/pdf",
)

st.markdown("---")

# --- ABOUT ---
st.header("About Me")
st.write(
    """
    I am a BAcc (Hons) Accounting graduate (2:1 expected) from the University of the West of Scotland, 
    with certifications in Xero Advisor and QuickBooks Online. I combine a strong foundation in 
    financial reporting, bookkeeping, and payroll with practical skills in Python for accounting analytics, 
    including portfolio modelling, optimisation, and dashboard development.

    I am seeking Accounts Assistant and Graduate Scheme opportunities in practice (audit, advisory, tax) 
    or industry (assistant accountant, payroll, purchase ledger), with the goal of progressing towards ACCA/CIMA/ACA qualification.
    """
)

# --- EDUCATION & CERTIFICATIONS ---
st.header("Education & Certifications")

st.subheader("🎓 University of the West of Scotland (2021–2025)")
st.write("BAcc (Hons) Accounting, 2:1 expected")
st.write("Key modules: Public Sector Accounting, Management Accounting, Python for Accounting, Dissertation on AI in Accounting")

st.subheader("🎓 Ayrshire College (2019–2021)")
st.write("HND Accounting")

st.subheader("📜 Certifications")
st.write("- Xero Advisor Certified (2022)")
st.write("- QuickBooks Online Certified ProAdvisor (2022)")
st.write("- Xero Payroll Certified (in progress)")

# --- EXPERIENCE ---
st.header("Experience")

with st.expander("Atlas FM, Kilmarnock – Cleaner (2025–Present)"):
    st.write(
        """
        - Maintained high hygiene and safety standards in compliance with regulations.  
        - Followed strict protocols, demonstrating accuracy and attention to detail.  
        - Worked independently with accountability and reliability.  
        """
    )

with st.expander("Quality Control Inspector – Various Employers (5 years)"):
    st.write(
        """
        - Conducted compliance checks and ensured accuracy in production environments.  
        - Investigated discrepancies and documented findings, building audit/finance transferable skills.  
        - Strengthened analytical ability through process monitoring and reporting.  
        """
    )

with st.expander("Cleaning Roles – Various Employers (10 years)"):
    st.write(
        """
        - Delivered consistent service quality across multiple sites while meeting deadlines.  
        - Demonstrated reliability, commitment, and strong work ethic.  
        - Built teamwork and communication skills while balancing multiple commitments.  
        """
    )

# --- PROJECTS ---
st.header("Projects (Interactive & GitHub Links)")

st.markdown(
    """
    - **[Portfolio Optimiser (Streamlit App)](https://share.streamlit.io/amcbhome/portfolio_app)**  
      Built in Python using pandas and NumPy; calculates portfolio risk, return, and efficient frontier.  

    - **[Delivery Schedule Optimisation (GitHub Repo)](https://github.com/amcbhome/delivery_schedule_test)**  
      Linear programming model to minimise delivery costs under constraints.  

    - **[FX Time Series Dashboard (Streamlit App)](https://share.streamlit.io/amcbhome/fx-timeseries-app)**  
      Live exchange rate visualisation with statistical analysis.  

    - **[Management Accounting Forecasting (GitHub Repo)](https://github.com/amcbhome/linear_regression)**  
      Regression-based cost forecaster with charts and variance analysis.  
    """
)

# --- SKILLS ---
st.header("Skills")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Accounting & Finance")
    st.write("Bookkeeping, Payroll Processing, Ledger Management, Reconciliations, Financial Reporting, Budgeting")

    st.subheader("Software")
    st.write("Xero (Advisor Certified), QuickBooks (Certified), Sage, MS Excel (PivotTables, Formulas)")

with col2:
    st.subheader("Analytics")
    st.write("Python for Accounting & Data Analytics, Linear Programming, Portfolio Modelling, Dashboards")

    st.subheader("Professional")
    st.write("Attention to Detail, Compliance Awareness, Process Efficiency, Time Management, Teamwork")

