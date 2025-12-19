# Q1:Write a function that takes a list as input and prints the length of the list.
cities = ["new york", "washington", "berlin", "madrid","barcelona"]
nums = [2, 13, 14, 16, 20, 25, 30]

def print_lists(list):
    print(len(list))

print_lists(cities)
print_lists(nums)


#Q2:Write a Python function that takes a list as input and prints all its elements.
cities = ["new york", "washington", "berlin", "madrid","barcelona"]
nums = [2, 13, 14, 16, 20, 25, 30]

def print_len(list):
    print(len(list))
def print_list(items):
    for item in items:
        print(item, end=" ")


print_list(cities)   


#Q :Write a Python function that returns the maximum number from a list without using built in functions.
def find_max(nums):
    max_num = nums[0]
    for n in nums:
        if n > max_num:
            max_num = n
    return max_num

print(find_max([3, 9, 1, 7]))
