#参考 https://www.youtube.com/watch?v=k4YzlaOXfvQ
#NumPy20本ノック
# NumPyをnpとしてインポート（数値計算ライブラリ）
import numpy as np

# matplotlib.pyplotをpltとしてインポート（グラフ描画ライブラリ）
import matplotlib.pyplot as plt  # 通常、pyplotは plt と略すのが一般的

# ① -10から12まで2刻みの配列（要素数12）を作って4行×3列に整形
a = np.arange(-10, 13, 2).reshape(4, -1)
# → a の形状: (4, 3)

# ② 3行4列の単位行列から2を引く（→ 対角が -1、他が -2）
b = np.eye(3, 4) - 2
# → b の形状: (3, 4)

# ③ 形状を確認
a1 = a.shape, b.shape
print(a1)
# → ((4, 3), (3, 4))

# ④ 行列積（@）を計算
ab = a @ b
print(ab)

# ⑤ 行列abの左上2行2列だけを抽出（スライス）
c = ab[:2, :2]  # → (2, 2)行列
print(c)

# ⑥ 行列cの転置（行と列を入れ替える）
c1 = c.T  # → (2, 2)行列（転置しても2×2）
print(c1)
# ⑦ 転置した行列の行列式（スカラー）を計算
c2 =np.linalg.det(c.T)
print(c2)
# ⑧ 行列式が0でなければ逆行列を求める
c3 =np.linalg.inv(c.T)
print(c3)








"""
NumPy20本ノック18
# ① -10から12まで2刻みの配列（要素数12）を作って4行×3列に整形
a = np.arange(-10, 13, 2).reshape(4, -1)
# → a の形状: (4, 3)

# ② 3行4列の単位行列から2を引く（→ 対角が -1、他が -2）
b = np.eye(3, 4) - 2
# → b の形状: (3, 4)

# ③ 形状を確認
a1 = a.shape, b.shape
print(a1)
# → ((4, 3), (3, 4))

# ④ 行列積（@）を計算
ab = a @ b
print(ab)
"""

"""
NumPy20本ノック17-1
# 0〜29の整数をランダムに100個生成（例：アンケートの点数や日付のようなイメージ）
date = np.random.randint(0, 30, 100)
print(date)  # ランダムな整数配列を出力して確認

# ヒストグラムを描画（各値が何回出てきたかを棒グラフで表示）
plt.hist(date)
plt.show()
"""

"""
NumPy20本ノック17-1
# 0 から 2π（円周）までを500等分した数値を作成 → x軸のデータ
x = np.linspace(0, 2 * np.pi, 500)
print(x)  # 作成したxの配列を出力（確認用）

# xの要素数（500）を取得して表示
x1 = x.size
print(x1)

# xに対するsin(x)の値を計算し、グラフに描画（折れ線グラフ）
x2 = plt.plot(x, np.sin(x))  # sin波の描画
print(x2)  # プロットオブジェクトがリスト形式で出力される（Line2Dオブジェクト）

# xに対するcos(x)も同じグラフに重ねて描画
x3 = plt.plot(x, np.cos(x))  # cos波の描画
print(x3)  # 同様にLine2Dオブジェクトが出力される

# 描画を実行して、ウィンドウにグラフを表示する
# ※plt.show() を呼び出さないと、グラフは表示されない！
plt.show()
"""

"""
NumPy20本ノック16
#.reshape(3, -1) は3行にして、列数は自動で計算という意味
a = np.array([[1,4,3],[8,5,4],[2,6,7]]).reshape(3,-1)
b = np.array([[1,4,3],[4,3,4],[8,9,4]]).reshape(3,-1)
#縦結合
tab=np.vstack((a,b))
print(tab) 
#横結合
yab=np.hstack((a,b))
print(yab) 
#縦に2分割
tab2=np.vsplit(tab,2)
print(tab2) 
#横に2分割
yab2=np.hsplit(yab,2)
print(yab2) 
"""

"""
NumPy20本ノック15
#.reshape(3, -1) は3行にして、列数は自動で計算という意味
a = np.array([[1,4,3],[8,5,4],[2,6,7]]).reshape(3,-1)
b = np.array([[1,4,3],[4,3,4],[8,9,4]]).reshape(3,-1)
#縦結合
tab=np.vstack((a,b))
print(tab) 
#横結合
yab=np.hstack((a,b))
print(yab) 
"""

