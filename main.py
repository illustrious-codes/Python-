# num1 = [1, 9, 1, 6, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 2]
# num2 = []
# for num in num1:
#     if num not in num2:
#         num2.append(num)
# print(num2)


"""def sum(num1):
    num = [8, 2, 3, 0, 7]
    for i in num:
        num1 += i
    return num1
print(sum(0))"""

"""def multiply(num1):
    num = [8, 2, 3, -1, 7]
    for i in num:
        num1 *= i
    return num1
print(multiply(1))"""

"""def reverse():
    r = "1234abcd"
    rn = r[::-1]
    return rn
print(reverse())"""

"""def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
        print(result)
    return result
print(factorial(5))"""

"""def num_range():
    num = int(input("Enter number "))
    if num >= 10 and num <= 20:
        print("You guess right")
    else:
        print("Wrong")
    return "keep it up"
print(num_range())"""

# def count_string_num():
#     string_num = "The quick Brow Fox"
#     uppercase = 0
#     lowercase = 0

#     for i in string_num:
#         if i.isupper():
#             uppercase += 1
#         elif i.islower():
#             lowercase += 1

#     return (f"uppercase {uppercase}, lowercase {lowercase}")
# print(count_string_num())

"""def check():
    num1 = [1,2,3,3,3,3,4,5]
    num2 = []
    for i in num1:
        if i not in num2:
            num2.append(i)
    return num2
print(check())"""

"""def prime_num():
    num = int(input("Enter a prime number "))
    if num % 2 == 1:
        print("This is a PRIME NUMBER")
    else:
        print("This is not a PRIME NUMBER")
    return (f"The input number is {num}")
print(prime_num())"""

def even_num():
    num = int(input("Enter a even number "))
    if num % 2 == 0:
        print("This is a EVEN NUMBER")
    else:
        print("This is not a EVEN NUMBER")
    return (f"The input number is {num}")
print(even_num())