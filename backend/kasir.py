from .koneksi import koneksiKeDatabase
from .login import session
from .apoteker import batalkanKeranjang
from datetime import date

sessionKeranjangSaatIni = {
    'keranjangSaatini' : None
}

def cariObatLayakJual(keyword=""):
    db = koneksiKeDatabase()
    if db is None:
        return "Gagal koneksi ke database"

    cursor = db.cursor()
    
    # Kalau keyword kosong, tampilin semua yang AMAN
    if not keyword:
        query = """
            SELECT * FROM obat 
            WHERE kadaluarsa >= CURDATE() 
            AND stok > 0
        """
        cursor.execute(query)
    else:
        # Kalau ada keyword, cari nama/ID tapi tetep filter tanggalnya
        try:
            obatId = int(keyword)
            query = """
                SELECT * FROM obat 
                WHERE obatId = %s 
                AND kadaluarsa >= CURDATE()
            """
            cursor.execute(query, (obatId,))
        except ValueError:
            query = """
                SELECT * FROM obat 
                WHERE namaObat LIKE %s 
                AND kadaluarsa >= CURDATE()
            """
            cursor.execute(query, (f"%{keyword}%",))
    
    hasil = cursor.fetchall()
    cursor.close()
    db.close()
    
    if not hasil:
        return 'Data obat tidak ditemukan atau stok kosong/kadaluarsa'
    
    return hasil

def cariKeranjangByJam(keyword):
    db = koneksiKeDatabase()
    if db is None:
        return "Gagal koneksi ke database"
    
    cursor = db.cursor()
    
    # Query: Cari status 'dikirim', TAPI filter jam-nya mirip sama keyword
    # DATE(k.tanggalDibuat) = CURDATE() -> Biar yang dicari cuma transaksi HARI INI
    query = """
        SELECT 
            k.keranjangId,
            k.namaPembeli,
            k.totalHarga,
            u.nama AS namaApoteker,
            k.status,
            k.tanggalDibuat
        FROM keranjang AS k
        JOIN user AS u ON u.userId = k.apotekerId
        WHERE k.status = 'dikirim' 
        AND DATE(k.tanggalDibuat) = CURDATE()
        AND TIME(k.tanggalDibuat) LIKE %s
    """
    
    # Tambahin % di depan belakang biar bisa search fleksibel (contoh: "14" bakal nemu 14:00, 14:30)
    param = f"%{keyword}%"
    
    cursor.execute(query, (param,))
    data = cursor.fetchall()
    
    cursor.close()
    db.close()
    
    if not data:
        return [] # Balikin list kosong kalau gak nemu
        
    return data

def buatKeranjang(apotekerId, namaPembeli):
    db = koneksiKeDatabase()
    if db is None:
        pesan = 'Gagal terkoneksi ke database'
        return pesan
    
    cursor = db.cursor()
    query = 'insert into keranjang(apotekerId,namaPembeli) values(%s,%s)'
    cursor.execute(query,(apotekerId,namaPembeli))
    db.commit()
    
    keranjangTerbaru = cursor.lastrowid
    cursor.close()
    db.close()
    
    if keranjangTerbaru :
        sessionKeranjangSaatIni['keranjangSaatIni'] = {
            'keranjangId' : keranjangTerbaru['keranjangId'],
            'apotekerId' : session['dataUser']['userId'],
            'namaPembeli' : namaPembeli
        }
    
    return keranjangTerbaru

