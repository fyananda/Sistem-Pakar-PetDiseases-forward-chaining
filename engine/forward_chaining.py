import pandas as pd

# ============================================================
# DESKRIPSI & SARAN PER PENYAKIT
# Tambahkan entri baru di sini saat menambah penyakit baru
# ============================================================

DESKRIPSI_PENYAKIT = {
    "Parvovirus": {
        "deskripsi": "Parvovirus adalah infeksi virus yang sangat menular pada anjing, "
                     "menyerang sistem pencernaan dan kekebalan tubuh.",
        "saran":     "Segera bawa ke dokter hewan. Hewan perlu cairan infus dan perawatan intensif."
    },
    "Parvovirus Anjing": {
        "deskripsi": "Parvovirus Anjing menyerang usus halus dan sumsum tulang, "
                     "menyebabkan diare berdarah dan penurunan sel darah putih.",
        "saran":     "Isolasi hewan dari anjing lain. Segera ke dokter hewan untuk terapi suportif."
    },
    "Infeksi Saluran Pernapasan Atas": {
        "deskripsi": "Infeksi pada saluran pernapasan bagian atas yang umum terjadi "
                     "pada kucing dan anjing, biasanya disebabkan virus atau bakteri.",
        "saran":     "Konsultasikan ke dokter hewan untuk pemberian antibiotik atau antivirus yang tepat."
    },
    "Infeksi Saluran Pernapasan Atas Kucing": {
        "deskripsi": "Infeksi saluran pernapasan atas pada kucing umumnya disebabkan "
                     "oleh Herpesvirus atau Calicivirus.",
        "saran":     "Jauhkan dari kucing lain. Berikan makanan lembut dan pastikan tetap terhidrasi."
    },
    "Gastroenteritis": {
        "deskripsi": "Peradangan pada lambung dan usus yang menyebabkan diare dan muntah, "
                     "dapat dipicu oleh infeksi bakteri, virus, atau makanan.",
        "saran":     "Pastikan hewan tetap terhidrasi. Berikan makanan ringan dan pantau kondisinya."
    },
    "Infeksi Jamur": {
        "deskripsi": "Infeksi yang disebabkan oleh jamur seperti Ringworm atau Aspergillus, "
                     "biasanya menyerang kulit, kuku, atau organ dalam.",
        "saran":     "Gunakan antijamur sesuai resep dokter. Jaga kebersihan lingkungan hewan."
    },
    "Distemper Anjing": {
        "deskripsi": "Penyakit virus yang sangat menular pada anjing, menyerang sistem "
                     "pernapasan, pencernaan, dan saraf.",
        "saran":     "Tidak ada pengobatan spesifik. Perawatan suportif dan isolasi segera diperlukan."
    },
    "Penyakit Mulut dan Kuku": {
        "deskripsi": "Penyakit virus yang sangat menular pada hewan berkuku belah seperti sapi, "
                     "kambing, dan domba, menyebabkan lepuhan di mulut dan kaki.",
        "saran":     "Laporkan ke dinas peternakan setempat. Isolasi hewan yang terinfeksi segera."
    },
    "Rabies": {
        "deskripsi": "Penyakit virus fatal yang menyerang sistem saraf pusat pada semua mamalia "
                     "termasuk manusia. Ditularkan melalui gigitan.",
        "saran":     "BAHAYA: Segera hubungi dokter hewan dan dinas kesehatan. Hewan harus dikarantina."
    },
    "Mastitis": {
        "deskripsi": "Peradangan pada kelenjar susu, umumnya terjadi pada sapi perah, "
                     "kambing, dan domba yang sedang laktasi.",
        "saran":     "Hubungi dokter hewan untuk terapi antibiotik. Lanjutkan pemerahan secara teratur."
    },
    "Kurap": {
        "deskripsi": "Infeksi jamur pada kulit yang menyebabkan rambut/bulu rontok melingkar "
                     "dan kulit bersisik. Dapat menular ke manusia.",
        "saran":     "Gunakan salep antijamur. Cuci tangan setelah memegang hewan dan bersihkan kandang."
    },
    "Leptospirosis": {
        "deskripsi": "Infeksi bakteri Leptospira yang menyerang ginjal dan hati. "
                     "Dapat menular ke manusia melalui urin hewan.",
        "saran":     "Segera ke dokter hewan untuk antibiotik. Hindari kontak langsung dengan urin hewan."
    },
    "Leptospirosis Anjing": {
        "deskripsi": "Infeksi bakteri pada anjing yang menyerang ginjal dan hati, "
                     "sering ditularkan melalui air yang terkontaminasi.",
        "saran":     "Segera ke dokter hewan. Gunakan sarung tangan saat merawat dan bersihkan area hewan."
    },
    "Influenza Kuda": {
        "deskripsi": "Penyakit pernapasan menular pada kuda yang disebabkan virus influenza, "
                     "menyebabkan demam tinggi dan batuk kering.",
        "saran":     "Istirahatkan kuda dari aktivitas berat. Konsultasi dokter hewan untuk antivirus."
    },
    "Penyakit Lyme": {
        "deskripsi": "Infeksi bakteri Borrelia yang ditularkan melalui gigitan kutu, "
                     "menyebabkan demam, pincang, dan pembengkakan sendi.",
        "saran":     "Berikan antibiotik sesuai resep dokter. Gunakan anti-kutu secara rutin."
    },
    "Parasit Usus": {
        "deskripsi": "Infestasi cacing atau protozoa di saluran pencernaan yang menyebabkan "
                     "diare, penurunan berat badan, dan perut buncit.",
        "saran":     "Berikan obat cacing sesuai petunjuk dokter hewan. Jaga kebersihan kandang."
    },
    "Demam Babi Afrika": {
        "deskripsi": "Penyakit virus sangat mematikan pada babi domestik dan liar "
                     "tanpa pengobatan atau vaksin yang tersedia.",
        "saran":     "WAJIB laporkan ke dinas peternakan. Lakukan biosekuriti ketat di area peternakan."
    },
    "Cacar Domba": {
        "deskripsi": "Penyakit virus pada domba dan kambing yang menyebabkan demam "
                     "dan lesi kulit papular di seluruh tubuh.",
        "saran":     "Isolasi hewan yang terinfeksi. Vaksinasi domba sehat di sekitarnya."
    },
    "Cacar Kambing": {
        "deskripsi": "Penyakit virus pada kambing yang menyebabkan lesi kulit, demam, "
                     "dan gangguan pernapasan, dapat mematikan pada anak kambing.",
        "saran":     "Isolasi segera dan hubungi dokter hewan. Lakukan vaksinasi pencegahan."
    },
    "Kolik Kuda": {
        "deskripsi": "Nyeri perut parah pada kuda yang dapat disebabkan oleh berbagai kondisi "
                     "gastrointestinal, dari gas berlebih hingga penyumbatan usus.",
        "saran":     "DARURAT: Segera hubungi dokter hewan. Jangan beri makan dan tetap gerakkan kuda."
    },
    "Bronkitis Kronis": {
        "deskripsi": "Peradangan kronis pada saluran bronkus yang menyebabkan batuk "
                     "persisten dan produksi lendir berlebih.",
        "saran":     "Konsultasikan ke dokter hewan. Jauhkan dari asap rokok dan debu."
    },
    "Koksidiosis": {
        "deskripsi": "Infeksi parasit protozoa Eimeria pada saluran pencernaan yang "
                     "umum terjadi pada hewan muda.",
        "saran":     "Berikan koksidiostat sesuai resep dokter. Jaga kebersihan kandang dan pakan."
    },
    "Pneumonia": {
        "deskripsi": "Peradangan pada paru-paru yang dapat disebabkan bakteri, virus, atau jamur, "
                     "menyebabkan kesulitan bernapas dan demam.",
        "saran":     "Segera ke dokter hewan untuk antibiotik atau antivirus. Pastikan hewan hangat."
    },
    "Arthritis": {
        "deskripsi": "Peradangan sendi yang menyebabkan nyeri, bengkak, dan keterbatasan gerak, "
                     "umum pada hewan tua.",
        "saran":     "Berikan anti-inflamasi sesuai resep dokter. Kurangi aktivitas fisik berat."
    },
}

