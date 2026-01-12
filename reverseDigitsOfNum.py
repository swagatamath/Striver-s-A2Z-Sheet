# brute force approach
def reverseNumber(num):
    # using slicing
    # num = str(num)
    # rev = num[-1::-1]
    # Mathematical approach
    rev =0
    sign = -1 if num < 0 else 1
    num = abs(num)
    while num>0:
        rem = num % 10
        rev = rev * 10 + rem
        num = num // 10
    return rev*sign
n = int(input("Enter a number you want to reverse: "))
print("Reversed Number is:", reverseNumber(n))