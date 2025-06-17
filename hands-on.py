h = int(5)
for i in range(1, h + 1):
    for j in range(i):
        print("*", end="")
    print()






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