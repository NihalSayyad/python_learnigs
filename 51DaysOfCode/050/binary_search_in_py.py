import time

def linear_search(numbers, number_to_find):
    for index, element in enumerate(numbers):
        if element == number_to_find:
            return index

    return -1

def binary_search(numbers, number_to_find):
    left_index = 0
    mid_index = 0
    last_index = len(numbers) - 1

    while left_index <= last_index:
        mid_index = (left_index + last_index) // 2
        mid_number = numbers[mid_index]

        if mid_number == number_to_find:
            return mid_index

        if mid_number < number_to_find:
            left_index = mid_index + 1
        else:
            last_index = mid_index - 1

    return -1

def binary_search_recursive(number_list, number_to_find, left_index, right_index):
    mid = (left_index + right_index + 1) // 2
    if number_to_find == number_list[mid]:
        return mid

    if number_to_find < number_list[mid]:
        right_index = mid-1
        return binary_search_recursive(number_list, number_to_find, left_index, right_index)

    if number_to_find > number_list[mid]:
        left_index = mid + 1
        return binary_search_recursive(number_list, number_to_find, left_index, right_index)

    return -1


if __name__ == "__main__":
    numbers = [12, 15, 17, 19, 21, 24, 45, 67, 68, 69, 72, 74, 78, 79, 81, 88, 89, 90, 91, 93, 95, 96, 99, 100]
    number_to_find = 100
    t1 = time.time()
    index = linear_search(numbers, number_to_find)
    print(f"Number found at index {index} using linear search in {time.time() - t1} time")

    t1 = time.time()
    index = binary_search(numbers, number_to_find)
    print(f"Number found at index {index} using binary search in {time.time() - t1} time")

    t1 = time.time()
    right_index = len(numbers) - 1
    index = binary_search_recursive(numbers, number_to_find, 0, right_index)
    print(f"Number found at index {index} using binary search in {time.time() - t1} time")