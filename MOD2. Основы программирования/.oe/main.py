from player import Player
from utils import load_random_word


WORDS_URL = 'https://www.jsonkeeper.com/b/M3WW'


def main():
    """
    Main function. Starts the game and the main loop with conditions.
    Displays game results.
    """
    original_word = load_random_word(WORDS_URL)

    name_player: str = input('Введите имя игрока: ')
    print(f'Привет, {name_player}\n'
          f'Составьте 8 слов из слова >>  {original_word.word}\n'
          f'Слова должны быть не короче 3 букв\n'
          f'Чтобы закончить игру, угадайте все слова или напишите "stop"\n'
          f'Поехали, ваше первое слово? ')

    # Declaring Variables
    player = Player(name_player)
    sub_words = original_word.sub_words

    # Main game loop
    while player.count_words() < original_word.counting_sub_words():
        user_input = input()
        word_check = player.word_check(user_input)

        if user_input.lower() == 'stop' or user_input.lower() == 'стоп':
            break
        elif len(user_input) < 3:
            print(f'слишком короткое слово')
        elif user_input.lower() not in sub_words:
            print(f'неверно')
        elif word_check:
            print(f'уже использовано')
        else:
            player.append_used_word(user_input)
            print(f'Верно')

    # Output of game results
    statistics = len(player.used_words)
    print(f'Игра завершена, вы угадали {statistics} слов!')


if __name__ == '__main__':
    main()
