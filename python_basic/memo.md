## [[Python] 何度も調べてしまうリスト操作をまとめてみた](http://www.yoheim.net/blog.php?q=20150801)

#### リストを生成する

```
# 空のリストを作る
>>> list01 = list()
>>> list01 = []

# 初期値を指定する
>>> list01 = ["a", "b", "c"]

# タプルからリストを作る
>>> aTapple = (1, 2)
>>> list01 = list(aTapple)
[1, 2]

# セットからリストを作る
>>> aSet = set([1,2,3,4,5])
>>> list01 = list(aSet)
[1, 2, 3, 4, 5]

# 文字列から作る
>>> list01 = list("abcde")
['a', 'b', 'c', 'd', 'e']

# 文字列から作る
>>> list01 = "1,2,3,4,5".split(",")
['1', '2', '3', '4', '5']

# レンジから作る
>>> list01 = range(1,10)
[1, 2, 3, 4, 5, 6, 7, 8, 9]

# レンジで数値が小さくなるように作る
>>> list = range(10, 1, -1)
[10, 9, 8, 7, 6, 5, 4, 3, 2]
```

#### 値を追加する

```
list01 = ["a", "b", "c"]

# 後ろに追加
>>> list01.append("d")
['a', 'b', 'c', 'd']

# 前に追加
>>> list01.insert(0, "z")
['z', 'a', 'b', 'c', 'd']

# 任意の場所に追加
>>> list01.insert(2, "hoge")
['z', 'a', 'hoge', 'b', 'c', 'd']

# 配列に配列を追加
>>> list01.extend([10, 20, 30, 10, 20, 30])
['z', 'a', 'hoge', 'b', 'c', 'd', 10, 20, 30, 10, 20, 30]

>>> list02 = list01 + [1,2,3,4,5]
```

#### 値を削除する

```
list01 = ["a", "b", "c"]

# 要素の削除（複数存在する場合は1つ目のみ）
>>> list01.remove("c")
['a', 'b']

# 要素の削除（複数存在するものを全部）
>>> list01 = [item for item in list01 if item is not "c"]
['a', 'b']

>>> list01 = filter(lambda a: a != "c", list01)

# 位置を指定して削除（1件）
>>> del list01[0]
['b', 'c']

# 位置を指定して削除（複数件）
>>> del list01[1:2]

# 位置を指定して削除（全部）
>>> del list01[:]
```

#### 値の取得、出現回数、サイズ

```
>>> list01 = [1, 2, 3, 4, 5]

# 範囲指定で取り出す
# 要素0〜1
>>> print list01[0:2]
# 要素1〜後ろから2つ目まで
>>> print list01[0:-1]
# 要素0〜2まで
>>> print list01[:3]
# 要素3〜最後まで
>>> print list01[3:]

# 2つ置きに取得する
>>> list01[::2]
[1, 3, 5]

# 逆順に取得する
>>> list01[::-1]
[5, 4, 3, 2, 1]

# 逆順に2つ置きに取得する
>>> list01[::-2]
[5, 3, 1]

# 指定した要素の位置を取得する
>>> index = list01.index(1.4)

# 最後の要素を取得して同時に削除する
>>> item = list01.pop()

# 指定した位置の要素を取得して同時に削除する
>>> item = list01.pop(1)

# 指定した要素の出現回数を取得する
>>> count = list01.count(10)

# サイズを確認する
>>> len(list01)

# 要素の存在確認
>>> list01 = [1,2,3,4,5]
>>> print 2 in list01
True
>>> print 6 in list01
False
```


#### 値を変更する

```
>>>list01 = ["a", "b", "c", "d"]

# 要素3の値を変更する
>>>list01[3] = "D"
['a', 'b', 'c', 'D']

# 要素0〜2を変更する
>>>list01[:3] = ["A", "B", "C"]
['A', 'B', 'C', 'D']

# 一番後ろ〜の値を変更する（追加要素が多い場合は末尾に追加される）
>>>list01[-1:] = ["E", "F"]
['A', 'B', 'C', 'E', 'F']
```

