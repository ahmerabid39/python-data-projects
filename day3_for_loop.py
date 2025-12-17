#Q1: print the elements of the following list using a for loop.
list = [12, 15, 14, 23, 45, 67, 34, 46, 25]

for el in list:
    print(el)


#Q2: Search for a number x in this Tuple using for loop.
nums = (12, 15, 14, 23, 45, 67, 34, 46, 25)

x=45
idx = 0
for i in nums:
    if (i == x):
        print(idx)
    idx += 1
    
    
#Q3: Print numbers from 1 to 100.
for i in range(1, 101):
    print(i)


#Q4: Print numbers from 100 to 1.
for i in range(100, 0, -1):
    print(i)


#Q5: Print the multiplication table of a number n.
n = int(input("enter your number: "))

for i in range(1, 11):
    print(n*i)


#Q6: Write a program to find the sum of first natural numbers.
n = 5
fact = 1

for i in range(1, n+1):
    fact *= i

print("factorial=", fact)


#Q7: Write a program to find the factorial of first n numbers. 
n = 5
sum = 0
for i in range(1, n+1):
    sum += i

print("total sum=", sum)
