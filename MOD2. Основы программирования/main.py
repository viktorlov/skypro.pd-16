from players import Player
from utilities import load_random_word

url = 'https://www.jsonkeeper.com/b/Y52Q'


def main():
    codeword = load_random_word(url)
    player_name: str = input('Введите имя игрока: ')
    player = Player(name=player_name)

    print(f'Привет, {player.name}\n'
          f'Составьте {len(codeword.subwords)} слов из слова >> {codeword.word}\n'
          f'Слова должны быть не короче 3 букв\n'
          f'Чтобы закончить игру, угадайте все слова или напишите "stop"\n'
          f'Поехали, ваше первое слово? ')

    while player.get_count_used_words() != len(codeword.subwords):
        stab = input().lower()

        if stab in ("stop", "стоп", "break"):
            break
        elif len(stab) < 3:
            print(f'слишком короткое слово')
        elif stab not in codeword.subwords:
            print(f'неверно')
        elif player.check_word(stab):
            print(f'уже использовано')
        else:
            player.add_used_word(stab)
            print(f'Верно')

    statistics = len(player.used_words)
    print(f'Игра завершена, вы угадали {statistics} слов!')


if __name__ == '__main__':
    main()
