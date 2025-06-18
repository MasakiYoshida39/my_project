
""" コメント(2-3)
"""
from datetime import datetime
# now()で現在の日付と時刻を取得
now = datetime.now()
# strftimeでフォーマットを任意の形式に変更
formatted_date = now.strftime("%Y年%m月%d日")

print("今日の日付は", formatted_date)









""" コメント(datetimeライブラリ)

# datetimeライブラリ(現在の日付と時刻を返す）をインポート
from datetime import datetime

# now()で現在の日付と時刻を取得
now = datetime.now()

print("今日の日付は", now)
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