def lihatKeranjang(keranjangId):
    if not sessionKeranjangSaatIni['keranjangSaatIni']:
        return 'Buat Keranjang Dulu'
    
    db = koneksiKeDatabase()
    if db is None:
        pesan = 'Gagal terkoneksi ke database'
        return pesan
    
    cursor = db.cursor()
    queryKeranjang = '''
        select
            k.keranjangId, 
            k.namaPembeli, 
            k.totalHarga,
            k.status,
            u.nama as namaApoteker
        from keranjang as k
        join user as u on u.userId = k.apotekerId
        where keranjangId = %s
    '''
    cursor.execute(queryKeranjang,(keranjangId,))
    dataKeranjang = cursor.fetchone()
    
    if not dataKeranjang :
        cursor.close()
        db.close()
        pesan = 'Keranjang tidak ditemukan'
        return pesan
    
    queryDetailKeranjang = '''
        select 
            dk.detailKeranjangId,
            o.namaObat,
            kat.namaKategori,  
            dk.jumlah,
            dk.subtotal
        from keranjangdetail as dk
        join obat as o on o.obatId = dk.obatId
        left join kategoriObat as kat on kat.kategoriId = o.kategoriId
        where dk.keranjangId = %s
    '''

    cursor.execute(queryDetailKeranjang, (dataKeranjang['keranjangId'],))
    detailObatDiKeranjang = cursor.fetchall()
    
    cursor.close()
    db.close()
    
    dataKeranjang['detailObat'] = detailObatDiKeranjang
    
    return dataKeranjang

def tambahObatKeKeranjang(keranjangId, obatId, jumlah):
    if not sessionKeranjangSaatIni['keranjangSaatIni']:
        return 'Buat Keranjang Dulu'
    
    if jumlah <= 0:
        return "Jumlah obat tidak boleh kurang dari 1"
    
    db = koneksiKeDatabase()
    if db is None:
        pesan = 'Gagal terkoneksi ke database'
        return pesan

    cursor = db.cursor()
    
    query = 'select * from obat where obatId = %s'
    cursor.execute(query,(obatId,))
    dataObat = cursor.fetchone()
    
    if not dataObat:
        cursor.close(); db.close()
        return "Data obat tidak ditemukan"
    
    # --- VALIDASI TAMBAHAN: KADALUARSA ---
    # Cek apakah tanggal hari ini lebih besar dari tanggal kadaluarsa obat
    if dataObat['kadaluarsa'] and dataObat['kadaluarsa'] < date.today():
        cursor.close(); db.close()
        return f"GAGAL! Obat {dataObat['namaObat']} sudah kadaluarsa ({dataObat['kadaluarsa']}). Tidak boleh dijual!"
    # -------------------------------------

    if dataObat['stok'] < jumlah:
        cursor.close(); db.close()
        pesan = 'Stok obat tidak mencukupi'
        return pesan
    
    subTotal =  float(dataObat['harga']) * jumlah
    
    queryTambahKeKeranjang = 'insert into keranjangdetail(keranjangId, obatId, jumlah, subtotal) values(%s,%s,%s,%s)'
    cursor.execute(queryTambahKeKeranjang,(keranjangId, obatId, jumlah, subTotal))
    
    queryKurangiStok = 'update obat set stok = stok - %s where obatId = %s'
    cursor.execute(queryKurangiStok, (jumlah, dataObat['obatId']))
    
    queryUpdateTotalPembayaranDiKeranjang = 'update keranjang set totalHarga = totalHarga + %s where keranjangId = %s'
    cursor.execute(queryUpdateTotalPembayaranDiKeranjang, (subTotal, keranjangId))
    
    db.commit()
    cursor.close()
    db.close()
    pesan = f"Obat {dataObat['namaObat']} berhasil ditambahkan ke keranjang"
    return pesan

