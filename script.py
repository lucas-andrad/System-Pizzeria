# Importing library to make connection with sql
import pymysql.cursors 

# Creating connection with mysql
connection = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    db = 'pizzeria',
    charset = 'utf8mb4',
    cursorclass = pymysql.cursors.DictCursor
)

# Condition for authenticate
auth = False

# Function to make login or register
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

# Function to register product in database
def RegisterProduct():
    name = input('Type the product name: ')
    ingredients = input('Type the ingredients: ')
    group = input('Type the product group: ')
    price = float(input('Type the product price: '))
    try:
        with connection.cursor() as cursor:
            cursor.execute(f'INSERT INTO products(name, ingredients, class, price) VALUES ("{name}", "{ingredients}", "{group}", "{price}")')
            connection.commit()
            print('Sucess! Product registered')
    except:
        print('UNKOWN ERROR')  

# Function to show products
def ListProducts():
    products = []
    try:
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM products')
            results = cursor.fetchall()
    except:
        print('UNKOWN ERROR') 
    for i in results:
        products.append(i)
    if len(products) != 0:
        for i in range(0, len(products)):
            print(products[i])
    else:
        print('0 products registereds')    

# Function to delete products
def DeleteProducts():
    id = int(input('Type the product id you want to delete'))
    try:
        with connection.cursor() as cursor:
            cursor.execute(f'DELETE FROM products WHERE id = {id}')
            connection.commit()
            print('Success! Product deleted')
    except:
        print('UNKOWN ERROR')

# Function to list orders in pizzeria
def ListOrders():
    orders = []
    decision = 0

    while decision == 0:
        orders.clear()
        try:
            with connection.cursor() as cursor:
                cursor.execute('SELECT * FROM orders')
                results = cursor.fetchall()
        except:
            print('UNKOWN ERROR')
        for i in results:
            orders.append(i)
        if len(orders) != 0:
            for i in range(0, len(orders)):
                print(orders[i])
        else:
            print('None orders')
        decision = int(input('Type 0 to give a product as delivered or 1 to exit'))

        if decision == 0:
            id = int(input('Type the product ID'))
            
        try:
            with connection.cursor() as cursor:
                cursor.execute(f'DELETE FROM orders WHERE id = {id}')
                connection.commit()
                print('Success! Product deleted')
        except:
            print('UNKOWN ERROR')        


# Code running 
while not auth:
    decision = int(input('Type 1 to login or 2 to register'))

    try:
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM registration')
            result = cursor.fetchall()
    except:
        print('UNKOWN ERROR')   

    authenticate, PrincipalUser = loginRegister()

    if authenticate == True:
        print('authenticate')
        if PrincipalUser == True:
            UserDecision = 1
            while UserDecision != 0:    
                UserDecision = int(input('Type 0 to exit, 1 to register product, 2 to list registered products, 3 to list orders, 4 to visualize statistics'))

                if UserDecision == 1:
                    RegisterProduct()
                elif UserDecision == 2:
                    ListProducts()

                    delete = int(input('Type 1 to delete a product or 2 to exit'))
                    if delete == 1:
                        DeleteProducts()
                elif UserDecision == 3:
                    ListOrders()

                elif UserDecision == 4:
                    GenerateStatistic()
