import psycopg2
from datetime import datetime

print('Welcome To Atm')

# function for total balance
def balance():
    #connnection between python and pgadmin
    conn = psycopg2.connect(
        host="yourhost",
        port=5432,
        database="your databse name",
        user="your user name",
        password="your  password"
    )

    # Create a cursor object
    cur = conn.cursor()

    # Execute a query
    cur.execute(f"SELECT total_amount FROM Bank where username='{z}'")

    result=cur.fetchall()
    # Fetch the results

    for row in result:
        print("Your Total Balance is ", row[0] ,"₹")

    conn.close()  # connection closed

# Function for withdraw amount
def Withdraw_amount():
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="new1",
        user="postgres",
        password="Avinash"
    )

    # Create a cursor object
    cur = conn.cursor()

    # Execute a query
    cur.execute(f"SELECT total_amount FROM Bank where username='{z}';")

    result=cur.fetchall()
    # Fetch the results

    for row in result:
        x1= row[0]

    if wi_amount > x1:
        print(f'sorry insufficient balance you have only {x1} balance')
    else:
        wi_bal=x1 - wi_amount
        print(f'Your Total balance is {wi_bal} ₹')



    cur.execute(f"UPDATE Bank SET total_amount = {wi_bal}, last_login = '{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}' WHERE username='{z}';")

    conn.commit()

    conn.close()

#Function for deposite amount
def Deposite_amount():
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="new1",
        user="postgres",
        password="Avinash"
    )

    # Create a cursor object
    cur = conn.cursor()

    # Execute a query
    cur.execute(f"SELECT total_amount FROM Bank where username='{z}';")

    result=cur.fetchall()
    # Fetch the results

    for row in result:
        x1= row[0]


    Dep_amount=x1+de_amount
    print(f'Your Total balance is {Dep_amount} ₹')


    cur.execute(f"UPDATE Bank SET total_amount = {Dep_amount}, last_login = '{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}' WHERE username='{z}';")

    conn.commit()

    conn.close()

i=1
while i<=3:

    user = {1234: "Sachin", 1111: "Virat", 2222: "Rohit"}
    user_in = int(input('Entere Your pin :'))

    cho = [1, 2, 3]

    if user_in in user:
        z = user[user_in]
        print(f'Hello {z} welcome to Atm ')
        print('1. Check your balance\n2. Withdraw amount\n3. Deposite amount')

        while (True):

            choise = int(input('press no :\n'))
            if choise in cho:

                if choise == 1:
                    balance()

                    x = input("do you want to continue Y for yes N for no:\n")
                    if x == 'n' or x == 'N':
                        print('Thanks for visiting')
                        break
                    elif x == 'Y' or x == 'y':

                        continue
                    else:
                        print('invalid action')
                        break

                elif choise == 2:
                    wi_amount = int(input('Enter Withdraw  amount:\n '))
                    Withdraw_amount()

                    x = input("do you want to continue Y for yes N for no:\n")
                    if x == 'n' or x == 'N':
                        print('Thanks for visiting')
                        break
                    elif x == 'Y' or x == 'y':
                        continue
                    else:
                        print('invalid action')
                        break
                elif choise == 3:

                    de_amount = int(input('Enter Deposite  amount\n '))
                    Deposite_amount()

                    x = input("do you want to continue Y for yes N for no:\n")
                    if x == 'n' or x == 'N':
                        print('Thanks for visiting')
                        break
                    elif x == 'Y' or x == 'y':
                        continue
                    else:
                        print('invalid action')
                        break
            else:
                print('invalid action')

        break
    else:
        attempt=3-i
        if attempt==0:
            print(f'sorry your all attempt are over . Try after some times.')
            break
        else:
            print(f'sorry you are not valid user {attempt} attempt left : enter correct pin ')
        i+=1
