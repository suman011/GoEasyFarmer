

#CODE TO CREATE DATA BAASE FILE
#RUN ONLY ONCE IN YOUR WHOLE LIFE

import sqlite3
from soil import soil

conn=sqlite3.connect('soilpro.db')
c=conn.cursor()
c.execute("""CREATE TABLE soil ( soiltype text, dm1 real,dm2 real,om1 real,om2 real,ph1 real,ph2 real,n1 real,n2 real)""")

c.execute("INSERT INTO soil VALUES ('Sand',80,97,3.5,4.2,6,7.7,0.05,1.6),('Sub soil sandy',65,74.1,25,28.5,6,7.7,0.05,1.6),('Sandy Loam',65,72.7,25,29.5,6,7.7,0.05,1.6),('Clay soil',65,74.1,25,28.5,6,7.7,0.05,1.6),('Sub soil loam',65,72,27,34,6,7.7,0.05,1.6),('Loam with compost',56,65,37,43,6,7.6,0.05,1.6),('Loam with leaf',56,63,47,53,5,5.8,0.05,1.6),('Compost',22,30,78,85,6,7.7,1,1.85)")
conn.commit()

