"""
FizzBuzz問題
1から100までの数字を順番に出力してください。
ただし、以下のルールに従って出力を変えてください：
3の倍数のときは "Fizz" を出力
5の倍数のときは "Buzz" を出力
3と5両方の倍数のときは "FizzBuzz" を出力
それ以外の数は、そのまま数値を出力

進め方
1,適当な和のループ分を作成（今回は20)
2,3の倍数のときは "Fizz" を出力
3,5の倍数のときは "Buzz" を出力
4,3と5両方の倍数のときは "FizzBuzz" を出力
5,修正
"""
# 変数aには0を代入
a = 1
# while文でaが20より小さい場合は繰り返しを続ける
while a <= 20:
    # コードは上から下に流れるからFizzBuzzの処理を先にしないとダメ
    if a%15 == 0:
         print(str(a)+"FizzBuzz")
    elif a%3 == 0:
        print(str(a)+"Fizz")
    elif a%5 == 0:
        print(str(a)+"Buzz")
    else:
        print(a)
    # 毎回aに1を足していく
    a += 1


"""
#コンストラクターは必ず第1引数にselfを記載（Javaと違う）
class Person:
    def __init__(self, name): # コンストラクタ
		    self.name = name
    
    def introduce(self):
        return f"私の名前は{self.name}です。"
        
taro = Person("タカ") # インスタンス化
# 下の仕組みがよくわからない
print(taro.introduce()) 
print(taro.name) 


# 引数3つ、デフォルト値あり
def add1(num1=1, num2=2, num3=3):
    return num1 * num2 * num3

# 引数2つ、税込み計算
def add(num1, num2):
    sum = num1 + num2 
    taxincluded = sum * 1.08
    consumptiontax = sum * 0.08
    return sum, taxincluded, consumptiontax

# 関数の呼び出し
sum, taxincluded, consumptiontax = add(100, 200)

# 結果の表示 int(taxincluded)にすることで小数点を消す
print(f"合計: {sum}, 税込: {int(taxincluded)}, 消費税: {consumptiontax}")
print(add1(3, 9, 3)) 
print(add1())  # デフォルト値使用（1×2×3 = 6）





# 簡単な関数
def greet(name):
    return f"こんにちは、{name}さん！"
 
# 関数の呼び出し
message = greet("田中")
print(message)  


 
 # 8未満の数値を繰り返し出力
count = 0
while count < 8:
    print(count)  
    count += 1  

# インデントが大事
# リストの作成
Rbs = ["砂糖", "カフェイン", "タウリン"]
 #	Pythonでは拡張for文と言わないらしい
for Rb in Rbs:
    print(Rb)


# リストの作成
Rb = ["砂糖", "カフェイン", "タウリン"]
 
# 配列の要素は０から始まる
print(Rb [0])  
print(Rb [1])  


# if文と「数字と文字を繋げる（連結する）」方法

x = int(input("数字を入力してください: "))

if x > 5:
    print(str(x) + " は 5 より大きい")
elif x == 5:
    print("{} は 5 と等しい".format(x))
else:
    print(f"{x} は 5 より小さい")




# 最初を小文字はダメ
a= True
b=False
print(a and b)
print(a or b)
print(not a)





# コマンドラインツール入力
name = input("あなたの好きな言語を教えて: ")
print("あなたが好きな言語は、" + name + "ですね")


キウイ 300円 3個
リンゴ 1000円 2個
ぶどう 6600円 4個
合計を出力

Kiwi = 300*3
Apple = 1000*2
Grapes = 6600*4
Total = Grapes + Apple+ Kiwi
print(Total)



#ターミナルでpython my_file.pyを行う
# "青, 黒" という結果を生む式
print("青、" + "黒"  )
# 189という結果を生む式
print(94+95)


int takasi = 10 * 5
下記のエラー発生JavaやC言語みたいな記載禁止
 File "/Users/masa/my_project/my_file.py", line 9
    int takasi = 10 * 5         
        ^^^^^^
SyntaxError: invalid syntax    

itihara = 4 * 8
kasahara = 8 * 5
meesi = 6 * 9
CR7 = 9 * 20
honnda = 11 + 10

print(CR7)

"""  

