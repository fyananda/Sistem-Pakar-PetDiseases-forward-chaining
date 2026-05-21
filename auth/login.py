import streamlit as st


# ============================================================
# KREDENSIAL
# ============================================================
USERS = {
    "admin"  : {"password": "admin123",  "role": "Admin"},
    "pasien" : {"password": "pasien123", "role": "Pasien"},
}


# ============================================================
# INIT SESSION
# ============================================================
def init_auth():
    if "login" not in st.session_state:
        st.session_state.login = False
    if "role" not in st.session_state:
        st.session_state.role = ""


# ============================================================
# HALAMAN LOGIN
# ============================================================
def show_login():

    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }

    #MainMenu, footer, header { visibility: hidden; }

    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e3a5f 60%, #0f4c75 100%) !important;
        min-height: 100vh;
    }

    .block-container {
        padding-top: 0 !important;
        padding-bottom: 0 !important;
        max-width: 100% !important;
    }

    /* ── BRAND ── */
    .login-brand-icon {
        font-size: 56px;
        text-align: center;
        display: block;
        margin-bottom: 14px;
        filter: drop-shadow(0 4px 12px rgba(56,189,248,0.4));
    }
    .login-title {
        font-size: 24px;
        font-weight: 800;
        color: #f0f9ff;
        text-align: center;
        letter-spacing: -0.02em;
        line-height: 1.2;
        margin-bottom: 6px;
    }
    .login-subtitle {
        font-size: 12px;
        color: #64748b;
        text-align: center;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        font-weight: 600;
        margin-bottom: 32px;
    }
    .login-divider {
        height: 1px;
        background: rgba(255,255,255,0.08);
        margin-bottom: 28px;
    }

    /* ── LABEL ── */
    .stTextInput label {
        font-size: 11.5px !important;
        font-weight: 700 !important;
        color: #94a3b8 !important;
        text-transform: uppercase !important;
        letter-spacing: 0.08em !important;
    }

    /* ── INPUT — warna teks hitam tegas di atas background putih ── */
    .stTextInput > div > div > input {
        background: #ffffff !important;
        border: 1.5px solid rgba(255,255,255,0.18) !important;
        border-radius: 14px !important;
        height: 50px !important;
        color: #0f172a !important;
        font-size: 15px !important;
        font-weight: 500 !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        padding: 0 16px !important;
        transition: border-color 0.2s, box-shadow 0.2s !important;
    }
    .stTextInput > div > div > input::placeholder {
        color: #94a3b8 !important;
    }
    .stTextInput > div > div > input:focus {
        border-color: #38bdf8 !important;
        box-shadow: 0 0 0 3px rgba(56,189,248,0.20) !important;
    }

    /* ── BUTTON ── */
    .stButton > button {
        width: 100% !important;
        height: 52px !important;
        border-radius: 14px !important;
        background: linear-gradient(135deg, #0ea5e9 0%, #2563eb 100%) !important;
        color: #ffffff !important;
        font-size: 15px !important;
        font-weight: 700 !important;
        border: none !important;
        letter-spacing: 0.02em !important;
        box-shadow: 0 8px 24px rgba(37,99,235,0.40) !important;
        margin-top: 4px !important;
        transition: opacity 0.2s, transform 0.15s !important;
    }
    .stButton > button:hover {
        opacity: 0.88 !important;
        transform: translateY(-1px) !important;
    }

    /* ── HINT ── */
    .login-hint {
        margin-top: 20px;
        background: rgba(56,189,248,0.07);
        border: 1px solid rgba(56,189,248,0.20);
        border-radius: 14px;
        padding: 14px 18px;
        font-size: 12.5px;
        color: #7dd3fc;
        line-height: 1.9;
    }
    .login-hint b { color: #38bdf8; font-weight: 700; }
    .login-hint code {
        background: rgba(56,189,248,0.14);
        border-radius: 6px;
        padding: 1px 8px;
        font-family: 'JetBrains Mono', monospace;
        font-size: 12px;
        color: #e0f2fe;
    }

    div[data-testid="stAlert"] {
        border-radius: 12px !important;
        font-size: 13.5px !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<div style='height:5vh'></div>", unsafe_allow_html=True)

    _, col, _ = st.columns([1, 1.6, 1])

    with col:
        st.markdown("""
        <span class="login-brand-icon">🐾</span>
        <div class="login-title">Pet Diseases<br>Smart System</div>
        <div class="login-subtitle">Expert System · Forward Chaining</div>
        <div class="login-divider"></div>
        """, unsafe_allow_html=True)

        username  = st.text_input("👤 Username", placeholder="Masukkan username")
        password  = st.text_input("🔒 Password", type="password", placeholder="Masukkan password")

        st.markdown("<div style='height:4px'></div>", unsafe_allow_html=True)

        login_btn = st.button("🚀 Masuk ke Sistem")

        st.markdown("""
        <div class="login-hint">
            🔑 <b>Demo Credentials</b><br>
            Admin &nbsp;→ <code>admin</code> / <code>admin123</code><br>
            Pasien → <code>pasien</code> / <code>pasien123</code>
        </div>
        """, unsafe_allow_html=True)

        if login_btn:
            u = username.strip().lower()
            if u in USERS and password == USERS[u]["password"]:
                st.session_state.login = True
                st.session_state.role  = USERS[u]["role"]
                st.rerun()
            else:
                st.error("❌ Username atau password salah.")