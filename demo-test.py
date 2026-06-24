def is_palindrome(s: str) -> bool:
    """
    Checks if a given string is a palindrome.
    A string is a palindrome if it reads the same forwards and backwards.
    This function performs a case-sensitive check.
    """
    return s == s[::-1]