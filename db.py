import sqlite3
def createdb():
    conn = sqlite3.connect('example.db')

    c = conn.cursor ()
    c.execute('''CREATE TABLE links
             (link text, redirect_url text)''')
    c.execute("INSERT INTO links VALUES ('asdfgh','https://www.google.com')")
    conn.commit()
    conn.close()

def getdata():
    with sql.connect("example.db") as con:
        cur = con.cursor()
        data = cur.execute('SELECT * FROM links')
        return data

def insertdata(query):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute(query)
    conn.commit()
    conn.close()

createdb()