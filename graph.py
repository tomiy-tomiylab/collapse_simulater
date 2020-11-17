import numpy as np
import matplotlib.pyplot as plt
import csv

ax, fig = plt.subplots()

x = np.array([])
y = np.array([])

with open('./to_graph.csv') as f:
    reader = csv.reader(f)
    readed = [row for row in reader]
    msg_f = readed[0]
    del readed[0]
    msg_e = readed[-1]
    del readed[-1]
    for row in readed:
        x = np.append(x, row[0].replace(' 回目', ''))
        y = np.append(y, row[1].replace(' %', ''))

length = len(x)
print(msg_f)
print(msg_e)
'''
x = np.delete(x, length - 1)
y = np.delete(y, length - 1)
x = np.delete(x, 0)
y = np.delete(y, 0)
'''
# x = np.flipud(x)
# y = np.flipud(y)

plt.plot(x, y, linewidth=1, color="red")
plt.show()
