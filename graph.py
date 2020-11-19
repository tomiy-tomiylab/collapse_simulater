import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd

ax, fig = plt.subplots()

fig.set_ylim(0, 100)
# start, end = fig.get_ylim()
# stepsize = 25
# fig.yaxis.set_ticks(pd.np.arange(start, end, stepsize))

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

print("length x = {}".format(len(x)))
print("length y = {}".format(len(y)))
print("x max = {}".format(x[np.argmax(x)]))
print("x min = {}".format(x[np.argmin(x)]))
print("y max = {}".format(y[np.argmax(y)]))
print("y min = {}".format(y[np.argmin(y)]))

# x = np.flipud(x)
# y = np.flipud(y)

fig.plot(x, y, linewidth=1, color="red")
plt.show()
