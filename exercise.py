### Exercises: Level 1
##
#1. Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py
#2. Write a python comment saying 'Day 2: 30 Days of python programming'
#3. Declare a first name variable and assign a value to it
#4. Declare a last name variable and assign a value to it
#5. Declare a full name variable and assign a value to it
#6. Declare a country variable and assign a value to it
#7. Declare a city variable and assign a value to it
#8. Declare an age variable and assign a value to it
#9. Declare a year variable and assign a value to it
#10. Declare a variable is_married and assign a value to it
#11. Declare a variable is_true and assign a value to it
#12. Declare a variable is_light_on and assign a value to it
#13. Declare multiple variable on one line

## answers:
first_name="sneha"
last_name="Banik"
full_name="Sneha Banik"
country="India"
city="sambalpur"
age=20
year=2026
is_married=False
is_true=True
is_light_on=True
name, age, subject = "Sneha", 20, "Python"

print(name)
print(age)
print(subject)
print(first_name)
print(last_name)
print(full_name)
print(country)
print(city)
print(age)
print(year)
print(is_married)
print(is_true)
print(is_light_on)



### Exercises: Level 2

#1. Check the data type of all your variables using type() built-in function
#2. Using the _len()_ built-in function, find the length of your first name
#3. Compare the length of your first name and your last name
#4. Declare 5 as num_one and 4 as num_two
#5. Add num_one and num_two and assign the value to a variable total
#6. Subtract num_two from num_one and assign the value to a variable diff
#7. Multiply num_two and num_one and assign the value to a variable product
#8. Divide num_one by num_two and assign the value to a variable division
#9. Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
#10. Calculate num_one to the power of num_two and assign the value to a variable exp
#11. Find floor division of num_one by num_two and assign the value to a variable floor_division
#12. The radius of a circle is 30 meters.
 #   1. Calculate the area of a circle and assign the value to a variable name of _area_of_circle_
  #  2. Calculate the circumference of a circle and assign the value to a variable name of _circum_of_circle_
   # 3. Take radius as user input and calculate the area.
#13. Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
#14. Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords


first_name="sneha"
last_name="Banik"
full_name="Sneha Banik"
country="India"
city="sambalpur"
age=20
year=2026
is_married=False
is_true=True
is_light_on=True
name, age, subject = "Sneha", 20, "Python"

print(type(name))
print(type(age))
print(type(subject))
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(len(first_name))
num_1=5
num_2=4
sum=num_1+num_2
dif=num_2-num_1
mul=num_1*num_2
div=num_1/num_2
rem=num_1%num_2
pow=num_1**num_2
floor_division=num_1//num_2
print(num_1)
print(num_2)
print(sum)
print(dif)
print(mul)
print(div)
print(rem)
print(pow)
print(floor_division)
radius=30
area=3.14*radius*radius
cir=2*3.14*radius
print(area)
print(cir)
rad=int(input("enter the radius:"))
area_user=3.14*rad*rad
print(area_user)
name=input("enter your first name:")
last_name=input("enter ur last name:")
age=int(input("enter the age:"))
country=input("enter ur country:")
print(name)
print(last_name)
print(age)
print(country)
help('keywords')
print("day 2 completed")