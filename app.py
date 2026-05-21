import streamlit as st

# IMPORT HALAMAN
from pages.dashboard import show_dashboard
from pages.form_input import show_form_input
from pages.hasil_diagnosa import show_hasil_diagnosa
from pages.history_diagnosa import show_history_diagnosa

# PAGE CONFIG
st.set_page_config(
    page_title="Sistem Pakar Diagnosa Hewan",
    page_icon="🐾",
    layout="wide"
)

# SIDEBAR
st.sidebar.title("🐾 PetDiseases Expert System")

menu = st.sidebar.radio(
    "Menu Navigasi",
    [
        "Dashboard",
        "Form Input",
        "Hasil Diagnosa",
        "History Diagnosa"
    ]
)

# ROUTING MENU
if menu == "Dashboard":
    show_dashboard()

elif menu == "Form Input":
    show_form_input()

elif menu == "Hasil Diagnosa":
    show_hasil_diagnosa()

elif menu == "History Diagnosa":
    show_history_diagnosa()