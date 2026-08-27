# Smart Hybrid Solar Dome Dryer – Sistem Monitoring IoT

Sistem monitoring dan manajemen energi berbasis Internet of Things (IoT) untuk pengering biji kakao hibrida yang mengintegrasikan energi surya, biomassa limbah kulit buah kakao (Cocoa Pod Husk/CPH), data cuaca, dan dashboard Blynk.

## 1. Gambaran Umum

Smart Hybrid Solar Dome Dryer merupakan sistem pengering biji kakao yang dirancang dengan menggabungkan energi surya dan biomassa Cocoa Pod Husk (CPH) sebagai sumber energi alternatif.

Sistem IoT digunakan untuk memantau kondisi lingkungan, kondisi pengeringan, dan ketersediaan energi, serta memberikan rekomendasi penggunaan sumber energi berdasarkan kondisi lingkungan.

## 2. Tahap Pengembangan Saat Ini

Pada tahap pengembangan awal, prototipe fisik Solar Dome dan sistem sensor berbasis ESP32 masih dalam tahap pengembangan.

Oleh karena itu, sistem saat ini menggunakan data lingkungan aktual dari wilayah Kecamatan Suli Barat, Kabupaten Luwu, yang diperoleh melalui Open-Meteo API. Data tersebut diproses menggunakan Python dan dikirimkan ke Blynk untuk visualisasi dan pemantauan.

Arsitektur sistem pada tahap awal:

Open-Meteo API
↓
Python
↓
Rule-Based Decision System
↓
Blynk Cloud
↓
Blynk Dashboard

Implementasi ini digunakan untuk menguji dan memvalidasi fungsi awal sistem monitoring dan manajemen energi sebelum diintegrasikan dengan sensor fisik.

## 3. Parameter yang Dipantau

Sistem saat ini memantau beberapa parameter berikut:

- Temperatur udara (°C)
- Kelembapan relatif (%)
- Solar irradiance (W/m²)
- Curah hujan (mm)
- Cloud cover (%)
- Energy mode
- Drying condition

## 4. Sistem Pengambilan Keputusan

Data lingkungan digunakan sebagai masukan untuk sistem pengambilan keputusan berbasis aturan (rule-based decision system).

### Energy Mode

Sistem menentukan tiga kondisi penggunaan energi:

- `SOLAR`
- `SOLAR + BIOMASS`
- `BIOMASS`

Penentuan mode didasarkan pada ketersediaan energi surya dan kondisi cuaca.

### Drying Condition

Sistem juga menghasilkan indikator kondisi pengeringan:

- `FAVORABLE`
- `MODERATE`
- `UNFAVORABLE`

Klasifikasi tersebut ditentukan berdasarkan kombinasi solar irradiance, curah hujan, dan kelembapan relatif.

Nilai ambang yang digunakan pada tahap awal merupakan parameter pengujian dan akan dievaluasi kembali setelah data dari sensor fisik tersedia.

## 5. Blynk Dashboard

Dashboard Blynk digunakan untuk menampilkan kondisi lingkungan dan rekomendasi penggunaan energi secara berkala.

Datastream yang digunakan:

| Virtual Pin | Datastream | Satuan |
|-------------|------------|--------|
| V0 | ambient_temperature | °C |
| V1 | relative_humidity | % |
| V2 | solar_irradiance | W/m² |
| V3 | precipitation | mm |
| V4 | cloud_cover | % |
| V5 | energy_mode | - |
| V6 | drying_condition | - |
| V7 | last_update | Waktu |

Selain parameter lingkungan dan rekomendasi energi, dashboard juga menampilkan waktu pembaruan terakhir (`last_update`) untuk menunjukkan kapan data terakhir diperbarui.
Data juga disimpan sebagai data historis dan ditampilkan melalui grafik untuk memantau perubahan kondisi lingkungan dari waktu ke waktu.

## 6. Perangkat Lunak

Sistem menggunakan:

- Python 3.12
- Requests
- Open-Meteo API
- Blynk Cloud
- Blynk Dashboard

## 7. Instalasi

### 7.1 Clone Repository

```bash
git clone https://github.com/USERNAME/solar-dome-hybrid-iot.git
cd solar-dome-hybrid-iot
