def fibonacci(n):
    return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)

for i in range(10):
    print(fibonacci(i), end=' ')
print()