# array =[64, 25, 12, 22, 11]
# size = len(array)#5

# # print(size)
# for i in range(size):
#     # print(i)
#     for j in range(size - i - 1):
#         # print(j)
#         if array[j] > array[j + 1]:
#             array[j], array[j + 1] = array[j + 1], array[j]

# # print(array)

# the above code uses for loop

def bubble(list_a):
    indexing_length = len(list_a) - 1 #Scan not apply comparision starting with last item of list (No item to right)
    sorted = False #Create variable of sorted and set it equal to false
   
    while not sorted:  #Repeat until sorted = True
        sorted = True  # Break the while loop whenever we have gone through all the values
  
    #     for i in range(0, indexing_length): # For every value in the list
    #         if list_a[i+1]>list_a[i]:#"Angled brackets not allowed in Youtube Description :( list_a[i+1]: #if value in list is greater than value directly to the right of it,
    #             sorted = False # These values are unsorted
    #             list_a[i], list_a[i+1] = list_a[i+1], list_a[i] #Switch these values
    # return list_a # Return our list "unsorted_list" which is not sorted.


print(bubble([4,8,1,14,8,2,9,5,7,6,6]))