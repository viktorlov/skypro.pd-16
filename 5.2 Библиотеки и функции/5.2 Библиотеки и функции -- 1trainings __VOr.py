### 4 ###


def hours_to_days(hours, period=24):
    return hours // period


# print(hours_to_days(48))  # Вернет 2
# print(hours_to_days(12))  # Вернет 0
# print(hours_to_days(36, 12))  # Вернет 3


### 5 ###


def get_distance(fuel, consumption=20):
    return fuel / consumption


# print(get_distance(100)) # Вернет 5.0
# print(get_distance(200)) # Вернет 10.0
# print(get_distance(100, 20)) # Вернет 5.0
# print(get_distance(100, 50)) # Вернет 2.0
# print(get_distance(200, 50)) # Вернет 4.0


### 6 ###


def count_sucessful(students, score=50):
    return sum(1 if students[each] >= score else 0 for each in range(len(students)))


# print(count_sucessful([])) # Возвращает 0
# print(count_sucessful([50, 50])) # Возвращает 2
# print(count_sucessful([20, 20])) # Возвращает 0
# print(count_sucessful([40, 40], 40)) # Возвращает 2
# print(count_sucessful([80, 40])) # Возвращает 1
# print(count_sucessful([80, 40], 40)) # Возвращает 2
# print(count_sucessful([60, 60], 90)) # Возвращает 0


### 11 ###


def lost_time(*args):
    return sum(list(args))


# print(lost_time(1, 2, 3))  # Вернет 6
# print(lost_time(3, 3, 3, 3))  # Вернет 12
