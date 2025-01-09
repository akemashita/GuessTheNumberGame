import sys
import random
import math

if __name__ == '__main__':
    try:

        print('----------------------------------------')
        print('| Guess The Number Game - 数当てゲーム |')
        print('----------------------------------------')

        top5 = [
            [[100, 1000], 5, 10000, 'No Name 1'],
            [[100, 1000], 10, 5000, 'No Name 2'],
            [[2, 10], 2, 200, 'No Name 3'],
            [[2, 10], 4, 100, 'No Name 4'],
            [[3, 3], 1, 0, 'No Name 5'],
        ]

        def show_ranking():
            print('★ランキング')
            print('順位　スコア　名前　　　　　　試行数　要素数（設定した値の範囲）')

            top5_sorted = sorted(top5, key=lambda x: (-x[2], x[1]))
            for idx, (range, attempts, score, user_name) in enumerate(top5_sorted[:5]):
                print(f'{(idx + 1):>4}　{score:>6}　{user_name:<10}　{attempts:>10}　{(range[1] - range[0] + 1):>6} ({range[0]} 〜 {range[1]})')

        show_ranking()


        def get_score(range, attempts):
            if attempts == 0:
                raise ValueError('試行数は１以上の整数としてください。\n')

            number_of_elements = range[1] - range[0] + 1
            ideal_attempts = math.ceil(math.log(number_of_elements))
            ideal_attempts = 1 if ideal_attempts == 0 else ideal_attempts  # 要素数１の場合は、理想の試行数が０となるので１に変更する
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


        def chceck_top5(range, attempts, score):
            lowest_score = top5[-1][2]
            return score > lowest_score
        

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
                    while True:
                        user_input = input('コンピュータが選んだ数は何でしょう？：')

                        try:
                            guess = int(user_input.strip())
                        except ValueError:
                            print('入力が間違っています。整数を入力してください。\n')
                            continue
                        
                        if guess < small:
                            print('範囲（' + str(small) + ' 〜 ' + str(large) + '）より小さい数です。入力しなおしてください。\n')

                        elif guess > large:
                            print('範囲（' + str(small) + ' 〜 ' + str(large) + '）より大きい数です。入力しなおしてください。\n')

                        elif guess < target:
                            attempts += 1
                            print('残念！もっと　▲大きい数▲　です。\n')
                        
                        elif guess > target:
                            attempts += 1
                            print('残念！もっと　▼小さい数▼　です。\n')

                        elif guess == target:
                            attempts += 1
                            print('正解です！おめでとう！＼(^o^)／\n')
                            print('正解までの試行数は ' + str(attempts) + ' 回でした。\n')
                            current_score = get_score(range_values, attempts)

                            print('今回のスコアは ' + str(current_score) + ' でした。')

                            if chceck_top5(range_values, attempts, current_score):
                                print('おめでとう！TOP5に入りました！')

                            break

                ask_guess()

            else:
                print('入力が間違っています。整数を２つ入力してください。\n')
                set_range()

        set_range()
    
    except KeyboardInterrupt:
        print('\nゲームを中断しました。また遊んでね！')