from .koneksi import *
import bcrypt

def register(nama, username, password, role):
    db = koneksiKeDatabase()                          
    if db is None:                          
        return "Gagal koneksi ke database"
    
    cursor = db.cursor()                    
 
    
    queryCek = "SELECT * FROM user WHERE username = %s"
    cursor.execute(queryCek, (username,))
    existingUser = cursor.fetchone()

    if existingUser:                        
        cursor.close()
        db.close()
        return "Username sudah digunakan."
    
    hashedPassword = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    queryInsert = "INSERT INTO user (nama, username, password, role) VALUES (%s, %s, %s, %s)"
    cursor.execute(queryInsert, (nama, username, hashedPassword, role))
    db.commit()                             
    
    cursor.close()                           
    db.close()                              
    
    return f"User '{username}' berhasil terdaftar sebagai {role}."
