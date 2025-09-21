# Program to check if a number is a palindrome

# Take input from user
num = int(input("Enter a number: "))

# Reverse the number
temp = num
rev = 0

while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10

# Check if palindrome
if num == rev:
    print(f"{num} is a Palindrome.")
else:
    print(f"{num} is NOT a Palindrome.")