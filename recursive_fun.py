def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0:
        return 1  # The factorial of 0 is 1
    elif n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage:
num = int(input("Enter a non-negative integer: "))
result = factorial(num)
print("The factorial of", num, "is:", result)
