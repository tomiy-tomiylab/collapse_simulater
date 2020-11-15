import numpy as np
import matplotlib.pyplot as plt
import csv

ax, fig = plt.subplots()

fig.grid()

x = np.array([])
y = np.array([])

with open('./to_graph.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        x = np.append(x, row[0].replace(' 回目', ''))
        y = np.append(y, row[1].replace(' %', ''))

length = len(x)
x = np.delete(x, length - 1)
y = np.delete(y, length - 1)
x = np.delete(x, 0)
y = np.delete(y, 0)

plt.plot(x, y, linewidth=1, color="red")
plt.show()
