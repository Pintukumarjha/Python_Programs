a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))


for i in range(2,min(a,b)+1):
    if(a%i==0 and b%i==0):
        print("Numbers are not coprime")
        break
else:
    print("Numbers are coprime")
