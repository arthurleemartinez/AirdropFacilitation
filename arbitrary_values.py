import random
random1 = random.random()
x = []
y = []
for i in range(100):
    y = random.random() * 1600000
    zz = round(y, 6)
    x.append(zz)
print(x)
