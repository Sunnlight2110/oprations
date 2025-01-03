def sum_of_all_numbers(number:int)->int:
    sum = 0
    for i in range (0,number+1):
        sum += i
    return sum

number = input("Enter the number to find the sum of all numbers: ")
print(sum_of_all_numbers(int(number)))

def piramid(number:int)->None:
    for i in range (0,number):
        for j in range(0,i+1):
            print("*",end="")
        print("")

number = input("Enter the number to print the piramid: ")
piramid(int(number))