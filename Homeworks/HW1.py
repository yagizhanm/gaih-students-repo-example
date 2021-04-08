
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
