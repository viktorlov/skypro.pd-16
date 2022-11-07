from random import shuffle, choice
import json


def shuffle_word(word):
    word = list(word)
    shuffle(word)
    return ''.join(word)


print("Введите ваше имя")
user_name = input("Пользователь: ")

with open("words.txt") as file:
    words = file.readlines()
words = [x.strip() for x in words]

score = 0

for _ in range(len(words)):
    word_to_scramble = choice(words)
    scramble_word = shuffle_word(word_to_scramble)
    print(f"Угадайте слово: {scramble_word}")
    attempt = input("")
    if word_to_scramble == attempt:
        print(f"Верно! Вы получаете 10 очков!")
        score += 10
    else:
        print(f"Неверно! Верный ответ – {word_to_scramble}.")

with open('history.json', "r") as f:
    history = json.load(f)
history[user_name] = score
with open('history.json', 'w') as f:
    json.dump(history, f)

print(f"Всего сыграно игр {len(history)}.\nМаксимальный рекорд: {max(list(history.values()))}")