#### ソートする

```
# ソートする（元のリスト自体をソートする）
>>>list01.sort()

# ソートする（元のリストは変更しない）
>>>list01 = sorted(list01)

# ソート条件を指定する（cmp） ※ Python2系の場合
>>>list01.sort(cmp=lambda x,y: x<y)
>>>list01 = sorted(list01, cmp=lambda x,y:x<y)

# ソート条件を指定する（key） ※ Python3系の場合
>>>list01.sort(key=lambda x: x)
>>>list01 = sorted(list01, key=lambda x: x)


# ソートの前処理を指定する
>>>["a", "AA" , "Ab", "ac"].sort(key=str.lower)

# 逆順にソートする（元のリスト自体をソートする）
list01.sort(reverse=True)

# または（元のリストは変更しない）
list01 = list(reversed(list01))
```

#### リストをスタックとして使う

```
>>> stuck = [3, 4, 5]
[3, 4, 5]

>>> stuck.append(6)
[3, 4, 5, 6]
>>> stuck.pop()
6

>>> stuck
[3, 4, 5]
```

#### リストをキューとして使う

```
# リストのappendとpop(0)で実現できるが、
# pop(0)を行うと全要素の位置を変更するため処理が遅い
# 代わりに以下の実装を利用すると高速
>>> from collections import deque

>>> queue = deque(["A", "B", "C"])
deque(['A', 'B', 'C'])

>>> queue.append("D")
deque(['A', 'B', 'C', 'D'])

>>> queue.popleft()
'A'

>>> queue
deque(['B', 'C', 'D'])
```

#### 関数プログラミング（filter、map、reduce）

```
>>> list01 = [1,2,3,4,5]

# filter（条件に一致する要素に絞り込む、元のリストは不変）
# ラムダ型の場合
>>> filter(lambda x: x % 2 is 0, list01)
[2, 4]
# 関数型の場合
>>> def isEven(x): return x % 2 is 0
>>> filter(isEven, list01)
[2, 4]

# map（各要素に処理を行う、元のリストは不変）
# ラムダ型の場合
>>> map(lambda x:x*2, list01)
[2, 4, 6, 8, 10]
# 関数型の場合
>>> def makeDouble(x): return x * 2
>>> map(makeDouble, list01)
[2, 4, 6, 8, 10]

# reduce（各要素を組み合わせて1つの結果を作る、元のリストは不変）
# ラムダ型の場合
>>> reduce(lambda x,y:x*y, list01)
120
# 関数型の場合
>>> def multiple(x,y): return x * y
>>> reduce(multiple, list01)
120
```

#### リスト内包表記

```
>>> list01 = range(1,6)
[1, 2, 3, 4, 5]

>>> [i * 2 for i in list01]
[2, 4, 6, 8, 10]

>>> print [i * 2 for i in range(10)]
>>> print [i * 2 for i in range(10) if i % 2 is 1]
>>> print [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
```

#### ループ処理

```
>>> list01 = list("abcde")

# 1件ずつ処理する
>>> for item in list01:
>>>    print item

# ループ処理（indexも一緒に取得したい）
>>> for i, v in enumerate(list01):
>>>    print i, v

# ループ処理（2つの配列を同時に処理する）
>>> firstNames = ["a", "b", "c"]
>>> lastNames  = ["A", "B", "C"]
>>> for f, l in zip(firstNames, lastNames):
>>>     print f, l

# ループ中に、ループ対象のリストを処理する
>>> list01 = range(10)
>>> for i in list01[:]:
>>>     if i % 3 is 0:
>>>         list01.append(i)
>>> print list01
```

## [[Python] for文処理が1行で書ける！素敵なリスト内包表記](http://www.yoheim.net/blog.php?q=20150702)

あとで書く
