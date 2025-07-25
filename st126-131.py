
""" コメント(5-)
"""


""" コメント(5-２)
# 🌟 バブルソート関数を作るよ！
def bubble_sort(data):
    # データが1個以下なら、もう並べる必要なし！
    if len(data) <= 1:
        return data

    # リストの中を何回もチェック（最大でn-1回）
    for i in range(len(data) - 1):
        # 左から順に、となり同士を比べる
        for j in range(len(data) - i - 1):
            # もし左の方が大きかったら、入れかえる！
            if data[j] > data[j + 1]:
                # Pythonの入れかえテク：左右を一気に入れかえ！
                data[j], data[j + 1] = data[j + 1], data[j]
    
    # 並び終わったら返すよ！
    return data

# 🔢 並べたいデータ
data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]

# 📦 元のデータはそのまま残して、コピーを並べる
sorted_data = bubble_sort(data.copy())

# 🖨 結果を表示！
print(f"{data} => {sorted_data}")
"""

""" コメント(5-1)
num1 = int(input("1つ目の数字を入力して下さい"))
num2 = int(input("2つ目の数字を入力して下さい"))

if num1 <= 1 or num2 <= 1:
    print(False)
else:
    for i in range(2, (num1 // 2) + 1):
        if num1 % i == 0:
            print(False)
            break
    else:
        for i in range(2, (num2 // 2) + 1):
            if num2 % i == 0:
                print(False)
                break
        else:
            print(True)
"""





""" コメント(4-4)
a = 0
b = 1
while a < 10000:
    print(a, end=' ')
    tmp = a
    a = b
    b = tmp + b
print()


# 【プラスα】関数として記述
def fib(n):
    a = 0
    b = 1
    while a < n:
        print(a, end=' ')
        tmp = a
        a = b
        b = tmp + b
    print()

"""

""" コメント(4-2)
h = int(input("数字を入力して下さい"))

# 1行目
for i in range(h):
    print("*", end="")
print()

# 受取った値が1でない場合
if h != 1:
    for i in range(2, h):
        print("*", end="")
        for j in range(2, h):
            print(" ", end="")
        print("*")
    # 最終行
    for i in range(h):
        print("*", end="")
    print()
""" 

""" コメント(4-1)
for i in range(1, 10):
    for j in range(1, 10):
        print(i, "x", j, "=", i * j)

i = 1
while i <= 9:
    j = 1
    while j <= 9:
        print(i, "x", j, "=", i * j)
        j = j + 1
    i = i + 1
"""

""" コメント(3-3)
print("1つ目の数字")
x = input()
print("2つ目の数字")
y = input()
nam1 =int(x)
nam2 =int(y)

print("足し算の合計", nam1 + nam2)

print("引き算の合計", nam1 - nam2)
"""


""" コメント(3-2)
x = input()
for i in x:
    if int(i) == 5:
        print("5です!!")
    else:
        print("5じゃないです")
"""


""" コメント(3-1)
x = 0
v = 1
for i in range(10):
    j = int(input("数字を入力して下さい"))
    if j == x:
        v = v + 1
        print("{}回連続".format(v))
        if v == 10:
            print("perfect!!")
    else:
        v = 1
        print("連続なし")
    x = j
"""

""" コメント(2-3)
x = 0
limit = 20000

for i in range(2, limit + 1):
    for j in range(2, (i // 2) + 1):
        if i % j == 0:
            break
    else:
        x += i
print(x)
"""

""" コメント(2-2)
h = int(5)
for i in range(1, h + 1):
    for j in range(i):
        print("*", end="")
    print()
"""

""" コメント(2-1)
i = int(input("iの数字を入力してください: "))
j = int(input("jの数字を入力してください: "))

print("i =", i, ", j =", j)

print("反対にします")

flee = i
i = j
j = flee

print("i =", i, ", j =", j)
""" 

""" コメント(1-3)
# 入力された文字列を変数に格納
nam1 = int(input("１回目の数字を入力してください: "))
nam2 = int(input("２回目の数字を入力してください: "))

nam3 = nam1 +nam2
print("合計は" + str(nam3))
""" 

""" コメント(1-2)
# 入力された文字列を変数に格納
name = int(input("数字を入力してください: "))
if name % 3 == 0:
    print("foo")
else:
     print("noo")
""" 


""" コメント(1-1)
for i in range(1, 10):
    for j in range(1, 10):
        print(i * j, end= " ")
    print("「{}」の段です".format(i))
""" 