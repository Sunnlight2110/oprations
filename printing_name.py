import string,time
name = input("Enter your name: ")
alphabet = string.ascii_letters

namelist = []
for i in name:
    for j in alphabet:
        if i == j:
            namelist.append(j)
        print( ''.join(namelist),end="")
        if ''.join(namelist) == name:
            break
        print(j)
        time.sleep(0.05)
        
            
    

