list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_ = list_numbers[0]

for current_pos, current_value in enumerate(list_numbers):
    if current_value > max_:
        max_ = current_value
        max_pos = current_pos

list_numbers[max_pos], list_numbers[-1] = list_numbers[-1], list_numbers[max_pos]

print(list_numbers)

