"""
参考URL
https://www.youtube.com/watch?v=Fbynk_9TfXg
"""

"""
Scikit-learn20本ノック
"""


# 数値計算ライブラリ NumPy をインポート（npという別名で）
import numpy as np

# データ分析ライブラリ Pandas をインポート（pdという別名で）
import pandas as pd

# グラフ描画ライブラリ matplotlib の pyplot モジュールをインポート（pltという別名で）
import matplotlib.pyplot as plt

# ファイル名のパターンマッチングを行う glob 関数をインポート（今回は未使用）
from glob import glob

# scikit-learn の MinMaxScaler をインポート（今回は未使用）
from sklearn.preprocessing import MinMaxScaler

# scikit-learn の StandardScaler をインポート（今回はこちらを使用）
from sklearn.preprocessing import StandardScaler

from sklearn.decomposition import PCA #主成分分析器

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


"""
Scikit-learn20本ノック６
# 'Age'列の平均値を計算（欠損値は無視される）
ave = df['Age'].mean()

# 'Age'列の標準偏差を計算（欠損値は無視される）
std = df['Age'].std()

# 'Age'列の欠損値（NaN）の数をカウント
num = df['Age'].isnull().sum()

# 欠損値の個数分だけ、平均±標準偏差の範囲でランダムな整数を生成（補完用）
# randintの範囲は整数で指定するため、int()でキャストする
rand = np.random.randint(int(ave - std), int(ave + std), size=num)

# 元のDataFrameの'Age'列の欠損値部分に、生成したランダムな整数を代入して補完
df.loc[df['Age'].isnull(), 'Age'] = rand

# 補完後の'Age'列のデータを、70個のビンを使ってヒストグラムとして描画
ab = df['Age'].hist(bins=70)

# ヒストグラムのグラフを画面に表示
plt.show()

# 描画オブジェクトを表示（オブジェクトの情報が出力されるが、グラフはplt.show()で表示済み）
print(ab)
"""


"""
Scikit-learn20本ノック7
# DataFrameの 'Sex' 列だけを抽出し、最初の5行を表示（欠損があるか確認用）
ab = df[['Sex']].head()
print(ab)

# 'Sex'列の欠損値を「前の行の値（ffill = forward fill）」で補完し、先頭5行を表示
ab = df[['Sex']].fillna(method="ffill").head()
print(ab)
"""

"""
Scikit-learn20本ノック8
# 'Sex'列をワンホットエンコーディング（カテゴリをダミー変数に変換）し、
# 'male'列を削除（基準カテゴリとして除外）→ 最初の5行を表示
ab = pd.get_dummies(df['Sex']).drop('male', axis=1).head()
print(ab)
"""

"""
Scikit-learn20本ノック9
# MinMaxScaler のインスタンスを作成（0〜1の範囲にスケーリング）
mmscaler = MinMaxScaler(feature_range=(0, 1), copy=True)

# 'Age'列の最小値と最大値を取得
lim_min, lim_max = df['Age'].min(), df['Age'].max()

# 最小値と最大値を使ってスケーラーを学習させる
# reshape(-1, 1) で2次元配列に変換（scikit-learnの要求仕様）
mmscaler.fit(np.array([lim_min, lim_max]).reshape(-1, 1))

# 'Age'列をスケーラーで変換し、0〜1の範囲にスケーリングした結果を得る
ab = mmscaler.transform(df[['Age']])

# スケーリング後の結果を出力
print(ab)
"""

"""
Scikit-learn20本ノック10
# StandardScaler のインスタンスを作成（平均0・標準偏差1になるよう変換）
ss = StandardScaler()

# 'Age'列を標準化（平均0、標準偏差1のスケールに変換）
ab = ss.fit_transform(df[['Age']])

# スケーリング後の結果を出力
print(ab)
"""


"""
Scikit-learn20本ノック11
# CSV読み込み
df_wine = pd.read_csv("wine.csv")

# DataFrame情報表示
df_wine.info()
print(df_wine.head(2))

# StandardScalerインスタンス作成
ss = StandardScaler()

# class 列を除いて標準化
dfs = pd.DataFrame(
    ss.fit_transform(df_wine.drop("class", axis=1)),
    columns=df_wine.columns.drop("class")
)
# 確認表示
print(dfs.head())
"""

"""
Scikit-learn20本ノック1２
#主成分分析の実行
pca = PCA()
pca.fit(dfs) # 学習
# データを主成分空間に写像
feature = pca.transform(dfs)
feature = pd.DataFrame(feature, columns=["PC{}".format(x + 1) for x in range(len(dfs.columns))]) # データフレームへ変換 以下のようにカラム名を設定
feature.head()
"""