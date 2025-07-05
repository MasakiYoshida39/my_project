#NumPyを使用する宣言
import numpy as np






z = np.arange(10).reshape(2, 5)
print(z)

#arange()関数は指定された範囲の値で配列を生成
y = np.arange(10)
print(y)


#配列の作成
x = np.array([1, 2, 3, 4, 5])
print(x)


#配列の形状はshape属性で確認
x = np.array([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]])
print(x.shape)


#
print(x + 5)


"""
"""
#