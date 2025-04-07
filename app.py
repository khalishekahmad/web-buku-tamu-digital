import streamlit as st
import firebase_admin
import json
from firebase_admin import credentials, firestore

# Ambil kredensial dari Streamlit Secrets dan hapus whitespace di sekitarnya
firebase_credentials = st.secrets["firebase"]["credentials"].strip()

# Tambahkan baris debugging untuk melihat isi string credentials
st.write("DEBUG credentials:", repr(firebase_credentials))

try:
    cred_data = json.loads(firebase_credentials)
except json.JSONDecodeError as e:
    st.error("Failed to parse JSON credentials: " + str(e))
    st.stop()

try:
    cred = credentials.Certificate(cred_data)
except Exception as e:
    st.error("Failed to initialize certificate credential: " + str(e))
    st.stop()

if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

db = firestore.client()
collection = db.collection("pengunjung")

st.write("Firebase dan Firestore berhasil diinisialisasi!")

# Sidebar untuk navigasi antar halaman
page = st.sidebar.selectbox("Pilih Halaman", ["Input Data", "Tampilkan Data"])

if page == "Input Data":
    st.title("📋 Buku Tamu Digital")
    st.write("Silakan isi data kamu di bawah ini:")

    # Gunakan st.form untuk input form dengan auto-reset
    with st.form(key='tamu_form', clear_on_submit=True):
        nama = st.text_input("Nama")
        email = st.text_input("Email")
        komentar = st.text_area("Komentar / Pesan")
        submit = st.form_submit_button(label="Kirim")

        if submit:
            if nama and email:
                data = {
                    "nama": nama,
                    "email": email,
                    "komentar": komentar
                }
                collection.add(data)
                st.success("✅ Data berhasil dikirim ke Firebase!")
            else:
                st.warning("❗ Nama dan email tidak boleh kosong.")

elif page == "Tampilkan Data":
    st.subheader("📌 Data Pengunjung:")
    docs = collection.stream()
    rows = []
    for i, doc in enumerate(docs, start=1):
        item = doc.to_dict()
        rows.append({
            "No": i,
            "Nama": item.get("nama", ""),
            "Email": item.get("email", ""),
            "Komentar": item.get("komentar", "")
        })

    df = pd.DataFrame(rows)
    html_table = df.to_html(index=False)
    st.markdown(html_table, unsafe_allow_html=True)

# Tambahkan footer di bagian bawah aplikasi
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align: center;'>Copyright © 2025 Daffa Asyqar. All Rights Reserved.</p>",
    unsafe_allow_html=True
)

