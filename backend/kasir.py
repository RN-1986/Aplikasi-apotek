from .koneksi import koneksiKeDatabase
from .login import session
from .apoteker import batalkanKeranjang

def lihatDaftarKeranjangDikirim():
    db = koneksiKeDatabase()
    if db is None:
        return "Gagal koneksi ke database"
    
    cursor = db.cursor()
    query = """
        SELECT 
            k.keranjangId,
            k.namaPembeli,
            k.totalHarga,
            u.nama AS namaApoteker,
            k.status
        FROM keranjang AS k
        JOIN user AS u ON u.userId = k.apotekerId
        WHERE k.status = 'dikirim'
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
    
    cursor = db.cursor(dictionary=True)
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
            d.jumlah,
            d.subtotal
        FROM keranjangdetail AS d
        JOIN obat AS o ON o.obatId = d.obatId
        WHERE d.keranjangId = %s
    """
    cursor.execute(queryDetail, (keranjangId,))
    dataKeranjang["detail"] = cursor.fetchall()
    
    cursor.close()
    db.close()
    return dataKeranjang


def ubahKondisiTransaksi(keranjangId, kondisi):
    db = koneksiKeDatabase()
    if db is None:
        return "Gagal koneksi ke database"
    
    cursor = db.cursor()

    if kondisi == "dibayar":
        updateKeranjang = "UPDATE keranjang SET status = 'lunas' WHERE keranjangId = %s"
        cursor.execute(updateKeranjang, (keranjangId,))

       
        queryKeranjang = "SELECT totalHarga FROM keranjang WHERE keranjangId = %s"
        cursor.execute(queryKeranjang, (keranjangId,))
        dataKeranjang = cursor.fetchone()
        totalHarga = dataKeranjang["totalHarga"]

        
        insertTransaksi = """
            INSERT INTO transaksi (keranjangId, kasirId, tanggalTransaksi, totalHarga)
            VALUES (%s, %s, NOW(), %s)
        """
        kasirId = session['dataUser']['id']
        cursor.execute(insertTransaksi, (keranjangId, kasirId, totalHarga))
        transaksiId = cursor.lastrowid

        detail = lihatDetailKeranjangUntukKasir(keranjangId)['detail']
        for item in detail:
            insertDetail = """
                INSERT INTO detailtransaksi (transaksiId, obatId, jumlah, subtotal)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(insertDetail, (transaksiId, item['obatId'], item['jumlah'], item['subtotal']))

        pesan = f"Transaksi keranjang {keranjangId} telah diterima dan dilunasi"

    elif kondisi == "dibatalkan": 
        hasil = batalkanKeranjang(keranjangId)
        pesan = f"Transaksi keranjang {keranjangId} telah dibatalkan. ({hasil})"

    else:
        cursor.close()
        db.close()
        return "Kondisi tidak dikenali"
    
    db.commit()
    cursor.close()
    db.close()
    return pesan
