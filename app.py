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

current_language = 'ja'
messages = {
    'load_data_completed': {
        'ja': 'ランキングデータの読込みが完了しました。\n',
        'en': 'Ranking data has been loaded.\n',
    },        
    'load_data_invalid': {
        'ja': 'ランキングデータが破損していました。初期データを使用します。',
        'en': 'Ranking data was corrupted. Initial data has been used.',
    },
    'load_data_not_found': {
        'ja': 'ランキングデータが見つかりませんでした。初期データを使用します。\n',
        'en': 'Ranking data was not found. Initial data has been used.\n',
    },
    'show_attempts': {
        'ja': '正解までの試行数は {attempts} 回でした。',
        'en': 'It took you {attempts} attempts to guess the number.',
    },
    'title': {
        'ja': '|             数あてゲーム             |',
        'en': '|        Guess The Number Game         |',
    },            
    'ranking_header': {
        'ja': '★ランキング',
        'en': 'RANKING',
    },                            
    'table_header': {
        'ja': '順位　スコア　名前　　　　　　試行数　要素数 (設定した範囲)',
        'en': 'RANK   SCORE  NAME          ATTEMPTS    SIZE (SET RANGE)',
    },                                                             
    'prompt_show_description': {
        'ja': '\n遊び方の説明を見ますか？[y/N]：',
        'en': '\nWould you like to see HOW TO PLAY? [y/N]: ',
    },          
    'game_description': {
        'ja': '★遊び方：\nあなたが設定する２つの整数の間にある数から、\nコンピュータがランダムに１つを選びます。\nコンピュータが選んだ数を当てられたら、あなたの勝ちです。\n',
        'en': 'HOW TO PLAY:\nFirst, you set two integers.\nThe computer will then randomly choose an integer\n between the range you set.\nYou win if you guess the correct number.\n',
    },                                
    'game_example': {
        'ja': '★例：\nあなたが設定した数：2, 10\nコンピュータが選べる範囲：2, 3, 4, 5, 6, 7, 8, 9, 10\nコンピュータが選んだ数：7\n正解となる入力：7\n不正解となる入力：7以外の数\n',
        'en': 'EXAMPLE:\nYour set integers: 2, 10\nThe computer can choose from: 2, 3, 4, 5, 6, 7, 8, 9, 10\nThe computer chose number: 7\nCorrect input: 7\nIncorrect input: any number other than 7\n',
    },                
    'game_start': {
        'ja': '\nそれでは、始めましょう！',
        'en': '\nLet\'s get started!',
    },
    'prompt_set_player_name': {
        'ja': 'ランキング用の名前を入力してください：',
        'en': 'Please enter a player name for the ranking: ',
    },         
    'registration_completed': {
        'ja': 'ランキングへの登録が完了しました。\n',
        'en': 'Registration to the ranking has been completed.\n',
    },            
    'prompt_confirm_retry': {
        'ja': '\nもう一度ゲームをやりますか？[Y/n]：',
        'en': '\nWould you like to play again? [Y/n]: ',
    },
    'goodbye': {
        'ja': '遊んでくれてありがとう(*\'ω\'*)また遊んでね！'  ,
        'en': 'Thanks for playing! Play again! :)',
    },        
    'prompt_set_range': {
        'ja': '整数を２つ入力してください（例：2, 10）：',
        'en': 'Please input two integers (e.g. 2, 10): ',
    },                            
    'show_set_range': {
        'ja': 'あなたが設定した範囲は [{small} 〜 {large}] です。\n',
        'en': 'The range you set is [{small} - {large}].\n',
    },
    'prompt_guess': {
        'ja': 'コンピュータが選んだ整数は何でしょう？：',
        'en': 'What integer did the computer choose?: ',
    },
    'invalid_range_exceed': {
        'ja': '入力に誤りがあります。設定された範囲 [{small} 〜 {large}] を超えています。\n',
        'en': 'Invalid input. Your input exceeds the range [{small} - {large}].\n',
    },
    'guess_smaller': {
        'ja': '残念！もっと　▲大きい数▲　です。\n',
        'en': 'Ooops! The correct number is LARGER.\n',
    },
    'guess_larger': {
        'ja': '残念！もっと　▼小さい数▼　です。\n',
        'en': 'Ooops! The correct number is smaller.\n',
    },
    'correct_answer': {
        'ja': '正解です！おめでとう！＼(^o^)／\n',
        'en': 'Correct! Congratulations! 🎉\n',
    },
    'show_score': {
        'ja': '今回のスコアは {current_score} です。\n',
        'en': 'Your score this time is {current_score}.\n',
    },    
    'congrats_top5': {
        'ja': 'すごいです！TOP5に入りました！\n',
        'en': 'Amazing! You made the Top 5!\n',
    },
    'invalid_input': {
        'ja': '入力に誤りがあります。\n',
        'en': 'Invalid input.\n',
    },        
    'keyboard_interrupt': {
        'ja': '\nゲームを中断しました。また遊んでね！(*\'ω\'*)',
        'en': '\nThe game has been interrupted. Play again! :)',
    },
}

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
                        # print('ランキングデータが破損しているため、初期データを使用します。')
                        print(get_message('load_data_invalid'))

                # print('ランキングデータの読込みが完了しました。')
                print(get_message('load_data_completed'))
            
            except FileNotFoundError:
                # print('ランキングデータが見つからないため、初期データを使用します。')
                print(get_message('load_data_not_found'))


        def get_message(key, **kwargs):
            global current_language
            message_template = messages.get(key, {}).get(current_language, '')
            if not message_template:
                return f'[Missing translation for "{key}"]'
            return message_template.format(**kwargs)


        def select_language():
            global current_language
            print('Select your language:')
            print('1. 日本語 (Japanese)')
            print('2. English')
            user_input = input('Enter your choice (1 or 2): ')
            if user_input == '2':
                current_language = 'en'
            else:
                current_language = 'ja'


        def save_top5():
            with open('top5.json', 'w') as file:
                json.dump(top5, file)
                if debugmode:
                    print('[DEBUG] Top5 data has been saved as file.')


        def show_title():
            print('----------------------------------------')
            print(get_message('title'))
            print('----------------------------------------')


        def validate_load_data(data):
            data_sorted = sorted(data, key=lambda x: (-x[2], x[1]))
            for idx, (range, attempts, score, user_name) in enumerate(data_sorted[:5]):
                f'{(idx + 1):>4}　{score:>6}　{user_name:<10}　{attempts:>10}　{(range[1] - range[0] + 1):>6} ({range[0]} 〜 {range[1]})'


        def show_ranking():
            # print('★ランキング')
            # print('順位　スコア　名前　　　　　　試行数　要素数（設定した値の範囲）')
            print(get_message('ranking_header'))
            print(get_message('table_header'))


            top5_sorted = sorted(top5, key=lambda x: (-x[2], x[1]))
            for idx, (range, attempts, score, user_name) in enumerate(top5_sorted[:5]):
                print(f'{(idx + 1):>4}　{score:>6}　{user_name:<10}　{attempts:>10}　{(range[1] - range[0] + 1):>6} ({range[0]} 〜 {range[1]})')


        def initialize_game():
            select_language()
            load_top5()
            show_title()
            show_ranking()

            # user_input = input('\n遊び方の説明を見ますか？[y/N]：')
            user_input = input(get_message('prompt_show_description'))

            if user_input.lower() == 'debugmode':
                global debugmode
                debugmode = True
                print('[DEBUG] Debugmode enabled!')

            elif user_input.upper() == 'Y':
                print(get_message('game_description'))
                print(get_message('game_example'))


            # print('それでは、始めましょう！\n')
            print(get_message('game_start'))
           

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
            # user_input = input('ランキングに載せる名前を入力してください。')
            user_input = input(get_message('prompt_set_player_name'))

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
            # print('ランキングへの登録が完了しました。\n')
            print(get_message('registration_completed'))

            if debugmode:
                print('\n[DEBUG] After limiting top5')
                print(top5)

            show_ranking()
            confirm_retry()


        def confirm_retry():
            # user_input = input('\nもう一度ゲームをやりますか？[Y/n]：')
            user_input = input(get_message('prompt_confirm_retry'))

            if user_input == '' or user_input.upper() == 'Y':
                set_range()

            else:
                save_top5()
                # print('遊んでくれてありがとう(*\'ω\'*)また遊んでね！')
                print(get_message('goodbye'))
                exit(0)


        def set_range():
            while True:
                # user_input = input('整数を２つ入力してください（例：2, 10）：')
                user_input = input(get_message('prompt_set_range'))

                try:
                    range_values = list(map(int, user_input.split(',')))
                    range_values.sort()
                except ValueError:
                    # print('入力が間違っています。整数を２つ入力してください。\n')
                    print(get_message('invalid_input'))
                    set_range()
                    continue

                if len(range_values) == 2:
                    small, large = range_values
                    # print('あなたが設定した範囲は ' + str(range_values[0]) + ' 〜 ' + str(range_values[1]) + ' です。\n')
                    print(get_message('show_set_range', small = range_values[0], large = range_values[1]))

                    target = random.randint(range_values[0], range_values[1])
                    if debugmode:
                        print('[DEBUG] The computer chose: ' + str(target))

                    attempts = 0
                    def ask_guess():
                        nonlocal attempts
                        while True:
                            # user_input = input('コンピュータが選んだ数は何でしょう？：')
                            user_input = input(get_message('prompt_guess'))

                            try:
                                guess = int(user_input.strip())
                            except ValueError:
                                # print('入力が間違っています。整数を入力してください。\n')
                                print(get_message('invalid_input'))
                                continue
                            
                            if guess < small or guess > large:
                                # print('範囲（' + str(small) + ' 〜 ' + str(large) + '）より小さい数です。入力しなおしてください。\n')
                                print(get_message('invalid_range_exceed', small = small, large = large))

                            # elif guess > large:
                            #     # print('範囲（' + str(small) + ' 〜 ' + str(large) + '）より大きい数です。入力しなおしてください。\n')
                            #     print(get_message('invalid_range_exceed', small = small, large = large))

                            elif guess < target:
                                attempts += 1
                                # print('残念！もっと　▲大きい数▲　です。\n')
                                print(get_message('guess_smaller'))

                            elif guess > target:
                                attempts += 1
                                # print('残念！もっと　▼小さい数▼　です。\n')
                                print(get_message('guess_larger'))

                            elif guess == target:
                                attempts += 1
                                # print('正解です！おめでとう！＼(^o^)／\n')
                                print(get_message('correct_answer'))
                                print(get_message('show_attempts', attempts = attempts))
                                current_score = get_score(range_values, attempts)

                                # print('今回のスコアは ' + str(current_score) + ' でした。')
                                print(get_message('show_score', current_score = current_score))

                                if chceck_top5(range_values, attempts, current_score):
                                    # print('おめでとう！TOP5に入りました！')
                                    print(get_message('congrats_top5'))
                                    player_name = set_player_name()
                                    set_ranking(range_values, attempts, current_score, player_name)
                                
                                confirm_retry()


                    ask_guess()
                    break

                else:
                    # print('入力が間違っています。整数を２つ入力してください。\n')
                    print(get_message('invalid_input'))
                    continue

        
        initialize_game()
        set_range()
    
    except KeyboardInterrupt:
        save_top5()
        # print('\nゲームを中断しました。また遊んでね！')
        print(get_message('keyboard_interrupt'))
