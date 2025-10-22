from .login import session

def logout():
    session['is_login'] = False,
    session['dataUser'] = None
    
    return 'Terimakasih'