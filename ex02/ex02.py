import string
import random
import psycopg2

alpha = string.ascii_uppercase
l = []

while len(l) < 100:
    res = ''
    for i in range(16):
        a = random.choice(alpha)
        n = str(random.randrange(10))
        rand = random.choice([a, n])
        res += rand

    if res not in l:
        l.append(res)
        # print(res)

print(len(l))
print(l)


conn = psycopg2.connect(database="cheng", user="cheng", host="127.0.0.1", port="5432")
cur = conn.cursor()
cur.execute("CREATE TABLE code (id serial PRIMARY KEY, data varchar, is_valid BOOLEAN);")
conn.commit()
print("Table created successfully")


for index, value in enumerate(l):
    cur.execute("INSERT INTO code (data, is_valid) VALUES (%s, True)", (value, ))

conn.commit()
print("Records Inserted successfully")


cur.execute("SELECT id, data, is_valid from code")
rows = cur.fetchall()
for row in rows:
    print(row[0], row[1], row[2])

print("Query finished successfully")
conn.close()
