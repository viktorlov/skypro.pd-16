def load_candidates() -> list[str]:
    import json
    with open('candidates.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def get_all() -> list[str]:
    return load_candidates()


def get_by_pk(arg: int) -> str:
    for each in get_all():
        if each['pk'] == arg:
            return each
    return False


def get_by_skill(arg: str) -> list[str]:
    return [_ for _ in load_candidates() if arg in _['skills'].lower()]


if __name__ == '__main__':
    print(load_candidates())
    print(get_all())
    print(get_by_pk(1))
    print(get_by_pk(10))
    print(get_by_skill('python'))
    print(get_by_skill('pUthon'))
