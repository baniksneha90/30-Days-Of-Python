'''
1. Iterate 0 to 10 using for loop, do the same using while loop.
2. Iterate 10 to 0 using for loop, do the same using while loop.
3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:

   ```py
     #
     ##
     ###
     ####
     #####
     ######
     #######
   ```

4. Use nested loops to create the following:

   ```sh
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   ```

5. Print the following pattern:

   ```sh
   0 x 0 = 0
   1 x 1 = 1
   2 x 2 = 4
   3 x 3 = 9
   4 x 4 = 16
   5 x 5 = 25
   6 x 6 = 36
   7 x 7 = 49
   8 x 8 = 64
   9 x 9 = 81
   10 x 10 = 100
   ```

6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
7. Use for loop to iterate from 0 to 100 and print only even numbers
8. Use for loop to iterate from 0 to 100 and print only odd numbers
'''
## answers:
#1.
for i in range(11):
    print(i)
# while 
i = 0
while i <= 10:
    print(i)
    i += 1

#2.
for i in range(10,-1,-1):
    print(i)
## while 
i=10
while i>=0:
    print(i)
    i-=1
#3.
for i in range(1,8):
    print("#" * i)
#4.
for i in range(8):
    for j in range(8):
        print("#", end =" ")
    print()
#5.
for i in range(11):
    print( i, "x", i, "=", i*i)
#6.
l=['Python', 'Numpy','Pandas','Django', 'Flask'] 
for i in l:
    print(i)
#7.
for i in range(0,101):
    if i%2==0:
        print("even nums:",i)
#8.
for i in range(0,101):
    if i%2!=0:
        print("odd nums:",i)

### Exercises: Level 2
'''
1.  Use for loop to iterate from 0 to 100 and print the sum of all numbers.

```sh
The sum of all numbers is 5050.
```

2. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.

   ```sh
   The sum of all evens is 2550. And the sum of all odds is 2500.
   ```
'''
# answers:
#1.
sum=0
for i in range(101):
    sum=sum+i
    print("The sum of all numbers are:",sum)
#2.
even =0
odd=0
for i in range(101):
    if i%2==0:
        even=even+i
    else:
        odd=odd+i
print("sum of even:",even)
print("sum of odd :",odd)


### Exercises: Level 3
'''
1. Go to the data folder and use the [countries.py](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries.py) file. Loop through the countries and extract all the countries containing the word _land_.
1. This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
1. Go to the data folder and use the [countries_data.py](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file.
   1. What are the total number of languages in the data
   2. Find the ten most spoken languages from the data
   3. Find the 10 most populated countries in the worldgit 

🎉 CONGRATULATIONS ! 🎉

[<< Day 9](../09_Day_Conditionals/09_conditionals.md) | [Day 11 >>](../11_Day_Functions/11_functions.md)
'''
#1.
countries = ['Finland', 'Sweden', 'Iceland', 'India', 'Ireland', 'Nepal']
for i in countries:
    if "land" in i:
        print(i)
#2.
fruits=['banana', 'orange', 'mango', 'lemon'] 
for i in range(len(fruits)-1, -1, -1):
    print(fruits[i])

#3.
countries = ['Finland', 'Sweden', 'Iceland', 'India', 'Ireland', 'Nepal']


