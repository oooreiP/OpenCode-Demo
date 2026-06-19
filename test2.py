def find_biggest_number(numbers_list):
    if not numbers_list:
        return None  # Or raise an error, depending on desired behavior for empty lists
    return max(numbers_list)