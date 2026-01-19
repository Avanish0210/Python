def gcd(a,b):
    if a==0 :
        return b
    while(a>0 and b>0):
        if a>b:
            a=a%b
        else:
            b=b%a
    return a

num1 = int(input("Enter the first number :"))
num2 = int(input("Enter the second number :"))
print(gcd(num1,num2))