def updateJumlahObatYangDiBeli(detailKeranjangId, jumlahBaru):
    # Pengecekan session dihapus agar bisa digunakan dari detail view
    
    if jumlahBaru <= 0:
        return "Jumlah obat tidak boleh kurang dari 1"
    
    db = koneksiKeDatabase()
    if db is None:
        pesan = 'Gagal terkoneksi ke database'
        return pesan
    
    cursor = db.cursor()
    
    try:
        # 1. Ambil data keranjang detail yang lama
        query = 'select * from keranjangdetail where detailKeranjangId = %s'
        cursor.execute(query,(detailKeranjangId,))
        dataLama = cursor.fetchone()
        
        if not dataLama:
            cursor.close(); db.close()
            return "Item keranjang tidak ditemukan"
        
        # 2. Ambil data stok obat terkini di gudang
        queryAmbilDataObat = 'select * from obat where obatId = %s'
        cursor.execute(queryAmbilDataObat,(dataLama['obatId'], ))
        dataObat = cursor.fetchone()
        
        if not dataObat:
            cursor.close(); db.close()
            return "Data obat tidak ditemukan"
        
        # 3. Hitung selisih (Jumlah Baru - Jumlah Lama)
        selisihJumlah = jumlahBaru - dataLama['jumlah']
        
        # --- LOGIC VALIDASI STOK (BARU) ---
        if selisihJumlah > 0 :
            # Kalau nambah jumlah, cek dulu stok gudang cukup gak?
            if dataObat['stok'] < selisihJumlah:
                cursor.close(); db.close()
                return f"Gagal! Stok tidak cukup. Sisa stok cuma {dataObat['stok']}, tapi kamu minta tambah {selisihJumlah} lagi."
            
            # Kalau cukup, baru update
            queryKurangiStok = 'update obat set stok = stok - %s where obatId = %s'
            cursor.execute(queryKurangiStok,(selisihJumlah, dataObat['obatId']))
            
        elif selisihJumlah < 0:
            # Kalau mengurangi jumlah (misal dari 5 jadi 3), balikin stok ke gudang
            queryKembalikanStok = 'update obat set stok = stok + %s where obatId = %s'
            cursor.execute(queryKembalikanStok,(abs(selisihJumlah), dataObat['obatId']))
        # ----------------------------------
        
        # Update Subtotal dan Jumlah di Keranjang
        # PENTING: Konversi ke float untuk menghindari error Decimal vs float
        subTotalLama = float(dataLama['subtotal'])
        subTotalBaru = float(dataObat['harga']) * jumlahBaru
        selisihSubTotal = subTotalBaru - subTotalLama
        
        queryUpdateDataDetailKeranjang = '''
            update keranjangdetail 
            set 
                jumlah = %s, 
                subtotal = %s
            where detailKeranjangId = %s
        '''   
        cursor.execute(queryUpdateDataDetailKeranjang, (jumlahBaru, subTotalBaru, detailKeranjangId))
        
        # Update Total Harga Keranjang Utama
        if selisihSubTotal > 0:
            queryTambahTotal = 'update keranjang set totalHarga = totalHarga + %s where keranjangId = %s'
            cursor.execute(queryTambahTotal,(selisihSubTotal, dataLama['keranjangId']))
        elif selisihSubTotal < 0:
            queryKurangTotal = 'update keranjang set totalHarga = totalHarga - %s where keranjangId = %s'
            cursor.execute(queryKurangTotal,(abs(selisihSubTotal), dataLama['keranjangId']))
            
        db.commit()
        pesan = f"Item {dataObat['namaObat']} pada keranjang berhasil di update"
        
    except Exception as e:
        db.rollback()
        pesan = f"Terjadi kesalahan: {e}"
        
    cursor.close()
    db.close()
    return pesan

