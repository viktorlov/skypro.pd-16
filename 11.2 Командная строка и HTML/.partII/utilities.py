def load_candidates_from_json() -> list[str]:
    import json
    with open('candidates.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def get_all() -> list[str]:
    return load_candidates_from_json()


def get_candidate(arg: int) -> str | bool:
    for each in get_all():
        if each['pk'] == arg:
            return each
    return False


def get_candidates_by_name(arg: str) -> list[str]:
    return [_ for _ in load_candidates_from_json() if arg.lower() in _['name'].lower()]


def get_candidates_by_skill(arg: str) -> list[str]:
    return [_ for _ in load_candidates_from_json() if arg.lower() in _['skills'].lower().split(', ')]


if __name__ == '__main__':
    print(load_candidates_from_json())
    print(get_all())
    print(get_candidate(1))
    print(get_candidate(10))
    print(get_candidates_by_name('Adela'))
    print(get_candidates_by_name('qwerty'))
    print(get_candidates_by_skill('python'))
    print(get_candidates_by_skill('go'))
    print(get_candidates_by_skill('qwerty'))
