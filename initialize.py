import sqlite3
conn = sqlite3.connect("personal.db")
c = conn.cursor()
c.execute('create table PREFERENCES (OPTION char, VALUE text)')
c.execute('insert into PREFERENCES VALUES ("ViewMode", "Light")')
conn.commit()
conn.close()