def find_palindrome(s: str) -> bool:
    cleaned_s = "".join(char for char in s.lower() if char.isalnum())
    return cleaned_s == cleaned_s[::-1]