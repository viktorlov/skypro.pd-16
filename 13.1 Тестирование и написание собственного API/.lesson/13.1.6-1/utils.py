def get_grade(points):
    if type(points) != int: raise TypeError("Должно быть int")
    if points < 0 or points > 100: raise ValueError("Должно быть от 0 до 100")

    if points < 20:
        return 2
    elif points < 40:
        return 3
    elif points < 80:
        return 4
    else:
        return 5
