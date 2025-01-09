import sys
import random
import math
import json

debugmode = False
top5 = [
    [[100, 1000], 5, 10000, 'No Name 1'],
    [[100, 1000], 10, 5000, 'No Name 2'],
    [[2, 10], 2, 200, 'No Name 3'],
    [[2, 10], 4, 100, 'No Name 4'],
    [[3, 3], 1, 0, 'No Name 5'],
]

if __name__ == '__main__':
    try:
        def load_top5():
            try:
                with open('top5.json', 'r') as file:
                    global top5
                    data = json.load(file)

                    try:
                        validate_load_data(data)
                        top5 = data
                    except :
                        print('ランキングデータが破損しているため、初期データを使用します。')

                print('ランキングデータの読込みが完了しました。')
            
            except FileNotFoundError:
                print('ランキングデータが見つからないため、初期データを使用します。')


        def save_top5():
            with open('top5.json', 'w') as file:
                json.dump(top5, file)
                if debugmode:
                    print('[DEBUG] Top5 data has been saved as file.')


        def show_title():
            print('----------------------------------------')
            print('| Guess The Number Game - 数当てゲーム |')
            print('----------------------------------------')


        def validate_load_data(data):
            data_sorted = sorted(data, key=lambda x: (-x[2], x[1]))
            for idx, (range, attempts, score, user_name) in enumerate(data_sorted[:5]):
                f'{(idx + 1):>4}　{score:>6}　{user_name:<10}　{attempts:>10}　{(range[1] - range[0] + 1):>6} ({range[0]} 〜 {range[1]})'


        def show_ranking():
            print('★ランキング')
            print('順位　スコア　名前　　　　　　試行数　要素数（設定した値の範囲）')

            top5_sorted = sorted(top5, key=lambda x: (-x[2], x[1]))
            for idx, (range, attempts, score, user_name) in enumerate(top5_sorted[:5]):
                print(f'{(idx + 1):>4}　{score:>6}　{user_name:<10}　{attempts:>10}　{(range[1] - range[0] + 1):>6} ({range[0]} 〜 {range[1]})')


        def initialize_game():
            load_top5()
            show_title()
            show_ranking()

            user_input = input('遊び方の説明を見ますか？[y/N]：')

            if user_input.lower() == 'debugmode':
                global debugmode
                debugmode = True
                print('[DEBUG] Debugmode enabled!')

            elif user_input.upper() == 'Y':
                print('★遊び方：')
                print('あなたが設定する２つの整数の間にある数から、')
                print('コンピュータがランダムに１つを選びます。')
                print('コンピュータが選んだ数を当てられたら、あなたの勝ちです。')
                print('')
                print('★例：')
                print('あなたが設定した数：2, 10')
                print('コンピュータが選べる範囲：2, 3, 4, 5, 6, 7, 8, 9, 10')
                print('コンピュータが選んだ数：7')
                print('正解となる入力：7')
                print('不正解となる入力：7以外の数')
                print('')

            print('それでは、始めましょう！\n')
           

        def get_score(range, attempts):
            if attempts == 0:
                raise ValueError('試行数は１以上の整数としてください。\n')

            number_of_elements = range[1] - range[0] + 1
            ideal_attempts = math.ceil(math.log(number_of_elements, 2))
            ideal_attempts = 1 if ideal_attempts == 0 else ideal_attempts  # 要素数１の場合は、理想の試行数が０となるので１に変更する
            if debugmode:
                print(f'[DEBUG] number_of_elements: {number_of_elements}, ideal_attempts: {ideal_attempts}')

            leverage = 100;
            if number_of_elements >= 1000:
                leverage = 10000
            elif number_of_elements >= 100:
                leverage = 5000
            elif number_of_elements >= 50:
                leverage = 2500
            
            if debugmode:
                print(f'[DEBUG] leverage: {leverage}')

            score = (ideal_attempts / attempts) * leverage            
            if debugmode:
                print(f'[DEBUG] score: {score}')

            return int(score)


        def chceck_top5(range, attempts, score):
            lowest_score = top5[-1][2]
            return score > lowest_score
        

        def set_player_name():
            user_input = input('ランキングに載せる名前を入力してください。')
            return user_input.strip() or 'No Name'
        
        def set_ranking(range, attempts, score, player_name):
            top5.append([range, attempts, score, player_name])
            if debugmode:
                print('\n[DEBUG] unsorted top5 + 1')
                print(top5)

            top5.sort(key=lambda x: x[2], reverse=True)
            if debugmode:
                print('\n[DEBUG] sorted top5 + 1')
                print(top5)

            top5[:] = top5[:5]
            print('ランキングへの登録が完了しました。\n')

            if debugmode:
                print('\n[DEBUG] After limiting top5')
                print(top5)

            show_ranking()
            confirm_retry()


        def confirm_retry():
            user_input = input('\nもう一度ゲームをやりますか？[Y/n]：')
            if user_input == '' or user_input.upper() == 'Y':
                set_range()

            else:
                save_top5()
                print('遊んでくれてありがとう(*\'ω\'*)また遊んでね！')
                exit(0)


        def set_range():
            while True:
                user_input = input('整数を２つ入力してください（例：2, 10）：')

                try:
                    range_values = list(map(int, user_input.split(',')))
                    range_values.sort()
                except ValueError:
                    print('入力が間違っています。整数を２つ入力してください。\n')
                    set_range()
                    continue

                small, large = range_values
                if len(range_values) == 2:
                    print('あなたが設定した範囲は ' + str(range_values[0]) + ' 〜 ' + str(range_values[1]) + ' です。\n')
                    target = random.randint(range_values[0], range_values[1])
                    if debugmode:
                        print('[DEBUG] The computer chose: ' + str(target))

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
                                    player_name = set_player_name()
                                    set_ranking(range_values, attempts, current_score, player_name)
                                
                                confirm_retry()


                    ask_guess()
                    break

                else:
                    print('入力が間違っています。整数を２つ入力してください。\n')
                    continue

        
        initialize_game()
        set_range()
    
    except KeyboardInterrupt:
        save_top5()
        print('\nゲームを中断しました。また遊んでね！')