import re
import unittest

import main
import solution
from tools import SkyproTestCase


class SeasonsTestCase(SkyproTestCase):
    def setUp(self):
        self.student_query = self.get_query_info(main.sqlite_query)
        self.author_query = self.get_query_info(solution.sqlite_query)

    def test_main_has_result(self):
        self.assertTrue(hasattr(main, 'result'),
                        r'%@Проверьте, что переменная result существует')

    def test_result_format_is_correct(self):
        self.assertRegex(
            main.result,
            r'Длительность\sвсех\sсериалов\sрежиссера\sAlastair\sFothergill\s'
            r'составляет\s[0-9]*\sсезона.?\s*$',
            r'%@Проверьте, что используете правильный формат выдачи')

    def test_hours_value_is_correct(self):
        value = int(re.findall(r"\d+", main.result)[0])
        self.assertEqual(
            value, 3,
            (r'%@Проверьте, что количество сезонов посчитано верно.'))

    def test_query_columns_is_correct(self):
        student_columns = self.student_query.get('cursor_info').get('columns')
        author_columns = self.author_query.get('cursor_info').get('columns')
        self.assertEqual(student_columns, author_columns,
                         (r'%@Проверьте, что правильно выбрали'
                          ' колонку в базе данных. '
                          f'Вы выбрали {student_columns}, тогда '
                          f'как необходимо {author_columns}'))

    def test_rows_count_superfluous_condition(self):
        count = self.student_query.get('cursor_info').get('rows_count')
        author_count = self.author_query.get('cursor_info').get('rows_count')
        self.assertFalse(count > author_count,
                         (r'%@Кажется, в запросе имеется лишнее условие.'
                          f'В запросе больше строк ({count}) '
                          f'чем предполагалось {author_count}'))

    def test_rows_count_lack_condition(self):
        count = self.student_query.get('cursor_info').get('rows_count')
        author_count = self.author_query.get('cursor_info').get('rows_count')
        self.assertFalse(count < author_count,
                         (r'%@Кажется, в запросе нехватает условия.'
                          f'В запросе меньше строк ({count}) '
                          f'чем предполагалось {author_count}'))


if __name__ == "__main__":
    unittest.main()
