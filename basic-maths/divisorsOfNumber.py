import math
def divisorsOfNumber(num):
    divisors= []
    # brute force approach
    # for i in range(1, num):
        # if num%i ==0:
        #     divisors.append(i)
    # optimal approach
    for i in range(1, int(math.sqrt(num)+1)):
        if (num%i ==0):
            divisors.append(i)
            if i!= num//i:
                divisors.append(num//i)
    return sorted(divisors);
n= int(input("enter the number"))
print("the divisors of the number are" , divisorsOfNumber(n));   

