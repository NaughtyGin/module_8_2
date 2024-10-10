def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    try:
        for i in range(len(numbers)):
            if isinstance(numbers[i], int):
                result += numbers[i]
            else:
                incorrect_data += 1
                print(f'Некорректный тип данных для подсчёта суммы: "{numbers[i]}".')
    except TypeError:
        # print('Я в except функции personal_sum')
        if isinstance(numbers, int):
            incorrect_data += 1
    finally:
        return result, incorrect_data

def calculate_average(numbers):
    try:
        result, incorrect_data = personal_sum(numbers)
        avg_res = result / (len(numbers) - incorrect_data)
    except TypeError:
        print('В numbers записан некорректный тип данных')
        avg_res = None
    except ZeroDivisionError:
        # print('Я в except функции calculate_average: деление на 0')
        avg_res = 0
    return avg_res


print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
print(f'Результат 5: {calculate_average([])}')