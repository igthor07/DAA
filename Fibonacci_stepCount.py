def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        step_count = 1
        for _ in range(2, n + 1):
            step_count += 1
            a, b = b, a + b
        return b, step_count

n = int(input("Enter the value of n: "))
result, steps = fibonacci(n)
print(f"The {n}-th Fibonacci number is: {result}")
print(f"Number of steps taken to calculate: {steps}")
