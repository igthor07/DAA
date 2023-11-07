#Write a program to calculate GCD of Given Two Numbers.
def calculate_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate GCD
gcd = calculate_gcd(num1, num2)

# Output
print(f"The GCD of {num1} and {num2} is {gcd}")

