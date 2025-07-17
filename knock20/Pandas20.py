"""
参考URL
https://www.youtube.com/watch?v=ZQZ38rK28Gk
"""
import pandas as pd
df=pd.read_csv('weather.csv')
df_pe = pd.read_csv('people.csv')

#ユニークな値の抽出＝一次元のみOK
df1 = df_pe['nationality'].unique()
print(df1)
df1 = df_pe['name'].unique()
print(df1)
df1 = df_pe['age'].unique()
print(df1)

"""
Pandas20本ノック6
print(df_pe)

df1 = df_pe[df_pe['nationality'] == 'America']
print(df1)

df1 = df_pe.query('nationality == "America"')
print(df1)

df1 = df_pe['nationality'].isin(['America'])
print(df1)

#20以上30未満

df1 = df_pe[(df_pe['age'] >= 20) & (df_pe['age'] < 30)]
print(df1)

df1 = df_pe.query('age >=20 & age <30')
print(df1)
"""


"""
Pandas20本ノック5
#任意の要素の取り出し(行、列)
df1 = df.iloc[4:10,2:6]
print(df1)
df1 = df.loc[5:10,'平均気温(℃)': '最深積雪(cm)']
print(df1)
"""

"""
Pandas20本ノック4

#カラムの確認
df1 = df.dtypes
print(df1)
#サイズを確認
df1 = df.shape
print(df1)
# カラムを表示
df1 = df.columns
print(df1)
# インデックス番号取り出し
df1 = df.index
print(df1)
"""

"""
Pandas20本ノック3
df=pd.read_csv('weather.csv')
# カラムを表示
df1 = df.columns
print(df1)
# 必要な部分のみ記載
df1=df[['年月日', 
        '平均気温(℃)', 
        '平均気温(℃).1', 
        '最低気温(℃)', 
        '降水量の合計(mm)',
        '最深積雪(cm)',
       '平均雲量(10分比)',  
       '平均蒸気圧(hPa)',
       '平均風速(m/s)',
        '日照時間(時間)']][1:] 
#  [1:]=1行目からスタートする

df1=df1.head(2)
print(df1)
"""



"""
Pandas20本ノック2

df=pd.read_csv('weather.csv')
# head(3)＝先頭3行を表示
df1=df.head(3)
print(df1)
# tail(10)＝後ろ10行を表示
df1=df.tail(10)
print(df1)
"""

"""
Pandas20本ノック１

df=pd.read_csv('weather.csv')
print(df)

"""