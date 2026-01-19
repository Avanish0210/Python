def dectobin(num):
    if num==0:
        return 0
    else:
        dectobin(num//2)
        print(num%2 , end = ' ')
num = int(input("Enter the number :"))
print(dectobin(num ))
