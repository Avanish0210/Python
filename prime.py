def prime(num):
    prime = False
    for i in range(2,num):
        if(num%i==0):
            print("The number is not prime")
            prime = True
            break
    if(prime==False):
        print("the number is prime")
        


num = 9   
prime(num )