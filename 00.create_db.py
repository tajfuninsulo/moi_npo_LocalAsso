# using sqlite3

import sqlite3

conn = sqlite3.connect('npo_list.db')
print("Opened database successfully")

conn.execute('''DROP TABLE IF EXISTS TWNGO_LIST;''')
conn.execute('''CREATE TABLE IF NOT EXISTS TWNGO_LIST (
                ID TEXT NOT NULL,
                TYPE TEXT NOT NULL,
                NAME TEXT NOT NULL,
                ADDR TEXT NOT NULL,
                TELP TEXT NOT NULL,
                ADMR TEXT NOT NULL
                 );''')
print("Table created successfully")


conn.close()
