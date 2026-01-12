import math
def primeNumber(num):
    division= False;
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            division = True
            break
    if division == False:
        return True
    else:
        return False
n = int(input("enter to check whetehr number is prime"))
if primeNumber(n) == True:
    print("the number is prime")
else:
    print("the number is not prime")

            