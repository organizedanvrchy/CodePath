# Write a function that takes in two strings and returns True if the second string is a substring of the first, and False otherwise.
# NOTE: You may not use the in operator (Python) or call a library function that tests for substrings, such as substring() or indexOf() (Java).

def substr(s1: str, s2: str) -> bool:
    # If s2 is longer than s1, then it is not a substring.
    if len(s2) > len(s1):
        return False

    # Iterate through loop for valid positions where s2 can fit into s1
    # then slice to compare sections of s1 with s2
    for i in range(len(s1) - len(s2) + 1):
        if s1[i:i + len_s2] == s2:
            return True

    return False
