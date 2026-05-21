import streamlit as st
import pandas as pd

def show_form_input():

    # =========================
    # LOAD DATASET
    # =========================
    df = pd.read_csv("data/dataset_diagnosa_penyakit_hewan.csv")

    # =========================
    # DATA PILIHAN
    # =========================
    pilihan_hewan    = sorted(df["Jenis_Hewan"].dropna().unique().tolist())
    pilihan_kelamin  = sorted(df["Jenis_Kelamin"].dropna().unique().tolist())
    pilihan_gejala   = sorted(set(
        df["Gejala_1"].dropna().tolist() +
        df["Gejala_2"].dropna().tolist() +
        df["Gejala_3"].dropna().tolist() +
        df["Gejala_4"].dropna().tolist()
    ))
    opsi_ya_tidak = ["Ya", "Tidak"]

    # =========================
    # CUSTOM CSS
    # =========================
    st.markdown("""
    <style>
    .title {
        text-align: center;
        font-size: 42px;
        font-weight: bold;
        color: #1f2937;
    }
    .subtitle {
        text-align: center;
        color: #6b7280;
        margin-bottom: 30px;
    }
    .stButton>button {
        width: 100%;
        background-color: #2563eb;
        color: white;
        border-radius: 12px;
        height: 50px;
        font-size: 18px;
        font-weight: bold;
        border: none;
    }
    .stButton>button:hover {
        background-color: #1d4ed8;
    }
    </style>
    """, unsafe_allow_html=True)

    # =========================
    # HEADER
    # =========================
    st.markdown("<div class='title'>🐾 Sistem Diagnosa Penyakit Hewan</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Form Diagnosa Hewan Berbasis Streamlit</div>", unsafe_allow_html=True)

    # =========================
    # FORM UTAMA
    # =========================
    with st.form("form_diagnosa"):
        st.subheader("📋 Data Hewan")
        col1, col2 = st.columns(2)

        with col1:
            nama_hewan = st.text_input("Nama Hewan")
            jenis      = st.selectbox("Jenis Hewan", pilihan_hewan)
            usia       = st.number_input("Usia Hewan (tahun)", min_value=0)
            kelamin    = st.selectbox("Jenis Kelamin", pilihan_kelamin)

        with col2:
            berat = st.number_input("Berat Badan (kg)", min_value=0.0, format="%.1f")
            suhu  = st.number_input("Suhu Tubuh (°C)", min_value=30.0, max_value=45.0, value=38.5, format="%.1f")
            detak = st.number_input("Detak Jantung (bpm)", min_value=0)

        st.markdown("---")
        st.subheader("🩺 Gejala Klinis")

        col3, col4 = st.columns(2)
        with col3:
            gejala1     = st.selectbox("Gejala 1", pilihan_gejala)
            gejala2     = st.selectbox("Gejala 2", pilihan_gejala)
            nafsu_makan = st.radio("Nafsu Makan Hilang", opsi_ya_tidak, horizontal=True)
            muntah      = st.radio("Muntah", opsi_ya_tidak, horizontal=True)

        with col4:
            gejala3 = st.selectbox("Gejala 3", pilihan_gejala)
            gejala4 = st.selectbox("Gejala 4", pilihan_gejala)
            diare   = st.radio("Diare", opsi_ya_tidak, horizontal=True)
            batuk   = st.radio("Batuk", opsi_ya_tidak, horizontal=True)

        sesak = st.radio("Kesulitan Bernafas", opsi_ya_tidak, horizontal=True)

        st.markdown("<br>", unsafe_allow_html=True)
        submitted = st.form_submit_button("🔍 Diagnosa Sekarang")

    # =========================
    # PROSES SETELAH SUBMIT
    # =========================
    if submitted:
        # Validasi nama hewan tidak kosong
        if not nama_hewan.strip():
            st.warning("⚠️ Nama hewan tidak boleh kosong.")
            return

        # Simpan semua input ke session_state
        # agar bisa dibaca oleh halaman hasil_diagnosa
        st.session_state["data_diagnosa"] = {
            "nama_hewan"    : nama_hewan,
            "jenis_hewan"   : jenis,
            "usia"          : usia,
            "jenis_kelamin" : kelamin,
            "berat_badan"   : berat,
            "suhu_tubuh"    : suhu,
            "detak_jantung" : detak,
            "gejala_1"      : gejala1,
            "gejala_2"      : gejala2,
            "gejala_3"      : gejala3,
            "gejala_4"      : gejala4,
            "nafsu_makan"   : nafsu_makan,
            "muntah"        : muntah,
            "diare"         : diare,
            "batuk"         : batuk,
            "sesak_nafas"   : sesak,
        }
        st.session_state["sudah_diagnosa"] = True

        st.success("✅ Data berhasil diproses! Silakan buka menu **Hasil Diagnosa** di sidebar.")