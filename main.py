import sqlite3


#initialise sqlite
connection = sqlite3.connect('OurDataBase.db')
cursor = connection.cursor()

#creates database
cursor.execute('CREATE TABLE employees(name TEXT, surname TEXT, salary REAL)')

#Add values to the table
cursor.execute("INSERT INTO employees VALUES('Max', 'Maxington', 300000)")
connection.commit()

#Fetch all data
cursor.execute("SELECT * FROM employees")
print(cursor.fetchall())

#fetch one
print(cursor.fetchone())

#iterate through table
for i in cursor.execute("SELECT * FROM employees"):
    print(i)


#Use variables to add values
name = 'King'
surname = 'Arthur'
salary = 50000

cursor.execute("INSERT INTO employees VALUES(?,?,?)", (name, surname, salary))


