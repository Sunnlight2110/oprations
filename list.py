import random
list = [random.choice([i for i in range(0,100)]) for i in range(0,10)]
print("list: ",list)

print("adding the element at the end of the list")
list.append(11)#add the element at the end of the list
print("list: ",list)

print("inserting the element at the given index")
indx,value = input("Enter the index and value followed by comma to insert: ").split(",")
list.insert(int(indx),int(value))#insert the value at the given index
print("list: ",list)

print("removing the element from the list")
rm_element = int(input("Enter the element to remove: "))
list.remove(rm_element)#remove the element from the list
print("list: ",list)

print("length of list: ",end=" ")
print(len(list))#return the length of the list

print("index of the element")
index = int(input("Enter the index to see: "))
print(list[index])#return the value at the given index

print("reversed list")
print(list[::-1])#reverse the list

print("sorted list")
sorted_list = sorted(list)#sort the list
print(sorted_list)

print("max value from the list:",end=" ")
max = 0
for i in list:#return the maximum value from the list
    if i>max:
        max = i
print(max)

print("removing the last element from the list")
list.pop()#remove the last element from the list
print("list: ",list)

print("If number is in the list or not")
user_input = int(input("Enter the number to find if number is in the list or not: "))
if user_input in list:
    print("Number is in the list.")#number is in the list
else:
    print("Number is not in the list.")#number is not in the list

print("concatenating the list")
list2 = [i for i in range(0,10)]
print("list1: ",list)
print("list2: ",list2)
list+=list2#concatenate the list
print("list: ",list)