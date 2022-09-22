import sys #インタプリタや実行環境に関する情報を扱うためのライブラリ

print("==============================")
# arg = argument
# プログラム中で関数やメソッド、サブルーチン等を呼び出すときに渡す値のこと
print(sys.argv)
args = sys.argv

if len(args) == 3:
    print(args) #コマンドライン引数を出力
    print(type(args))
    print(type(args[0]))
    print(type(args[1]))
    print(type(args[2]))
    # print(type(args[3])) # list index out of range
    print(len(args))
else:
    print("コマンドライン引数を三つ入力してください\n第一引数はstr型,第二引数はfloat型です")


print("==============================")
# sys version
print(sys.version)
# os version
print(sys.platform)

print("==============================")
