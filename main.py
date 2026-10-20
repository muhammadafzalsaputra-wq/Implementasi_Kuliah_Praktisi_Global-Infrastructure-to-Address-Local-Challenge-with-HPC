import csv

def baca_data_pm25(nama_file):
    data_wilayah = []
    try:
        with open(nama_file, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for baris in reader:
                # Menghitung rata-rata harian PM2.5 dari pagi, siang, dan malam
                rata_rata = (float(baris['pm25_pagi']) + float(baris['pm25_siang']) + float(baris['pm25_malam'])) / 3
                baris['rata_rata'] = round(rata_rata, 2)
                data_wilayah.append(baris)
        return data_wilayah
    except FileNotFoundError:
        print(f"File {nama_file} tidak ditemukan!")
        return []

def analisis_kualitas_udara(data):
    print("=== LAPORAN ANALISIS KUALITAS UDARA (PM2.5) LOKAL ===")
    print("Materi: Bridging Global Infrastructure to Address Local Challenge with HPC\n")
    
    if not data:
        print("Tidak ada data untuk dianalisis.")
        return

    print(f"{'Wilayah':<15} | {'Rata-rata PM2.5':<15} | {'Status Udara':<15}")
    print("-" * 51)

    for item in data:
        avg = item['rata_rata']
        if avg > 50:
            status = "Tidak Sehat"
        elif avg > 30:
            status = "Sedang"
        else:
            status = "Baik"
            
        print(f"{item['wilayah']:<15} | {avg:<15} | {status:<15}")

    # Mencari wilayah dengan polusi tertinggi (Simulasi komputasi pencarian nilai ekstrem)
    terburuk = max(data, key=lambda x: x['rata_rata'])
    print("\n[Rekomendasi Tindakan Lokal]:")
    print(f" Wilayah dengan tingkat polusi tertinggi adalah **{terburuk['wilayah']}** dengan rata-rata PM2.5 sebesar {terburuk['rata_rata']}.")
    print(" Solusi: Diperlukan penerapan pemodelan berbasis HPC/Cloud untuk mitigasi dini dan peringatan bagi warga.")

if __name__ == "__main__":
    file_path = "data_pm25.csv"
    data_sensor = baca_data_pm25(file_path)
    analisis_kualitas_udara(data_sensor)