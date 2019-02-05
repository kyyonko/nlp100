## [Pythonで複数のリストをまとめて処理する：zip()](http://uxmilk.jp/13726)

#### リストをまとめる

```
name_list = ["John", "Mike", "Bob"]
age_list = [23, 31, 28]
result = zip(name_list, age_list)
print result # [('John', 23), ('Mike', 31), ('Bob', 28)]
```

もしzip()の引数の要素数が異なる場合は、要素数が小さい方に合わせられ残りの要素を捨てられます。
```
name_list = ["John", "Mike", "Bob"]
age_list = [23, 31]
result = zip(name_list, age_list)
print result # [('John', 23), ('Mike', 31)]
```

#### リストをまとめてループ処理を行う

zip()を使えばループ処理の際に2つのリストをインデックス無しで同時に扱えるので便利。

```
name_list = ["John", "Mike", "Bob"]
age_list = [23, 31, 28]
 
for (name, age) in zip(name_list, age_list):
    print str(name) + ":" + str(age)

# John:23
# Mike:31
# Bob:28
```
