import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt
 
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
"""
a = range(0, 7)
b = [55, 21, 61, 98, 85, 52, 99]
plt.bar(a, b)
plt.show()
