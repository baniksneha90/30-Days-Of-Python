### Exercises: Level 1


#1. Create an empty tuple
#2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
#3. Join brothers and sisters tuples and assign it to siblings
#4. How many siblings do you have?
#5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members.

#1.
empty=()
print(empty)
#2.
bro=('bibek',)
sis=('sneha',)
##3.
sib=bro+sis
print(sib)
##4
print(len(sib))
##5. for modification first i have to make it list .
lst= list(sib)
lst = list(sib)
lst.append("Father")
lst.append("Mother")

family_members = tuple(lst)
print(family_members)

### Exercises: Level 2
'''
1. Unpack siblings and parents from family_members
1. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
1. Change the about food_stuff_tp  tuple to a food_stuff_lt list
1. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
1. Slice out the first three items and the last three items from food_stuff_lt list
1. Delete the food_stuff_tp tuple completely
1. Check if an item exists in  tuple:

- Check if 'Estonia' is a nordic country
- Check if 'Iceland' is a nordic country

  ```py
  nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
  ```

'''
family_members=("Bibek","Sneha","mother","father")
bro,sis,mother,father=family_members
print(bro)
print(sis)
print(father)
print(mother)
##2.
fruits=("apple","banana","litchi","mango")
veg=("potato","tomato","garlic","carrot")
animal=("dog","cat","parrot")
fruit_stuff_tp=fruits+veg+animal
print(fruit_stuff_tp)
fruit_stuff_lt=list(fruit_stuff_tp)
print(fruit_stuff_lt)
middle = len(fruit_stuff_lt)//2
print(fruit_stuff_lt[:3])
print(fruit_stuff_lt[-3:])
del fruit_stuff_tp
nordic_countries = (
    "Denmark",
    "Finland",
    "Iceland",
    "Norway",
    "Sweden"
)
print("estonia" in nordic_countries)
