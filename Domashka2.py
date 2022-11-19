import sqlite3
conn = sqlite3.connect("database.db")
curs = conn.cursor()
curs.execute("""CREATE TABLE AUTH(login TEXT, password TEXT);
""")
conn.commit()
curs.close()
conn.close()