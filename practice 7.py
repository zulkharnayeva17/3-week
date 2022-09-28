#example 1
def printChar(S):
    print (S)
sim = input('enter character: ')
printChar(sim)
printChar(' *')


#example 2
x=int(input('enter the number:\n '))
print('initial value\n ', x)
def pr():
    global x
    x=pow(x,10)
    print( 'changed value\n', x)
pr()


#task 0
#1
import math
def s(x,y,z):
    p=(x+ y+ z)/2 
    s=math.sqrt(p*(p-x)* (p-y) * (p-z))
    return s
A=[]
for i in range (3):
    print ('введите стороны', i, '-го треугольника:' )
    a=int(input('a: '))
    b=int(input('b: '))
    c=int(input('c: '))
    A.append(s(a,b,c))
for i in range (3) :
    print('Площадь', i, '-го треугольника {:.2f} '. format(A[i]))
if A[0] == A[1]:
    if A[0] == A[2]:
        print ('Треугольники равновеликие' )
else: print ('Треугольники не равновеликие')



#task 1
#1
def calculate_area(name):
     if name == "rectangle":
      a = int(input("Enter rectangle's length: "))
      b = int(input("Enter rectangle's breadth: "))
      rectangle_area = a * b
      print(f"The area of rectangle is", rectangle_area )

     elif name == "square":
      s = int(input("Enter square's side length: "))
      sqt_area = s**2
      print(f"The area of square is " , sqt_area)

     elif name == "triangle":
      a = int(input("Enter triangle's height length: "))
      b = int(input("Enter triangle's breadth length: "))
      triangle_area = 0.5 * b * a
      print(f"The area of triangle is" ,  triangle_area)

     elif name == "circle":
      r = int(input("Enter circle's radius length: "))
      pi = 3.14
      circ_area = pi * r * r
      print("The area of circle is " , {circ_area})
     else:
      print("Sorry! This shape is not available")


if __name__ == "__main__" :
   print("Calculate Shape Area")
   shape_name = input("Enter the name of shape whose area you want to find: ")
   calculate_area(shape_name)

 #2

import random
def sum(n):
    sum = 0
    for i in n:
        sum += i
    return sum

def mean(n,sum):
    return sum/len(n)

for i in range(3):
    a = random.sample(range(100), 15)
    print(a)
    print(sum(a))
    print(mean(a,sum(a)))



#task 2

#1
import math
def s(a):
    s=(3*math.sqrt(3)* a**2)/2
    return s
print('enter the length of side a')
a=int(input('a:'))
print('The area of a regular hexagon: ' , s(a))


#2

def s(a,b):
    s=a*b
    return s
A=[]
for i in range(3):
    print('enter the data of ', i, 'rectangle')
    a=int(input('a: '))
    b=int(input('b: '))
    A.append(s(a,b))
for i in range(3):
    print('the area of ', i, ' rectangle is ', A[i])





#task 3
#1
import math  
katet1_1 = int(input("Length of the first side of the first triangle:"))
katet2_1 = int(input("Length of the second side of the first triangle:"))
katet1_2 = int(input("Length of the first side of the second triangle:"))
katet2_2 = int(input("Length of the second side of the second triangle:"))
gip1 = math.sqrt(katet1_1 ** 2 + katet2_1 ** 2)
gip2 = math.sqrt(katet2_2 ** 2 + katet2_2 ** 2)
print('hypotenuse of the first triangle:',  gip1)
print('hypotenuse of the second triangle:',  gip2)
if gip1 > gip2:
    print('The hypotenuse of the first triangle is larger')
else: 
    print('The hypotenuse of the second triangle is larger')


#2
def sortS(a):
    return ''.join(sorted(a))
     
a=input('enter the any word')
print(sortS(a))


#Task_4

#1
from fractions import Fraction
a,b = 4,3
c,d = 8,9
ir_fr = Fraction(Fraction(a,b), Fraction(c,d))
print("The irreducible fraction: ", ir_fr)
def gcd(a, b):  
    if a > b: s = b  
    else: s = a  
    for i in range(1, s + 1):  
        if((a%i==0)and(b%i==0)):  
            gcd = i  
    print(gcd)
gcd(ir_fr.numerator, ir_fr.denominator)

#2
x = 1;
y = 1;
p1,p2 = 0,4
f1,f2 = 3,2
n1,n2 = 1,2
radius = 3
def point_in(px, py, radius, x, y):
    if ((x-px)**2+(y-py)**2)<=radius**2:
        print("Point is inside if the circle!")
    else:
        print("Point is outside of the circle!")
point_in(p1,p2,radius,x,y)
point_in(f1,f2,radius,x,y)
point_in(n1,n2,radius,x,y)


#task 5
#1
from fractions import Fraction
a,b = 4,3
c,d = 8,9
ir_f = Fraction(Fraction(a,b) - Fraction(c,d))
print("The irreducible fraction: ", ir_f)
def gcd(a, b):  
    if a > b: s = b  
    else: s = a  
    for i in range(1, s + 1):  
        if((a%i==0)and(b%i==0)):  
            gcd = i  
    print(gcd)
