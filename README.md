# collapse_simulater



放射性同位体が時間の経過とともに崩壊し、どのように数が減るのかシミュレーション

不安定なCs137がβ崩壊して安定なBa137になり、それ以上崩壊しない状況を想定



## 使い方

collapse_simulater.pyでシュミレーション

result.csvからシュミレーション1回分の結果をto_graph.csvに移す

graph.pyで結果をグラフ化



## collapse_simulater.py

### パラメータ

num_atoms: 原子の数 intで指定

collapse_rate: 1judgeで崩壊する確率[‰] (千分率) intで指定

end_rate: 崩壊していない原子の割合がこの値になるとシミュレーションを終了

### 注意

・結果はresult.csvに上書きせずに追記する

・result.csvのファイルサイズが大きくなることがある

Atom: 10000,Collapse rate: 2 ‰ で 69.8 MB 

​	TODO:result.csvに残す情報を必要最小限に抑えるモードを実装

・結構時間がかかる

Atom: 10000,Collapse rate: 2 ‰ 

で 2m04.675338sかかった. 環境は以下の通り

Python 3.6.10 :: Anaconda, Inc.

ProductName:	Mac OS X
ProductVersion:	10.15.7
BuildVersion:	19H15

MacBook Pro  (13inch , 2018, Four Thundererbolt3 Ports)

Processer 2.7GHz Quad-Core Intel Core i7

Memory 16GB 2133 Mhz LPDDR3



## graph.py

### 注意

・結構重たい?

