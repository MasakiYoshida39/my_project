"""
Matplotlib20本ノック
参考https://www.youtube.com/watch?v=bsYJ3hTvx7c
"""
import numpy as np                  # 数値計算ライブラリNumPyをnpとしてインポート
import matplotlib.pyplot as plt     # グラフ描画ライブラリMatplotlibのpyplotモジュールをpltとしてインポート

# データ
date = [5, 3, 4, 3, 5, 0, 3, 2, 1, 4, 6, 8]

# プロット
plt.plot(date)

# 注釈（最小値をマーク）
plt.annotate('min value',
             xy=(5, 0),              # 最小値の位置
             xytext=(9, 0.5),        # 注釈のテキスト位置
             arrowprops=dict(facecolor='black', shrink=0.05))

# グラフ表示
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

"""
Matplotlib20本ノック4
# x軸のラベル（名前のリスト）
x = ['sam', 'john', 'kevin', 'adam']

# 0以上200未満の整数を4つランダムに生成（各人の値として使用）
y = np.random.randint(0, 200, 4)

# 棒グラフを描画（xが名前、yが値）
plt.bar(x, y)

# グラフを画面に表示
plt.show()
"""

"""
Matplotlib20本ノック5
# xに0〜9の連続した整数を生成
x = np.arange(10)

# yに-10以上10未満の整数を10個ランダムに生成
y = np.random.randint(-10, 10, 10)

# 折れ線グラフを描画
plt.plot(x, y)

# グラフのタイトルを設定
plt.title('Res')

# x軸のラベルを設定
plt.xlabel('x axis')

# y軸のラベルを設定
plt.ylabel('y axis')

# グラフを表示（これより後にラベル設定しても反映されない）
plt.show()
"""


"""
Matplotlib20本ノック6
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

# x軸の表示範囲を0〜40に設定
plt.xlim(0, 40)

# y軸の表示範囲を0〜40に設定
plt.ylim(0, 40)

# グラフを画面に表示
plt.show()
"""

"""
Matplotlib20本ノック7
# 0から10までを500分割したxの配列を生成
x = np.linspace(0, 10, 500)

# y = e^x の値を計算（指数関数）
y = np.exp(x)

# y軸を対数スケールに設定（ログスケール）
plt.yscale('log')

# 折れ線グラフを描画
plt.plot(x, y)

# グラフを表示
plt.show()
"""

"""
Matplotlib20本ノック8
# 0〜2πまでを500等分した配列を生成（x軸の値）
x = np.linspace(0, 2 * np.pi, 500)

# sin(x) の値を計算（y1に格納）
y1 = np.sin(x)

# cos(x) の値を計算（y2に格納）
y2 = np.cos(x)

# sin(x) の折れ線グラフを描画（ラベル付き）
plt.plot(x, y1, label='sin')

# cos(x) の折れ線グラフを描画（ラベル付き）
plt.plot(x, y2, label='cos')

# y軸の範囲を -2〜2 に設定
plt.ylim(-2, 2)

# 凡例を表示（labelで設定した内容）
# loc=2 は「左上（upper left）」を意味する
plt.legend(loc=2)


# グラフを画面に表示
plt.show()
"""

"""
Matplotlib20本ノック9
# xとyのデータを3グループ分ランダム生成
x1 = np.random.randint(10, 35, 20)
x2 = np.random.randint(5, 45, 20)
x3 = np.random.randint(0, 40, 20)

y1 = np.random.randint(50, 100, 20)
y2 = np.random.randint(0, 40, 20)
y3 = np.random.randint(20, 80, 20)

# グループ1の散布図（星型マーカー、サイズ80）
plt.scatter(x1, y1, marker='*', s=80)

# グループ2の散布図（三角マーカー、サイズ60）
plt.scatter(x2, y2, marker='^', s=60)

# グループ3の散布図（×マーカー、サイズ30）
plt.scatter(x3, y3, marker='x', s=30)

# グラフを表示
plt.show()
"""