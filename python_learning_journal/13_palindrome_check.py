str1 = 'radar'
is_palindrome = str1 == str1[::-1]
print(f'{str1} is a palindrome' if is_palindrome else f'{str1} is not a palindrome')