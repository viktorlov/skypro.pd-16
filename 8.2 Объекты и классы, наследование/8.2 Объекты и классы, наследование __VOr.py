import json
from random import shuffle


class Question:

    def __init__(self, text, difficulty, correct_answer, is_asking=False, user_answer=None):
        self.text = text
        self.difficulty = difficulty
        self.correct_answer = correct_answer
        self.is_asking = is_asking
        self.user_answer = user_answer
        self.cost = 10 * int(self.difficulty)

    def __repr__(self):
        return f'class Question'

    def get_points(self):
        """
        Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
        """
        return self.cost

    def is_correct(self):
        """
        Возвращает True, если ответ пользователя совпадает с верным ответом, иначе False.
        """
        return str(self.correct_answer) == str(self.user_answer)

    def build_question(self):
        """
        Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность: 4/5
        """
        # return ['Вопрос: ' + str(self.text), 'Сложность: ' + str(self.difficulty) + '/5']
        return [f'Вопрос: {str(self.text)}', f'Сложность: {str(self.difficulty)}/5']

    def build_feedback(self):
        """
        Возвращает:
        Ответ верный, получено __ баллов
        либо
        Ответ неверный, верный ответ __
        """
        return f'Ответ верный, получено {self.cost} баллов' \
            if self.correct_answer == self.user_answer \
            else f'Ответ неверный, верный ответ {self.correct_answer}'


with open('questions.json', encoding='utf8') as file0:
    issues = json.load(file0)

shuffle(issues)


def list_creation(arg: list) -> list:
    return [(Question(arg[_]["q"], arg[_]["d"], arg[_]["a"], False, None)) for _ in range(len(arg))]


questions = list_creation(issues)

for i in range(len(questions)):
    print("")
    print(*questions[i].build_question(), sep='\n')
    stab = input('Введите ответ: ')
    questions[i].user_answer = stab
    questions[i].is_asking = True
    print(questions[i].build_feedback())


def statistics_processing(arg: list):
    correct_ = [arg[_].is_correct() for _ in range(len(arg))]
    points_ = [arg[_].get_points() for _ in range(len(arg)) if arg[_].is_correct()]
    print(f"""
----------------------------------------
Вот и всё!
Отвечено на {correct_.count(True)} вопроса из {len(arg)}
Набрано {sum(points_)} баллов
----------------------------------------
""")


statistics_processing(questions)
