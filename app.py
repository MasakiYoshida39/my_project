from flask import Flask
from datetime import datetime
import pytz 


app = Flask(__name__)
"""
def hello():で関数を宣言していて、
returnで文字列を返しています。
"""

@app.route('/', methods=['GET'])
def hello():
    return 'Test'

"""
現在の日時を日本時間で取得し、
「現在時刻は〇年〇月〇日　〇時〇分〇秒です」を返す
"""

# /timeへgetでアクセスしたら現在時刻を知らせる
@app.route('/time', methods=['GET'])
def current_time():
    dt_now = datetime.now(pytz.timezone('Asia/Tokyo'))
    date = dt_now.strftime('%Y年%m月%d日  %H時%M分%S秒')
    return f'現在時刻は{date}です'


if __name__ == "__main__":
    app.run()
