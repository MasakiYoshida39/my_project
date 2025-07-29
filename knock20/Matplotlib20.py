"""
Matplotlib20本ノック
参考https://www.youtube.com/watch?v=bsYJ3hTvx7c
"""
import numpy as np                  # 数値計算ライブラリNumPyをnpとしてインポート
import matplotlib.pyplot as plt     # グラフ描画ライブラリMatplotlibのpyplotモジュールをpltとしてインポート

# x軸のラベル（名前のリスト）
x = ['sam', 'john', 'kevin', 'adam']

# 0以上200未満の整数を4つランダムに生成（各人の値として使用）
y = np.random.randint(0, 200, 4)

# 棒グラフを描画（xが名前、yが値）
plt.bar(x, y)

# グラフを画面に表示
plt.show()


"""
Matplotlib20本ノック１
# xの値を0から9までの整数の配列として作成
x = np.arange(10)

# -10から9までの範囲でランダムな整数を10個生成しyに代入
y = np.random.randint(-10, 10, 10)

# xとyのデータを使って折れ線グラフを描画
plt.plot(x, y)

# グラフを画面に表示
plt.show()
"""

"""
Matplotlib20本ノック2
# 10以上20未満の整数を20個ランダム生成（x1のデータ）
x1 = np.random.randint(10, 20, 20)
# 20以上30未満の整数を20個ランダム生成（x2のデータ）
x2 = np.random.randint(20, 30, 20)
# ここが問題！50以上10未満の整数を20個ランダム生成しようとしているためエラーまたは空の配列になる
# y1 = np.random.randint(50, 10, 20)  ← 上限値が下限値より小さいので正しく動作しない
# 正しくは下限＜上限に直す必要あり（例: 10以上50未満）
y1 = np.random.randint(10, 50, 20)
# 0以上40未満の整数を20個ランダム生成（y2のデータ）
y2 = np.random.randint(0, 40, 20)

# x1,y1の点を散布図で描画
plt.scatter(x1, y1)
# x2,y2の点を散布図で描画
plt.scatter(x2, y2)

# グラフを画面に表示
plt.show()
"""


"""
Matplotlib20本ノック3
# 0以上10未満の整数を10個ランダムに生成（データ配列）
date = np.random.randint(0, 10, 10)

# 生成したデータを使ってヒストグラム（度数分布図）を描画
plt.hist(date)

# グラフを画面に表示
plt.show()
"""

"""
Matplotlib20本ノック3(についてbins)
# データのヒストグラムをビンの数を15に指定して描画（ビン＝棒の数）
plt.hist(date, bins=15)

# 新しいグラフを画面に表示
plt.show()
"""