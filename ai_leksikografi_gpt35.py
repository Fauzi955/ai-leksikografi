
# AI Leksikografi: Identifikasi Kelas Kata dan Contoh Kalimat
# Platform: Streamlit Web App

import streamlit as st
import openai

# Konfigurasi API OpenAI (ganti dengan API key Anda jika dijalankan secara lokal)
openai.api_key = st.secrets.get("openai_api_key", "sk-...")

st.set_page_config(page_title="AI Leksikografi", page_icon="📚")
st.title("📚 Asisten AI Leksikografi")
st.write("Masukkan entri (kata) atau makna dari entri yang ingin Anda analisis. Bot ini akan mengidentifikasi kelas kata dan membuat contoh kalimat yang sesuai.")

pilihan = st.radio("Pilih metode input:", ["Kata", "Makna (Definisi)"])

input_teks = st.text_input("Masukkan kata atau makna entri:")

if input_teks:
    if pilihan == "Kata":
        dengan_konteks = f"Identifikasikan kelas kata dari kata '{input_teks}' dalam bahasa Indonesia. Beri satu kata saja seperti 'nomina', 'verba', atau 'adjektiva'."
        kalimat_prompt = f"Buat satu kalimat sederhana dalam bahasa Indonesia menggunakan kata '{input_teks}'."
    else:
        dengan_konteks = f"Dari makna berikut ini: '{input_teks}', tentukan kelas katanya dalam bahasa Indonesia. Jawab dengan satu kata: 'nomina', 'verba', atau 'adjektiva'."
        kalimat_prompt = f"Berdasarkan makna '{input_teks}', buat satu kalimat sederhana dalam bahasa Indonesia yang cocok untuk kelas kata tersebut."

    with st.spinner("Mengidentifikasi kelas kata..."):
        kelas_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": dengan_konteks}
            ]
        )
        kelas_kata = kelas_response.choices[0].message.content.strip()

    st.success(f"🔤 Kelas kata: {kelas_kata}")

    with st.spinner("Membuat contoh kalimat sesuai kelas katanya..."):
        kalimat_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": kalimat_prompt + f" Gunakan gaya bahasa yang baku."}
            ]
        )
        contoh_kalimat = kalimat_response.choices[0].message.content.strip()

    st.markdown("---")
    st.write("📝 Contoh Kalimat:")
    st.success(contoh_kalimat)

st.markdown("---")
st.caption("Dikembangkan untuk membantu tugas leksikografi dan kebahasaan. 🇮🇩")
