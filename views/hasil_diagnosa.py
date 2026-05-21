import streamlit as st

def show_hasil_diagnosa():

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
    .card {
        background: white;
        border-radius: 16px;
        padding: 24px 30px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        margin-bottom: 20px;
    }
    .penyakit-nama {
        font-size: 28px;
        font-weight: bold;
        color: #dc2626;
    }
    .badge {
        display: inline-block;
        background: #fef2f2;
        color: #dc2626;
        border: 1px solid #fecaca;
        border-radius: 999px;
        padding: 4px 14px;
        font-size: 13px;
        font-weight: 600;
        margin-bottom: 12px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='hasil-title'>🩺 Hasil Diagnosa</div>", unsafe_allow_html=True)
    st.markdown("<div class='hasil-subtitle'>Hasil analisis berdasarkan gejala yang diinput</div>", unsafe_allow_html=True)

    # =========================
    # CEK SESSION STATE
    # =========================
    if "sudah_diagnosa" not in st.session_state or not st.session_state["sudah_diagnosa"]:
        st.info("ℹ️ Belum ada data diagnosa. Silakan isi **Form Input** terlebih dahulu.")
        return

    data = st.session_state["data_diagnosa"]

    # =========================
    # RINGKASAN DATA HEWAN
    # =========================
    st.subheader("📋 Data Hewan")
    col1, col2, col3 = st.columns(3)
    col1.metric("Nama Hewan",    data["nama_hewan"])
    col2.metric("Jenis Hewan",   data["jenis_hewan"])
    col3.metric("Jenis Kelamin", data["jenis_kelamin"])

    col4, col5, col6 = st.columns(3)
    col4.metric("Usia",          f'{data["usia"]} tahun')
    col5.metric("Berat Badan",   f'{data["berat_badan"]} kg')
    col6.metric("Suhu Tubuh",    f'{data["suhu_tubuh"]} °C')

    st.markdown("---")

    # =========================
    # RINGKASAN GEJALA
    # =========================
    st.subheader("🩺 Gejala yang Dilaporkan")

    gejala_klinis_raw = [
        data["gejala_1"],
        data["gejala_2"],
        data["gejala_3"],
        data["gejala_4"],
    ]
    # Hanya ambil gejala yang benar-benar diisi (bukan None)
    gejala_klinis = [g for g in gejala_klinis_raw if g]
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
                st.markdown(f"- {g}")
        else:
            st.caption("Tidak ada gejala klinis yang dipilih.")
    with col_g2:
        st.markdown("**Gejala Tambahan**")
        for label, nilai in gejala_tambahan.items():
            icon = "✅" if nilai == "Ya" else "❌"
            st.markdown(f"{icon} {label}")

    st.markdown("---")

    # =========================
    # HASIL DIAGNOSA (MOCK)
    # TODO: ganti bagian ini dengan pemanggilan engine forward chaining
    # Contoh: from engine.forward_chaining import diagnosa
    #         hasil = diagnosa(data)
    # =========================
    st.subheader("🔬 Hasil Diagnosa")

    # Mock: cocokkan gejala sederhana untuk demo
    gejala_aktif = set(g.lower() for g in gejala_klinis)
    gejala_aktif.update(k.lower() for k, v in gejala_tambahan.items() if v == "Ya")

    if "demam" in gejala_aktif and "muntah" in gejala_aktif:
        mock_penyakit    = "Parvovirus"
        mock_keyakinan   = "82%"
        mock_deskripsi   = "Parvovirus adalah infeksi virus yang sangat menular pada anjing, menyerang sistem pencernaan dan kekebalan tubuh."
        mock_saran       = "Segera bawa ke dokter hewan. Hewan perlu cairan infus dan perawatan intensif."
    elif "batuk" in gejala_aktif or "kesulitan bernafas" in gejala_aktif:
        mock_penyakit    = "Infeksi Saluran Pernapasan Atas"
        mock_keyakinan   = "74%"
        mock_deskripsi   = "Infeksi pada saluran pernapasan bagian atas yang umum terjadi pada kucing dan anjing."
        mock_saran       = "Konsultasikan ke dokter hewan untuk pemberian antibiotik atau antivirus yang tepat."
    elif "diare" in gejala_aktif:
        mock_penyakit    = "Gastroenteritis"
        mock_keyakinan   = "68%"
        mock_deskripsi   = "Peradangan pada lambung dan usus yang menyebabkan diare dan muntah."
        mock_saran       = "Pastikan hewan tetap terhidrasi. Berikan makanan ringan dan pantau kondisinya."
    else:
        mock_penyakit    = "Tidak Teridentifikasi"
        mock_keyakinan   = "-"
        mock_deskripsi   = "Gejala yang diinput belum cukup untuk menentukan diagnosa."
        mock_saran       = "Tambahkan gejala lebih spesifik atau konsultasikan langsung ke dokter hewan."

    # Tampilkan hasil
    st.markdown(f"""
    <div class='card'>
        <div class='badge'>⚠️ MOCK RESULT — Engine belum terhubung</div><br>
        <div class='penyakit-nama'>🦠 {mock_penyakit}</div>
        <p style='color:#6b7280; margin: 8px 0 16px 0;'>Tingkat Keyakinan: <b>{mock_keyakinan}</b></p>
        <p><b>Deskripsi:</b><br>{mock_deskripsi}</p>
        <p><b>Saran:</b><br>{mock_saran}</p>
    </div>
    """, unsafe_allow_html=True)

    # =========================
    # TOMBOL ULANGI
    # =========================
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔄 Ulangi Diagnosa"):
        st.session_state["sudah_diagnosa"] = False
        st.session_state["data_diagnosa"]  = {}
        st.rerun()