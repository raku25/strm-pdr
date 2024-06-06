import pickle
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
import base64

# Function to load image as base64
@st.cache_data
def get_img_as_base64(file):
  with open(file, "rb") as f:
    data = f.read()
  return base64.b64encode(data).decode()

# Get base64 data for your background image
img_base64 = get_img_as_base64("background.png") 

# Use base64 image data as background
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] {{
  background-image: url('data:image/png;base64,{img_base64}');
  background-size: cover;
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

# --- Menambahkan Head Bar ---
st.markdown("""
<header style="display: flex; flex-direction: row; justify-content: space-between; padding: 10px 10px; background-color: ();">
  <a href="#" style="text-decoration: none; font-size: 100px; font-weight: bold;">HypertenZ.AP</a>
  <div>
    </div>
</header>
""", unsafe_allow_html=True)

# Memuat model
hipertensi_model = pickle.load(open('hipertensi_model.sav', 'rb'))

# Memuat dataset
dataset_path = 'hipertensi.csv'
data = pd.read_csv(dataset_path)

# Membuat menu navigasi
with st.sidebar:
  selected = option_menu(
      menu_title="Main Menu",  # required
      options=["Home", "Prediksi"],  # required
      icons=["house", "bar-chart"],  # optional
      menu_icon="cast",  # optional
      default_index=0,  # optional
  )

# Halaman "Home"
if selected == "Home": 
  st.image('sakit.png', use_column_width=True)  # Menambahkan gambar hero
  st.title('PENYAKIT HIPERTENSI')

  st.header('Apa sih :red[Hipertensi]', divider='blue')
  st.text('Hipertensi, atau lebih dikenal dengan tekanan darah tinggi.')
  st.text('Kondisi kesehatan yang terjadi ketika tekanan darah berada di atas batas normal.')

  st.text('Tekanan darah sendiri memiliki dua komponen penting, yaitu :')

  st.text('1. Sistolik, Tekanan saat jantung berkontraksi dan memompa darah ke seluruh tubuh.')
  st.text('2. Diastolik adalah Tekanan saat jantung beristirahat di antara kontraksi.')

  st.text('Menurut pedoman umum, tekanan darah dikatakan tinggi jika hasil pengukuran')
  st.text('Sistolik lebih dari atau sama dengan 140 mmHg')
  st.text('Diastolik lebih dari atau sama dengan 90 mmHg')

  st.header('**Bahaya** :red[Hipertensi]', divider='blue')
  st.text('Hipertensi mendapat julukan "silent killer"')
  st.text('Karena seringkali tidak menimbulkan gejala pada tahap awal.')
  st.text('Namun, bila tidak terkontrol, hipertensi bisa menimbulkan komplikasi serius.')
  st.text('seperti gagal jantung, stroke, penyakit ginjal , dan kerusakan pada mata')

  st.header('Penyebab :red[Hipertensi]', divider='blue')
  st.text('Sekitar 90% kasus, penyebabnya tidak diketahui secara pasti (hipertensi primer)')
  st.text('Faktor-faktor yang bisa meningkatkan risiko hipertensi primer meliputi:')
  st.text('1. Riwayat keluarga dengan hipertensi')
  st.text('2. Usia (risiko meningkat seiring bertambahnya usia)')
  st.text('3. Berat badan berlebih atau obesitas')
  st.text('4. Kurang aktivitas fisik')
  st.text('5. Konsumsi makanan tinggi garam (sodium)')
  st.text('6. Konsumsi alkohol berlebihan')
  st.text('7. Stres')
  st.text('8. Merokok')
  st.text('Hipertensi juga bisa terjadi akibat kondisi medis tertentu (hipertensi sekunder).')
  st.text('Beberapa kondisi yang bisa memicu hipertensi sekunder adalah:')
  st.text('1. Penyakit ginjal')
  st.text('2. Penyakit arteri koroner')
  st.text('3. Sleep apnea')
  st.text('4. Hipertiroidisme')

  st.header('Pengenalan dan Penanganan :red[Hipertensi]', divider='blue')
  st.text('Pendeteksian hipertensi dilakukan melalui pengukuran tekanan darah secara rutin.')
  st.text('Deteksi dini menjadi penting untuk mencegah komplikasi.')
  st.text('Selain pengukuran tekanan darah, dokter mungkin akan melakukan pemeriksaan lain')
  st.text('untuk menilai kondisi kesehatan secara menyeluruh.')
  st.text('Pengobatan hipertensi umumnya bergantung pada tingkat keparahannya dan')
  st.text('dan penyebab yang mendasari.')
  st.text('Berikut beberapa langkah penanganan yang biasa dilakukan:')
  st.text('- Pola makan sehat rendah garam, berolahraga secara teratur, dan berhenti merokok.')
  st.text('- Lalu obat-obatan, dengan resep dokter obat-obatan untuk menurunkan tekanan darah.')

  st.header('Pencegahan :red[Hipertensi]', divider='blue')
  st.text('Hipertensi bisa dicegah dengan menerapkan pola hidup sehat, seperti:')
  st.text('1. Memperbanyak konsumsi buah, sayur, dan whole grains.')
  st.text('2. Batasi konsumsi makanan olahan, makanan tinggi lemak jenuh dan tinggi garam.')
  st.text('3. Jaga berat badan ideal.')
  st.text('4. Berolahraga secara teratur minimal 30 menit per hari, 5 hari per minggu.')
  st.text('5. Batasi konsumsi alkohol.')
  st.text('6. Kelola stres dengan baik.')
  st.text('7. Tidak merokok.')

  st.header('Layanan Kami', divider='blue')
  st.text('Menerapkan pola hidup sehat tidak hanya membantu mencegah hipertensi,')
  st.text('tapi juga dapat menjaga kesehatan secara keseluruhan.')
  st.text('Jika Anda memiliki  kekhawatiran tentang tekanan darah tinggi,')
  st.text('silahkan tes hipertensi anda!')

# Halaman "Prediksi"
if selected == "Prediksi":
  st.image('hero.png', use_column_width=True)

  st.title(':blue-background[Ayo Prediksi Hipertensi Sekarang:drop_of_blood:]')

  st.divider()

  col1, col2 = st.columns(2)

  with col1:
    Usia = st.text_input('Usia')

    with col2:
        Kelamin = st.selectbox('Jenis Kelamin', options=[None, 0, 1], format_func=lambda x: 'Pilih' if x is None else 'Perempuan' if x == 0 else 'Laki-Laki')

    with col2:
        BMI = st.text_input('Input Nilai BMI')

    with col1:
        Rokok = st.text_input('Input Nilai Rokok (Batang/hari)')

    with col2:
        Alkohol = st.text_input('Input Nilai Alkohol per minggu (gram)')

    with col1:
        Aktivitas = st.text_input('Input Nilai Aktivitas Fisik (Jam/Minggu)')

    with col2:
        Kolestrol = st.text_input('Input Kadar Kolestrol (mg/dL)')

    with col1:
        Sistolik = st.text_input('Input Nilai Tekanan Darah Sistolik (mmHg)')

    with col1:
        Diastolik = st.text_input('Input Nilai Tekanan Darah Diastolik (mmHg)')

    hiper_diagnosis = ''

    if st.button('Test Prediksi Hipertensi'):
        try:
            # Konversi nilai input ke tipe data yang sesuai
            Usia = float(Usia)
            Kelamin = float(Kelamin)
            BMI = float(BMI)
            Rokok = float(Rokok)
            Alkohol = float(Alkohol)
            Aktivitas = float(Aktivitas)
            Kolestrol = float(Kolestrol)
            Sistolik = float(Sistolik)
            Diastolik = float(Diastolik)

            # Buat array input untuk prediksi
            input_data = [[Usia, Kelamin, BMI, Rokok, Alkohol, Aktivitas, Kolestrol, Sistolik, Diastolik]]

            # Lakukan prediksi
            hiper_prediction = hipertensi_model.predict(input_data)

            if hiper_prediction[0] == 1:
                hiper_diagnosis = 'Pasien terkena Hipertensi'
            else:
                hiper_diagnosis = 'Pasien tidak terkena Hipertensi'
            st.success(hiper_diagnosis)

            # Tambahkan data baru ke dataset
            new_data = pd.DataFrame({
                'Usia': [Usia],
                'Kelamin': [Kelamin],
                'BMI': [BMI],
                'Rokok': [Rokok],
                'Alkohol': [Alkohol],
                'Aktivitas': [Aktivitas],
                'Kolestrol': [Kolestrol],
                'Sistolik': [Sistolik],
                'Diastolik': [Diastolik],
                'Hipertensi': [hiper_prediction[0]]
            })

            # Menggunakan pd.concat untuk menambahkan data baru ke dataset
            data = pd.concat([data, new_data], ignore_index=True)

            # Simpan dataset yang diperbarui ke file CSV
            data.to_csv(dataset_path, index=False)

        except ValueError as e:
            st.error(f"Error: {str(e)}. Please enter valid numeric values for all input fields.")
