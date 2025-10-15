import mysql.connector

def koneksiKeDatabase():
    try:
        koneksi = mysql.connector.connect(
           host = 'localhost',
           user = 'root',
           password = '',
           database = 'apotek_app_python'  
        )
        return koneksi
    except mysql.connector.Error as error:
        print(f"Gagal koneksi ke database: {error}")
        return None