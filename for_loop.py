end_number = int(input("Enter the end number: "))

print("Foor loop:")
for i in range(0, end_number+1):
    print(i)

print("-"*50)
print("While loop:")
i = 0
while i <= end_number:
    print(i)
    i +=1
    
print("-"*50)
print("Even or odd:")
for i in range(0, end_number+1):
    if i%2 == 0:
        print(i, " is even.")
    else:
        print(i, " is odd.")