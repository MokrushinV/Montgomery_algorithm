from monty import monty_multiply, monty_pow


def console_interface():
    while True:
        print("\nВыберите операцию:")
        print("1.Умножение Монтгомери (x * y mod N)")
        print("2.Возведение в степень Монтгомери (x^k mod N)")
        print("3.Выход")

        choice = input("Введите номер действия (1-3): ").strip()

        if choice == '3':
            print("Программа завершена")
            break

        if choice not in ('1', '2'):
            print("Ошибка: Неверный пункт меню.")
            continue

        try:
            N = int(input("Введите НЕЧЕТНЫЙ модуль N (N > 2): "))

            if choice == '1':
                x = int(input("Введите число x: "))
                y = int(input("Введите число y: "))
                res = monty_multiply(x, y, N)
                print(f"\n[Ответ]: {x} * {y} mod {N} = {res}")
                print(f"[Проверка]: {x} * {y} % {N} = {x * y % N}")

            elif choice == '2':
                x = int(input("Введите основание x: "))
                k = int(input("Введите степень k (k >= 0): "))
                res = monty_pow(x, k, N)
                print(f"\n[Ответ]: {x} ^ {k} mod {N} = {res}")
                print(f"[Проверка]: {x} ^ {k} mod {N} = {pow(x, k, N)}")

        except ValueError as err:
            print(f"\n[ОШИБКА]: {err}")

if __name__ == "__main__":
    console_interface()