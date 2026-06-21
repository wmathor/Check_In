num = int(input("Enter a number: "))
original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

if original == reverse:
    print(f"{original} is a palindrome number.")
else:
    print(f"{original} is NOT a palindrome number.")
