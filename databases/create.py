import sqlite3

conn = sqlite3.connect("p.db")

#send strings of sql to connection
q = "create table people(name text, id integer)"
c = conn.cursor()
c.execute(q)

q = """
create table classes (code text, grade integer, id integer)
"""

c.execute(q);
#changes when commit
#should commit regularly
conn.commit();
