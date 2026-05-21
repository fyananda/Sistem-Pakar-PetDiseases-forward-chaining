import streamlit as st

def show_form_input():
    st.title("Form Input Diagnosa")

    st.write("Silakan pilih gejala yang dialami hewan.")

    demam = st.checkbox("Demam")
    muntah = st.checkbox("Muntah")
    diare = st.checkbox("Diare")
    batuk = st.checkbox("Batuk")
    lesu = st.checkbox("Lesu")

    if st.button("Diagnosa"):
        st.success("Proses diagnosa berhasil dilakukan")