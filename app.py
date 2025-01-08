import sys
import random
import math

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

    small, large = range_values
    if len(range_values) == 2:
        print('あなたが設定した範囲は ' + str(range_values[0]) + ' 〜 ' + str(range_values[1]) + ' です。\n')
        target = random.randint(range_values[0], range_values[1])
        print('コンピュータが選んだ数は ' + str(target) + ' です。')

        attempts = 0
        def ask_guess():
            nonlocal attempts
            user_input = input('コンピュータが選んだ数は何でしょう？：')

            try:
                guess = int(user_input.strip())
            except ValueError:
                print('入力が間違っています。整数を入力してください。\n')
                ask_guess()
                return
            
            if guess < small:
                print('範囲（' + str(small) + ' 〜 ' + str(large) + '）より小さい数です。入力しなおしてください。\n')
                ask_guess()

            elif guess > large:
                print('範囲（' + str(small) + ' 〜 ' + str(large) + '）より大きい数です。入力しなおしてください。\n')
                ask_guess()

            elif guess < target:
                attempts += 1
                print('残念！もっと　▲大きい数▲　です。\n')
                ask_guess()
            
            elif guess > target:
                attempts += 1
                print('残念！もっと　▼小さい数▼　です。\n')
                ask_guess()

            elif guess == target:
                attempts += 1
                print('正解です！おめでとう！＼(^o^)／\n')
                print('正解までの試行数は ' + str(attempts) + ' 回でした。\n')
                print(get_score(range_values, attempts))

        ask_guess()

    else:
        print('入力が間違っています。整数を２つ入力してください。\n')
        set_range()

def get_score(range, attempts):
    if attempts == 0:
        raise ValueError('試行数は１以上の整数としてください。\n')

    number_of_elements = range[1] - range[0] + 1
    ideal_attempts = math.ceil(math.log(number_of_elements))
    print(f'要素数：{number_of_elements}, 理想的な試行数：{ideal_attempts}')
    
    leverage = 100;
    if number_of_elements >= 1000:
        leverage = 10000
    elif number_of_elements >= 100:
        leverage = 5000
    elif number_of_elements >= 50:
        leverage = 2500
    print(f'倍率：{leverage}')

    score = (ideal_attempts / attempts) * leverage
    print(f'スコア：{score}')

    return int(score)


set_range()