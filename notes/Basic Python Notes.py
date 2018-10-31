'''

print("Hello World!")
print()
# This is a comment. I can write whatever I want
# Here and it won't do anything about it.
# It has no effect on the code.
print()  # This adds extra spaces on the terminal
print("This will print here. Notice the spacing.")

a = 4
b = 3
print(a + b)
print(a * 5)
print(5 - 3)
print(6 / 5)  # Results in a float (with decimals)


print("Figure this out")
print(6 // 4)  # Results in a integer (Without decimals)
print(12 // 3)
print(9 // 4)


# MORE MATH STUFF

# Variables

car_name = "The Wiebe Mobile"
car_type = "Tesla"
car_cylinders = 1024
car_miles_per_gallon = 0.01
print("I have a car called %s. It's pretty nice." % car_name)

# Input
name = input("What is your name? ")
print("Hello %s" % name)

'''
# function
def printhelloworld():
    print("helloworld")
'''
thhis is a multi-line comment
I can type anywhere
if here:
'''

printhelloworld()
'''
this is a multi-line comment 
I csn type anywhere here.
'''
# f(x) = 2x + 3
def f (x):
    print (2*x +3 )


f(1)
f(5)
f(5000)

        # Loop
for i in (1,2,3):
    printhelloworld()
    print()
for i in range(1000000) :
    printhelloworld()


for i in range (5):
    printhelloworld()
print()
for i in range (5): # rang starts at 0 and goes to 4
    f(i)

for i in range (5):
    print(i**2)


a = 0
# while loops
while a < 10:
    print(a)
    a += 1 # this is the same thing as a = a+ 1


'''
Hints with loops:
for loops - use when you don't know how many iterations
whike loops - Use when you Don't know how many interations
'''

# Random numbers
import random  # this shold always be on line 1
print (random.randint (0' 100)

# Control Statement
def grade_calc (percentage) :
    if (percentage) >= 90:
        return "A"
    elif percentage >= 80:
        return "b"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    elif:
        return "F"



    print (grade_calc(82))



    print (grade_calc(82))

