# Q1: Print numbers from 1 to 100.
i = 1
while i <= 100:
    print(i)
    i +=1

# Q2: Print numbers from 100 to 1.
i = 100
while i >= 1:
    print(i)
    i -= 1

# Q3: Print the multiplication of a number 3.
i = 1
while i<=10:
    print(3*i)
    i += 1

# Q4: Print the elements of the following list using loop.
nums = [1, 4, 7, 13, 16, 18, 24, 34, 36]

idx = 0
while idx < len(nums):
    print(nums[idx])
    idx +=1

#Another one:
heroes = ["ironman", "superman", "batman", "spiderman"]

idx = 0
while idx < len(heroes):
    print(heroes[idx])
    idx += 1


# Q5: search for a number x in this tuple using loop.
nums = (1, 4, 7, 13, 16, 18, 24, 34, 36)
x = 18
i=0
while i < len(nums):
    if (nums[i] == x):
        print(i)
    i += 1

