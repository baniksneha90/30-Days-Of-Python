### Exercises: Level 1
'''
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
1. Find the length of the set it_companies
2. Add 'Twitter' to it_companies
3. Insert multiple IT companies at once to the set it_companies
4. Remove one of the companies from the set it_companies
5. What is the difference between remove and discard
'''
## ansswers:
company={'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
c=len(company)
print(c)
company.add('Twitter')
print(company)
## for adding multiple items to the sets use .update
company.update({'samsung','qualcomm','NVDIA','AMD'})
print(company)
company.remove('IBM')
print(company)

### Exercises: Level 2
'''
1. Join A and B
2. Find A intersection B
3. Is A subset of B
4. Are A and B disjoint sets
5. Join A with B and B with A
6. What is the symmetric difference between A and B
7. Delete the sets completely
'''

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

r= A|B
a=A&B
print(r)
print(a)
print(A.issubset(A))
print(B.union(A))
print(A.isdisjoint(B) )
print(A-B)
del (r)

### Exercises:3 Level 3
'''
1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
2. Explain the difference between the following data types: string, list, tuple and set
3. _I am a teacher and I love to inspire and teach people._ How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
'''
## answers:
age = [22, 19, 24, 25, 26, 24, 25, 24]
s=set(age)
print(len(s))
print(len(age))
if len(age)> len(s):
    print("list is bigger")
else:
    print("set is bigger")
sen="I am a teacher and I love to inspire and teach people."
w=sen.split()
unique_words=set(w)
print(unique_words)
print(len(unique_words))

