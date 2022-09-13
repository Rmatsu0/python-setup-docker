import sys

def fizzBuzz(n):
    if n <= 0:
        return ()
    else:
        fizzBuzz(n-1)
        if n % 3 == 0 and n % 5 == 0:
            print(n, ' : ', 'FizzBuzz')
        elif n % 3 == 0:
            print(n, ' : ', 'Fizz')
        elif n % 5 == 0:
            print(n, ' : ', 'Buzz')
        else:
            print(n, ' : ', n)
        return ()

# 他のプログラム（上）がモジュールとして、ほかのプログラムから読み込まれた場合に
# この下の処理を実行させないようにするためのif文
if __name__ == '__main__':
    args = sys.argv
    if 2 <= len(args):
        if args[1].isdigit():
            fizzBuzz(int(args[1]))
        else:
            print('Argument is not digit')
    else:
        print('Arguments are too short')

print("last")