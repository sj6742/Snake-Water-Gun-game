# print("hi ! Sujal Here")

# import pyttsx3
# engine = pyttsx3.init()
# engine.say( '''')
# engine.runAndWait()

# a = 5
# b = 10
# print(a+b)

# a = 1000
# b= 34
# print("Remainder When a is divide by b is :", a%b)

# 
# a = int(int(input()("Enter Number 1 : "))
# b = int(int(input()("Enter Number 2 : "))

# print("a is grater then b is :", (a+b)/2)

# a = int(int(input()("Enter your Number  : )"))
# print("The Squre of The Number is :", a**2)

# a = "0123456789"
# a[1:7:3]

# Escape sequential charecters

# print("Hello\n World")  # New Line
# print("Hello\t World")  # Tab Space
# print("This is a backslash: \\")  # Backslash
# print("She said, \"Hello!\"")  # Double Quote
# print('It\'s a beautiful day!')  # Single Quote
# print("ABC\b D")  # Backspace (Removes 'C')
# print("Sujal \r Here")
# print("hey what are \vyou doing ?")

# Marks = []
# f1 = int(input("Enter Marks Name 1:"))
# Marks.append(f1)
# f2= int(input("Enter Marks Name 2:"))
# Marks.append(f2)
# f3 = int(input("Enter Marks Name 3:"))
# Marks.append(f3)
# f4 = int(input("Enter Marks Name 4:"))
# Marks.append(f4)
# f5 = int(input("Enter Marks Name 5:"))
# Marks.append(f5)
# f6 = int(input("Enter Marks Name 6:"))
# Marks.append(f6)
# Marks.sort
# print(Marks)

# s={
#     "Sujal":100,
#     "Vaibhav":40,
#     "Moksh":60,
#     "Rutul":77
# }
# print(s,["Sujal"])


# my_dict = {"name": "Sujal"}
# my_dict["age"] = 21  # Add key-value pair
# my_dict.update({"city": "Ahmedabad", "country": "India"})
# print(my_dict)  # {'name': 'Sujal', 'age': 21, 'city': 'Ahmedabad', 'country': 'India'}


# my_dict = {"name": "Sujal", "age": 21, "city": "Ahmedabad"}
# my_dict.pop("age")  # Removes 'age'
# print(my_dict)  # {'name': 'Sujal', 'city': 'Ahmedabad'}

# my_dict.popitem()  # Removes last key-value pair
# print(my_dict)  # {'name': 'Sujal'}


# words = {
#     "madad": "Help",
#     "khursi": "Chair",
#     "billi":"Cat",
#     "Kutta":"Dog"
# }
# word = input("Enter the word you want :")
# print(words[word])

# s = set()
# n=input("Enter the Number:")
# s.add(int(n))
# n=input("Enter the Number:")
# s.add(int(n))
# n=input("Enter the Number:")
# s.add(int(n))
# n=input("Enter the Number:")
# s.add(int(n))
# n=input("Enter the Number:")
# s.add(int(n))
# n=input("Enter the Number:")
# s.add(int(n))
# n=input("Enter the Number:")
# s.add(int(n))
# print(s)


#If elif else Lader Program 
# a = int (input("Enter Your Age:"))

# if(a>=18):
#     print("You are the above age of the conset:")
#     print("Good for You:")

# elif(a<0):
#     print("You are entering an envalid age number") 

# elif(a==0):
#     print("You are entering 0 whisch is not valid age:")    

# else:
#     print("You are the below age of consent")

# print("End of the program")

#Greatest Number Program:-
# a1 = int(input("Enter The Number 1: "))
# a2 = int(input("Enter The Number 2: "))
# a3 = int(input("Enter The Number 3: "))
# a4 = int(input("Enter The Number 4: "))

# if(a1>a2 and a1>a3 and a1>a4):
#     print("Greatest number a1:",a1)
# if(a2>a1 and a2>a3 and a2>a4):
#     print("Greatest number a2:",a2)
# if(a3>a2 and a3>a1 and a3>a4):
#     print("Greatest number a3:",a3)
# if(a4>a2 and a4>a3 and a4>a1):
#     print("Greatest number a4:",a4)

#Student Pass/Fail Program :-

#Spam Comment Program:- 
# p1 = "Make a lot of money".lower()
# p2 = "Buy Now".lower()
# p3 = "Click This".lower()
# p4 = "subscribe this".lower()

# def new_func(p1, p2, p3, p4):
#     message = input("Enter You Comment: ")

#     if((p1 in message .lower()) 
#     or (p2 in message .lower()) 
#     or (p3 in message .lower()) 
#     or (p4 in message .lower())):
#         print("This Comment is a Spam")
#     else:
#         print("This Comment is not a Spam")

#     marks = int(input("Enter Your Marks:-"))
#     return marks

# marks = new_func(p1, p2, p3, p4)

# if(marks<=100 and marks>=90):
#     grade = "Ex"
# elif(marks<90 and marks>=80):
#     grade = "A"
# elif(marks<80 and marks>=70):
#     grade = "B"
# elif(marks<70 and marks>=60):
#     grade = "C"
# elif(marks<60 and marks>=50):
#     grade = "D"
# elif(marks<50):
#     grade = "F"
# if(marks>100):
#     print("Enter the valid Marks")
# print("Your Grade is: ",grade)


#Loops Programs

# n = int(input("Enter a Number:- "))
# i = 1
# while(i<11):
#     print(f"{n} X {i} = {n * i}")
#     i +=1

#Factorial Program

# n = int(input("Enter The Number: "))
# product = 1
# for i in range(1, n+1):
#     product = product * i
# print(f"The Factorial of {n} is {product}")
'''----------------------------------------------------------------------------------------------------------'''
#STAR PROGRAM
'''
  *
 ***
*****
# '''
# n = int(input("Enter the Number:-"))
# for i in range(1,n+1):
#     print(" "* (n-i),end="")
#     print("*"* (2*i-1),end="")
#     print()

'''
*
**
***
****
*****
'''

    
# n = int(input("Enter the Number:-"))
# for i in range(1,n+1):
#     print("*"* i,end="")
#     print()

'''

* * *
*   *
* * *

'''
# n = int(input("Enter The Number:- "))
# for i in range(1,n+1):
#     if(i==1 or i==n):
#         print("*"* n, end="")
#     else:
#         print("*",end="")
#         print(" "*(n-2),end="")
#         print("*",end="")
#     print("")


#PRINT THE TABLE BUT FROM ENDING 

# n= int(input("Enter The Number:- "))
# for i in range(1,11):
#     print(f"{n} X {11-i} = {n*(11-i)}")
# ---------------------------------------------------------------------------------------------------------------
#FUNCTION PROGRAMS 

#FUNCTION DEFINATION 
# def avg():
#     a= int(input("Enter Your Number"))
#     b= int(input("Enter Your Number"))
#     c= int(input("Enter Your Number"))
    
#     avg =  (a+b+c)/3
#     print(avg)
# avg() #Function Call
# print("Thank You ")
# avg()
# print("Thank You ")
# avg()
# print("Thank You ")
# avg()
# print("Thank You ")
# avg()

#PATTENES USING A FUNCTIONS 
'''
*****
****
***
**
*
# '''
# def pattern (n):
#     if(n==0):
#         return
#     print("*"*n)
#     pattern(n-1)
# pattern(5)     

#PRINT MULTIPLICAATION TABLE USING THE FUNCTION 
a = int(input("Enter Your Multiplication Table Number:- "))
# print(a)
def multiply(a):
    for i in range(1,11):
      print(f"{a} X {i} = {a*i}")  
multiply(a)
