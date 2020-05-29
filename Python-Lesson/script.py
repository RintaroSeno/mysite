# coding:utf-8
answers = ['はい', 'いいえ']
index = 0

for answer in answers:
    print(str(index) + '.' + answer)
    index += 1
input_answer = int(input('勉強は好きですか？番号で答えてください：'))
if input_answer == 0:
    print('素晴らしいですね！')
else :
    print('私もです')
