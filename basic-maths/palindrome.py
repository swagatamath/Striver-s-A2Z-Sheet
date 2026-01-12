def palindrome(num):
    if num < 0:
        return False  # Negative numbers are not palindromes
    rev = 0
    original = num
    while num > 0:
        rem = num % 10
        rev = rev * 10 + rem
        num = num // 10
    return rev == original

n = int(input("Enter a number you want to check for palindrome: "))
if palindrome(n):
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")
