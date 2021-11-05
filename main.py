import sqlite3
conn = sqlite3.connect('personal.db')
c = conn.cursor()
x = c.execute("select OPTION,VALUE from PREFERENCES where OPTION='ViewMode'")
vmode=x.fetchall()
#print(vmode[0][1])