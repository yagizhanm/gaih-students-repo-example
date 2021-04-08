
#Question 1

my_list = [1,2,3,4,5,6,7,8,9,10] # Program is coded so that choice of the list does not matter.However,it's better to choose len(my_list) = 2k, where k = {0,1,...}. i.e,the number of elements are even.
x=0
k = int(len(my_list)/2) # Getting the half-length.
l=k # Needed extra variable.
while x < k: # Changing one by one up to the half-length k.
    my_list[x], my_list[l] = my_list[l], my_list[x]
    x += 1
    l += 1
print(my_list)

# Question 2 : 

l = int(input("Please give me a positive integer number n : "))
while l < 0 : #Being sure that l is a non-negative integer.
    print("You have to put a positive number")
    l = input("Please give me a positive integer number n : ")
x = 0
while x <= l: # Printing the even integer values from 0 up to (including) l by a simple while loop.
    print(x)
    x += 2
