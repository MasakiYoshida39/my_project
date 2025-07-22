"""
"""
# 必要なライブラリをインポート
from sklearn import datasets  # scikit-learn のデータセットモジュール
from sklearn.model_selection import train_test_split  # データを学習用とテスト用に分割する関数
from sklearn import svm  # SVM（サポートベクターマシン）のモジュール
from sklearn.metrics import accuracy_score  # 精度（正解率）を計算する関数

# Iris（アヤメ）のデータセットをロード
iris = datasets.load_iris()  # 特徴量とラベルを含んだ辞書型データが返る
X = iris.data  # 特徴量（がく片・花弁の長さと幅の4つの値）
y = iris.target  # ラベル（0, 1, 2：3種類のアヤメの分類）

# 学習データとテストデータに分割（8:2の割合）
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# SVM（サポートベクターマシン）による分類器を作成
clf = svm.SVC(gamma='auto')  # gammaはカーネル関数のパラメータ

# 学習用データでモデルを学習
clf.fit(X_train, y_train)

# テストデータを使って予測を実行
test_result = clf.predict(X_test)

# 予測結果と実際の正解ラベルを表示
print("予測結果:", test_result)
print("正解ラベル:", y_test)

# 正解率を計算して表示
print("正解率:", accuracy_score(y_test, test_result))
