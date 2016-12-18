import string
import random

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
