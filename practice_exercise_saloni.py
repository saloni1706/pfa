#Exercise1
#Question 1 and 2
print(7+10) #Addition
#Mathematical operations
#Question3
print (5+5) #addition
print (5-5) #substraction
print (3*5) #Multiplication
print (10/2) #Divisiom
print (18%7) #Modulus
print (4**2) # (4^2 i.e. 4 has a power of 2 )
#Simple Interest Question 4
#when the values are given in advance
I = 5000
R = 7/100
T = 5
SI = I*R*T #(Simple interst)
print (SI)
print ('Total amount in account is', (I + SI))

#Using input function
Investment = input('Enter the amount invested')
rate = input ('Enter the rate')
Time = input ('Enter time')
I = float(Investment)
R = float(rate)
T = float(Time)
SI =I*R*T
print ("Simple interest is", SI)
print ('Total amount in account is', (I + SI))
#question 5
I = 8000
R = 8.7/100
Interest = 4872
print ("Time taken by the orginal amount to earn 4,872 as interest will be", Interest/(R*I),"years")
#QUestion 6
Investment=3000
Time= 4
Interest =768
print ("The rate at which the amount gives 768 as an interest is", (Interest*100)/(Investment*Time))
#question 7
I=100
R=10/100
T=7
print("The amount received after 7  years will be", (I*(1+R)**T))
#Exercise 2
#Question1
savings =100
print(type(savings))
#Question2
growth_multiplier = 1.1
Time = 7
result = (savings*(1+growth_multiplier)**Time)
print (result)
#question3
desc = "compound interest"
profitable = True
#question4
A = 10.7
B = "This is python course"
C = False
print(type(A))
print(type(B))
print(type(C))
#question5
savings=100
growth_multiplier = 1.1
Time = 7
year1 = (savings*(1+growth_multiplier)**Time)
print (year1)
#The printing type of year1 can be float
print(type(year1)desc = "compound interest"
doubledesc = (desc+desc)
print(doubledesc)
#Yes, We were told during classes that string varaibles can be added in this way and in the output variables would be added in the form of sentence.

#question6
savings=100
growth_multiplier = 1.1
Time = 7
result = (savings*(1+growth_multiplier)**Time)
r = float(result)
print("I started with $", savings, "and now I have $", result, "Awesome!")

#Question7
#Defining of pi_string
pi_string = "3.1415926"
#COnverting string to float
pi_float = float(pi_string)
double_pi = 2*(pi_float)
print(double_pi)

#question8
#I think their would be an error in statement 2,3 and 4. But when we print them we get output for for all the statments and error is incured only in 3 statemnet.
print("I can add integers, like "+ str(5) + "to strings.")
print("I said" + ("Hey" *2)+"Hey!")
print(True+False)
print("The correct answer to thid multiple choice exercise is answer number" + 2)

#Exercise 3
#Question1
number = input("enter the number")
n = float(number)
if (n%2==0):
    print ("The number is even")
else:
    print("The number is odd")

#Question2
Temperature = input("enter the tempertature in Centrigate")
TC= float(Temperature)
TF= (TC*9/5)+32
print( "The temperature in fahrenheit is", TF)

#question3
import math
SideA = input ("Enter first side of triangle")
SideB = input ("Enter Second side of triangle")
SideC = input ("Enter third side of triangle")
A = float (SideA)
B = float (SideB)
C = float (SideC)
s = (A+B+C)/2
Area = math.sqrt(s*(s-A)*(s-B)*(s-C))
print(" The area of triangle is", Area)

#Question4
radius = input("Enter the radius of circle")
r= float(radius)
import math
print('pi is', math.pi)
C = 2*3.14*r
print(" The circumference of circle is", C)
A = 3.14*(r**2)
print("The area of circle is", A)
