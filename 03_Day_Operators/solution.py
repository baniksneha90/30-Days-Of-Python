#1. Declare your age as integer variable
#2. Declare your height as a float variable
#3. Declare a variable that store a complex number
#4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).

#```py
 #   Enter base: 20
  #  Enter height: 10
   # The area of the triangle is 100
#```

#5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).

#```py
#Enter side a: 5
#Enter side b: 4
#Enter side c: 3
#The perimeter of the triangle is 12
#```

#6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
#7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
#8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
#9. Slope is (m = y2-y1/x2-x1). Find the slope and [Euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance#:~:text=In%20mathematics%2C%20the%20Euclidean%20distance,being%20called%20the%20Pythagorean%20distance.) between point (2, 2) and point (6,10) 
#10. Compare the slopes in tasks 8 and 9.
#11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
#12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
#13. Use _and_ operator to check if 'on' is found in both 'python' and 'dragon'
#14. _I hope this course is not full of jargon_. Use _in_ operator to check if _jargon_ is in the sentence.
#15. There is no 'on' in both dragon and python
#16. Find the length of the text _python_ and convert the value to float and convert it to string
#17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
#18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
#19. Check if type of '10' is equal to type of 10
#20. Check if int('9.8') is equal to 10
#21. Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?

#```py
#Enter hours: 40
#Enter rate per hour: 28
#Your weekly earning is 1120
#```

#22. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years

#```py
#Enter number of years you have lived: 100
#You have lived for 3153600000 seconds.
#```

#23. Write a Python script that displays the following table

#```py
#1 1 1 1 1
#2 1 2 4 8
#3 1 3 9 27
#4 1 4 16 64
#5 1 5 25 125
#```

# solutions:
age=20
print(age)
height=162.3
print(height)
complex=2+5j
print(complex)
b=int(input("enter the base:"))
h=int(input("enter the height:"))
area=0.5*h*b
print("area of the triangle:",area)
a=int(input("enter the side:"))
b=int(input("enter the side:"))
c=int(input("enter the side:"))
perimeter=a+b+c
print("peri of triangle is:",perimeter)
l=int(input("enter the length:"))
w=int(input("enter the width:"))
area=l*w
perimeter=2*(l+w)
print("area of the rect:",area)
print("peri of triangle is:",perimeter)
r=int(input("enter the radius:"))
area=3.14*r*r
cir=2*3.14*r
print("area of circle:",area)
print("circumference of the circle:",cir)
m=2
x=1
y=-2

x1,y1=2,2
x2,y2=3,4
slope=(y2-y1)/(x2-x1)
distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

print("Slope:", slope)
print("Distance:", distance)
##11.
x=int(input("enter the num: "))
y=x**2+6*x+9
print (y)
#12.
a="PYTHON" 
b="DRAGON"
print(len(a))
print(len(b))
print(len(a)!=len(b))
print("'on' in both:","on"in a and "on" in b )
sentence="I hope this course is not full of jargon"
print("jargon" in sentence)
print(a)

num=int(input("enter a num:"))
if(num%2==0):
    print("even")
else:
    print("odd")
## 18
print(7//3==int(2.7))
print(type('10')==type(10))
print(int(float('9.8'))==10)
##21
h=int(input("enter hours:"))
rate=int(input("enter hours:"))
earning =h*rate
print("weekly earning is ",earning)
years=int(input("enter num of year:"))
sec=years*365*24*60*60
print(sec)
for i in range (1,6):
    print(i,1,i,i**2,i**3)
