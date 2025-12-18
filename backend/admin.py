from .koneksi import *

# Kelola Obat 
def tambahObat(namaObat, jenis, harga, stok, tgl_produksi, kadaluarsa, kategoriId):
    db = koneksiKeDatabase()
    
    if db is None:
        return "Gagal koneksi ke database"

    cursor = db.cursor() 
    
    try:
        # Format string biar rapi
        namaObat = str(namaObat).strip().title()
        jenis = str(jenis).strip().title()
        
        # Pastikan input angka aman
        stok_input = int(stok)
        harga_input = float(harga) 

        # 1. CEK DULU: Cari obat yang atributnya KEMBAR (termasuk tanggal)
        query_cek = '''
            SELECT obatId, stok FROM obat 
            WHERE namaObat = %s 
            AND jenis = %s 
            AND kategoriId = %s
            AND tgl_produksi = %s 
            AND kadaluarsa = %s
        '''
        cursor.execute(query_cek, (namaObat, jenis, kategoriId, tgl_produksi, kadaluarsa))
        data_exist = cursor.fetchone()
        
        if data_exist:
            # === UPDATE (REPLACE STOK) ===
            obatId_lama = data_exist['obatId']  
            
            # REVISI: Langsung pakai stok_input (jangan ditambah stok_lama)
            # Jadi stok di database akan berubah sesuai inputan baru
            
            query_update = '''
                UPDATE obat 
                SET stok = %s, harga = %s 
                WHERE obatId = %s
            '''
            cursor.execute(query_update, (stok_input, harga_input, obatId_lama))
            pesan = f'Data Double Ditemukan: Stok obat "{namaObat}" telah diubah (replace) menjadi {stok_input}'
            
        else:
            # === INSERT (DATA BARU) ===
            query_insert = '''
                INSERT INTO obat(namaObat, jenis, harga, stok, tgl_produksi, kadaluarsa, kategoriId) 
                VALUES(%s, %s, %s, %s, %s, %s, %s)
            '''
            cursor.execute(query_insert, (namaObat, jenis, harga_input, stok_input, tgl_produksi, kadaluarsa, kategoriId))
            pesan = 'Data obat baru berhasil ditambahkan'

        db.commit()
        
    except Exception as e:
        print(f"Error detail: {e}") 
        pesan = f"Terjadi kesalahan {e}"
        
    finally:
        cursor.close()
        db.close()
    
    return pesan

def lihatSemuaDataObat():
    db = koneksiKeDatabase()
    if db is None:
        pesan = "Gagal koneksi ke database"
        return pesan
    
    cursor = db.cursor()
    query = '''
        SELECT 
            o.*, 
            k.namaKategori 
        FROM obat o
        LEFT JOIN kategoriObat k ON o.kategoriId = k.kategoriId
    '''
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
    
    cursor = db.cursor()
    query = 'select * from obat where obatId = %s'
    cursor.execute(query, (obatId,))
    dataObat = cursor.fetchone()
    
    if not dataObat:
        pesan = 'Data obat tidak ditemukkan'
        return pesan
    
    cursor.close()
    db.close()
    return dataObat

