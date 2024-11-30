# Check if a String is a Palindrome
def is_palindrome(s):
    return s == s[::-1]

# Example usage:
print(is_palindrome('racecar'))  # Output: True
print(is_palindrome('hello'))    # Output: False