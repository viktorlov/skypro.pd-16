import utils


def TESTS():
    query = 'SELECT `show_id`, `title`, `release_year`, `description` FROM netflix LIMIT 5 '
    print(*utils.db_connect('netflix.db', query), sep='\n')
    assert type(utils.db_connect('netflix.db', query)) == list, 'error utils.db_connect type'

    # print(utils.get_movie_by_title('heroes'))
    # assert type(utils.get_movie_by_title('heroes')) == dict, 'error utils.get_movie_by_title type'

    # print(*utils.get_movies_by_years(2001, 2003), sep='\n')
    # assert type(utils.get_movies_by_years(2001, 2003)) == list, 'error utils.get_movies_by_years type'

    # print(*utils.get_movies_by_genre('dramas'), sep='\n')
    # assert type(utils.get_movies_by_genre('dramas')) == list, 'error utils.get_movies_by_genre type'

    # print(utils.get_cast_located_with_2_actors('Rose McIver', 'Ben Lamb'))
    # assert type(utils.get_cast_located_with_2_actors('Rose McIver', 'Ben Lamb')) == list, 'error utils.get_cast_located_with_2_actors type'
    # print(utils.get_cast_located_with_2_actors('Jack Black', 'Dustin Hoffman'))
    # assert type(utils.get_cast_located_with_2_actors('Jack Black', 'Dustin Hoffman')) == list, 'error utils.get_cast_located_with_2_actors type'

    # print(*utils.get_movies_by_multiple('movie', 2013, 'dramas'), sep='\n')
    # assert type(utils.get_movies_by_multiple('movie', 2013, 'dramas')) == list, 'error utils.get_movies_by_multiple'

    # print(*utils.get_movies_by_category('children'), sep='\n')
    # assert type(utils.get_movies_by_category('children')) == list, 'error utils.get_movies_by_category type'


if __name__ == '__main__':
    TESTS()
