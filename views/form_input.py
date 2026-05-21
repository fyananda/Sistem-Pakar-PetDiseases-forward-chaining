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
    pilihan_hewan   = sorted(df["Jenis_Hewan"].dropna().unique().tolist())
    pilihan_kelamin = sorted(df["Jenis_Kelamin"].dropna().unique().tolist())
    opsi_ya_tidak   = ["Tidak", "Ya"]

    TIDAK_ADA = "— Tidak Ada —"

    # Gejala dropdown: HANYA gejala yang TIDAK punya kolom biner sendiri
    GEJALA_BINER_LABELS = {
        "Kehilangan Nafsu Makan",
        "Muntah",
        "Diare",
        "Batuk",
        "Kesulitan Bernafas",
        "Pincang",
        "Lesi Kulit",
        "Keluar Lendir Hidung",
        "Keluar Cairan Mata",
    }

    semua_gejala = set(
        df["Gejala_1"].dropna().tolist() +
        df["Gejala_2"].dropna().tolist() +
        df["Gejala_3"].dropna().tolist() +
        df["Gejala_4"].dropna().tolist()
    )
    # Hanya tampilkan di dropdown gejala yang tidak punya kolom biner
    pilihan_gejala = [TIDAK_ADA] + sorted(semua_gejala - GEJALA_BINER_LABELS)

    pilihan_durasi = [
        "— Tidak Ada —", "1 hari", "2 hari", "3 hari", "4 hari", "5 hari",
        "6 hari", "1 minggu", "2 minggu", "lebih dari 2 minggu"
    ]

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
    .section-header {
        font-size: 18px;
        font-weight: 600;
        color: #374151;
        margin-top: 10px;
        margin-bottom: 6px;
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
    st.markdown("<div class='subtitle'>Isi form di bawah sesuai kondisi hewan Anda</div>", unsafe_allow_html=True)

    # =========================
    # FORM UTAMA
    # =========================
    with st.form("form_diagnosa"):

        # ── Data Hewan ──────────────────────────────────────
        st.subheader("📋 Data Hewan")
        col1, col2 = st.columns(2)

        with col1:
            nama_hewan = st.text_input("Nama Hewan")
            jenis      = st.selectbox("Jenis Hewan", pilihan_hewan)
            usia       = st.number_input("Usia Hewan (tahun)", min_value=0)
            kelamin    = st.selectbox("Jenis Kelamin", pilihan_kelamin)

        with col2:
            berat  = st.number_input("Berat Badan (kg)", min_value=0.0, format="%.1f")
            suhu   = st.number_input("Suhu Tubuh (°C)", min_value=30.0, max_value=45.0, value=38.5, format="%.1f")
            detak  = st.number_input("Detak Jantung (bpm)", min_value=0)
            durasi = st.selectbox("Durasi Gejala", pilihan_durasi)

        st.markdown("---")

        # ── Gejala Klinis (Dropdown) ─────────────────────────
        st.subheader("🩺 Gejala Klinis")
        st.caption("Pilih gejala spesifik yang tidak tercantum di bagian bawah.")

        col3, col4 = st.columns(2)
        with col3:
            gejala1 = st.selectbox("Gejala 1 *", pilihan_gejala)
            gejala2 = st.selectbox("Gejala 2 (opsional)", pilihan_gejala)
        with col4:
            gejala3 = st.selectbox("Gejala 3 (opsional)", pilihan_gejala)
            gejala4 = st.selectbox("Gejala 4 (opsional)", pilihan_gejala)

        st.markdown("---")

        # ── Gejala Biner (Ya / Tidak) ────────────────────────
        st.subheader("✅ Gejala Tambahan")
        st.caption("Centang gejala yang dialami hewan.")

        b1, b2, b3 = st.columns(3)

        with b1:
            nafsu_makan        = st.radio("Kehilangan Nafsu Makan",  opsi_ya_tidak, horizontal=True)
            muntah             = st.radio("Muntah",                   opsi_ya_tidak, horizontal=True)
            diare              = st.radio("Diare",                    opsi_ya_tidak, horizontal=True)

        with b2:
            batuk              = st.radio("Batuk",                    opsi_ya_tidak, horizontal=True)
            sesak              = st.radio("Kesulitan Bernafas",       opsi_ya_tidak, horizontal=True)
            pincang            = st.radio("Pincang",                  opsi_ya_tidak, horizontal=True)

        with b3:
            lesi_kulit         = st.radio("Lesi Kulit",               opsi_ya_tidak, horizontal=True)
            keluar_lendir      = st.radio("Keluar Lendir Hidung",     opsi_ya_tidak, horizontal=True)
            keluar_cairan_mata = st.radio("Keluar Cairan Mata",       opsi_ya_tidak, horizontal=True)

        st.markdown("<br>", unsafe_allow_html=True)
        submitted = st.form_submit_button("🔍 Diagnosa Sekarang")

    # =========================
    # PROSES SETELAH SUBMIT
    # =========================
    if submitted:
        if not nama_hewan.strip():
            st.warning("⚠️ Nama hewan tidak boleh kosong.")
            return

        if gejala1 == TIDAK_ADA:
            st.warning("⚠️ Minimal **Gejala 1** harus diisi.")
            return

        def bersihkan(g):
            return None if g == TIDAK_ADA else g

        st.session_state["data_diagnosa"] = {
            "nama_hewan"          : nama_hewan,
            "jenis_hewan"         : jenis,
            "usia"                : usia,
            "jenis_kelamin"       : kelamin,
            "berat_badan"         : berat,
            "suhu_tubuh"          : suhu,
            "detak_jantung"       : detak,
            "durasi"              : bersihkan(durasi),
            "gejala_1"            : bersihkan(gejala1),
            "gejala_2"            : bersihkan(gejala2),
            "gejala_3"            : bersihkan(gejala3),
            "gejala_4"            : bersihkan(gejala4),
            "nafsu_makan"         : nafsu_makan,
            "muntah"              : muntah,
            "diare"               : diare,
            "batuk"               : batuk,
            "sesak_nafas"         : sesak,
            "pincang"             : pincang,
            "lesi_kulit"          : lesi_kulit,
            "keluar_lendir_hidung": keluar_lendir,
            "keluar_cairan_mata"  : keluar_cairan_mata,
        }
        st.session_state["sudah_diagnosa"] = True

        st.success("✅ Data berhasil diproses! Silakan buka menu **Hasil Diagnosa** di sidebar.")