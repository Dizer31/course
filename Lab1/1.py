numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

sum_a_ = sum([item for item in numbers if item != None]) / len(numbers)
numbers[4] = sum_a_
# TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:", numbers)
