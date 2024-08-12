# def sort(name:list[str], height:list[str]) -> list[str]:
#     dic ={}
#     for i in range(len(name)):
#         for j in range(len(height)):
#             if i == j:
                
#                 dic[name[i]] =   height[j]

#                 # print([height[j]])
#                 print([name[i]] )
#     # while dic[name[i]] is height[j]:
#     while dict[i+1] < arr[i] and i>0:
#         arr[i+1],arr[i]=arr[i],arr[i+1]
#         i+1
#     #     if dic[name[i]]
        
#     return dic

# print(sort(["Mary","John","Emma"], [180,165,170]))

print("hello")

arr = [5,3,2,7,0,1,5,3,2,1,9]
min_val = min(arr)
max_val =max(arr)
# print(min_val)
# print(max_val)
len_of_el =max_val-min_val+1
# print(len_of_el)
count =[0] * len_of_el

print(count)
for num in arr:
    count[num-min_val] +=1
   

# print(count)# [1, 2, 2, 2, 0, 2, 0, 1, 0, 1]
# arr = [5,3,2,7,0,1,5,3,2,1,9]
for i in range(1, len(count)):
    count[i] += count[i - 1]

print(count)#[1, 3, 5, 7, 7, 9, 9, 10, 10, 11]
# # then len(arr) - 1 means the last unsorted element up to -1 means up to -1 we reverse sorting  -1

for i in range(len(arr) - 1, -1, -1):
    count[arr[i] - min_val] -= 1
print(count)