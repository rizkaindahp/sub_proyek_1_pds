# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Perusahaan Jaya Jaya Maju merupakan perusahaan multinasional yang telah berdiri sejak tahun 2000. Perusahaan ini memiliki lebih dari 1000 pegawai yang tersebar di seluruh negeri. Dalam beberapa tahun terakhir, perusahaan menghadapi tantangan besar dalam mempertahankan pegawainya. Tingkat attrition rate (tingkat pengunduran diri atau pemutusan hubungan kerja) terus meningkat, melebihi 10%, yang berpotensi mengganggu stabilitas bisnis dan produktivitas perusahaan.


### Permasalahan Bisnis
1. Seberapa tinggi tingkat attrition di perusahaan ini?
2. Faktor apa saja yang mempengaruhi tingkat attrition rate di perusahaan?
3. Department dan JobRole apa yang paling tinggi tingkat attrition nya?
4. Menyediakan business dashboard untuk membantunya memonitoring berbagai faktor tersebut.


### Cakupan Proyek
Proyek ini akan berfokus pada:
- Analisis Data: Mengidentifikasi pola dan faktor utama yang memengaruhi attrition rate.
- Pemodelan Prediktif: Membangun model machine learning untuk memprediksi potensi attrition.
- Business Dashboard: Membuat dashboard interaktif untuk membantu HR dalam monitoring faktor-faktor attrition secara real-time.
- Rekomendasi Strategis: Memberikan insight dan rekomendasi bagi HR untuk mengurangi turnover pegawai.


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
Distribusi attrition berdasarkan fitur seperti OverTime, MaritalStatus, DistanceFromHOme, Department, BusinessTravel, JobRole, JobSatisfaction dan JobLevel.
- Feature Importance:
Visualisasi kontribusi semua fitur dengan berdasarkan status dari attrition.
- Kemudahan dalam penggunaan Dashboard. [Link Dashboard](https://lookerstudio.google.com/reporting/9adf8a82-dff7-4101-8bb8-26a5aa4b560c)  

## Conclusion
1. Dari data yang telah kita analisa, tinggi nya attrition/pengunduran berada di 16.9%. Attrition rate yang melebihi 15% ini sangat berdampak pada perusahaan Jaya Jaya Maju. Angka ini berarti menunjukkan ketidak nyamanan pegawai dalam beberapa faktor.
2. 5 Faktor yang sangat mempengaruhi atau berkolerasi dengan attrition yaitu OverTime, MaritalStatus, DistanceFromHome, Department, dan JobRole.
3. Dari data yang sudah kita analisa fitur Department dan JobRole yang paling banyak attrition berada di Department *Research & Development* serta JobRole sebagai *Laboratory Technician*.
4. Tampilan dashboard berikut ini bisa mempermudah HR dalam mengumpulkan, menganalisis, dan memantau data pegawai secara real-time. Dengan dashboard, HR dapat mengambil keputusan berbasis data untuk meningkatkan efisiensi, mengelola tenaga kerja dengan lebih baik, dan mengurangi masalah seperti tingginya attrition rate.
Bisa di akses melalui [Link Dashboard](https://lookerstudio.google.com/reporting/9adf8a82-dff7-4101-8bb8-26a5aa4b560c) ini. 


### Rekomendasi Action Items (Optional)
1. Mengevaluasi lingkungan pekerjaan pada Departemen atau JobRole yang memiliki tingkat attrition yang tinggi guna meningkatkan kepuasan pegawai.
2. Kurangi jumlah lembur dengan mengoptimalkan beban kerja dan tenaga kerja.
3. Memberikan kemudahan akses ke kantor dengan opsi remote work (WFH) atau subsidi transportasi.
4. Beri kesempatan pengembangan karier kepada pegawai.
5. Perbaiki jalur karier dan kesejahteraan pegawai dalam JobRole tertentu agar mereka lebih loyal.