def hapusObatDariKeranjang(detailKeranjangId):
    if not sessionKeranjangSaatIni['keranjangSaatIni']:
        return 'Buat Keranjang Dulu'
    
    db = koneksiKeDatabase()
    if db is None:
        return "Gagal koneksi ke database"

    cursor = db.cursor()
    
    queryAmbilObatYangAkanDihapus = """
        select
            kd.obatId,
            o.namaObat, 
            kd.jumlah, 
            kd.subtotal, 
            k.keranjangId
        from keranjangdetail as kd
        join keranjang as k ON k.keranjangId = kd.keranjangId
        join obat as o on o.obatId = kd.obatId
        where kd.detailKeranjangId = %s
    """
    cursor.execute(queryAmbilObatYangAkanDihapus, (detailKeranjangId,))
    dataDetailKeranjang = cursor.fetchone()
    
    if not dataDetailKeranjang:
        cursor.close()
        db.close()
        return "Data detail keranjang tidak ditemukan"
    
    queryKembalikanStok = 'update obat set stok = stok + %s where obatId = %s'
    cursor.execute(queryKembalikanStok,(dataDetailKeranjang['jumlah'], dataDetailKeranjang['obatId']))
    
    queryKurangiTotal = 'update keranjang set totalHarga = totalHarga - %s where keranjangId = %s'
    cursor.execute(queryKurangiTotal, (dataDetailKeranjang['subtotal'], dataDetailKeranjang['keranjangId'])) 
    
    queryHapusDetailKeranjang = 'delete from keranjangdetail where detailKeranjangId = %s'
    cursor.execute(queryHapusDetailKeranjang,(detailKeranjangId,))
    
    db.commit()
    cursor.close()
    db.close()
    return f"Obat {dataDetailKeranjang['namaObat']} telah berhasil dihapus dari keranjang"

def kirimKeranjangKeKasir(keranjangId):
    if not sessionKeranjangSaatIni['keranjangSaatIni']:
        return 'Buat Keranjang Dulu'
    
    db = koneksiKeDatabase()
    if db is None:
        return "Gagal koneksi ke database"
    
    cursor = db.cursor()
    queryKirim = "update keranjang set status = 'dikirim' where keranjangId = %s"
    cursor.execute(queryKirim,(keranjangId,))

    db.commit()
    cursor.close()
    db.close()
    
    sessionKeranjangSaatIni['keranjangSaatIni'] = None
    return f"Keranjang dengan id {keranjangId} berhasil dikirim ke kasir"

def batalkanKeranjang(keranjangId):
    if not sessionKeranjangSaatIni['keranjangSaatIni']:
        return 'Buat Keranjang Dulu'
    
    db = koneksiKeDatabase()
    if db is None:
        return "Gagal koneksi ke database"

    cursor = db.cursor()
    
    try:
        queryAmbilDetailKeranjang = '''
            select
                obatId,
                jumlah
            from keranjangdetail
            where keranjangId = %s
        '''
        cursor.execute(queryAmbilDetailKeranjang,(keranjangId,))
        daftarObat = cursor.fetchall()
        
        for item in daftarObat:
            queryKembalikanStok = 'update obat set stok = stok + %s where obatId = %s'
            cursor.execute(queryKembalikanStok,(item['jumlah'], item['obatId']))
            
        # queryHapusDetailKeranjang = 'delete from keranjangdetail where keranjangId = %s'
        # cursor.execute(queryHapusDetailKeranjang,(keranjangId,))
        
        # queryHapusKeranjang = 'delete from keranjang where keranjangId = %s'
        # cursor.execute(queryHapusKeranjang,(keranjangId,))
        
        db.commit()
        pesan = f"Keranjang dengan id {keranjangId} berhasil di batalkan"
    except Exception as e:
        db.rollback()
        pesan = f"Gagal membatalkan keranjang : {e}"
    
    
    cursor.close()
    db.close()
    sessionKeranjangSaatIni['keranjangSaatIni'] = None
    return pesan
    

def lihatDaftarKeranjangDikirim():
    db = koneksiKeDatabase()
    if db is None:
        return "Gagal koneksi ke database"
    
    cursor = db.cursor()
    # Tampilkan semua keranjang dengan status 'dikirim' (tidak dibatasi tanggal)
    # Agar kasir bisa lihat semua keranjang yang menunggu pembayaran
    query = """
        SELECT 
            k.keranjangId,
            k.namaPembeli,
            k.totalHarga,
            u.nama AS namaApoteker,
            k.status,
            k.tanggalDibuat
        FROM keranjang AS k
        JOIN user AS u ON u.userId = k.apotekerId
        WHERE k.status = 'dikirim'
        ORDER BY k.tanggalDibuat DESC
    """
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    db.close()
    
    return data

