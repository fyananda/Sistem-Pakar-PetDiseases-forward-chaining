import streamlit as st
import pandas as pd
import os


def show_history_diagnosa():

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
    .page-header {
        margin-bottom: 28px;
    }
    .page-header-title {
        font-size: 28px;
        font-weight: 800;
        color: #0f172a;
        letter-spacing: -0.02em;
        margin-bottom: 4px;
    }
    .page-header-sub {
        font-size: 14px;
        color: #64748b;
    }

    /* ── FILTER CARD ── */
    .filter-card {
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        padding: 20px 24px;
        margin-bottom: 24px;
    }
    .filter-card-title {
        font-size: 13px;
        font-weight: 700;
        color: #64748b;
        text-transform: uppercase;
        letter-spacing: 0.07em;
        margin-bottom: 14px;
    }

    /* ── SECTION TITLE ── */
    .section-title {
        font-size: 18px;
        font-weight: 700;
        color: #0f172a;
        margin-bottom: 12px;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    /* ── SUMMARY STRIP ── */
    .summary-strip {
        display: flex;
        gap: 12px;
        margin-bottom: 20px;
    }
    .summary-pill {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 100px;
        padding: 6px 16px;
        font-size: 13px;
        font-weight: 600;
        color: #475569;
    }
    .summary-pill span {
        color: #0f172a;
        font-family: 'JetBrains Mono', monospace;
    }

    /* ── ACTION ROW ── */
    .action-row {
        display: flex;
        gap: 10px;
        margin-top: 20px;
        justify-content: flex-end;
    }

    /* ── EMPTY STATE ── */
    .empty-state {
        text-align: center;
        padding: 64px 24px;
        background: #f8fafc;
        border: 1px dashed #cbd5e1;
        border-radius: 20px;
        margin-top: 8px;
    }
    .empty-icon {
        font-size: 48px;
        margin-bottom: 16px;
    }
    .empty-title {
        font-size: 18px;
        font-weight: 700;
        color: #1e293b;
        margin-bottom: 6px;
    }
    .empty-desc {
        font-size: 14px;
        color: #64748b;
    }

    /* ── Streamlit overrides ── */
    div[data-testid="stDataFrame"] {
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        overflow: hidden;
    }
    .stSelectbox label, .stTextInput label {
        font-size: 13px !important;
        font-weight: 600 !important;
        color: #374151 !important;
    }
    .stButton > button {
        border-radius: 10px !important;
        font-weight: 600 !important;
        font-size: 14px !important;
    }
    .stDownloadButton > button {
        background: #0f172a !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 10px !important;
        font-weight: 600 !important;
        font-size: 14px !important;
    }
    .stDownloadButton > button:hover {
        background: #1e293b !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # ── PAGE HEADER ──────────────────────────────────────────
    st.markdown("""
    <div class="page-header">
        <div class="page-header-title">📜 Riwayat Diagnosa</div>
        <div class="page-header-sub">Daftar semua sesi diagnosa yang telah dilakukan sebelumnya</div>
    </div>
    """, unsafe_allow_html=True)

    history_path = "history_diagnosis.csv"

    # ── EMPTY STATE ──────────────────────────────────────────
    if not os.path.exists(history_path):
        st.markdown("""
        <div class="empty-state">
            <div class="empty-icon">📭</div>
            <div class="empty-title">Belum Ada Riwayat</div>
            <div class="empty-desc">Riwayat diagnosa akan muncul di sini setelah kamu melakukan diagnosa pertama.</div>
        </div>
        """, unsafe_allow_html=True)
        return

    df = pd.read_csv(history_path)

    if df.empty:
        st.markdown("""
        <div class="empty-state">
            <div class="empty-icon">🗂️</div>
            <div class="empty-title">Riwayat Kosong</div>
            <div class="empty-desc">Tidak ada data diagnosa yang tersimpan saat ini.</div>
        </div>
        """, unsafe_allow_html=True)
        return

    # ── FILTER ───────────────────────────────────────────────
    st.markdown("""
    <div class="filter-card">
        <div class="filter-card-title">🔍 Filter & Pencarian</div>
    </div>
    """, unsafe_allow_html=True)

    # Inject filter inside a styled container
    col1, col2 = st.columns([1, 1])
    with col1:
        jenis_filter = st.selectbox(
            "Jenis Hewan",
            ["Semua"] + list(df["Jenis Hewan"].unique())
        )
    with col2:
        cari_nama = st.text_input(
            "Cari Nama Hewan",
            placeholder="Ketik nama hewan..."
        )

    # Apply filters
    filtered_df = df.copy()
    if jenis_filter != "Semua":
        filtered_df = filtered_df[filtered_df["Jenis Hewan"] == jenis_filter]
    if cari_nama:
        filtered_df = filtered_df[
            filtered_df["Nama Hewan"].str.contains(cari_nama, case=False, na=False)
        ]

    # ── SUMMARY PILLS ────────────────────────────────────────
    total      = len(df)
    ditampilkan = len(filtered_df)
    jenis_unik = df["Jenis Hewan"].nunique() if "Jenis Hewan" in df.columns else "-"

    st.markdown(f"""
    <div class="summary-strip">
        <div class="summary-pill">Total: <span>{total}</span> data</div>
        <div class="summary-pill">Ditampilkan: <span>{ditampilkan}</span></div>
        <div class="summary-pill">Jenis Hewan: <span>{jenis_unik}</span></div>
    </div>
    """, unsafe_allow_html=True)

    # ── TABLE ────────────────────────────────────────────────
    st.markdown('<div class="section-title">📋 Tabel Riwayat</div>', unsafe_allow_html=True)

    if filtered_df.empty:
        st.markdown("""
        <div class="empty-state">
            <div class="empty-icon">🔎</div>
            <div class="empty-title">Tidak Ditemukan</div>
            <div class="empty-desc">Tidak ada data yang cocok dengan filter yang dipilih.</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.dataframe(filtered_df, use_container_width=True, hide_index=True)

        # ── ACTIONS ──────────────────────────────────────────
        col_dl, col_del = st.columns([1, 1])

        with col_dl:
            csv = filtered_df.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="⬇️ Download CSV",
                data=csv,
                file_name="history_diagnosis.csv",
                mime="text/csv",
                use_container_width=True
            )

        with col_del:
            if st.button("🗑️ Hapus Semua Riwayat", use_container_width=True, type="secondary"):
                pd.DataFrame(columns=df.columns).to_csv(history_path, index=False)
                st.success("✅ Riwayat berhasil dihapus.")
                st.rerun()