def updateObat(obatId, namaObat, jenis, harga, stok, tgl_produksi, kadaluarsa, kategoriId):
    db = koneksiKeDatabase()
    if db is None:
        return "Gagal koneksi ke database"
    
    cursor = db.cursor()
    try:
        # Format nama obat dan jenis ke title case (awal kata kapital)
        namaObat = namaObat.strip().title()
        jenis = jenis.strip().title()
        
        query = '''
            update obat 
            set 
                namaObat = %s, 
                jenis = %s, 
                harga = %s, 
                stok = %s, 
                tgl_produksi = %s, 
                kadaluarsa = %s,
                kategoriId = %s
            where obatId = %s
        '''
        cursor.execute(query, (namaObat, jenis, harga, stok, tgl_produksi, kadaluarsa, kategoriId, obatId))
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

    cursor = db.cursor()
    
    if not keyword:
        lihatSemuaDataObat()
        
    try:
        obatId = int(keyword)
        query = '''
            SELECT 
                o.*, 
                k.namaKategori 
            FROM obat o
            LEFT JOIN kategoriObat k ON o.kategoriId = k.kategoriId
            WHERE o.obatId = %s
        '''
        cursor.execute(query, (obatId,))
    except ValueError:
        query = '''
            SELECT 
                o.*, 
                k.namaKategori 
            FROM obat o
            LEFT JOIN kategoriObat k ON o.kategoriId = k.kategoriId
            WHERE o.namaObat LIKE %s
        '''
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
    
    cursor = db.cursor()
    query = '''
        select
            t.transaksiId,
            t.tanggalTransaksi,
            COALESCE(k.namaPembeli, '-') as namaPembeli,
            u.username as Kasir,
            t.totalHarga
        from transaksi as t
        left join keranjang k on t.keranjangId = k.keranjangId
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
    
    cursor = db.cursor()
    query = '''
        select  
            d.detailId,
            o.namaObat,
            d.jumlah,
            d.subtotal,
            k.namaPembeli
        from detailtransaksi as d
        join obat as o on d.obatId = o.obatId
        join transaksi as t on d.transaksiId = t.transaksiId
        left join keranjang as k on t.keranjangId = k.keranjangId
        where d.transaksiId = %s
    '''
    cursor.execute(query,(transaksiId,))
    dataDetailTransaksi = cursor.fetchall()
    
    cursor.close()
    db.close()
    return dataDetailTransaksi

def tambahKategori(namaKategori):
    db = koneksiKeDatabase()
    if db is None:
        return "Gagal koneksi ke database"
    
    cursor = db.cursor()
    try:
        query = 'insert into kategoriObat(namaKategori) values(%s)'
        cursor.execute(query, (namaKategori,))
        db.commit()
        pesan = 'Kategori baru berhasil ditambahkan'
    except Exception as e:
        pesan = f"Terjadi kesalahan: {e}"
        
    cursor.close()
    db.close()
    return pesan

def lihatSemuaKategori():
    db = koneksiKeDatabase()
    if db is None:
        return []
    
    cursor = db.cursor()
    query = 'select * from kategoriObat'
    cursor.execute(query)
    data = cursor.fetchall()
    
    cursor.close()
    db.close()
    return data

def lihatObatKadaluarsa():
    db = koneksiKeDatabase()
    if db is None:
        return "Gagal koneksi ke database"
    
    cursor = db.cursor()
    # Query: Ambil obat yang tanggalnya LEBIH KECIL dari hari ini
    query = """
        SELECT 
            o.*, 
            k.namaKategori 
        FROM obat o
        LEFT JOIN kategoriObat k ON o.kategoriId = k.kategoriId
        WHERE o.kadaluarsa < CURDATE()
        ORDER BY o.kadaluarsa ASC
    """
    cursor.execute(query)
    dataObat = cursor.fetchall()
    
    cursor.close()
    db.close()
    
    if not dataObat:
        return 'Tidak ada obat yang kadaluarsa'
    
    return dataObat

def filterTransaksiBerdasarkanWaktu(waktu):
    """
    Menampilkan transaksi mulai dari waktu yang dipilih (Format: 'YYYY-MM-DD HH:MM:SS').
    Contoh: filterTransaksiBerdasarkanWaktu('2021-04-05 06:00:00')
    """
    db = koneksiKeDatabase()
    if db is None:
        pesan = "Gagal koneksi ke database"
        return pesan
    
    cursor = db.cursor()
    
    # Query: Ambil transaksi yang tanggalnya LEBIH BESAR ATAU SAMA DENGAN waktu input
    query = '''
        SELECT
            t.transaksiId,
            t.tanggalTransaksi,
            u.username as Kasir,
            t.totalHarga
        FROM transaksi as t
        JOIN user as u on t.kasirId = u.userId
        WHERE t.tanggalTransaksi >= %s
        ORDER BY t.tanggalTransaksi ASC
    '''
    
    try:
        cursor.execute(query, (waktu,))
        dataTransaksi = cursor.fetchall()
    except Exception as e:
        pesan = f"Terjadi kesalahan query: {e}"
        return pesan
    
    cursor.close()
    db.close()
    
    # Cek apakah data kosong
    if not dataTransaksi:
        pesan = 'Tidak ada transaksi mulai dari waktu tersebut.'
        return pesan
    
    return dataTransaksi