def lihatDetailKeranjangUntukKasir(keranjangId):
    db = koneksiKeDatabase()
    if db is None:
        return "Gagal koneksi ke database"
    
    cursor = db.cursor()
    queryKeranjang = """
        SELECT 
            k.keranjangId, 
            k.namaPembeli, 
            k.totalHarga,
            u.nama AS namaApoteker,
            k.status
        FROM keranjang AS k
        JOIN user AS u ON u.userId = k.apotekerId
        WHERE k.keranjangId = %s
    """
    cursor.execute(queryKeranjang, (keranjangId,))
    dataKeranjang = cursor.fetchone()
    
    if not dataKeranjang:
        cursor.close()
        db.close()
        return "Keranjang tidak ditemukan"
    
    queryDetail = """
        SELECT 
            d.detailKeranjangId,
            o.obatId,
            o.namaObat,
            o.jenis,
            kat.namaKategori,
            d.jumlah,
            d.subtotal
        FROM keranjangdetail AS d
        JOIN obat AS o ON o.obatId = d.obatId
        LEFT JOIN kategoriObat AS kat ON kat.kategoriId = o.kategoriId
        WHERE d.keranjangId = %s
    """
    cursor.execute(queryDetail, (keranjangId,))
    dataKeranjang["detail"] = cursor.fetchall()
    
    cursor.close()
    db.close()
    return dataKeranjang

