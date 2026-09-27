 ##Q1. sq of each num
numbers = [1, 2, 3, 4, 5]

result = [i * i for i in numbers]

print(result)
#q2.
num=[1,2,3,4,5,6,7,8,9]
result=[i for i in num if i%2!=0]
print(result)
##q3
names=["sneha","shrestha"]
result=[names.upper() for name in names]
print(result)
##q4
num=[[1,2],[3,4],[5,6]]
result=[num for row in num for num in row ]
print(result)
##q5
larger = lambda a, b: a if a > b else b
print(larger(10, 25))
## Excercise
##q1.
num=[-4,-3,-2,-1,0,2,4,6]
result=[ i for i in num if i <=0]
print(result)
##q2.
result = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print(result)
##q3.
countries = [
    [('Finland', 'Helsinki')],
    [('Sweden', 'Stockholm')],
    [('Norway', 'Oslo')]
]
result = [
    [country.upper(), country[:3].upper(), city.upper()]
    for item in countries
    for country, city in item
]

print(result)