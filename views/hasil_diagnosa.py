import streamlit as st
import pandas as pd
from engine.forward_chaining import jalankan_forward_chaining

# ============================================================
# CACHE DATASET — hanya load sekali selama sesi berjalan
# ============================================================

@st.cache_data
def load_data():
    return pd.read_csv("data/dataset_diagnosa_penyakit_hewan.csv")


def show_hasil_diagnosa():

    # ========================
    # CSS
    # ========================
    st.markdown("""
    <style>
    .hasil-title {
        text-align: center;
        font-size: 36px;
        font-weight: bold;
        color: #1f2937;
        margin-bottom: 6px;
    }
    .hasil-subtitle {
        text-align: center;
        color: #6b7280;
        margin-bottom: 30px;
    }
    .card-utama {
        background: white;
        border-left: 6px solid #2563eb;
        border-radius: 16px;
        padding: 24px 30px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        margin-bottom: 20px;
    }
    .card-utama .penyakit-nama {
        font-size: 26px;
        font-weight: bold;
        color: #1e40af;
    }
    .persen-badge {
        display: inline-block;
        background: #eff6ff;
        color: #1d4ed8;
        border: 1px solid #bfdbfe;
        border-radius: 999px;
        padding: 4px 14px;
        font-size: 13px;
        font-weight: 700;
        margin-bottom: 12px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='hasil-title'>🩺 Hasil Diagnosa</div>", unsafe_allow_html=True)
    st.markdown("<div class='hasil-subtitle'>Hasil analisis berdasarkan gejala yang diinput</div>",
                unsafe_allow_html=True)

    # ========================
    # CEK SESSION STATE
    # ========================
    if not st.session_state.get("sudah_diagnosa"):
        st.info("ℹ️ Belum ada data diagnosa. Silakan isi **Form Input** terlebih dahulu.")
        return

    data = st.session_state["data_diagnosa"]
    df   = load_data()

    # ========================
    # RINGKASAN DATA HEWAN
    # ========================
    st.subheader("📋 Data Hewan")

    col1, col2, col3 = st.columns(3)
    col1.metric("Nama Hewan",    data["nama_hewan"])
    col2.metric("Jenis Hewan",   data["jenis_hewan"])
    col3.metric("Jenis Kelamin", data["jenis_kelamin"])

    col4, col5, col6 = st.columns(3)
    col4.metric("Usia",         f'{data["usia"]} tahun')
    col5.metric("Berat Badan",  f'{data["berat_badan"]} kg')
    col6.metric("Suhu Tubuh",   f'{data["suhu_tubuh"]} °C')

    st.markdown("---")

    # ========================
    # RINGKASAN GEJALA
    # ========================
    st.subheader("🩺 Gejala yang Dilaporkan")

    gejala_klinis = [
        g for g in [
            data["gejala_1"], data["gejala_2"],
            data["gejala_3"], data["gejala_4"]
        ] if g
    ]
    gejala_tambahan = {
        "Nafsu Makan Hilang" : data["nafsu_makan"],
        "Muntah"             : data["muntah"],
        "Diare"              : data["diare"],
        "Batuk"              : data["batuk"],
        "Kesulitan Bernafas" : data["sesak_nafas"],
    }

    col_g1, col_g2 = st.columns(2)
    with col_g1:
        st.markdown("**Gejala Klinis**")
        if gejala_klinis:
            for g in gejala_klinis:
                st.markdown(f"✅ {g}")
        else:
            st.caption("Tidak ada gejala klinis yang dipilih.")
    with col_g2:
        st.markdown("**Gejala Tambahan**")
        for label, nilai in gejala_tambahan.items():
            icon = "✅" if nilai == "Ya" else "❌"
            st.markdown(f"{icon} {label}")

    st.markdown("---")

    # ========================
    # JALANKAN ENGINE
    # ========================
    st.subheader("🔬 Hasil Diagnosa")

    with st.spinner("Menganalisis gejala..."):
        hasil = jalankan_forward_chaining(data, df)

    # ========================
    # TIDAK ADA HASIL
    # ========================
    if not hasil:
        st.error("❌ Tidak ditemukan penyakit yang sesuai dengan gejala yang diinput.")
        st.markdown("**Saran:** Coba tambahkan gejala yang lebih spesifik atau "
                    "konsultasikan langsung ke dokter hewan.")

    else:
        # ========================
        # DIAGNOSA UTAMA (peringkat 1)
        # ========================
        top = hasil[0]

        st.markdown(f"""
        <div class="card-utama">
            <div class="persen-badge">🎯 Kecocokan Tertinggi: {top['kecocokan']}%</div>
            <div class="penyakit-nama">🦠 {top['penyakit']}</div>
            <p style="color:#6b7280; margin: 6px 0 14px 0;">
                Gejala cocok: <b>{top['gejala_cocok']}</b> dari <b>{top['total_rule']}</b> gejala dalam rule
            </p>
            <p><b>📖 Deskripsi:</b><br>{top['deskripsi']}</p>
            <p><b>💊 Saran:</b><br>{top['saran']}</p>
        </div>
        """, unsafe_allow_html=True)

        # ========================
        # TABEL SEMUA HASIL
        # ========================
        st.subheader("📋 Seluruh Kemungkinan Diagnosa")

        tabel = pd.DataFrame([{
            "Penyakit"        : h["penyakit"],
            "Kecocokan (%)"   : h["kecocokan"],
            "Gejala Cocok"    : h["gejala_cocok"],
            "Total Rule"      : h["total_rule"],
        } for h in hasil])

        st.dataframe(tabel, use_container_width=True, hide_index=True)

        # ========================
        # DIAGRAM BATANG
        # ========================
        st.subheader("📈 Diagram Tingkat Kecocokan")

        chart_df = tabel.set_index("Penyakit")[["Kecocokan (%)"]]
        st.bar_chart(chart_df)

        # ========================
        # DETAIL TIAP KEMUNGKINAN
        # (selain diagnosa utama)
        # ========================
        if len(hasil) > 1:
            with st.expander("📂 Lihat detail kemungkinan lainnya"):
                for h in hasil[1:]:
                    st.markdown(f"**🦠 {h['penyakit']}** — {h['kecocokan']}%")
                    st.markdown(f"_{h['deskripsi']}_")
                    st.markdown(f"💊 {h['saran']}")
                    st.markdown("---")

    # ========================
    # EXPANDER DATASET
    # ========================
    with st.expander("📁 Lihat Dataset"):
        st.dataframe(df, use_container_width=True)

    # ========================
    # TOMBOL ULANGI
    # ========================
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔄 Ulangi Diagnosa"):
        st.session_state["sudah_diagnosa"] = False
        st.session_state["data_diagnosa"]  = {}
        st.rerun()