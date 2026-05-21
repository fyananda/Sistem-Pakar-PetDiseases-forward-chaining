import streamlit as st

from auth.login import init_auth, show_login
from views.dashboard import show_dashboard
from views.form_input import show_form_input
from views.hasil_diagnosa import show_hasil_diagnosa
from views.history_diagnosa import show_history_diagnosa

# ── PAGE CONFIG ──────────────────────────────────────────────
st.set_page_config(
    page_title="Pet Diseases Smart System",
    page_icon="🐾",
    layout="wide"
)

# ── INIT AUTH SESSION ────────────────────────────────────────
init_auth()

# ── AUTH GATE: tampilkan login jika belum login ──────────────
if not st.session_state.login:
    show_login()
    st.stop()

# ── GLOBAL CSS (sidebar + misc) ──────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
}

/* ── Sidebar background ── */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0f172a 0%, #1e293b 100%) !important;
    border-right: 1px solid #1e3a5f;
}
section[data-testid="stSidebar"] * {
    color: #e2e8f0 !important;
}

/* ── Sidebar brand header ── */
.sidebar-brand {
    padding: 8px 4px 24px 4px;
    border-bottom: 1px solid #1e3a5f;
    margin-bottom: 24px;
}
.sidebar-brand-icon {
    font-size: 36px;
    display: block;
    margin-bottom: 6px;
}
.sidebar-brand-name {
    font-size: 20px;
    font-weight: 800;
    color: #ffffff !important;
    line-height: 1.2;
}
.sidebar-brand-sub {
    font-size: 12px;
    color: #94a3b8 !important;
    font-weight: 500;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    margin-top: 2px;
}

/* ── Radio buttons → custom nav items ── */
div[data-testid="stSidebar"] .stRadio > label {
    display: none;
}
div[data-testid="stSidebar"] .stRadio > div {
    gap: 4px !important;
    display: flex;
    flex-direction: column;
}
div[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label {
    display: flex !important;
    align-items: center !important;
    gap: 10px !important;
    padding: 12px 14px !important;
    border-radius: 10px !important;
    font-size: 16px !important;
    font-weight: 600 !important;
    color: #94a3b8 !important;
    cursor: pointer;
    transition: background 0.15s, color 0.15s;
    border: 1px solid transparent !important;
}
div[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:hover {
    background: rgba(56,189,248,0.08) !important;
    color: #ffffff !important;
    border-color: rgba(56,189,248,0.15) !important;
}
div[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label[data-checked="true"],
div[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:has(input:checked) {
    background: rgba(56,189,248,0.12) !important;
    color: #ffffff !important;
    border-color: rgba(56,189,248,0.25) !important;
}
div[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label span:first-child {
    display: none !important;
}

/* ── Role badge di sidebar ── */
.sidebar-role-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: rgba(56,189,248,0.12);
    border: 1px solid rgba(56,189,248,0.25);
    border-radius: 100px;
    padding: 4px 12px;
    font-size: 12px;
    font-weight: 700;
    color: #38bdf8 !important;
    margin-top: 8px;
    letter-spacing: 0.04em;
}

/* ── Sidebar footer ── */
.sidebar-footer {
    position: fixed;
    bottom: 24px;
    padding: 12px 16px;
    background: rgba(30,58,95,0.4);
    border: 1px solid #1e3a5f;
    border-radius: 12px;
    font-size: 12px;
    color: #64748b !important;
    line-height: 1.5;
    width: 220px;
}
.sidebar-footer strong {
    color: #94a3b8 !important;
}

/* ── Logout button ── */
.logout-btn > div > button,
.logout-btn button[kind="secondary"],
.logout-btn button[kind="primary"],
.logout-btn button {
    width: 100% !important;
    background: #991b1b !important;
    background-color: #991b1b !important;
    color: #ffffff !important;
    border: 1px solid #7f1d1d !important;
    border-radius: 10px !important;
    font-size: 14px !important;
    font-weight: 600 !important;
    padding: 10px !important;
    margin-top: 8px !important;
    box-shadow: none !important;
}
.logout-btn > div > button:hover,
.logout-btn button:hover {
    background: #b91c1c !important;
    background-color: #b91c1c !important;
    color: #ffffff !important;
    border-color: #991b1b !important;
    box-shadow: none !important;
}
            
.block-container { padding-top: 1.5rem !important; }
</style>
""", unsafe_allow_html=True)

# ── SIDEBAR ──────────────────────────────────────────────────
with st.sidebar:
    role = st.session_state.role
    role_icon = "🛡️" if role == "Admin" else "🐾"

    st.markdown(f"""
    <div class="sidebar-brand">
        <span class="sidebar-brand-icon">🐾</span>
        <div class="sidebar-brand-name">Pet Diseases<br>Smart System</div>
        <div class="sidebar-brand-sub">Expert System · Forward Chaining</div>
        <div class="sidebar-role-badge">{role_icon} {role}</div>
    </div>
    """, unsafe_allow_html=True)

    # ── Menu berbeda per role ─────────────────────────────────
    if role == "Admin":
        menu_options = [
            "Dashboard",
            "Form Input",
            "Hasil Diagnosa",
            "History Diagnosa",
        ]
    else:  # Pasien hanya bisa input & lihat hasil
        menu_options = [
            "Dashboard",
            "Form Input",
            "Hasil Diagnosa",
        ]

    menu = st.radio(
        "Menu Navigasi",
        menu_options,
        label_visibility="collapsed"
    )

    st.markdown("<br>" * 2, unsafe_allow_html=True)

    # ── Logout ────────────────────────────────────────────────
    if st.button("🚪Logout"):
        st.session_state.login          = False
        st.session_state.role           = ""
        st.session_state["sudah_diagnosa"] = False
        st.session_state["data_diagnosa"]  = {}
        st.session_state["sudah_disimpan"] = False
        st.rerun()

    st.markdown("""
    <div class="sidebar-footer">
        <strong>v1.0.0</strong> · Sistem Pakar<br>
        Diagnosa Penyakit Hewan Peliharaan
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <script>
    const observer = new MutationObserver(() => {
        const logoutDiv = document.querySelector('.logout-btn');
        if (logoutDiv) {
            const btn = logoutDiv.querySelector('button');
            if (btn) {
                btn.style.setProperty('background', '#991b1b', 'important');
                btn.style.setProperty('background-color', '#991b1b', 'important');
                btn.style.setProperty('color', '#ffffff', 'important');
                btn.style.setProperty('border', '1px solid #7f1d1d', 'important');
                btn.style.setProperty('border-radius', '10px', 'important');
                btn.style.setProperty('width', '100%', 'important');
                btn.style.setProperty('font-weight', '600', 'important');
            }
        }
    });
    observer.observe(document.body, { childList: true, subtree: true });
    </script>
    """, unsafe_allow_html=True)

# ── ROUTING ──────────────────────────────────────────────────
if "Dashboard" in menu:
    show_dashboard()
elif "Form Input" in menu:
    show_form_input()
elif "Hasil Diagnosa" in menu:
    show_hasil_diagnosa()
elif "History" in menu:
    show_history_diagnosa()