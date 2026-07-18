'''
## 💻 Exercises: Day 8

1. Create  an empty dictionary called dog
2. Add name, color, breed, legs, age to the dog dictionary
3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
4. Get the length of the student dictionary
5. Get the value of skills and check the data type, it should be a list
6. Modify the skills values by adding one or two skills
7. Get the dictionary keys as a list
8. Get the dictionary values as a list
9. Change the dictionary to a list of tuples using _items()_ method
10. Delete one of the items in the dictionary
11. Delete one of the dictionaries
'''

##Answers:
dog={}
print(dog)
dog={
    'Name':'silky',
    'breed':'german shephard',
    'legs':4,
    'age':21

}
print(dog)
student ={
    'first': 'Sneha',
    'last':'banik',
    'gender':'female',
    'age': 20,
    'marital status':'unmarried',
    'skills':['python ','java','dsa','vlsi','verilog'],
    'country': 'indian',
    'city':'sambalpur',
    'address': 'burla sbp'
     

}
print(student)
print(len(student))
values=student.values()
print(values)
## modifying the skills 
student['skills'].append(['html','javascript'])
print(student)
keys=student.keys()
print(keys)
print(list(student.items()))
del student['marital status']
print(student)
del student