def kondisiTransaksi(keranjangId, kondisi):
    db = koneksiKeDatabase()
    if db is None:
        return "Gagal koneksi ke database"
    
    cursor = db.cursor()
    
    # --- KONDISI DIBAYAR (LUNAS) ---
    if kondisi == "dibayar":
        # 1. Update status jadi 'bayar'
        updateKeranjang = "UPDATE keranjang SET status = 'bayar' WHERE keranjangId = %s"
        cursor.execute(updateKeranjang, (keranjangId,))

        # 2. Ambil total harga buat dicatat di tabel transaksi
        queryKeranjang = "SELECT totalHarga FROM keranjang WHERE keranjangId = %s"
        cursor.execute(queryKeranjang, (keranjangId,))
        dataKeranjang = cursor.fetchone()
        
        if not dataKeranjang:
             cursor.close(); db.close(); return "Keranjang tidak ditemukan"

        totalHarga = dataKeranjang['totalHarga']

        # 3. Catat di tabel Transaksi (Laporan Keuangan)
        # Pastikan session['userId'] ada isinya dari login
        kasirId = session.get('userId') 
        insertTransaksi = """
            INSERT INTO transaksi (kasirId, tanggalTransaksi, totalHarga, keranjangId)
            VALUES (%s, NOW(), %s, %s)
        """
        cursor.execute(insertTransaksi, (kasirId, totalHarga, keranjangId))
        transaksiId = cursor.lastrowid

        # 4. Pindahin detail belanja ke detail transaksi (Arsip)
        detail = lihatDetailKeranjangUntukKasir(keranjangId)['detail']
        for item in detail:
            insertDetail = """
                INSERT INTO detailtransaksi (transaksiId, obatId, jumlah, subtotal)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(insertDetail, (transaksiId, item['obatId'], item['jumlah'], item['subtotal']))

        pesan = f"Transaksi keranjang {keranjangId} berhasil dilunasi."

    # --- KONDISI DIBATALKAN (SOFT DELETE) ---
    elif kondisi == "dibatalkan": 
        # Cek dulu apakah statusnya masih 'dikirim'. Kalau udah 'bayar' gaboleh batal.
        cekStatus = "SELECT status FROM keranjang WHERE keranjangId = %s"
        cursor.execute(cekStatus, (keranjangId,))
        statusSaatIni = cursor.fetchone()
        
        if statusSaatIni and statusSaatIni['status'] == 'bayar':
            cursor.close(); db.close()
            return "Gagal! Transaksi sudah dibayar, tidak bisa dibatalkan."

        # 1. Ambil daftar obat buat balikin stok
        queryAmbilDetailKeranjang = '''
            select obatId, jumlah from keranjangdetail where keranjangId = %s
        '''
        cursor.execute(queryAmbilDetailKeranjang,(keranjangId,))
        daftarObat = cursor.fetchall()
        
        # 2. Balikin stok ke tabel obat
        for item in daftarObat:
            queryKembalikanStok = 'update obat set stok = stok + %s where obatId = %s'
            cursor.execute(queryKembalikanStok,(item['jumlah'], item['obatId']))
            
        # 3. JANGAN DIHAPUS, TAPI UPDATE STATUS JADI 'DIBATALKAN'
        # Biar bos bisa liat history: "Oh, keranjang ini batal gara-gara customer gak bawa duit"
        queryUpdateStatus = "UPDATE keranjang SET status = 'dibatalkan' WHERE keranjangId = %s"
        cursor.execute(queryUpdateStatus,(keranjangId,))
        
        db.commit()
        pesan = f"Transaksi keranjang {keranjangId} telah dibatalkan (Stok sudah dikembalikan)."

    else:
        cursor.close()
        db.close()
        return "Kondisi tidak dikenali"
    
    db.commit()
    cursor.close()
    db.close()
    return pesan

def hapusItemDiKasir(detailKeranjangId):
    db = koneksiKeDatabase()
    if db is None:
        return "Gagal koneksi ke database"

    cursor = db.cursor()

    # 1. Ambil data item yang mau dihapus
    # Kita perlu: obatId (buat balikin stok), jumlah, subtotal (buat potong harga), dan keranjangId
    queryGetItem = """
        SELECT 
            kd.obatId, 
            kd.jumlah, 
            kd.subtotal, 
            kd.keranjangId, 
            k.status, 
            o.namaObat
        FROM keranjangdetail kd
        JOIN keranjang k ON k.keranjangId = kd.keranjangId
        JOIN obat o ON o.obatId = kd.obatId
        WHERE kd.detailKeranjangId = %s
    """
    cursor.execute(queryGetItem, (detailKeranjangId,))
    dataItem = cursor.fetchone()

    if not dataItem:
        cursor.close()
        db.close()
        return "Item tidak ditemukan"

    # Validasi: Cuma boleh hapus kalau statusnya masih 'dikirim' (belum dibayar/batal)
    if dataItem['status'] != 'dikirim':
        cursor.close()
        db.close()
        return "Item tidak bisa dihapus karena status transaksi bukan 'dikirim'"

    try:
        # 2. Kembalikan stok obat ke gudang
        queryBalikinStok = "UPDATE obat SET stok = stok + %s WHERE obatId = %s"
        cursor.execute(queryBalikinStok, (dataItem['jumlah'], dataItem['obatId']))

        # 3. Kurangi Total Harga di Keranjang Utama
        queryUpdateTotal = "UPDATE keranjang SET totalHarga = totalHarga - %s WHERE keranjangId = %s"
        cursor.execute(queryUpdateTotal, (dataItem['subtotal'], dataItem['keranjangId']))

        # 4. Hapus Item dari Database
        queryHapusItem = "DELETE FROM keranjangdetail WHERE detailKeranjangId = %s"
        cursor.execute(queryHapusItem, (detailKeranjangId,))

        db.commit()
        pesan = f"Obat {dataItem['namaObat']} berhasil dibatalkan dari transaksi."

    except Exception as e:
        db.rollback()
        pesan = f"Terjadi kesalahan: {e}"

    cursor.close()
    db.close()
    return pesan
