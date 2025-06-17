# 入力された文字列を変数に格納
name = int(input("あなたの名前を入力してください: "))


if name % 3 == 0:
    print("foo")
else:
     print("noo")


""" コメント(1-1)
for i in range(1, 10):
    for j in range(1, 10):
        print(i * j, end= " ")
    print("「{}」の段です".format(i))
""" 