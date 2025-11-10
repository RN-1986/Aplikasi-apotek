import pymysql

def koneksiKeDatabase():
    try:
        koneksi = pymysql.connect(
           host = 'localhost',
           user = 'root',
           password = '',
           database = 'apotek_app_python',
           cursorclass= pymysql.cursors.DictCursor()  
        )
        return koneksi
    except pymysql.Error as error:
        print(f"Gagal koneksi ke database: {error}")
        return None