""" コメント(リストからランダム出力)
"""



#ランダムな値を生成するためのライブラリ
import random

numbers = [1, 2, 3, 4, 5]

# リストをシャッフル
random.shuffle(numbers)
print("Shuffled list:", numbers)







""" コメント(choiceを使用しリストからランダム出力)

#ランダムな値を生成するためのライブラリ
import random

fruits = ["apple", "banana", "cherry", "grape", "strawberry"]

# リストからランダムな要素を選ぶ
random_fruit = random.choice(fruits)
print(random_fruit)
"""

""" コメント(random ライブラリ)

#ランダムな値を生成するためのライブラリ
import random

# 1から10までのランダムな整数を生成
random_number = random.randint(1, 10)
print(random_number)
"""

""" コメント(timedeltaを使用し日付の計算)

# 日付の計算
from datetime import datetime, timedelta

# 現在の日付を取得
today = datetime.now()

# 7日後の日付を計算
future_date = today + timedelta(days=7)
formatted_future_date = future_date.strftime("%Y年%m月%d日")
print("7日後は:", formatted_future_date)

# 7日前の日付を計算
past_date = today - timedelta(days=7)
formatted_past_date = past_date.strftime("%Y年%m月%d日")
print("7日前は:", formatted_past_date)
"""

""" コメント(%Y年%m月%d日に変更)

from datetime import datetime
# now()で現在の日付と時刻を取得
now = datetime.now()
# strftimeでフォーマットを任意の形式に変更
formatted_date = now.strftime("%Y年%m月%d日")

print("今日の日付は", formatted_date)
"""

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