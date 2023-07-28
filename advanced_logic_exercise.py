# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:

evens = [num for num in numbers if (num % 2) == 0]
print(evens)

# 2. Print the difference between the largest and smallest value:

print(max(numbers)-min(numbers))

# 3. Print True if the list contains a 2 next to a 2 somewhere.

# last_num = None
# for num in numbers:
#     if num == 2 and last_num == 2:
#         print('True')
#     else: last_num = num

x = 0
while x < len(numbers)-1:
    if numbers[x] == numbers[x+1] == 2:
        print('True')
    x += 1


# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22

x = 0
flag = False
sum = 0
while x <= len(numbers)-1:
    if flag == False:
        if numbers[x] == 6:
            flag = True
        else:
            sum += numbers[x]
    else:
        if numbers[x] == 7:
            flag = False
    x += 1
print(sum)

# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 

x = 0
flag = False
sum = 0
while x <= len(numbers)-1:
    if flag == False:
        if numbers[x] == 13:
            flag = True
        else:
            sum += numbers[x]
    else:
        flag = False
    x += 1
print(sum)






