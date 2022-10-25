from morse_encode import morse_encode
from get_word import get_word
from print_statistics import print_statistics

word_list = ['snake', 'rainbow', 'twin', 'fish', 'moon']
# шпаргалка #
for word in word_list:
    print(word, morse_encode(word))

*tries, = range(5)
input('Сегодня мы потренируемся расшифровывать азбуку Морзе\nНажмите Enter и начнем\n')
answers = []
for each in tries:
    word_to_code = get_word(word_list)
    code_of_word = morse_encode(word_to_code)
    user_try = input(f'Слово {each + 1} {code_of_word}   ')
    if user_try == word_to_code:
        print(f'Верно!\n')
        answers.append(True)
    else:
        print(f'Неверно! Это {word_to_code}\n')
        answers.append(False)
print_statistics(answers)
