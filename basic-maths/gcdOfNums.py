# def gcdOfNums(list):

#     # optimal approach using inbuilt function

#     from math import gcd
#     result = list[0]
#     for i in range(1, len(list)):
#         result = gcd(result, list[i])
#     return result
# n = int(input("Enter number of elements in the list: "))
# arr = []    
# for i in range(n):
#     ele = int(input())
#     arr.append(ele) 
# print("GCD of the given numbers is:", gcdOfNums(arr))

# optimal approach without using inbuilt function
def gcdSub(a,b):
    while a != b:
        if a <b:
            b = b-a
        else:
            a= a-b
    return a
def gcdOfNums(list):
    result = list[0]
    for num in list[1:]:
        result = gcdSub(result, num)
    return result
n = int(input("Enter number of elements in the list: "))
arrayOfNums= []
for i in range(n):
    ele = int(input())
    arrayOfNums.append(ele)
print("GCD of the given numbers is:", gcdOfNums(arrayOfNums))