"""
NumPy20本ノック14
a = np.array([1,np.pi,np.pi/1,np.pi/2]).reshape(2,-1)
#sinを求める
a1 = np.sin(a)
print(a1) 
#cosを求める
a1 = np.cos(a)
print(a1) 
"""

"""
NumPy20本ノック13
a = np.array([1,4,1,2]).reshape(2,-1)
#平方根
a1 = np.sqrt(a)
print(a1) 

#指数関数
a1 = np.exp(a)
print(a1) 
"""

"""
NumPy20本ノック12
b = np.array([[1,4,3],[4,3,4],[8,9,4]])
#最大
b1=b.max()
print(b1)
#最小
b1=b.min()
print(b1)
#行毎の最小
b1=b.min(axis=1)
print(b1)
#総和
b1=b.sum()
print(b1)
#平均値
b1=b.mean()
print(b1)
#分散
b1=b.var()
print(b1)
#標準偏差
b1=b.std()
print(b1)
"""

"""
NumPy20本ノック11
a = np.arange(12)
#何行何列にする
a1 = a.reshape(3, 4)
print(a1)
"""

"""
NumPy20本ノック10
#行列にスカラーを掛ける
a = np.array([[1, 4], [4, 3]])  
a1 = a * 0.2
print(a1) 

b = np.array([[1,4,3],[4,3,4]])
b1 = b * 2
print(b1) 
"""

"""
NumPy20本ノック9
#np.linalg.det()=行列式を計算
b = np.array([[1, 4], [4, 3]])  
det = np.linalg.det(b)
print(det)  # 出力: -7.0

#np.linalg.inv()=逆行列
b = np.array([[1, 4], [4, 3]])  
inv = np.linalg.inv(b)
print(inv) 
"""

"""
NumPy20本ノック8
#転置＝行と列の入れ替え
a = np.array([1,2,3])
#a1=a.T一次元は無理

a = np.array([[1,2,3]])
a1=a.T
print(a1)

b = np.array([[1,4,3],[4,3,4]])
b1=b.T
print(b1)
"""

"""
NumPy20本ノック7
#足し算
a = np.array([[1,2],[1,3]])
b = np.array([[1,4],[4,3]])
c = a+b
print(c)

#引き算
a = np.array([[1,2],[1,3]])
b = np.array([[1,4],[4,3]])
c = a-b
print(c)

#掛け算
a = np.array([[1,2],[1,3]])
b = np.array([[1,4],[4,3]])

c=a@b
print(c)
c = a.dot(b)
print(c)
#アダマール積＝要素が同じ同士の掛け算
a = np.array([[1,2],[1,3]])
b = np.array([[1,4],[4,3]])
c =a * b
print(c)
"""

"""
NumPy20本ノック６
#1~13までの２こ飛ばしの配列を作成
a = np.arange(1,13,2)
print(a)

c = np.array([[1,2,2],
              [1,3,4],
              [4,3,5]])

#０スタートの２個目から-1は最後の一個前の値
a1=a[2]
print(a1)
#逆順の取り方
a1=a[::-1]
print(a1)
#1行目
c1=c[0]
print(c1)
#３行１列目
c1=c[2,0]
print(c1)

下記を出力する
[3,4]
[3,5]

c1 =c[1:,1:]
print(c1)
"""

"""
NumPy20本ノック5
C = np.array([[1,2],
              [1,3]])
print(C)

#形状を習得
a = C.shape
print(a)
#次元を習得
a = C.ndim
print(a)
#データ型を習得
a = C.dtype
print(a)
#要素数を習得
a = C.size
print(a)
"""

"""
NumPy20本ノック4
#np.eye()で単位行列を生成、斜めの成分も生成
a = np.eye(3)
print(a)
print("11111111111")
b = np.eye(3,4)
print(b)
"""

"""
NumPy20本ノック3
#np.zerosで要素が０しか入っていないベクトルを作成可能
a = np.zeros((1,2))
print(a)

#np.onesで要素が１しか入っていないベクトルを作成可能
b = np.ones((4,1))
print(b)
"""

"""
NumPy20本ノック2

C = np.array([[1,2],
              [1,3]])
print(C)

D = np.array([[1,2,5,6],
              [1,3,7,3],
              [6,7,8,9]])
print(D)
"""

"""
NumPy20本ノック1

a = np.array([1,2,3,4])
print(a)

b = np.array([[1],[2],[3]]) 
print(b)
"""