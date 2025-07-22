import pandas as pd

# Excelファイルを読み込む
df1 = pd.read_excel('./test.xlsx')

# データの表示
print(df1)



#データフレームに存在するカラム名を指定する
series = df1['Name']
print(series)

#カラムの値もしくは条件を指定することで、条件に合う行の値を取り出す
filtered_df1 = df1[df1['ID'] == 1]
print(filtered_df1)

 
filtered_df2 = df1[df1['ID'] > 8]
print(filtered_df2)

#groupby()メソッドで指定したカラムの重複する値をまとめる
#agg()メソッドに、キーにカラム名、値に適用する処理とした辞書を渡すことで、キーで指定したカラムに値で指定した処理を適用する

grouped_df = df1.groupby('Name').agg({'Age': 'sum'})
print(grouped_df)
#データフレームに新しいカラム名を指定して、値を代入することでカラムを追加する
df1['Gender'] = ['male', 'female', 'male', 'female', 'male', 'female',
                 'male', 'male', 'female', 'female']
print(df1)




"""
# Excelファイルとして書き出し
df2.to_excel('./new.xlsx')
"""



"""
"""