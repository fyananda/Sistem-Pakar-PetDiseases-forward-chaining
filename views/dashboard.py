import streamlit as st

def show_dashboard():

    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap');

    /* ── Reset & Base ── */
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }

    /* ── Hide default Streamlit header padding ── */
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
        max-width: 1100px !important;
    }

    /* ── HERO ── */
    .hero-wrap {
        background: linear-gradient(135deg, #0f172a 0%, #1e3a5f 60%, #0f4c75 100%);
        border-radius: 24px;
        padding: 56px 52px;
        margin-bottom: 32px;
        position: relative;
        overflow: hidden;
    }
    .hero-wrap::before {
        content: '';
        position: absolute;
        top: -80px; right: -80px;
        width: 320px; height: 320px;
        background: radial-gradient(circle, rgba(56,189,248,0.15) 0%, transparent 70%);
        border-radius: 50%;
    }
    .hero-wrap::after {
        content: '';
        position: absolute;
        bottom: -60px; left: -60px;
        width: 240px; height: 240px;
        background: radial-gradient(circle, rgba(99,179,237,0.10) 0%, transparent 70%);
        border-radius: 50%;
    }
    .hero-badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: rgba(56,189,248,0.15);
        border: 1px solid rgba(56,189,248,0.30);
        border-radius: 100px;
        padding: 4px 14px;
        font-size: 12px;
        font-weight: 600;
        color: #38bdf8;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        margin-bottom: 20px;
    }
    .hero-title {
        font-size: 42px;
        font-weight: 800;
        color: #f0f9ff;
        line-height: 1.15;
        margin: 0 0 16px 0;
        letter-spacing: -0.02em;
    }
    .hero-title span {
        color: #38bdf8;
    }
    .hero-desc {
        font-size: 16px;
        color: #94a3b8;
        line-height: 1.7;
        max-width: 560px;
        margin: 0 0 32px 0;
    }
    .hero-cta {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: #38bdf8;
        color: #0f172a;
        font-weight: 700;
        font-size: 15px;
        padding: 12px 24px;
        border-radius: 12px;
        text-decoration: none;
        cursor: default;
    }

    /* ── STATS STRIP ── */
    .stats-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 16px;
        margin-bottom: 32px;
    }
    .stat-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        padding: 22px 24px;
        position: relative;
        overflow: hidden;
    }
    .stat-card::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 3px;
        border-radius: 16px 16px 0 0;
    }
    .stat-card.blue::before  { background: #38bdf8; }
    .stat-card.green::before { background: #34d399; }
    .stat-card.amber::before { background: #fbbf24; }
    .stat-card.rose::before  { background: #f87171; }
    .stat-icon {
        font-size: 28px;
        margin-bottom: 10px;
        display: block;
    }
    .stat-value {
        font-size: 30px;
        font-weight: 800;
        color: #0f172a;
        font-family: 'JetBrains Mono', monospace;
        letter-spacing: -0.02em;
        line-height: 1;
        margin-bottom: 4px;
    }
    .stat-label {
        font-size: 13px;
        color: #64748b;
        font-weight: 500;
    }

    /* ── HOW IT WORKS ── */
    .section-title {
        font-size: 22px;
        font-weight: 700;
        color: #0f172a;
        margin-bottom: 4px;
    }
    .section-sub {
        font-size: 14px;
        color: #64748b;
        margin-bottom: 20px;
    }
    .steps-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 16px;
        margin-bottom: 32px;
    }
    .step-card {
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        padding: 24px;
    }
    .step-num {
        width: 36px; height: 36px;
        background: #0f172a;
        color: white;
        border-radius: 10px;
        font-size: 15px;
        font-weight: 700;
        display: flex; align-items: center; justify-content: center;
        margin-bottom: 14px;
        font-family: 'JetBrains Mono', monospace;
    }
    .step-title {
        font-size: 15px;
        font-weight: 700;
        color: #1e293b;
        margin-bottom: 6px;
    }
    .step-desc {
        font-size: 13px;
        color: #64748b;
        line-height: 1.6;
    }

    /* ── DISEASE CHIPS ── */
    .chip-wrap {
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        padding: 24px 28px;
        margin-bottom: 32px;
    }
    .chip-title {
        font-size: 15px;
        font-weight: 700;
        color: #1e293b;
        margin-bottom: 14px;
    }
    .chips {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
    }
    .chip {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 100px;
        padding: 5px 14px;
        font-size: 12.5px;
        color: #475569;
        font-weight: 500;
    }

    /* ── ALERT BOX ── */
    .alert-info {
        background: #eff6ff;
        border: 1px solid #bfdbfe;
        border-left: 4px solid #3b82f6;
        border-radius: 12px;
        padding: 16px 20px;
        font-size: 14px;
        color: #1e40af;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

    # ── HERO ────────────────────────────────────────────────
    st.markdown("""
    <div class="hero-wrap">
        <div class="hero-badge">🧠 Forward Chaining AI</div>
        <h1 class="hero-title">Diagnosa Penyakit Hewan<br><span>Lebih Cepat & Akurat</span></h1>
        <p class="hero-desc">
            Sistem pakar berbasis metode <strong style="color:#7dd3fc">Forward Chaining</strong> yang membantu
            pemilik hewan mendeteksi penyakit sejak dini berdasarkan gejala yang diamati.
        </p>
        <div class="hero-cta">🐾 Mulai Diagnosa via Form Input</div>
    </div>
    """, unsafe_allow_html=True)

    # ── STATS ────────────────────────────────────────────────
    st.markdown("""
    <div class="stats-grid">
        <div class="stat-card blue">
            <span class="stat-icon">🦠</span>
            <div class="stat-value">24</div>
            <div class="stat-label">Jenis Penyakit</div>
        </div>
        <div class="stat-card green">
            <span class="stat-icon">🐾</span>
            <div class="stat-value">8</div>
            <div class="stat-label">Jenis Hewan</div>
        </div>
        <div class="stat-card amber">
            <span class="stat-icon">🩺</span>
            <div class="stat-value">18</div>
            <div class="stat-label">Parameter Gejala</div>
        </div>
        <div class="stat-card rose">
            <span class="stat-icon">⚡</span>
            <div class="stat-value">Real‑time</div>
            <div class="stat-label">Hasil Diagnosa</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── HOW IT WORKS ─────────────────────────────────────────
    st.markdown('<div class="section-title">⚙️ Cara Kerja Sistem</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Tiga langkah sederhana untuk mendapatkan diagnosa</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="steps-grid">
        <div class="step-card">
            <div class="step-num">01</div>
            <div class="step-title">Isi Form Input</div>
            <div class="step-desc">Masukkan data hewan dan pilih gejala yang diamati — klinis maupun biner (Ya/Tidak).</div>
        </div>
        <div class="step-card">
            <div class="step-num">02</div>
            <div class="step-title">Proses Forward Chaining</div>
            <div class="step-desc">Mesin inferensi mencocokkan fakta gejala dengan basis aturan penyakit secara sistematis.</div>
        </div>
        <div class="step-card">
            <div class="step-num">03</div>
            <div class="step-title">Lihat Hasil Diagnosa</div>
            <div class="step-desc">Tampilkan penyakit yang cocok, persentase kecocokan, deskripsi, dan saran penanganan.</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── DISEASE CHIPS ─────────────────────────────────────────
    st.markdown("""
    <div class="chip-wrap">
        <div class="chip-title">🦠 Penyakit yang Dapat Dideteksi</div>
        <div class="chips">
            <span class="chip">Parvovirus</span>
            <span class="chip">Distemper Anjing</span>
            <span class="chip">Leptospirosis</span>
            <span class="chip">Rabies</span>
            <span class="chip">Gastroenteritis</span>
            <span class="chip">Infeksi Saluran Pernapasan Atas</span>
            <span class="chip">Penyakit Mulut dan Kuku</span>
            <span class="chip">Mastitis</span>
            <span class="chip">Kurap</span>
            <span class="chip">Infeksi Jamur</span>
            <span class="chip">Influenza Kuda</span>
            <span class="chip">Kolik Kuda</span>
            <span class="chip">Penyakit Lyme</span>
            <span class="chip">Parasit Usus</span>
            <span class="chip">Demam Babi Afrika</span>
            <span class="chip">Cacar Domba</span>
            <span class="chip">Cacar Kambing</span>
            <span class="chip">Koksidiosis</span>
            <span class="chip">Pneumonia</span>
            <span class="chip">Arthritis</span>
            <span class="chip">Bronkitis Kronis</span>
            <span class="chip">& lebih banyak lagi...</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── INFO ──────────────────────────────────────────────────
    st.markdown("""
    <div class="alert-info">
        <span>ℹ️</span>
        <span>Sistem ini bersifat <strong>pendukung keputusan</strong>, bukan pengganti dokter hewan.
        Selalu konsultasikan hasil diagnosa dengan profesional.</span>
    </div>
    """, unsafe_allow_html=True)