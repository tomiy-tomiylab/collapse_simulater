import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import csv

font_name = 'Noto Sans CJK JP'  # OSにインストールされているフォント名を指定
#  各OSでの一例です 
#  Mac: Hiragino Sans
#  Win: MS Gothic
#  Lin: Noto Sans CJK JP
font_weight = 'medium'  # もし細ければ'bold'に変更
ax, fig = plt.subplots()

# plt.grid()
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.minorticks_on()
plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

plt.title('放射性同位体の原子核数の時間変化', fontsize=15, fontname=font_name, fontweight=font_weight)
plt.xlabel('時間', fontsize=15, fontname=font_name, fontweight=font_weight)
plt.ylabel('崩壊せずに残っている原子の割合 [%]', fontsize=15, fontname=font_name,fontweight=font_weight)

x = np.array([], dtype=np.int)
y = np.array([], dtype=np.float32)

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

x = x.astype(np.int)
y = y.astype(np.float32)

length = len(x)
print(msg_f)
print(msg_e)

print("length x = {}".format(len(x)))
print("length y = {}".format(len(y)))
print("x max = {}".format(x[np.argmax(x)]))
print("x min = {}".format(x[np.argmin(x)]))
print("y max = {}".format(y[np.argmax(y)]))
print("y min = {}".format(y[np.argmin(y)]))

fig.plot(x, y, linewidth=1, color="red")
plt.show()
