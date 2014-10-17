import sqlite3
import csv

conn = sqlite3.connect("d.db")

c = conn.cursor()
BASE = "INSERT INTO people VALUES('%(name)s',%(id)s)"
for line in csv.DictReader(open("people.csv"));
    q = BASE%line
    print q
    c.execute(q)

conn.commit()
