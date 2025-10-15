from koneksi import *


session = {
    'is_login' : False,
    'dataUser' : None
}

def login(username,password):
    db = koneksiKeDatabase()
    if db is None:
        print('Koneksi ke database gagal')
        
    cursor = db.cursor(dictionary=True)
    query = 'select * from user where username = %s and password = %s'
    cursor.execute(query,(username,password))
    dataUserDariDatabase = cursor.fetchone()
    
    if dataUserDariDatabase:
        session['is_login'] = True
        session['dataUser'] = {
            'id' : dataUserDariDatabase['id'],
            'username' : dataUserDariDatabase['username'],
            'role' : dataUserDariDatabase['role']
        }
        pesan = f"Selamat datang {dataUserDariDatabase['username']}!"
    else:
        pesan = "Username atau password salah"
        
    cursor.close()
    db.close()
    
    return pesan
    