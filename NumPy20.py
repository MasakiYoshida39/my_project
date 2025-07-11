#参考 https://www.youtube.com/watch?v=k4YzlaOXfvQ
#NumPy20本ノック
import numpy as np


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