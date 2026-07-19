### Exercises: Level 1
'''
1. Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:

    ```sh
    Enter your age: 30
    You are old enough to learn to drive.
    Output:
    Enter your age: 15
    You need 3 more years to learn to drive.
    ```

2. Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:

    ```sh
    Enter your age: 30
    You are 5 years older than me.
    ```

3. Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:

```sh
Enter number one: 4
Enter number two: 3
4 is greater than 3
```
'''

##answers:
age= int(input("enter the age:"))
if (age>=18):
   print("You are old enough to learn to drive.")
else:
   yrs=18-age
   print("you need", yrs,"to drive " )
##2.
my_age = 25

your_age = int(input("Enter your age: "))

if your_age > my_age:
    diff = your_age - my_age

    if diff == 1:
        print("You are 1 year older than me.")
    else:
        print("You are", diff, "years older than me.")

elif your_age < my_age:
    diff = my_age - your_age

    if diff == 1:
        print("I am 1 year older than you.")
    else:
        print("I am", diff, "years older than you.")

else:
    print("We are the same age.")
    ##3.
a= int(input("Enter number one: "))
b = int(input("Enter number two: "))
if a>b:
   print(a,"is greater")
elif a<b:
   print(b,"is greater")
else:
   print("a=b")

   
      
   

   
### Exercises: Levael 2
'''
   1. Write a code which gives grade to students according to theirs scores:

    ```sh
    90-100, A
    80-89, B
    70-79, C
    60-69, D
    0-59, F
    ```
   2. Get the month from user input then check if the season is Autumn, Winter, Spring or Summer. If the user input is:
    September, October or November, the season is Autumn.
    December, January or February, the season is Winter.
    March, April or May, the season is Spring
    June, July or August, the season is Summer
   3. The following list contains some fruits:

    ```sh
    fruits = ['banana', 'orange', 'mango', 'lemon']
    ```

    If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
## answes 
##
'''
### Exercises: Level 3

marks=int(input("enter your marks:"))
if 90<=marks<=100:
    print("A")
elif 80<=marks<=89:
    print("B")
elif 70<=marks<=79:
    print("C")
elif 60<=marks<=69:
    print("D")
else:
    print("F")

##2.
month=input("enter the month")
if month in ["september", "october", "november"]:
    print("Autumn")

elif month in ["december", "january", "february"]:
    print("Winter")

elif month in ["march", "april", "may"]:
    print("Spring")

elif month in ["june", "july", "august"]:
    print("Summer")

else:
    print("Invalid month")

    ##3.
    fruits = ['banana', 'orange', 'mango', 'lemon']
    fruit = input("enter a fruits:")
    if fruit in fruits:
        print(" that fruit already exists in the lust ")
    else:
        fruits.append(fruit)
        print("fmodified lust",fruits)
    