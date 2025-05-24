
import streamlit as st
from PIL import Image

st.set_page_config(page_title="M Yahya Firza Afitian", layout="wide")

col1, col2 = st.columns([1, 3])

with col1:
    image = Image.open("assets/profile.jpg")
    st.image(image, width=200)

with col2:
    st.title("M Yahya Firza Afitian, S.Si.")
    st.markdown("""
    **📍 Cirebon, 45192**  
    **📧 Email:** fafitian@gmail.com  
    **📱 Telepon:** (+62) 85156281876  
    **🔗 LinkedIn:** [linkedin.com/in/myahyafirzaafitian10](https://linkedin.com/in/myahyafirzaafitian10)
    """)
    st.markdown("---")
    st.subheader("Ringkasan Profesional")
    st.write("""
    Lulusan Matematika dari Universitas Ahmad Dahlan (IPK 3.79) dengan minat kuat dalam Data Science & Data Analysis.
    Menguasai pengolahan data, analisis statistik, visualisasi data, dan model prediktif dengan Python, R, dan SQL.
    Berpengalaman dalam peran laboratorium, HR, dan pengajaran, serta memegang sertifikasi Associate Data Scientist dari BNSP.
    """)

st.markdown("---")
st.write("🔍 Gunakan menu di sebelah kiri untuk menelusuri proyek, keterampilan, dan pengalaman saya.")
