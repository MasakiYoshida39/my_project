"""
参考URL
https://www.youtube.com/watch?v=ZQZ38rK28Gk
"""
import pandas as pd

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