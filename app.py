import sys
import random

print('----------------------------------------')
print('| Guess The Number Game - 数当てゲーム |')
print('----------------------------------------')

def set_range():
    user_input = input('整数を２つ入力してください（例：2, 10）：')

    try:
        range_values = list(map(int, user_input.split(',')))
        range_values.sort()
    except ValueError:
        print('入力が間違っています。整数を２つ入力してください。\n')
        set_range()
        return

    if len(range_values) == 2:
        print('あなたが設定した範囲は ' + str(range_values[0]) + ' 〜 ' + str(range_values[1]) + ' です。\n')
        target = random.randint(range_values[0], range_values[1])
        print('コンピュータが選んだ数は ' + str(target) + ' です。')

        def ask_guess():
            user_input = input('コンピュータが選んだ数は何でしょう？：')

            try:
                guess = int(user_input.strip())
            except ValueError:
                print('入力が間違っています。整数を入力してください。\n')
                ask_guess()
                return
            
            if guess < target:
                print('残念！もっと　▲大きい数▲　です。\n')
                ask_guess()
            
            elif guess > target:
                print('残念！もっと　▼小さい数▼　です。\n')
                ask_guess()

            elif guess == target:
                print('正解です！おめでとう！＼(^o^)／\n')

        ask_guess()

    else:
        print('入力が間違っています。整数を２つ入力してください。\n')
        set_range()


set_range()