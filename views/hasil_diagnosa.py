import streamlit as st
import pandas as pd
import os
from datetime import datetime
from engine.forward_chaining import jalankan_forward_chaining

# ============================================================
# CACHE DATASET
# ============================================================

@st.cache_data
def load_data():
    return pd.read_csv("data/dataset_diagnosa_penyakit_hewan.csv")


# ============================================================
# SIMPAN KE HISTORY CSV
# ============================================================

def simpan_ke_history(data: dict, hasil: list):
    history_path = "history_diagnosis.csv"
    top = hasil[0] if hasil else {}

    baris = {
        "Tanggal"          : datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Nama Hewan"       : data.get("nama_hewan", ""),
        "Jenis Hewan"      : data.get("jenis_hewan", ""),
        "Jenis Kelamin"    : data.get("jenis_kelamin", ""),
        "Usia (tahun)"     : data.get("usia", ""),
        "Berat (kg)"       : data.get("berat_badan", ""),
        "Suhu (°C)"        : data.get("suhu_tubuh", ""),
        "Detak (bpm)"      : data.get("detak_jantung", ""),
        "Gejala 1"         : data.get("gejala_1", ""),
        "Gejala 2"         : data.get("gejala_2", ""),
        "Gejala 3"         : data.get("gejala_3", ""),
        "Gejala 4"         : data.get("gejala_4", ""),
        "Hasil Diagnosa"   : top.get("penyakit", "Tidak ditemukan"),
        "Kecocokan (%)"    : top.get("kecocokan", 0),
        "Jumlah Kandidat"  : len(hasil),
    }

    df_baris = pd.DataFrame([baris])

    if os.path.exists(history_path):
        df_existing = pd.read_csv(history_path)
        df_updated  = pd.concat([df_existing, df_baris], ignore_index=True)
    else:
        df_updated = df_baris

    df_updated.to_csv(history_path, index=False)


def show_hasil_diagnosa():

    # ========================
    # CSS
    # ========================
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }

    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
        max-width: 1100px !important;
    }

    /* ── PAGE HEADER ── */
    .page-header { margin-bottom: 28px; }
    .page-header-title {
        font-size: 28px;
        font-weight: 800;
        color: #0f172a;
        letter-spacing: -0.02em;
        margin-bottom: 4px;
    }
    .page-header-sub { font-size: 14px; color: #64748b; }

    /* ── EMPTY STATE (sama persis dengan history) ── */
    .empty-state {
        text-align: center;
        padding: 64px 24px;
        background: #f8fafc;
        border: 1px dashed #cbd5e1;
        border-radius: 20px;
        margin-top: 8px;
    }
    .empty-icon  { font-size: 48px; margin-bottom: 16px; }
    .empty-title { font-size: 18px; font-weight: 700; color: #1e293b; margin-bottom: 6px; }
    .empty-desc  { font-size: 14px; color: #64748b; }

    /* ── RESULT CARD ── */
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

    # ── PAGE HEADER ──────────────────────────────────────────
    st.markdown("""
    <div class="page-header">
        <div class="page-header-title">🩺 Hasil Diagnosa</div>
        <div class="page-header-sub">Hasil analisis berdasarkan gejala yang diinput</div>
    </div>
    """, unsafe_allow_html=True)

    # ========================
    # CEK SESSION STATE → EMPTY STATE
    # ========================
    if not st.session_state.get("sudah_diagnosa"):
        st.markdown("""
        <div class="empty-state">
            <div class="empty-icon">📋</div>
            <div class="empty-title">Belum Ada Data Diagnosa</div>
            <div class="empty-desc">Silakan isi <strong>Form Input</strong> terlebih dahulu untuk memulai diagnosa.</div>
        </div>
        """, unsafe_allow_html=True)
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
    col4.metric("Usia",        f'{data["usia"]} tahun')
    col5.metric("Berat Badan", f'{data["berat_badan"]} kg')
    col6.metric("Suhu Tubuh",  f'{data["suhu_tubuh"]} °C')

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
    # SIMPAN KE HISTORY (sekali per sesi)
    # ========================
    if not st.session_state.get("sudah_disimpan"):
        simpan_ke_history(data, hasil)
        st.session_state["sudah_disimpan"] = True

    # ========================
    # TIDAK ADA HASIL → EMPTY STATE
    # ========================
    if not hasil:
        st.markdown("""
        <div class="empty-state">
            <div class="empty-icon">🔎</div>
            <div class="empty-title">Tidak Ditemukan Penyakit</div>
            <div class="empty-desc">
                Tidak ada penyakit yang cocok dengan gejala yang diinput.<br>
                Coba tambahkan gejala yang lebih spesifik atau konsultasikan ke dokter hewan.
            </div>
        </div>
        """, unsafe_allow_html=True)

    else:
        # ── DIAGNOSA UTAMA ────────────────────────────────────
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

        # ── TABEL SEMUA HASIL ─────────────────────────────────
        st.subheader("📋 Seluruh Kemungkinan Diagnosa")

        tabel = pd.DataFrame([{
            "Penyakit"      : h["penyakit"],
            "Kecocokan (%)": h["kecocokan"],
            "Gejala Cocok"  : h["gejala_cocok"],
            "Total Rule"    : h["total_rule"],
        } for h in hasil])

        st.dataframe(tabel, use_container_width=True, hide_index=True)

        # ── DIAGRAM BATANG ────────────────────────────────────
        st.subheader("📈 Diagram Tingkat Kecocokan")
        chart_df = tabel.set_index("Penyakit")[["Kecocokan (%)"]]
        st.bar_chart(chart_df)

        # ── DETAIL KEMUNGKINAN LAIN ───────────────────────────
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
        st.session_state["sudah_disimpan"] = False
        st.rerun()