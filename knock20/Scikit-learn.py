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