# def sum_dict_value(d):
#     d = {"a":21, "b":32, "c":24, "d":25, "e":64}
#     return sum(d.values())
# print(sum_dict_value("d"))

# def swap_element():
#     names = ("goodness", "sade", "bola", "Tade")
#     names = list(names)
#     names[0] = "Illustrious"
#     names[3] = "Oluwatade"
#     return names
# print(swap_element())

# def filter_tuples():
#     num = (1, 2, 3, 4, 5, 6, 7, 8, 9)
#     nums = list(num)
#     num1 = 0
#     if (nums % 2 == 0):
#         num1.append(nums)
#     print(num1)
# print(filter_tuples())


#WEEK 3 ASSIGNMENT
my_list = [1, 2, 3, 6, 10]
my_tuple = tuple(my_list)
print(my_tuple)


tuple1 = (1, 2)
tuple2 = (3, 4)
concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple)


def reverse_tuple(input_tuple):
    return input_tuple[::-1]
original_tuple = (1, 2, 3, 4, 5)
reversed_tuple = reverse_tuple(original_tuple)
print(reversed_tuple)


def tuple_length(input_tuple):
    return len(input_tuple)
my_tuple = (1, 2, 3, 4, 5)
print(tuple_length(my_tuple))



my_tuple = (10, 20, 30)
a, b, c = my_tuple
print("a:", a)
print("b:", b)
print("c:", c)


def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()
    merged_dict.update(dict2)  
    return merged_dict
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged = merge_dicts(dict1, dict2)
print(merged)


my_dict = {"a": 1, "b": 2}
value_of_b = my_dict["b"]
print(value_of_b)


def key_exists(dictionary, key):
    return key in dictionary
my_dict = {"a": 1, "b": 2, "c": 3}
key_to_check = "b"
if key_exists(my_dict, key_to_check):
    print(f"The key '{key_to_check}' exists in the dictionary.")
else:
    print(f"The key '{key_to_check}' does not exist in the dictionary.")


my_dict = {"a": 1, "b": 2}
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")



def swap_keys_and_values(input_dict):
    swapped_dict = {value: key for key, value in input_dict.items()}
    return swapped_dict
original_dict = {"a": 1, "b": 2, "c": 3}
swapped = swap_keys_and_values(original_dict)
print(swapped)


def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None
numerator = 10
denominator = 0
result = safe_divide(numerator, denominator)
if result is not None:
    print("Result:", result)



def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except (ZeroDivisionError, TypeError):
        print("Error: Division by zero is not allowed, or wrong types were provided.")
        return None
result1 = divide_numbers(10, 0)
result2 = divide_numbers(10, '2') 
print("Result 1:", result1)
print("Result 2:", result2)



class NonPositiveIntegerError(Exception):
    pass

def check_positive_integer(n):
    if not isinstance(n, int) or n <= 0:
        raise NonPositiveIntegerError("Input must be a positive integer.")
def process_input(input_value):
    try:
        check_positive_integer(input_value)
        print("Input is a positive integer.")
    except NonPositiveIntegerError as e:
        print(e)
process_input(5)
process_input(0)
process_input(-10)    
process_input("abc")  


def safe_access(dictionary, key, default_value):
    return dictionary.get(key, default_value)
my_dict = {"a": 1, "b": 2, "c": 3}
result1 = safe_access(my_dict, "b", 0)
print("Result 1:", result1)
result2 = safe_access(my_dict, "d", 0)
print("Result 2:", result2) 



def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None
    finally:
        print("This code always executes.")
result1 = divide_numbers(10, 2)
print("Result 1:", result1)
print()
result2 = divide_numbers(10, 0)
print("Result 2:", result2)
