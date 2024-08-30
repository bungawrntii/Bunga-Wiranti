import streamlit as st
import pandas as pd

# Read data
data = pd.read_excel('C:/Semester 4/AI/CareerSheet.xlsx')

st.write("""
# Rekomendasi Pemilihan Karir
""")

st.write("""
Job Recommendation
""")

# Linear search function
def linear_search(data, key_skills, industries):
    rekomendasi = {}
    for index, row in data.iterrows():
        skor = 0

        if isinstance(row["Key Skills"], str):
            row_skills = row["Key Skills"].lower()
            for skill in key_skills:
                if skill.strip().lower() in row_skills:
                    skor += 1

        if isinstance(row["Industry"], str):
            row_industries = row["Industry"].lower()
            for industry in industries:
                if industry.strip().lower() in row_industries:
                    skor += 1

        job_title = row["Job Title"]
        if job_title not in rekomendasi:
            rekomendasi[job_title] = skor
        else:
            if skor > rekomendasi[job_title]:
                rekomendasi[job_title] = skor

    # Sort recommendations by highest score and filter out zero scores
    sorted_rekomendasi = [(job_title, skor) for job_title, skor in sorted(rekomendasi.items(), key=lambda x: x[1], reverse=True) if skor > 0]
    return sorted_rekomendasi

# User input
key_skills_input = st.text_input("Masukkan Kemampuan (jika lebih dari 1, pisahkan dengan koma): ")
industries_input = st.text_input("Masukkan Minat (jika lebih dari 1, pisahkan dengan koma): ")

# Split input into lists
key_skills = key_skills_input.split(',') if key_skills_input else []
industries = industries_input.split(',') if industries_input else []

if st.button("Cari :fire::fire::fire:"):
    hasil_rekomendasi = linear_search(data, key_skills, industries)

    if hasil_rekomendasi:
        st.success("Pekerjaan yang paling sesuai dengan preferensi Anda:")
        for job_title, skor in hasil_rekomendasi[:10]:
            st.write("-", job_title)
    else:
        st.write("Tidak ada rekomendasi pekerjaan yang sesuai dengan preferensi Anda.")
