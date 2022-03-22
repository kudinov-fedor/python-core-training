password = input('Type your password here:')
if len(password) >= 6:
    if not password.isalnum():
        print('Password must contain only letters or numbers')
    else:
        print('Good')
elif len(password) < 6:
    print('Password should be longer than 6 characters')