gcd(ir_f.numerator, ir_f.denominator)

#2
def div(a):
    for i in range(1, a+1):
        if a%i==0:
            print(i, end=" ")
        else: continue
n = int(input("Input the number: "))
div(n)

#task 6
#1
def gcd(a, b):  
    if a > b: s = b  
    else: s = a  
    for i in range(1, s + 1):  
        if((a%i==0)and(b%i==0)):  
            gcd = i  
    return gcd
def lcm(a, b):
    lcm = (a*b)/gcd(a,b)
    print(lcm)
a = int(input("Input the 1st number: "))
b = int(input("Input the 2nd number: "))
print(gcd(a,b))
lcm(a,b)

#2
a = float(input("First side: "))
b = float(input("Second side: "))
c = float(input("Third side: "))
d = float(input("Fourth side: "))
dia = float(input("Diagonal: "))
def quadl(a,b,c,d,dia):
    def heron_f(a,b,c):
        p=0.5*(a+b+c)
        return (p*(p-a)*(p-b)*(p-c))**0.5
    return heron_f(a,b,dia) + heron_f(c,d,dia)
print("The area of a quadliteral is: ", quadl(a,b,c,d,dia))

#task 7
#1
def triangleArea(base,height):
    return (height * base) / 2
def rectangleArea(length,width):
    return length * width

a = int(input("long base: "))
b = int(input("short base: "))
h = int(input("height: "))
t = int(input("leg: "))

print("Area:", triangleArea(a-b,h) + rectangleArea(b,h))



#2


def octal(n):
    on = [0] * 100
    i = 0
    while (n != 0):
        on[i] = n % 8
        n = int(n / 8)
        i += 1
    for j in range(i - 1, -1, -1):
        print(on[j], end="")
n = int(input('Enter the int: '))
octal(n)

#8 task 

#1

def div(n):
    ans = []
    for i in range(1,n+1):
        s = str(i)
        temp = True
        for j in s:
            if int(j) == 0:
                temp = False
            elif i % int(j) != 0:
                temp = False
        if temp:
            ans.append(i)
    return ans

n = int(input("n: "))
print(div(n))


#2

def swapFirstLast(a):
    a[0],a[len(a)-1] = a[len(a)-1],a[0]
    return a

m = int(input("length of array: "))
A = []
for i in range(m):
    n = int(input("element of array: "))
    A.append(n)

print(A)
print(swapFirstLast(A))


#9 task 
#1
def Digits(n):
    s = str(n)
    sum = 0
    for i in s:
        sum += int(i)
    return sum
n = int(input("Please enter the number: "))
sub = Digits(n)
ans = 0
while n > 0:
    ans += 1
    n -= sub
print(ans)

#2
import random
def sumArr(n):
    sum = 0
    for i in n:
        sum += i
    return sum

def meanArr(n,sum):
    return sum/len(n)

def prdArr(n):
    prd = 1
    for i in n:
        prd *= i
    return prd

for i in range(3):
    a = random.sample(range(100), 15)
    print(a)
    print(prdArr(a))
    print(meanArr(a,sumArr(a)))


#10 task 
    #1
    
def digits(n):
    ans = []
    s = str(n)
    for i in s:
        ans.append(int(i))
    return ans

N = int(input("N: "))
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

ans = []
for i in range(100,N):
    dgts = digits(i)
    if a in dgts:
        dgts.remove(a)
    if b in dgts:
        dgts.remove(b)
    if c in dgts:
        dgts.remove(c)
    if len(dgts) == 0:
        ans.append(i)
print(ans)


#2

def word(s):
    s = s.split()[::-1]
    ans = []
    for i in s:
        ans.append(i)
    return ' '.join(ans)

s = input("Enter word to reverse: ")
print(word(s))



# 11 task 
#1
def Twins(n):
    print([[i, i+2] for i in range(n, 2*n - 1)])
    
Twins(int(input('please enter the number' ))) 



#2

from random import randint as rd
def arrmax(arr) :
    amax = arr[0][0]
    n = len(arr)
    for i in range(n) :
        if max(arr[i]) > amax :
            amax = max(arr[i])
    return amax
    
def arrprint(a, b) :
    for i in a :
        print(*i)
    print()
    for i in b :
        print(*i)
    print()
 
print('enter the number of rows for the first matrix: ')
na = int(input())
print('number of elements : ')
ma = int(input())
print('enter the number of rows for the first matrix: ')
nb = int(input())
print('number of elements : ')
mb = int(input())
 
a = [[rd(1,50) for i in range(ma)] for j in range(na)]
b = [[rd(51,100) for i in range(mb)] for j in range(nb)]
 
arrprint(a,b)
 
amax = arrmax(a)
bmax = arrmax(b)
 
