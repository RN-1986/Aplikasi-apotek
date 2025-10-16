from koneksi import *
import hashlib

session = {
    'is_register': False,
    'message': None
}

def register(username, password, confirm_password, role='user'):
    db = koneksiKeDatabase()
    
    if db is None:
        print('Koneksi ke database gagal!')
        return "Koneksi ke database gagal!"
    
    try:
        cursor = db.cursor(dictionary=True)
        
        # Validasi input
        if not username or not password or not confirm_password:
            pesan = "Semua field harus diisi!"
            return pesan
        
        # Validasi panjang username
        if len(username) < 4:
            pesan = "Username minimal 4 karakter!"
            return pesan
        
        # Validasi panjang password
        if len(password) < 6:
            pesan = "Password minimal 6 karakter!"
            return pesan
        
        # Validasi konfirmasi password
        if password != confirm_password:
            pesan = "Password dan konfirmasi password tidak cocok!"
            return pesan
        
        # Cek apakah username sudah ada
        query_check = "SELECT * FROM user WHERE username = %s"
        cursor.execute(query_check, (username,))
        existing_user = cursor.fetchone()
        
        if existing_user:
            pesan = "Username sudah terdaftar!"
            return pesan
        
        # Hash password menggunakan MD5 (sesuaikan dengan sistem login Anda)
        # Catatan: Untuk keamanan lebih baik, gunakan bcrypt atau argon2
        hashed_password = hashlib.md5(password.encode()).hexdigest()
        
        # Insert user baru
        query_insert = "INSERT INTO user (username, password, role) VALUES (%s, %s, %s)"
        cursor.execute(query_insert, (username, hashed_password, role))
        db.commit()
        
        session['is_register'] = True
        session['message'] = "Registrasi berhasil! Silakan login."
        pesan = f"Selamat! Akun {username} berhasil dibuat."
        
    except mysql.connector.Error as error:
        db.rollback()
        print(f"Gagal registrasi ke database: {error}")
        pesan = "Registrasi gagal, terjadi kesalahan!"
        
    finally:
        cursor.close()
        db.close()
    
    return pesan