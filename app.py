import sys

print('----------------------------------------')
print('| Guess The Number Game - 数当てゲーム |')
print('----------------------------------------')

user_input = input('整数を２つ入力してください（例：2, 10）：')
# print(user_input)

range_values = list(map(int, user_input.split(',')))
range_values.sort()

if len(range_values) == 2:
    print('あなたが設定した範囲は ' + str(range_values[0]) + ' 〜 ' + str(range_values[1]) + ' です。')

else:
    print('入力が間違っています。整数を２つ入力してください。')