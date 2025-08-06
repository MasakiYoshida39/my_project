"""
参考URL
https://www.youtube.com/watch?v=Fbynk_9TfXg
"""

"""
Scikit-learn20本ノック
"""


# 数値計算ライブラリ NumPy をインポート（np という別名で）
import numpy as np

# データ分析ライブラリ Pandas をインポート（pd という別名で）
import pandas as pd

# グラフ描画ライブラリ matplotlib の pyplot モジュールをインポート（plt という別名で）
import matplotlib.pyplot as plt

# ファイル名のパターンマッチングを行う glob 関数をインポート
from glob import glob

# CSVファイル「data.csv」を読み込み、DataFrame形式の変数 df に格納する
df = pd.read_csv('data.csv')


"""
Scikit-learn20本ノック１
# CSVファイル「data.csv」を読み込み、DataFrame形式の変数 df に格納する
df = pd.read_csv('data.csv')

# 読み込んだデータの先頭5行を表示（データの中身を確認するため）
ab = df.head()

print(ab)
"""

"""
Scikit-learn20本ノック２
# CSVファイルを読み込む（例: 'data.csv' というファイル）
# ※実際にファイルがあるパスを指定してください
df = pd.read_csv('data.csv')

# 各列における欠損値（NaN）の個数をカウントして表示する
# 結果は列名と欠損値の個数がペアになった形式で出力される

ab = df.isnull().sum()
print(ab)
"""


"""
Scikit-learn20本ノック3
# CSVファイル「data.csv」を読み込み、DataFrame形式の変数 df に格納する
df = pd.read_csv('data.csv')

# 欠損値（NaN）を含む行をすべて削除し、新しいDataFrameとして返す（元のdfは変更されない）
ab = df.dropna()
print(ab)
"""

"""
Scikit-learn20本ノック4
# 欠損値（NaN）を含む行をすべて削除し、新しいDataFrameとして返す（元のdfは変更されない）
ab = df.dropna()

# 'Age' 列だけを取り出し、欠損値（NaN）を 0 に置き換えた新しいDataFrameを作成
df_zero = df[['Age']].fillna(0)

# 補完済みの 'Age' 列のデータから、最後の3行だけを抽出して変数 ab に再代入
ab = df_zero.tail(3)

# 最後に ab の中身を出力（これは 'Age' 列の最後の3行、欠損値があれば 0 に置き換えられている）
print(ab)
"""

"""
Scikit-learn20本ノック5
# 'Age'列の平均値（NaNは無視される）を計算し、変数 ave に格納
ave = df['Age'].mean()

# 'Age'列の標準偏差（NaNは無視される）を計算し、変数 std に格納
std = df['Age'].std()

# 'Age'列の欠損値（NaN）の数をカウントし、変数 num に格納
num = df['Age'].isnull().sum()

# 欠損値の個数と同じ数だけ、平均±標準偏差の範囲でランダムな整数を生成（補完用データ）
rand = np.random.randint(ave - std, ave + std, size=num)

print(rand)
"""