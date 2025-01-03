def squre(number:int)->int:
    return number*number

number = int(input("Enter the number to find the squre: "))
print(squre(number))

def reverse(string:str)->str:
    return string[::-1]

string = input("Enter the string to reverse: ")
print(reverse(string))

def length(variable:any)->int:
    try:
        length = len(variable)
        return length
    except:
        return 0
    
variable = input("Enter the variable to find the length: ")
print(length(variable))

def vovel_counter(string:str)->int:
    vovels = ['a','e','i','o','u']
    counter = 0
    for i in string:
        if i in vovels:
            counter +=1
    
    return counter

string = input("Enter the string to count the vovels: ")
print(vovel_counter(string))
