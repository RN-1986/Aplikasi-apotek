from .koneksi import *
import bcrypt

session = {
    'is_login' : False,
    'dataUser' : None
}

def login(username,password):
    db = koneksiKeDatabase()
    if db is None:
        pesan = 'Koneksi ke database gagal'
        return pesan
        
    cursor = db.cursor()
    query = 'select * from user where username = %s'
    cursor.execute(query,(username,))
    dataUserDariDatabase = cursor.fetchone()
    
    if dataUserDariDatabase and bcrypt.checkpw(password.encode('utf-8'), dataUserDariDatabase['password'].encode('utf-8')):
        session['is_login'] = True
        session['dataUser'] = {
            'id' : dataUserDariDatabase['userId'],
            'username' : dataUserDariDatabase['username'],
            'role' : dataUserDariDatabase['role']
        }
        pesan = f"Selamat datang {dataUserDariDatabase['username']}!"
    else:
        pesan = "Username atau password salah"
        
    cursor.close()
    db.close()
    
    return pesan
