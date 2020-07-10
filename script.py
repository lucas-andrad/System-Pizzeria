import pymysql.cursors

connection = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    db = 'pizzeria',
    charset = 'utf8mb4',
    cursorclass = pymysql.cursors.DictCursor
)

auth = False

def loginRegister():
    user = 0
    authenticate = False
    PrincipalUser = False
    ExistentUser = 0

    if decision == 1:
        name = input('Type your username: ')
        password = input('Type your password: ')
        for line in result:
            if name == line['name'] and password == line['password']:
                if line['level'] == 1:
                    PrincipalUser = False
                elif line['level'] == 2:
                    PrincipalUser = True
                    authenticate = True
                    break
                else:
                    authenticate = False
        if not authenticate:
            print('Wrong username or password. Try Again')
    elif decision == 2:
        print('Make your registration')
        name = input('Type your username: ')
        password = input('Type your password: ')
        verify = input('Repeat your password: ')
        if password != verify:
            print('Different name and password. Try Again')
        elif password == verify:
            for line in result:
                if name == line['name'] and password == line['password']:
                    ExistentUser = 1
            if ExistentUser == 1:
                print('User already registered')
            elif ExistentUser == 0:
                try:
                    with connection.cursor() as cursor:
                        cursor.execute(f'INSERT INTO registration(name, password, level) VALUES ("{name}", "{password}", "{1}")')
                        connection.commit()
                        print('Success! User registered!')
                except:
                    print('UNKOWN ERROR. Try Again')
    return authenticate, PrincipalUser





while not auth:
    decision = int(input('Type 1 for login or 2 for register'))

    try:
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM registration')
            result = cursor.fetchall()
    except:
        print('UNKOWN ERROR')   

    authenticate, PrincipalUser = loginRegister()

if auth == True:
    print('authenticate')