def find_largest_number(numbers):
    if not numbers:
        return None
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

# Example usage:
# my_list = [10, 5, 20, 15, 25]
# largest_num = find_largest_number(my_list)
# print(f"The largest number is: {largest_num}")