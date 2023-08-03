import mysql.connector
connection=mysql.connector.connect(host="localhost",port="3306",user="root",password="Mksql@123",database="mathan")
cursor=connection.cursor()
#cursor.execute("""DELETE FROM registeration WHERE name ='eren' """)
#cursor.execute("""create table registeration(name varchar(30),userid varchar(8),email varchar(100),password varchar(60))""")
#cursor.execute("INSERT INTO registration VALUES('mathankumar','mk1234','mk@gmail.com','mk12345')")
cursor.execute("""SELECT * from registeration""")

d=cursor.fetchall()
for i in d:
    print(i)

cursor.close()
connection.commit()
connection.close()


