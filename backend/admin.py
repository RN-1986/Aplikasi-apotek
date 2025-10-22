from .koneksi import *

# Kelola Obat 
def tambahObat(namaObat, jenis, harga, stok, kadaluarsa):
    db = koneksiKeDatabase()
    cursor = db.cursor()
    
    if db is None:
        pesan = "Gagal koneksi ke database"
        return pesan
    
    try:
        query = 'insert into obat(namaObat, jenis, harga, stok, kadaluarsa) values(%s,%s,%s,%s, %s)'
        cursor.execute(query,(namaObat,jenis,harga,stok,kadaluarsa))
        db.commit()
        pesan = 'Data obat baru telah ditambahkan'
    except Exception as e:
        pesan = f"Terjadi kesalahan {e}"
        return pesan

    cursor.close()
    db.close()
    return pesan

def lihatSemuaDataObat():
    db = koneksiKeDatabase()
    if db is None:
        pesan = "Gagal koneksi ke database"
        return pesan
    
    cursor = db.cursor(dictionary=True)
    query = 'select * from obat'
    cursor.execute(query)
    dataObat = cursor.fetchall()
    
    cursor.close()
    db.close()
    
    if not dataObat:
        pesan = 'Belum ada data obat'
        return pesan
    
    return dataObat

def ambilDataObatYangAkanDiUpdate(obatId):
    db = koneksiKeDatabase()
    if db is None:
        pesan = "Gagal koneksi ke database"
        return pesan
    
    cursor = db.cursor(dictionary=True)
    query = 'select * from obat where obatId = %s'
    cursor.execute(query, (obatId,))
    dataObat = cursor.fetchone()
    
    if not dataObat:
        pesan = 'Data obat tidak ditemukkan'
        return pesan
    
    cursor.close()
    db.close()
    return dataObat

def updateObat(obatId, namaObat, jenis, harga, stok, kadaluarsa):
    db = koneksiKeDatabase()
    if db is None:
        pesan = "Gagal koneksi ke database"
        return pesan
    
    cursor = db.cursor()
    try:
        query = 'update obat set namaObat = %s, jenis = %s, harga = %s, stok = %s, kadaluarsa = %s where obatId = %s'
        cursor.execute(query, (namaObat, jenis, harga, stok, kadaluarsa, obatId))
        db.commit()
        pesan = f'Data obat dengan id {obatId} berhasil di update'
    except Exception as e:
        pesan = f"Terjadi kesalahan {e}"
        
    cursor.close()
    db.close()
    
    return pesan

def hapusObat(obatId):
    db = koneksiKeDatabase()
    if db is None:
        pesan = "Gagal koneksi ke database"
        return pesan
    
    cursor = db.cursor()
    try:
        query = 'delete from obat where obatId = %s'
        cursor.execute(query, (obatId,))
        db.commit()
        pesan = f"Data obat dengan id {obatId} berhasil di hapus"
    except Exception as e:
        pesan = f"Terjadi kesalahan {e}"
        
    cursor.close()
    db.close()
    return pesan

def cariObat(keyword):
    db = koneksiKeDatabase()
    if db is None:
        return "Gagal koneksi ke database"

    cursor = db.cursor(dictionary=True)

    try:
        obatId = int(keyword)
        query = "SELECT * FROM obat WHERE obatId = %s"
        cursor.execute(query, (obatId,))
    except ValueError:
        query = "SELECT * FROM obat WHERE namaObat LIKE %s"
        cursor.execute(query, (f"%{keyword}%",))
    
    hasil = cursor.fetchall()
    if hasil == []:
        return 'Data obat tidak ditemukkan'
    
    
    cursor.close()
    db.close()
    return hasil


# Riwayat transaksi 
def lihatSemuaTransaksi():
    db = koneksiKeDatabase()
    if db is None:
        pesan = "Gagal koneksi ke database"
        return pesan
    
    cursor = db.cursor(dictionary=True)
    query = '''
        select
            t.transaksiId,
            t.tanggalTransaksi,
            u.username as Kasir,
            t.totalHarga
        from transaksi as t
        join user as u on t.kasirId = u.userId
        order by t.tanggalTransaksi desc
    '''    
    cursor.execute(query)
    dataTransaksi = cursor.fetchall()
    
    cursor.close()
    db.close()
    
    if not dataTransaksi:
        pesan = 'Belum ada data transaksi'
        return pesan
    
    return dataTransaksi

def lihatDetailTransaksi(transaksiId):
    db = koneksiKeDatabase()
    if db is None:
        pesan = "Gagal koneksi ke database"
        return pesan
    
    cursor = db.cursor(dictionary=True)
    query = '''
        select  
            d.detailId,
            o.namaObat,
            d.jumlah,
            d.subtotal
        from detailtransaksi as d
        join obat as o on d.obatId = o.obatId
        where d.transaksiId = %s
    '''
    cursor.execute(query,(transaksiId,))
    dataDetailTransaksi = cursor.fetchall()
    
    cursor.close()
    db.close()
    return dataDetailTransaksi