# create array 1
array1 = []
# create array 2
array2 = []
# create solution
solution = []
# get the target value
target_value = int(input("What is the target value? "))
# how many number go in the first array
array1_len = int(input("How many numbers go in the first list? "))
# how many number fo in the second array
array2_len = int(input("How many numbers go in the second list? "))
# get first arrays value
for i in range(1, array1_len + 1, 1):
   num_array1 = int(input("number " + str(i) + " in list 1: "))
   array1.append(num_array1)

# get second arrays value

for i in range(1, array2_len + 1, 1):
   num_array2 = int(input("number " + str(i) + " in list 2: "))
   array2.append(num_array2)

# create function
def check(array1, array2, target_value):
# go through first array
   for i in range(0, array1_len, 1):
       # print(i)
# go through second array
       for j in range(0, array2_len, 1):

# check how far the first pair is from the target value is
           if i == 0 and j == 0:
               closest = target_value - array1[i] - array2[j]
               # print(closest)
               the_arr = [array1[i], array2[j]]
# check all the other options
           else:
               check_closest = target_value - array1[i] - array2[j]
               if abs(check_closest) < abs(closest):
                   closest = check_closest
                   the_arr = [array1[i], array2[j]]
               elif abs(check_closest) == abs(closest):
                   the_arr.append(array1[i])
                   the_arr.append(array2[j])
   print(the_arr)
   # print(the_array2)





# go through second array
# compare array
# save values if they are near target value
# create function
# call function with parameters
check(array1, array2, target_value)
