def find_max(list_of_numbers):
    maximum = list_of_numbers[0]
    for number in list_of_numbers:
        if number > max:
            maximum = number
    return maximum

