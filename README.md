# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Perusahaan Jaya Jaya Maju merupakan perusahaan multinasional yang telah berdiri sejak tahun 2000. Perusahaan ini memiliki lebih dari 1000 karyawan yang tersebar di seluruh negeri. Dalam beberapa tahun terakhir, perusahaan menghadapi tantangan besar dalam mempertahankan karyawannya. Tingkat attrition rate (tingkat pengunduran diri atau pemutusan hubungan kerja) terus meningkat, melebihi 10%, yang berpotensi mengganggu stabilitas bisnis dan produktivitas perusahaan.


### Permasalahan Bisnis
1. Berapa persen attrition rate yang terjadi di perusahaan ini.
2. Faktor apa saja yang mempengaruhi tingkat attrition rate di perusahaan.
3. Department apa yang paling banyak tingkat attrition/pengunduran diri karyawan dan JobRole nya
4. Menyediakan business dashboard untuk membantunya memonitoring berbagai faktor tersebut.


### Cakupan Proyek
Proyek ini akan berfokus pada:
- Analisis Data: Mengidentifikasi pola dan faktor utama yang memengaruhi attrition rate.
- Pemodelan Prediktif: Membangun model machine learning untuk memprediksi potensi attrition.
- Business Dashboard: Membuat dashboard interaktif untuk membantu HR dalam monitoring faktor-faktor attrition secara real-time.
- Rekomendasi Strategis: Memberikan insight dan rekomendasi bagi HR untuk mengurangi turnover karyawan.


### Persiapan
Sumber data: dataset yang digunakan merupakan dataset Perusahaan [Jaya Jaya Maju](https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee).

Setup environment: Proyek ini membutuhkan lingkungan sederhana untuk menjalankan analisis data dan dashboard. Berikut langkah-langkah untuk mempersiapkan environment:
- Menjalankan `notebook.ipynb`
    - Pastikan dependensi, packages, library yang dibutuhkan sudah tersedia (lihat file requirements.txt untuk melihat dependensi yang dibutuhkan).
    ```
    pip install -r requirements.txt
    ```
    - Jalankan seluruh isi file notebook.ipynb menggunakan Google Colab/Jupyter Notebook untuk melihat hasil analisis data, temuan, dan insight yang diperoleh.
- Setup conda environtment (jika menggunakan conda bisa memakai ini):
    ```
    conda create --name myenv python=3.9
    conda activate myenv #MacOS
    conda activate myenv  # Windows
    ```


## Business Dashboard
Hasil dari analisis dan model prediktif dapat divisualisasikan dalam bentuk dashboard untuk membantu tim HR memantau dan memahami attrition secara real-time. Berikut adalah elemen-elemen yang dapat disertakan dalam dashboard:

- Tren Attrition:
Distribusi attrition berdasarkan fitur seperti OverTime, MaritalStatus, DistanceFromHOme, Department, BusinessTravel, JobROle, JobSatisfaction dan JobLevel.
- Feature Importance:
Visualisasi kontribusi semua fitur dengan berdasarkan status dari attrition.
- Kemudahan dalam penggunaan Dashboard. [Link Dashboard](https://lookerstudio.google.com/reporting/9adf8a82-dff7-4101-8bb8-26a5aa4b560c)  

## Conclusion



### Rekomendasi Action Items (Optional)


