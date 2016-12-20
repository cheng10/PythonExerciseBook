import string
import random
import redis

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


r = redis.StrictRedis(host='localhost', port=6379, db=0)
for item in l:
    r.set(item, True)

print("Showing data from redis:")
print(r.keys())
