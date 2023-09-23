# Write a Python function to sum all the numbers in a list.

# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20

# Explanation:
# Summation should like 8+2+3+0+7 = 20

def lst_sum(lst):

    sum = 0
    for i in lst:
        sum += i
    print(f"The sum of all numbers in the list : {sum} ")

lst = [8,2,3,0,7]
lst_sum(lst)