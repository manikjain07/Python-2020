def findDivisors(num):
    DivisorsList = []
    for numbers in range(1,num):
        if num%numbers == 0:
            DivisorsList.append(numbers)
    return DivisorsList

Number1,Number2 = map(int,input().split(" "))
Number1DivisorsList = list(findDivisors(Number1))
Number2DivisorsList = list(findDivisors(Number2))

if (sum(Number1DivisorsList) == Number2 and sum(Number2DivisorsList) == Number1):
    print(f"{Number1} {Number2}")
# else:
#     print("No Friendship!")

# print(findDivisors(Number1))
# print(findDivisors(Number2))
# print(sum(findDivisors(Number1)))
# print(sum(findDivisors(Number2)))
# print(Number1DivisorsList)
# print(Number2DivisorsList)
# print(sum(Number1DivisorsList))
# print(sum(Number2DivisorsList))