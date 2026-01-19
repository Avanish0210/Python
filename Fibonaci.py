def fb(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return fb(num-1) + fb(num-2)
    

num = int(input("Enter the number :"))
print("the numth term of fib series is ",fb(num))
