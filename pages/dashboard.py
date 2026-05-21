import streamlit as st

def show_dashboard():
    st.title("Sistem Pakar Diagnosa Penyakit Hewan Peliharaan")

    st.subheader("Menggunakan Metode Forward Chaining")

    st.write("""
    Selamat datang di sistem pakar diagnosa penyakit hewan peliharaan.
    
    Sistem ini membantu pengguna mendiagnosa penyakit berdasarkan gejala
    yang dipilih menggunakan metode Forward Chaining.
    """)

    st.info("Silakan pilih menu di sidebar.")