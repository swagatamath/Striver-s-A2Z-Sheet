def armstrongNum(num):
    length = len(str(num))
    sum = 0
    while num > 0:
        armSum = (num%10)**length
        sum = sum + armSum
        num = num//10
    return sum
n = int(input("Enter a number you want to check for Armstrong: "))
if armstrongNum(n) == n:
    print("The number is an Armstrong number")
else:
    print("The number is not an Armstrong number")