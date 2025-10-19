from .koneksi import koneksiKeDatabase
from .login import session

sessionKeranjangSaatIni = {
    'keranjangSaatini' : None
}

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
    db = koneksiKeDatabase()
    if db is None:
        pesan = 'Gagal terkoneksi ke database'
        return pesan
    
    cursor = db.cursor(dictionary=True)
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
            dk.jumlah,
            dk.subtotal
            from keranjangdetail as dk
            join obat as o on o.obatId = dk.obatId
            where dk.keranjangId = %s
    '''
    cursor.execute(queryDetailKeranjang, (dataKeranjang['keranjangId'],))
    detailObatDiKeranjang = cursor.fetchall()
    
    cursor.close()
    db.close()
    
    dataKeranjang['detailObat'] = detailObatDiKeranjang
    
    return dataKeranjang

def tambahObatKeKeranjang(keranjangId, obatId, jumlah):
    if jumlah <= 0:
        return "Jumlah obat tidak boleh kurang dari 1"
    
    db = koneksiKeDatabase()
    if db is None:
        pesan = 'Gagal terkoneksi ke database'
        return pesan
    
    cursor = db.cursor(dictionary=True)
    
    query = 'select * from obat where obatId = %s'
    cursor.execute(query,(obatId,))
    dataObat = cursor.fetchone()
    
    if not dataObat:
        cursor.close()
        db.close()
        return "Data obat tidak ditemukan"
        
    if dataObat['stok'] < jumlah:
        cursor.close()
        db.close()
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
    if jumlahBaru <= 0:
        return "Jumlah obat tidak boleh kurang dari 1"
    
    db = koneksiKeDatabase()
    if db is None:
        pesan = 'Gagal terkoneksi ke database'
        return pesan
    
    cursor = db.cursor(dictionary=True)
    
    try:
        query = 'select * from keranjangdetail where detailKeranjangId = %s'
        cursor.execute(query,(detailKeranjangId,))
        dataLama = cursor.fetchone()
        
        if not dataLama:
            cursor.close()
            db.close()
            return "Item keranjang tidak ditemukan"
        
        queryAmbilDataObat = 'select * from obat where obatId = %s'
        cursor.execute(queryAmbilDataObat,(dataLama['obatId'], ))
        dataObat = cursor.fetchone()
        
        if not dataObat:
            cursor.close()
            db.close()
            return "Data obat tidak ditemukan"
        
        selisihJumlah = jumlahBaru - dataLama['jumlah']
        if selisihJumlah > 0 :
            queryKurangiStok = 'update obat set stok = stok - %s where obatId = %s'
            cursor.execute(queryKurangiStok,(selisihJumlah, dataObat['obatId']))
        elif selisihJumlah < 0:
            queryKembalikanStok = 'update obat set stok = stok + %s where obatId = %s'
            cursor.execute(queryKembalikanStok,(abs(selisihJumlah), dataObat['obatId']))
        
        subTotalLama = dataLama['subtotal']
        subTotalBaru = dataObat['harga'] * jumlahBaru
        selisihSubTotal = subTotalBaru - subTotalLama
        
        queryUpdateDataDetailKeranjang = '''
            update keranjangdetail 
            set 
                jumlah = %s, 
                subtotal = %s
            where detailKeranjangId = %s
        '''   
        cursor.execute(queryUpdateDataDetailKeranjang, (jumlahBaru, subTotalBaru, detailKeranjangId))
        
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
    db = koneksiKeDatabase()
    if db is None:
        return "Gagal koneksi ke database"

    cursor = db.cursor(dictionary=True)
    
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
    db = koneksiKeDatabase()
    if db is None:
        return "Gagal koneksi ke database"

    cursor = db.cursor(dictionary=True)
    
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
            
        queryHapusDetailKeranjang = 'delete from keranjangdetail where keranjangId = %s'
        cursor.execute(queryHapusDetailKeranjang,(keranjangId,))
        
        queryHapusKeranjang = 'delete from keranjang where keranjangId = %s'
        cursor.execute(queryHapusKeranjang,(keranjangId,))
        
        db.commit()
        pesan = f"Keranjang dengan id {keranjangId} berhasil di batalkan"
    except Exception as e:
        db.rollback()
        pesan = f"Gagal membatalkan keranjang : {e}"
    
    
    cursor.close()
    db.close()
    sessionKeranjangSaatIni['keranjangSaatIni'] = None
    return pesan
    