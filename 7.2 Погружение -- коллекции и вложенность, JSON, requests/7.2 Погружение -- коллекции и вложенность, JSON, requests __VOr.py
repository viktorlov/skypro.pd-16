import json
from datetime import datetime

with open('questions.json', encoding='utf8') as file0:
    questions = json.load(file0)


def do_asking(arg_cate, arg_cost, arg_ques=questions):
    """
    Превращает пару "категория-стоимость" в отвеченную

    :param arg_cate: категория вопроса
    :type arg_cate: str
    :param arg_cost: стоимость вопроса
    :type arg_cost: str
    :param arg_ques: словарь вопросов
    :type arg_ques: dict
    """
    arg_ques[arg_cate][arg_cost]['asked'] = True


def not_asked(arg_dict=questions):
    """
    Возвращает словарь, в котором: ключи -- это категория вопроса, значение -- список незаданных вопросов.

    :param arg_dict: словарь questions
    :type arg_dict: dict
    :return: словарь: ключ -- категория, значение -- список ответов
    :rtype: dict[str, list[str]]
    """
    category_cost_ = dict()
    for key_, subdict_ in arg_dict.items():
        values_ = [k_ if not v_['asked'] else '' for k_, v_ in subdict_.items()]
        category_cost_[key_] = values_
    return category_cost_


def show_tableau(arg_dict):
    """
    Печатает таблицу с неотвеченными вопросами.

    :param arg_dict: словарь not asked questions
    :type arg_dict: dict
    """
    for key_, value_ in not_asked(arg_dict).items():
        print("{:<16} {:<10} {:<10} {:<10}".format(key_, *value_))


def check_string_format(arg, length=7, element=2):
    """
    Проверяем строку за соответствие условиям: длина, число элементов

    :param arg: строка для проверки
    :type arg: str
    :param length: минимальная длина строки
    :param element: число элементов строки
    :return: True/False соответствует или нет строка условиям
    :rtype: bool
    """
    sign_ = (len(arg) >= length) * \
            (len(arg.split(" ")) == element) * \
            (not arg.startswith(' ')) * \
            (not arg.endswith(' '))
    return sign_


def check_string_occurrence(arg_str, arg_dict=questions):
    """
    Проверяем строку на вхождение категории и цены в неотвеченные вопросы

    :param arg_str: строка для проверки
    :type arg_str: str
    :param arg_dict: словарь для проверки
    :type arg_dict: dict
    :return: True/False входит или нет пара (категория/цена) в неотвеченные вопросы
    :rtype: bool
    """
    category_ = arg_str.split()[0].strip().title()
    cost_ = arg_str.split()[1].strip()
    sign_ = cost_ in not_asked(arg_dict).get(category_, "")
    return sign_


def user_request():
    """
    Запрашивает у пользователя категорию и цену вопроса.

    :return: возвращает категорию и цену
    :rtype: tuple[str, str]
    """
    category_, cost_ = None, None

    while True:
        string_ = input('Выберете категорию и (через пробел) стоимость вопроса: ')
        if check_string_format(string_) and check_string_occurrence(string_):
            category_ = string_.split()[0].strip().title()
            cost_ = string_.split()[1].strip()
            break
        else:
            print(f"Такого вопроса нет, попробуйте еще раз!\n")
            continue
    return category_, cost_


def get_question(arg_cate, arg_cost, arg_dict=questions):
    """
    Возвращает вопрос и ответ

    :param arg_cate: категория вопроса
    :type arg_cate: str
    :param arg_cost: стоимость вопроса
    :type arg_cost: str
    :param arg_dict: словарь questions
    :type arg_dict: dict
    :return: кортеж (вопрос; ответ)
    :rtype: tuple[str, str]
    """
    question_ = arg_dict[arg_cate][arg_cost]['question']
    correct_answer_ = arg_dict[arg_cate][arg_cost]['answer']
    return question_, correct_answer_


def round_qa(arg_ques,
             arg_corr_answ,
             arg_cost,
             arg_score=0,
             arg_win=0,
             arg_los=0):
    """
    Возвращает стоимость выигрыша/проигрыша

    :param arg_ques: вопрос
    :param arg_corr_answ: правильный ответ
    :param arg_cost: стоимость вопроса
    :param arg_score: текущий счёт (по умолчанию в начале игры == 0)
    :param arg_win: правильных ответов (по умолчанию в начале игры == 0)
    :param arg_los: неправильных ответов (по умолчанию в начале игры == 0)
    :type arg_ques: str
    :type arg_corr_answ: str
    :type arg_cost: str
    :type arg_score: int
    :type arg_win: int
    :type arg_los: int
    :return: текущий скоринг: счёт, win, los
    :rtype: list [int, int, int]
    """
    print(f'Слово {arg_ques} в переводе означает... ')
    stab = input().lower()
    if stab == arg_corr_answ:
        arg_score += int(arg_cost)
        arg_win += 1
        print(f'Верно! Это правильный ответ! \nПриз: {int(arg_cost)}. Счет: {arg_score}.')
    else:
        arg_score -= int(arg_cost)
        arg_los += 1
        print(f'Неверно! Правильный ответ: {arg_corr_answ}\nПриз: {-1 * int(arg_cost)}. Счет: {arg_score}.')
    scoring_ = [arg_score, arg_win, arg_los]
    return scoring_


def writing_scoring(arg_scoring):
    """
    Запись скоринга прошедшей игры во внешний json-файл

    :param arg_scoring:
    :type arg_scoring: list [int, int, int]
    """
    with open('overall_results.json', 'r') as file1:
        results = json.load(file1)
    current_dict = {'game': str(len(results) + 1),
                    'datetime': str(datetime.now()),
                    'scoring': {'points': str(arg_scoring[0]),
                                'correct': str(arg_scoring[1]),
                                'incorrect': str(arg_scoring[2])}}
    results[len(results) + 1] = current_dict
    with open('overall_results.json', 'w') as file1:
        json.dump(results, file1)

# ------------------------------------------------------------------------------
# начало основной программы






# ------------------------------------------------------------------------------
# if __name__ == '__main__':
#     print(77 * '-', end='\n\n')
#     print(not_asked(questions))
#     show_tableau(questions)
#     print(get_question(category, cost))
#     print(round_qa('apple', 'яблоко', '100'))
