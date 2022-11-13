from random import randint
from typing import List
def get_unique_list_numbers() -> List[int]:
    list_ = [] #список, в который будут помещаться уникальные числа
    while len(list_) < 15: # ограничиваю размер списка
        random_num = randint(-10, 10) #генерация случайного числа
        if random_num not in list_: #проверяю, что это число не содержится в списке
            list_.append(random_num) #если ОК, добавляю это число в список
    return list_


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
