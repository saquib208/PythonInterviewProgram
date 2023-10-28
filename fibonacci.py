def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Test
print(fibonacci(6))  # Output: 8 (Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, ...)

print(list(map(fibonacci,range(8))))