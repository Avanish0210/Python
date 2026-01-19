print("Hello world")
if(5>2):
    print("five is grester than two")
x=2
y="hello python"
#strings are array
#this is comment
print(x)
print(y)
print("Hello" , end=" ")
print("world")
print(2*5)
print("i am " , 25 , "years old")
#if you want to specify the data type of a veriable is done by casting
a = str(3)
b = int(9)
print(type(x))
print(type(y))
print(type(a))
print(type(b))
#unpacking the values from a list or a touple 
fruits = ["apple" , "banana" , "orange"]
c , d , e = fruits
print(c,d,e)

# function
def myfun():
    print("The value of X is",x)

myfun()
#x is a global variable but what if you want to delare a global variable inside a function or modify a variable globally use global keyword

def func():
    global x 
    x = 55
    print("The change in x is " , x)

func()

#complex number . complex number always written with "j" , here j is imaginary part
f = -2j
print(f)
#you can convert from one type to another data type with the  int() , float() , complex() methods
import random
print(random.randrange(0,10))
g="banana"
for x in g:
    print(x)

print(bool(15))
thislist = ["apple" , " banana" , "kiwi" , "mango"]
newlist = [x for x in thislist ]
print(newlist)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, *yellow, red) = fruits

print(green)
print(yellow)
print(red)
print(5 and 0  , 0 or 5)



num = 12
rev = (num % 10)*10 + (num//10)


print(num)
print(18//4) #gives in int
print(format(10.32245 , ".2f"))  #10.32
num = 2e3
print(type(num)) #float
print(46%10)

num = 12.86
print(format(num,".0f"))

L1=[10,20,30,40,50,60]
print(L1[-1])  #print the last element of the list 60
print(L1[1])   #print 20
print(L1[2:5]) #[30, 40, 50]
print(L1[:5])  #[10, 20, 30, 40, 50]
print(L1[2:])  #[30, 40, 50, 60]
print(L1[-4:-1]) #[30, 40, 50]
print(L1[0:5:2]) #[10, 30, 50]
print(L1[::-1])  #[60, 50, 40, 30, 20, 10]  including and reverse
print(L1[:-1])   #[10, 20, 30, 40, 50]
print(L1[-1:0:-1]) #[60, 50, 40, 30, 20]

print(abs(45))
print(10//2)






