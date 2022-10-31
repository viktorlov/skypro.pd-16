from pin import check_pin

print("Введите ваш ПИН-код")
user_input = input()

if check_pin(user_input):
    print("Такой ПИН-код подходит")
else:
    print("Такой ПИН-код НЕ подходит")
