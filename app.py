from flask import Flask
from datetime import datetime
from flask import Flask, request
import pytz 
import random

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


"""
コマンド例: curl -X POST -d 'days=2022-10-03' http://localhost:5000/date
"""

# /dateにアクセスすると、入力メッセージが表示される
@app.route('/date', methods=['POST'])
def week_calculation():
    

    week_list = ['月曜日', '火曜日', '水曜日', '木曜日', '金曜日', '土曜日', '日曜日']
    input_date = request.form.get('days')
    # 受け取った文字を日付に変換する
    date = datetime.strptime(input_date, '%Y-%m-%d')

    # 日付を曜日に変換する
    #.weekday() は、日付から曜日を数学的な計算に基づいて自動的に導き出してる
    week = date.weekday()

    return f'{date}は{week_list[week]}です'


# /aphorismへアクセスすると、名言をランダムに返す
# curl localhost:5000/aphorism
@app.route('/aphorism', methods=['GET'])
def aphorism():
    aphorism_words = ['Done is better than perfect.',
                      'Stay hungry, stay foolish',
                      'We are What We Choose',
                      'Our greatest weakness lies in giving up.\
                      The most certain way to succeed is always \
                      to try just one more time.']

    #random.choice() は、そのリストの中からランダムに1つの要素を選ぶ
    aphorism = random.choice(aphorism_words)

    return aphorism

# /massageへアクセスすると、ねぎらいのメッセージが返ってくる。
#curl -X POST -d 'name=hoge' http://localhost:5000/message
#name=　　に出力したい名前を入れPOST で送信
@app.route('/message', methods=['POST'])
def gratitude_message():
    #request.form.get('name')=フォームから送られてきたPOSTデータの 'name' という項目を取得するためのコード
    username = request.form.get('name')
    return f'毎日お疲れ様。{username}さん、これからも情熱を忘れずに行こう!!!'







#ユーザー名とパスワードをJSON形式で受取り、その値を返す
"""
curl -X POST -d '{"username": "hoge", "password": "123456"}'
http://localhost:5000/login
"""
@app.route('/login', methods=['POST'])
def login_message():
    #リクエストの中にあるJSONデータを強制的に取り出す
    req = request.get_json(force=True)
    username = req.get('username', None)
    password = req.get('password', None)
    return f'username..."{username}"とpassword..."{password}"を登録しました。'







if __name__ == "__main__":
    app.run()
