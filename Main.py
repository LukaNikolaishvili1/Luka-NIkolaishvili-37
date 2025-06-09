import sqlite3


conn = sqlite3.connect("users.db")
c = conn.cursor()

c.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        phonenumber TEXT,
        address TEXT
    )
""")

conn.commit()
conn.close()



def add_user(username, phonenumber, address):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("INSERT INTO users (username, phonenumber, address) VALUES (?, ?, ?)",
              (username, phonenumber, address))
    conn.commit()
    conn.close()


def delete_user(user_id):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()



def update_user(user_id, username, phonenumber, address):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("""
        UPDATE users
        SET username = ?, phonenumber = ?, address = ?
        WHERE id = ?
    """, (username, phonenumber, address, user_id))
    conn.commit()
    conn.close()
