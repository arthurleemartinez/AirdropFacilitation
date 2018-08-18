import random
x = []
y = []
for i in range(100):
    y = random.random() * 7500
    zz = round(y, 6)
    x.append(zz)
print(x)
