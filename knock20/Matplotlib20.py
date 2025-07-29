"""
Matplotlib20本ノック
"""
import numpy as np                  # 数値計算ライブラリNumPyをnpとしてインポート
import matplotlib.pyplot as plt     # グラフ描画ライブラリMatplotlibのpyplotモジュールをpltとしてインポート

# xの値を0から9までの整数の配列として作成
x = np.arange(10)

# -10から9までの範囲でランダムな整数を10個生成しyに代入
y = np.random.randint(-10, 10, 10)

# xとyのデータを使って折れ線グラフを描画
plt.plot(x, y)

# グラフを画面に表示
plt.show()
