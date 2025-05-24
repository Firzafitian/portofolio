
import streamlit as st
import plotly.express as px
from PIL import Image

# ===== CONFIGURASI =====
st.set_page_config(page_title="Portfolio | M. Yahya Firza Afitian", page_icon="📊", layout="wide")

# ===== SIDEBAR =====
st.sidebar.image("assets/profile.jpg", width=150)
st.sidebar.title("📌 Navigasi")
menu = st.sidebar.radio("Pilih Halaman:", ["Tentang Saya", "Proyek", "Keahlian", "Pengalaman", "Kontak"])

# ===== HEADER UMUM =====
def header():
    st.markdown("""
        <style>
        .main-title {
            font-size: 2.5rem;
            font-weight: 700;
            color: #ff6f61;
        }
        .subtitle {
            font-size: 1.2rem;
            color: #666;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="main-title">M Yahya Firza Afitian, S.Si</div>
    <div class="subtitle">Data Analyst | Data Scientist | Machine Learning Enthusiast</div>
    """, unsafe_allow_html=True)
    st.write("📍 Cirebon | 📧 fafitian@gmail.com | [LinkedIn](https://linkedin.com/in/myahyafirzaafitian10)")

# ===== HALAMAN TENTANG SAYA =====
def about():
    header()
    st.write("""
    Lulusan Matematika dari Universitas Ahmad Dahlan dengan IPK 3.79. Memiliki ketertarikan kuat terhadap data science dan data analysis. Menguasai Python, R, SQL, serta alat visualisasi seperti Tableau dan Power BI. Berpengalaman dalam pengolahan data, analisis statistik, dan machine learning.
    """)

# ===== HALAMAN PROYEK =====
def projects():
    header()
    st.subheader("🧠 Daftar Proyek")
    proyek = [
        {"nama": "Analisis Sentimen Twitter", "deskripsi": "Menggunakan NLP untuk klasifikasi sentimen publik."},
        {"nama": "Dashboard Penjualan Retail", "deskripsi": "Menggunakan Power BI untuk visualisasi penjualan dan profit margin."},
        {"nama": "Model Prediksi Harga Rumah", "deskripsi": "Menggunakan regresi linier dan random forest pada dataset housing."}
    ]
    for p in proyek:
        with st.expander(p["nama"]):
            st.write(p["deskripsi"])

# ===== HALAMAN KEAHLIAN =====
def skills():
    header()
    st.subheader("📊 Komposisi Keahlian")
    data = {"Python": 30, "SQL": 25, "R": 15, "Excel": 10, "Power BI": 20}
    fig = px.pie(names=list(data.keys()), values=list(data.values()), title="Skill Set")
    st.plotly_chart(fig)

# ===== HALAMAN PENGALAMAN =====
def experience():
    header()
    st.subheader("💼 Pengalaman Kerja")
    st.markdown("""
    **Laboratory Analyst – PT Long Rich Indonesia** (Nov 2024 – Sekarang)  
    Melakukan pengujian dan analisis bahan sepatu untuk standar kualitas ASICS.

    **HRD – A.S.S Toserba Losari** (Jan 2024 – Nov 2024)  
    Menangani rekrutmen, penggajian, dan administrasi BPJS.

    **Asisten Praktikum & Mentor PSDS – UAD Yogyakarta**  
    Mengajar Python, optimisasi, dan machine learning pada mahasiswa.
    """)

# ===== HALAMAN KONTAK =====
def contact():
    header()
    st.subheader("📬 Hubungi Saya")
    with st.form("contact_form"):
        nama = st.text_input("Nama")
        email = st.text_input("Email")
        pesan = st.text_area("Pesan")
        submit = st.form_submit_button("Kirim")
        if submit:
            st.success("Pesan berhasil dikirim! (simulasi)")

# ===== RENDER SESUAI MENU =====
if menu == "Tentang Saya":
    about()
elif menu == "Proyek":
    projects()
elif menu == "Keahlian":
    skills()
elif menu == "Pengalaman":
    experience()
elif menu == "Kontak":
    contact()
