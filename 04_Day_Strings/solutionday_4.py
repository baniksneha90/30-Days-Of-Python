## 💻 Exercises - Day 4
'''
1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
3. Declare a variable named company and assign it to an initial value "Coding For All".
4. Print the variable company using _print()_.
5. Print the length of the company string using _len()_ method and _print()_.
6. Change all the characters to uppercase letters using _upper()_ method.
7. Change all the characters to lowercase letters using _lower()_ method.
8. Use capitalize(), title(), swapcase() methods to format the value of the string _Coding For All_.
9. Cut(slice) out the first word of _Coding For All_ string.
10. Check if _Coding For All_ string contains a word Coding using the method index, find or other methods.
11. Replace the word coding in the string 'Coding For All' to Python.
12. Change "Python for Everyone" to "Python for All" using the replace method or other methods. 
13. Split the string 'Coding For All' using space as the separator (split()) .
14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
15. What is the character at index 0 in the string _Coding For All_.
16. What is the last index of the string _Coding For All_.
17. What character is at index 10 in "Coding For All" string.
18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
19. Create an acronym or an abbreviation for the name 'Coding For All'.
20. Use index to determine the position of the first occurrence of C in Coding For All.
21. Use index to determine the position of the first occurrence of F in Coding For All.
22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
26. Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
27. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
28. Does 'Coding For All' start with a substring _Coding_?
29. Does 'Coding For All' end with a substring _coding_?
30. '&nbsp;&nbsp; Coding For All &nbsp;&nbsp;&nbsp; &nbsp;' &nbsp;, remove the left and right trailing spaces in the given string.
31. Which one of the following variables return True when we use the method isidentifier():
    - 30DaysOfPython
    - thirty_days_of_python
32. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
33. Use the new line escape sequence to separate the following sentences.
    ```py
    I am enjoying this challenge.
    I just wonder what is next.
    ```
34. Use a tab escape sequence to write the following lines.
    ```py
    Name      Age     Country   City
    Asabeneh  250     Finland   Helsinki
    ```
35. Use the string formatting method to display the following:

```sh
radius = 10
area = 3.14 * radius ** 2
The area of a circle with radius 10 is 314 meters square.
```

36. Make the following using string formatting methods:

```sh
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144
```
'''
# solutionss :
#1.
Str= "Thirty" +" " + "Days " + " " + "of" + " " + "python"
print(Str)
#2
p= "coding"+" "+"for "+" "+"all"
print (p)
#Q3-Q17
company = "coding for all"
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
first_word= company[:6]
print(first_word)
print("coding in",company)
print(company.replace("coding","python"))
r="python for all"
print(r.replace("all" , "everyone"))
print(company.split())
e="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" 
print(e.split(","))
print(company[0])
print(len(company)-1)
print(company[10])
s = "Python For Everyone"
acronym = "".join(word[0] for word in s.split())
print(acronym)
acr="".join(word[0] for word in company.split())
print(acr)
print(company.index("c"))
print(company.index("f"))
print(company.rfind("l"))
c='You cannot end a sentence with because because because is a conjunction'
print(c.find("because"))
print(c.rfind("because"))
start = c.find("because")
end = start + len("because because because")
print(c[start:end])
print(c.index("because"))
print(company.startswith("coding"))
print(company.endswith("Coding"))
w="30DaysOfPython"
p="thirty_days_of_python"
print(w.isidentifier())
print(p.isidentifier())
lib=['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print("#".join(lib))
print("I am enjoying this challenge.\n I just wonder what is next ")
rad=10
area=3.14*rad**2
print("the area of the circle with radius {}is {} msq".format(rad,area))
a=8
b=6
print("{}+{}={}".format(a,b,a+b))
print("{}-{}={}".format(a,b,a-b))
print("{}*{}={}".format(a,b,a*b))
print("{}/{}={}".format(a,b,a/b))
print("{}%{}={}".format(a,b,a%b))
print("{}//{}={}".format(a,b,a//b))
print("{}**{}={}".format(a,b,a**b))




