def calculator(a:int,b:int):
    print("a: ",a)
    print("b: ",b)
    print("Addition: ",a+b)
    print("Subtraction: ",a-b)
    print("Multiplication: ",a*b)
    print("Division: ",a/b)

def oprations(a:int,b:int):
    print("a: ",a)
    print("b: ",b)
    print("equal to: ",a==b)
    print("not equal to: ",a!=b)
    print("greater than: ",a>b)
    print("less than: ",a<b)
    print("greater than or equal to: ",a>=b)
    print("less than or equal to: ",a<=b)

a,b = input("Enter two numbers folowed by comma: ").split(",")
calculator(int(a),int(b))
oprations(int(a),int(b))