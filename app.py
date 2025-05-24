import streamlit as st
from PIL import Image
import plotly.express as px

# Konfigurasi halaman
st.set_page_config(
    page_title="Portofolio M Yahya Firza Afitian",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load gambar profil
try:
    image = Image.open("assets/profile.jpg")
except:
    image = None

# Sidebar navigasi
st.sidebar.title("📁 Navigasi")
menu = st.sidebar.radio("Pilih Halaman", ["Beranda", "Pengalaman", "Proyek", "Kontak"])

# Warna dan style
st.markdown("""
    <style>
    .main {background-color: #f5f7fa;}
    .css-1v0mbdj, .css-1d391kg {font-family: 'Segoe UI', sans-serif;}
    </style>
""", unsafe_allow_html=True)

# Konten halaman
if menu == "Beranda":
    st.title("👋 Selamat Datang di Portofolio Saya")
    col1, col2 = st.columns([1, 3])
    if image:
        col1.image(image, width=150)
    col2.markdown("""
        ### M Yahya Firza Afitian, S.Si
        Lulusan Matematika dengan minat besar dalam **Data Science & Data Analysis**. 
        Berpengalaman dalam Python, SQL, Machine Learning, dan Visualisasi Data.
    """)
    st.markdown("---")
    st.subheader("📌 Ringkasan Keahlian")
    st.markdown("""
    - Python, R, SQL
    - Machine Learning, Deep Learning
    - Power BI, Tableau, Excel, Jupyter, RStudio
    - Regresi, Klasifikasi, Clustering, Data Cleaning
    """)

elif menu == "Pengalaman":
    st.title("💼 Pengalaman Kerja & Organisasi")
    st.markdown("### Laboratory Analyst – PT Long Rich Indonesia (2024 - Sekarang)")
    st.markdown("- Uji kualitas bahan sepatu berdasarkan standar ASICS.")
    st.markdown("### HRD – A.S.S Toserba Losari (2024)")
    st.markdown("- Mengelola sistem SDM dan proses rekrutmen.")
    st.markdown("### Mentor – PSDS UAD Yogyakarta (2023)")
    st.markdown("- Mengajar Python & Machine Learning.")
    st.markdown("---")
    st.markdown("### Organisasi")
    st.markdown("- Ketua Umum HMPS Matematika UAD (2021-2022)")
    st.markdown("- Kepala Divisi PBSDM (2020-2021)")

elif menu == "Proyek":
    st.title("📊 Proyek & Visualisasi")
    df = px.data.iris()
    fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", title="Contoh Visualisasi Proyek")
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("### Klasifikasi Gambar dengan CNN")
    st.markdown("- Skripsi: *CNN dengan Aktivasi untuk Citra Noisy Poisson*")
    st.markdown("- Framework: TensorFlow, Keras")
    st.markdown("### Lainnya")
    st.markdown("- Dashboard Analisis Penjualan dengan Power BI")
    st.markdown("- Model Regresi Prediksi Harga")

elif menu == "Kontak":
    st.title("📬 Kontak Saya")
    st.markdown("""
    - 📍 **Cirebon, 45192**
    - 📧 [fafitian@gmail.com](mailto:fafitian@gmail.com)
    - 📱 +62 851 5628 1876
    - 💼 [LinkedIn](https://linkedin.com/in/myahyafirzaafitian10)
    """)
