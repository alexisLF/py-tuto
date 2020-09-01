import sqlite3, tkinter
conn = sqlite3.connect('ma_base.db')

cursor = conn.cursor()
cursor.execute("""DROP TABLE users""")
cursor.execute("""CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, name TEXT, pwd TEXT, age INTEGER)""")
conn.commit()

cursor.execute("""INSERT INTO users(name, age, pwd) VALUES(?, ?, ?)""", ("alexis", 21, "password1"))

cursor.execute("""INSERT INTO users(name, age, pwd) VALUES(?, ?, ?)""", ("Lea", 23, "password2"))
cursor.execute("""INSERT INTO users(name, age, pwd) VALUES(?, ?, ?)""", ("Coco", 21, "password3"))

cursor.execute("""SELECT * FROM users""")
user1 = cursor.fetchall()
print(user1)

root = tkinter.Tk()

for x in user1:
    tkinter.Label(root, text=x).pack()

root.mainloop()
