
def check_numbers(a,b,c):
    if a>0 and b>0 and c>0:
        print("All numbers are positive.")
    elif a<0 or b<0 or c<0:
        print("At least one number is negative.")
    elif a==0 and b==0 and c==0:
        print("All numbers are zero.")
    elif a==0 or b==0 or c==0:
        print("At least on number is zero.")

a,b,c = input("Enter three numbers folowed by comma: ").split(",")
check_numbers(int(a),int(b),int(c))
