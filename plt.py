import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt
 
"""
複数のグラフを並べて描画（subplotsを使用）
"""


fig, axs = plt.subplots(1, 2, figsize=(10, 5))  # 1行2列のサブプロット
x = np.linspace(0, 10, 100)

axs[0].plot(x, np.sin(x))
axs[1].plot(x, np.cos(x))

plt.show()  





"""
箱ひげ図
箱ひげ図（箱ひげ図／Boxplot）は、データのばらつき（分布）を視覚的に示すグラフ
data = np.random.normal(10, 5, 100)
#正規分布に従うランダムなデータを生成（平均（μ）標準偏差（σ）100個のデータ）
plt.boxplot(data)
#data の 箱ひげ図（Box plot） を描く
plt.show()
"""

"""
ヒストグラム
x = np.random.normal(10, 5, 1000)
plt.hist(x, bins=30)
#bins=30	データの範囲を分割する 区間（ビン）の数。ここでは30個のビンに分けて表示します。
plt.show()
"""

"""
円グラフ
labels = ["A", "B", "C", "D", "E"]
data = [54, 32, 18, 44, 29]
plt.pie(data, labels=labels, autopct="%1.1f%%")
#autopct	割合の表示形式を指定。例: "%1.1f%%" なら 小数1桁のパーセント表示になる。
plt.show()
"""

"""
x = np.linspace(-5, 5, 100) # -5から5までを100ステップに分けた配列を生成
y = np.sin(x) # xの各値に対してsin関数の値を計算
 
plt.plot(x, y) # 折れ線グラフをプロット
plt.show() # グラフを表示
"""

"""
折れ線グラフ
data = [2, 4, 6, 3, 5, 8, 4, 5]
plt.plot(data)
plt.show()
"""

"""
棒グラフ
a = range(0, 7)
b = [55, 21, 61, 98, 85, 52, 99]
plt.bar(a, b)
plt.show()
"""


"""
散布図
x = [10, 51, 44, 23, 55, 95]
y = [5, 125, 2, 55, 19, 55]
plt.scatter(x, y)
plt.show()
"""