for i in range(len(a)) :
    for j in range(len(a[i])) :
        a[i][j] = bmax if a[i][j] == amax else a[i][j]
for i in range(len(b)) :
    for j in range(len(b[i])) :
        b[i][j] = amax if b[i][j] == bmax else b[i][j]
    
arrprint(a,b)


#12 task 
#1
def getSum(value):
    res = 1
    for i in range(2, int(value**0.5) + 1):
        if value % i == 0:
            res += i + value // i
    return res

for i in range(10, 10000):
    sum1 = getSum(i)
    sum2 = getSum(sum1)
    if sum2 == i and sum1 != sum2:
        print(i, sum1)

# 2
import math
def median(a, b, c):

	n = (1 / 2)*math.sqrt(2*(b**2)
+ 2*(c**2)
- a**2)

	return n
a = 6
b = 7
c = 8

ans = median(a, b, c)
print(round(ans, 2))



#task 13
#1
num=int(input("please enter number: "))
for num in range(num, 1000):
    sum1=0
    numcp=num
    if(num>=10 and num<100):
        while(num>0):
            digit=int(num%10)
            d2=digit*digit
            sum1=sum1+d2
            num=int(num/10)

    if(num>=100 and num<1000):
        while(num>0):
            digit=int(num%10)
            d2=digit*digit*digit
            sum1=sum1+d2
            num=int(num/10)
    if(numcp==sum1):
        print("angstrong number: ", sum1)
#2
def acos(x, y) :
    return x  / ((x * x + y * y) ** 0.5)
x1, x2 = map(float,input("enter the coordinaties x1.x2" ).split())
y1, y2 = map(float,input("enter the coordinaties y1, y2").split())
z1, z2 = map(float,input("enter the coordinaties z1, z2" ).split())
res = [x1, x2]
acosx = acos(x1, x2)
acosy = acos(y1, y2)
if acosy > acosx :
    acosx = acosy
    res = [y1, y2]
acosz = acos(z1, z2)
if acosz > acosx :
    acosz = acosz
    res = [z1, z2]
print(*res)
n = 3
res = [tuple(map (float,input().split())) for i in range(n)]
rcos = [acos(*res[i]) for i in range(n)]
k = rcos.index(max(rcos))
print(res[k])

# task 14
#1
import math

def countDividers(n):
    if n <= 0: return 0 
    if n == 1: return 1

    k = 2 
    for i in range(2, round(math.sqrt(n)) + 1): 
        if n % i == 0:
            k += 1 if i == n // i else 2
    return k

def maxDividersCountAtRange(m , n):
    if m > n : m, n = n, m 

    maxDivs = 0 
    numberWithMaxDivs = [] 
    for i in range(m, n): 
        d = countDividers(i)
        if d > maxDivs: 
            maxDivs = d
            numberWithMaxDivs = [] 
        if d == maxDivs:
            numberWithMaxDivs.append(i) 

    return maxDivs, numberWithMaxDivs

print(maxDividersCountAtRange(20,80))

#2
import math
def distance(a, b):
    d = 0
    for i in range(3):
        d += pow((a[i]-b[i]),2)
    return d
 
coordinates=['x','y','z','t']
arr=[]
print("enter the coordinates of the points:")
for i in range(4):
    b=[]
    print("the coordinates of the points:",coordinates[i])
    for j in range(3):
        b.append(int(input()))
    arr.append(b)
 
flag = True
for i in range(3):
    for j in range(i+1, 4):
        dist = distance(arr[i],arr[j])
        if flag or max_dist < dist:
            m1=i
            m2=j
            max_dist = dist 
            flag = False
 
print(f'Maximum distance between points {coordinates[m1]} и {coordinates[m2]}')
print(f' distance = {max_dist**0.5:.3f}')



# task 15
#1
def Palindrome(n: int) -> bool:
    rev = 0
    i = n
    while i > 0:
        rev = rev * 10 + i % 10
        i //= 10
    return (n == rev)
def count(minn: int, maxx: int) -> None:
    for i in range(minn, maxx + 1):
        if Palindrome(i):
            print(i, end = " ")
if __name__ == "__main__":
    count(1, 1000)
#2
import math
def distance(a, b):
    d = 0
    for i in range(3):
        d += pow((a[i]-b[i]),2)
    return d
 
coordinates=['x','y','z','t']
arr=[]
print("enter the coordinates of the points:")
for i in range(4):
    b=[]
    print("the coordinates of the points:",coordinates[i])
    for j in range(3):
        b.append(int(input()))
    arr.append(b)
 
flag = True
for i in range(3):
    for j in range(i+1, 4):
        dist = distance(arr[i],arr[j])
        if flag or min_dist > dist:
            m1=i
            m2=j
            min_dist = dist 
            flag = False
 
print(f'Minimum distance between points {coordinates[m1]} и {coordinates[m2]}')
print(f' distance = {min_dist**0.5:.3f}')