# Deskripsi default untuk penyakit yang belum terdaftar
DESKRIPSI_DEFAULT = {
    "deskripsi": "Informasi detail untuk penyakit ini belum tersedia dalam database.",
    "saran":     "Segera konsultasikan ke dokter hewan untuk penanganan lebih lanjut."
}


# ============================================================
# FUNGSI UTAMA: FORWARD CHAINING
# ============================================================

def jalankan_forward_chaining(data: dict, df: pd.DataFrame) -> list[dict]:
    """
    Menjalankan algoritma Forward Chaining berdasarkan input pengguna.

    Parameters
    ----------
    data : dict
        Data dari session_state["data_diagnosa"], berisi:
        - jenis_hewan, jenis_kelamin, suhu_tubuh, detak_jantung
        - gejala_1..4 (bisa None), nafsu_makan, muntah, diare,
          batuk, sesak_nafas
    df : pd.DataFrame
        Dataset penyakit hewan yang sudah di-load.

    Returns
    -------
    list[dict] — daftar hasil diagnosa, sudah diurutkan dari
                 kecocokan tertinggi. Setiap item berisi:
                 penyakit, kecocokan, gejala_cocok, total_rule,
                 deskripsi, saran
    """

    GEJALA_COLUMNS = ["Gejala_1", "Gejala_2", "Gejala_3", "Gejala_4"]

    # ----------------------------------------------------------
    # 1. Kumpulkan semua gejala aktif dari input user
    # ----------------------------------------------------------
    selected_gejala = set()

    # Gejala klinis (dropdown)
    for key in ["gejala_1", "gejala_2", "gejala_3", "gejala_4"]:
        val = data.get(key)
        if val:
            selected_gejala.add(val.strip())

    # Gejala biner (Ya/Tidak) → masukkan ke set jika "Ya"
    GEJALA_BINER = {
        "nafsu_makan" : "Kehilangan Nafsu Makan",
        "muntah"      : "Muntah",
        "diare"       : "Diare",
        "batuk"       : "Batuk",
        "sesak_nafas" : "Kesulitan Bernafas",
    }
    for key, label in GEJALA_BINER.items():
        if data.get(key) == "Ya":
            selected_gejala.add(label)

    # ----------------------------------------------------------
    # 2. Filter dataset: cocokkan jenis hewan & kelamin
    # ----------------------------------------------------------
    filtered = df[
        (df["Jenis_Hewan"]   == data["jenis_hewan"]) &
        (df["Jenis_Kelamin"] == data["jenis_kelamin"])
    ]

    # ----------------------------------------------------------
    # 3. Bangun rules dari baris dataset
    # ----------------------------------------------------------
    rules = []
    for _, row in filtered.iterrows():
        rule_gejala = [
            str(row[col]).strip()
            for col in GEJALA_COLUMNS
            if pd.notna(row[col])
        ]
        rules.append({
            "penyakit" : row["Prediksi_Penyakit"],
            "gejala"   : rule_gejala,
            "suhu"     : row["Suhu_Tubuh"],
            "detak"    : row["Detak_Jantung"],
        })

    # ----------------------------------------------------------
    # 4. Hitung kecocokan tiap rule (Forward Chaining)
    # ----------------------------------------------------------
    akumulasi: dict[str, dict] = {}   # penyakit → hasil terbaik

    for rule in rules:
        if not rule["gejala"]:
            continue

        # Hitung gejala yang cocok
        cocok = sum(1 for g in selected_gejala if g in rule["gejala"])
        if cocok == 0:
            continue

        total_rule = len(rule["gejala"])
        persentase = (cocok / total_rule) * 100

        # Bonus suhu tubuh (toleransi ±2°C)
        try:
            suhu_rule = float(str(rule["suhu"]).replace("°C", "").strip())
            if abs(float(data["suhu_tubuh"]) - suhu_rule) <= 2:
                persentase += 10
        except (ValueError, TypeError):
            pass

        # Bonus detak jantung (toleransi ±30 bpm)
        try:
            detak_rule = int(str(rule["detak"]).replace("bpm", "").strip())
            if abs(int(data["detak_jantung"]) - detak_rule) <= 30:
                persentase += 10
        except (ValueError, TypeError):
            pass

        persentase = min(round(persentase, 2), 100.0)
        nama       = rule["penyakit"]

        # Simpan hanya nilai kecocokan tertinggi per penyakit
        if nama not in akumulasi or persentase > akumulasi[nama]["kecocokan"]:
            akumulasi[nama] = {
                "penyakit"     : nama,
                "kecocokan"    : persentase,
                "gejala_cocok" : cocok,
                "total_rule"   : total_rule,
            }

    # ----------------------------------------------------------
    # 5. Gabungkan dengan deskripsi & saran
    # ----------------------------------------------------------
    hasil = []
    for item in akumulasi.values():
        info = DESKRIPSI_PENYAKIT.get(item["penyakit"], DESKRIPSI_DEFAULT)
        hasil.append({
            **item,
            "deskripsi" : info["deskripsi"],
            "saran"     : info["saran"],
        })

    # Urutkan dari kecocokan tertinggi
    hasil.sort(key=lambda x: x["kecocokan"], reverse=True)
    return hasil