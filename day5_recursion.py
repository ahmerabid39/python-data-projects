#Q1:Write a recursive function to calculate the sum of first natural numbers.
def calc_sum(n):
    if(n == 0):
        return 0
    return calc_sum(n-1) + n

sum = calc_sum(5)
print(sum)


#Q2:Write a recursive function to print all elements in a list.
fruits = ["mango", "apple", "banana", "watermelon"]

def print_list(list, idx=0):
    if (idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)

print_list(fruits)
    