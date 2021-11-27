

import matplotlib.pyplot as plt

x = []
y = []
cord =[]

my_file = open("DS3.txt")
with my_file as f:
    for line in f:
            cord.append([int(x) for x in line.split()])

for i in range(len(cord)):
    for j in range(1):
        x.append(cord[i][0])
        y.append(960 - cord[i][1])

plt.figure('Малюнок за датасетом')
plt.scatter(x, y)
plt.show()
plt.close()
my_file.close()
