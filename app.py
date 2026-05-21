import streamlit as st

# CONFIG PAGE
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

# DASHBOARD
if menu == "Dashboard":
    st.title("Sistem Pakar Diagnosa Penyakit Hewan Peliharaan")
    st.subheader("Menggunakan Metode Forward Chaining")

    st.write("""
    Selamat datang di sistem pakar diagnosa penyakit hewan peliharaan.
    
    Sistem ini membantu pengguna mendiagnosa penyakit berdasarkan gejala
    yang dipilih menggunakan metode Forward Chaining.
    """)

# FORM INPUT
elif menu == "Form Input":
    st.title("Form Input Diagnosa")

    st.write("Silakan pilih gejala yang dialami hewan.")

    demam = st.checkbox("Demam")
    muntah = st.checkbox("Muntah")
    diare = st.checkbox("Diare")
    batuk = st.checkbox("Batuk")
    lesu = st.checkbox("Lesu")

    if st.button("Diagnosa"):
        st.success("Proses diagnosa berhasil dilakukan")

# HASIL DIAGNOSA
elif menu == "Hasil Diagnosa":
    st.title("Hasil Diagnosa")

    st.info("Hasil diagnosa akan tampil di sini.")

# HISTORY
elif menu == "History Diagnosa":
    st.title("History Diagnosa")

    st.warning("Belum ada history diagnosa.")