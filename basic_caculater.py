def add(P,Q):
    return P+Q
def subtract(P,Q):
    return P-Q
def multiply(P,Q):
    return P*Q  
def divide(P,Q):
    return P/Q
print("Please select the operation you want to perform:")
print("A. Add")
print("B. Subtract")
print("C. Multiply")
print("D. Divide")
choice=input("Enter your choice (A/B/C/D): ")
num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
if choice=='A':
    print(num1,"+",num2,"=", add(num1,num2))
elif choice=='B':
    print(num1,"-",num2,"=", subtract(num1,num2))
elif choice=='C':
    print(num1,"*",num2,"=", multiply(num1,num2))
elif choice=='D':
    print(num1,"/",num2,"=", divide(num1,num2))
else:
    print("Invalid input")