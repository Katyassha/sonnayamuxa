import random

m = []
b = 0
for i in range(0, 20):
    a = random.randint(0, 10000)
    m.append(a)
print(m)
b = 0
for i in range(0, 19):
    if m[i] % 3 == 0 and m[i + 1] % 3 != 0:
        b += 1
    if m[i] % 3 != 0 and m[i + 1] % 3 == 0:
        b += 1
print(b)
