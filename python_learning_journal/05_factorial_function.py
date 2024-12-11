def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

print(f'Factorial of 5: {factorial(5)}')