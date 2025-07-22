
""" コメント(4-)
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