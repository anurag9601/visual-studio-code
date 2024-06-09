'''getting square root of a number'''
# def square_root(num):
#     print(num**0.5)

# square_root(2)

# import math
# num = int(input("Enter the number: "))
# sr = math.sqrt(num)
# print(f"The Square Root of given number is {sr}")

# def area_tringle(b,h):
#     return 1/2*b*h

# print(area_tringle(5,7))

# height = float(input("enter the height of the traingle: "))
# base = float(input("enter the base of the traingle: "))
# area = (1/2)*base*height
# print(f"the area of the traingle height {height} and base {base} is {area}")

# swap variable values
# x = 12
# y = 13
# temp = y
# print(f"value of temp variable is {temp}")
# y = x
# print(f"value of Y variable is {y}")

# x = 5
# y = 9
# x,y = y,x
# print(f"value of x is {x}")
# print(f"value of Y is {y}")

# value = float(input("Enter the kilo's value :"))
# milligram = value*1000000
# print(f"in {value} kilogram there is {milligram} milligram")

# value = float(input("Enter the value of kilomete's : "))
# mile = value*0.62137119
# print(f"the mile's in {value} kilometer is {mile}")

# num = int(input("Enter a number: "))
# if num>0:
#     print("It's a positive number")
# elif num<0:
#     print("It's a negative number")
# else:
#     print("It's zero")

# num = int(input("Enter the number to check it's positive negative or zero: "))
# if num>0 and num%2==0:
#     print("It's a even Number")
# elif num>0 and num%2!=0 :
#     print("It's odd Number")
# elif num<0:
#     print("It's a negative number")
# else:
#     print("It's Zero")

# year = int(input("Enter the year: "))
# if year%4==0 and year%100!=0 or year%400==0 and year%100==0:
#     print("It's a leap year")
# else:
#     print("It's not a leap year")

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# num3 = int(input("Enter the third number: "))
# if num1>num2 and num1>num3:
#     print(f"{num1} is largest")
# if num2>num1 and num2>num3:
#     print(f"{num2} is largest")
# if num3>num2 and num3>num1:
#     print(f"{num3} is largest")

# num1 = int(input("Enter the first numbe: "))
# num2 = int(input("Enter the second number: "))
# num3 = int(input("Enter the third number: "))
# if num1<num2 and num1<num3:
#     print(f"{num1} is lowest number")
# elif num2<num1 and num2<num3:
#     print(f"{num2} is lowest number")
# elif num3<num1 and num3<num2:
#     print(f"{num3} is lowest number")

# print("***Leap Year List Tool: Yout Ultimate Guide\nto Identifying Leap Year***")
# print("LEAP YEAR LIST")
# def leapyears():
#     stryear = int(input("Start Year: "))
#     endyear = int(input("End Year: "))
#     print(f"Leap year between {stryear} to {endyear}:")
#     for i in range(stryear,endyear+1):
#         if i%4==0 and i%100!=0 or i%400==0 and i%100==0:
#             print(i,end = ",")
# leapyears()

# Dict = {
#         "anurag":26,
#         "sharad":0,
#         9:9
#     }
# print(Dict[9])
# print(Dict.get("sharad"))
# dict1={1:"anurag",2:"sharad",3:"abhimanu"}
# print("dictonary =",end = "")
# print(dict1)

# finding num is prime number of not 
# num = int(input("Enter a number: "))
# if num==1:
#     print("it's not a prime number")
# if num>1:
#     for i in range(2,num):
#         if num%i==0:
#             print("it's not a prime number")
#             break
#     else:
#         print("it's a prime number")

# import random
# print(random.randint(2,10))

# getting all primery number between entered number 
# num = int(input("Enter the number: "))
# for i in range(2,num+1):
#     if num>1:
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             print(i)

# celsius = int(input("Enter the celsius value: "))
# fahrenheit = (celsius*9/5)+32
# print(f"The celsius value {celsius} in fahrenheit is {fahrenheit}")

# num = int(input("Enter the number to get factorial of it: "))
# if num==0 or num==1:
#     print("factorial of",num,"is 1")
# factorial = 1
# if num>1:
#     for i in range(1,num+1):
#         factorial = factorial*i
#     print("factorial of",num,"is",factorial)

# import time
# str_time = time.time()
# num = int(input("Enter a number to get factorial: "))
# factorial = 1
# if num==0 or num==1:
#     print(f"factorial of {num} is 1")
# elif num>1:
#     for i in range(1,num+1):
#         factorial = factorial * i
#     print(f"factoraial of {num} is {factorial}")
# end_time = time.time()
# time = end_time - str_time
# print("total execution time is", time)

# factorial by using recursion recusion is when function is called in side with them selves
# import time
# str_time = time.time()
# def factorial(num):
#     if num==1 or num==0:
#         return 1
#     else:
#         return num*factorial(num-1)
# num = int(input("Enter a number here: "))
# result = factorial(num)
# print(f"factorial of {num} is {result}")
# end_time = time.time()
# time = end_time - str_time
# print("Total execution time is", time)
    
# getting table of any number using for loop 
# num = int(input("Enter a number here: "))
# for i in range(1,11):
#     print(num,"X" ,i ,"=" ,num*i)

# getting table of any number using while loop 
# num = int(input("Enter a number: "))
# i = 1
# while i<=10:
#     print(num*i)
#     i = i + 1

# fibonacci sequence
# num = int(input("enter a number here: "))
# a = 0
# b = 1
# if num == 1:
#     print(0)
# else: 
#     print(a)
#     print(b)
#     for i in range(2,num):
#         c = a + b
#         a = b
#         b = c
#         print(c)

# armstrong numbers in python

# identifying armstrong number by using while loop 
# num = int(input("Enter a number here: "))
# sum = 0
# temp = num
# while temp>0:
#     digit = temp%10
#     sum = sum + digit**3
#     temp = temp//10
# if sum==num:
#     print("It is a armstrong number")
# else:
#     print("It is not a armstrong number")

# identifying enter number is armstrong number or not by using for loop
# num = (input("enter a number: "))
# sum = 0
# for i in num:
#     sum = sum + int(i)**3
# if int(num)==sum:
#     print("its a armstrong number")
# else:
#     print("its not a armstrong number")

# finding armstrong number in range of two numbers 
# upper = int(input("enter a first number: "))
# lower = int(input("enter a second number: "))
# for num in range(upper,lower+1):
#     length = len(str(num))
#     sum = 0
#     temp = num
#     while temp>0:
#         digit = temp%10
#         sum = sum + digit**length
#         temp//=10
#     if num==sum:
#         print(num)

# find the sum of natural number using python 
# num = int(input("Enter a number here: "))
# sum = 0
# temp = num
# if num<0:
#     print("please enter a positive number")
# else:
#     while num>0:
#         sum = sum + num
#         num = num - 1
# print(f"Sum number {temp} is {sum}")

#lambda function is called as anonymous function
# power = int(input("enter the power: "))
# result = list(map(lambda x:5** x, range(power+1)))
# for i in range(power+1):
#     print("the number of 5 raised to power",i,"is",(result[i]))

# python program to find number divided by another number 
# num = int(input("number want to check: "))
# range1 = int(input("between range1: "))
# range2 = int(input(" to range2: "))
# for i in range(range1,range2+1):
#     if i%num==0:
#         print(i)

# filter function in python 
# l = [13,67,26,52]
# result = list(filter(lambda x:x%13==0,l))
# print(result)

# The filter() function returns an iterator where the items are filtered through a function to test if the item is accepted or not. 
# list = [12,16,18,20,22,59]
# def age(x):
#     if x > 18:
#         return True
#     else:
#         return False
# filtered = filter(age,list)
# for i in filtered:
#     print(i,end = " ")

# how to take decimal value by using built in functions 
# decimal = int(input("enter the decimal number for a value: "))
# print(f"the decimal value of given number {decimal} is")
# print(bin(decimal))
# print(oct(decimal))
# print(hex(decimal))

# ASCII stands for a american standard code for information interchange
# in ASCII we have 128 characters i.e,number,letters,uppercase letter,lowercase letter 
# char = input("Enter the character to get ASCII value: ")
# print("the ASCII value of",char,"is",ord(char))

# HCF stands for highest comman fector and GCD is greatest common devisor 
# hcf where both the entered number divide with the same highest number 
# def findhcf(x,y):
#     if x>y:
#         smaller = x
#     else:
#         smaller = y
#     for i in range(1,smaller+1):
#         if x%i==0 and y%i==0:
#             HCF = i
#     return HCF
# print(findhcf(12,30))

'''python program to find the factor of a number'''
# factor of a number is where number comes in any table so that table of number is factor of that number 
# num = int(input("Enter a number here: "))
# print(f"Factor of a number {num} is")
# for i in range(1,num+1):
#     if num%i==0:
#         print(i)

'''python program to make a simple calculator'''
# print("***MINI CALECULATOR***")
# num1 = int(input("Enter a first number: "))
# symbol = input("Enter the symbol: ")
# num2 = int(input("Enter a second number: "))
# if symbol=="-":
#     print(num1-num2)
# if symbol=="+":
#     print(num1+num2)
# if symbol=="/":
#     print(num1/num2)
# if symbol=="x":
#     print(num1*num2)
# if symbol=="**":
#     print(num1**num2)
# if symbol=="%":
#     print(num1&num2)
# if symbol=="//":
#     print(num1//num2)
# if symbol==">":
#     print(num1>num2)
# if symbol=="<":
#     print(num1<num2)

'''python program to shuffle deck of cards'''
# import random , itertools
# deck = list(itertools.product(range(1,14),["spade","club","hearts","Diamond"]))
# random.shuffle(deck)
# for i in range(5):
#     print(deck[i][0],"of",deck[i][1])

'''python program to check whether in list add of two is equal to the enter number or not''' 
# l = [[1,3],[2,2],[6,4],[9,1]]
# for i in range(len(l)):
#     if (l[i][0]+l[i][1]==10):
#         print(l[i])

'''python program to display the calender'''
# import calendar
# year = int(input("enter year: "))
# month = int(input("enter month: "))
# calendar = calendar.month(year,month)
# print(calendar)

'''python program to display fiboancci sequence using recursion'''
# def fibo(n):
#     if n<=1:
#         return n
#     else:
#         return fibo(n-2)+fibo(n-1)
# n = int(input("enter a number here: "))
# if n<=0:
#     print("please enter  a positive number")
# else:
#     for i in range(1,n):
#         print(fibo(i))

# a = 0
# b = 1
# num = int(input("enter a number: "))
# print(a)
# print(b)
# for i in range(2,num):
#     c = a + b
#     a = b
#     b = c
#     print(c)

'''python program to convert decimal to binary using recursion'''
# def binary(n):
#     if n>1:
#         binary(n//2)
#     print(n%2,end = "")
# print(binary(32))

'''python program to add two matrices'''
# a = [[1,2,3],
#      [4,5,6],
#      [7,8,9]]
# b = [[1,2,3],
#      [5,7,3],
#      [3,8,1]]
# result = [[0,0,0],
#           [0,0,0],
#           [0,0,0]]
# for i in range(len(a)):
#     for j in range(len(a[0])):
#         result[i][j] = a[i][j]+b[i][j]
# print(result)
# for r in result:
#     print(r)

# def matrix(m,n):
#     o = []
#     for i in range(m):
#         row = []
#         for j in range(n):
#             inp = int(input(f"Enter O [{i}][{j}]"))
#             row.append(inp)
#         o.append(row)
#     return o
# def sum(A,B):
#     output = []
#     for i in range(len(A)):
#         row = []
#         for j in range(len(A[0])):
#             row.append(A[i][j] + B[i][j])
#         output.append(row)
#     return output
# m = int(input("Enter the number of row: "))
# n = int(input("Enter the number of column: "))
# print("Enter matrix A")
# A = matrix(m,n)
# print(A)

# print("Enter matrix B")
# B = matrix(m,n)
# print(B)

# s = sum(A,B)
# print(s)

'''how to transfer a matrix'''
# A = [[1,2,3],
#      [4,5,6]]
# print(A)
# T = [[0,0],
#      [0,0],
#      [0,0]]
# for i in range(len(A)):
#     for j in range(len(A[0])):
#         T[j][i] = A[i][j]
# for r in T:
#     print(r)

'''check wether a string is palindrome or not'''
# inp = input("Enter the word: ")
# rev = inp[::-1]
# if inp==rev:
#     print("Its a palindrome word")
# else:
#     print("Its not a palindrome word")

'''how to remove punctuations from a string'''
# punc = '''!@#$%^&*()"':;?/>.<,+=_-'''
# string = input("Enter anything here: ")
# empty_str = ""
# for i in string:
#     if i not in punc:
#         empty_str = empty_str + i
# print(empty_str)

'''how to multiply two matrices'''
# A = [[1,2,3],
#      [4,5,6],
#      [7,8,9]]
# B = [[1,2,3],
#      [4,5,6],
#      [7,8,9]]
# result = [[0,0,0],
#           [0,0,0],
#           [0,0,0]]
# for i in range(len(A)):
#     for j in range(len(B[0])):
#         for k in range(len(B)):
#             result[i][j] += A[i][k] * B[k][j]
# for r in result:
#     print(r)

'''program to sort words in a a;phabetic order'''
# a = "Anurag Mishra is a Nice Guy"
# w = a.split()
# print(w)
# for i in range(len(w)):
#     w[i] = w[i].lower()
# print(w)
# w.sort()
# for i in w:
#     print(i)

'''python program to illustrate different set'''
# '|' this sybol is use in set for a union and '&' this for a intersection
# '-' hifun sybol for difference '^' for symmetric difference
# set1 = {1,2,3}
# set2 = {2,3,4}
# # example of union
# # set3 = set1 | set2
# set3 = set1.union(set2)
# print(set3) #{1, 2, 3, 4}
# # example of intersection 
# # set4 = set1 & set2
# set4 = set1.intersection(set2)
# print(set4) #{2, 3}
# # example of difference 
# # set5 = set1-set2
# set5 = set1.difference(set2)
# print(set5) #{1}
# # example of symmetric difference 
# # set6 = set1 ^ set2
# set6 = set1.symmetric_difference(set2)
# print(set6) #{1, 4}

'''python program to count the number of each vowel'''
# sen = (input("Enter anything here: "))
# sen = sen.lower()
# print(sen)
# char = "aeiou"
# count = 0
# for  i in sen:
#     for j in char:
#         if i==j:
#             count = count + 1
# print(count)

# sen = input("Enter anything here: ")
# vowels = "aeiou"
# sen = sen.casefold()
# print(sen)
# count = {}.fromkeys(vowels,0)
# for char in sen:
#     if char in count:
#         count[char]+=1
# print(count)

'''how to merge two Dictonaries'''
# dict1 = {"john":89,"Lisa":99}
# dict2 = {"Lisa":94,"Peter":78}
# dict3 = dict1 | dict2
# print(dict3)
# print({**dict1,**dict2})
# dict3 = dict2.copy()
# dict3.update(dict1)
# print(dict3)

'''index of list using for loop in python'''
# l = [12,4,44,5,77]
# for index,i in enumerate(l,start = 1):
#     print(index,"-",i)
# without using enumerate function 
# for index in range(len(l)):
#     value = l[index]
#     print(index,"-",value)

'''count number of alphabets using list method'''
# a = ["a","a","b","b","b","c"]
# output = []
# count = 1
# current = a[0]
# for i in range(1,len(a)):
#     if a[i]==current:
#         count = count + 1
#     else:
#         print(f"{count}{current}")
#         count = 1
#         current = a[i]
# print(f"{count}{current}")

'''iterate over dictionaries usign for loop'''
# dict = {1:"anubhav",2:'shashkant',3:"mithalesh"}
# for key,value in dict.items():
#     print(key,value)
# for key in dict.keys():
#     print(key)
# for values in dict.values():
#     print(values)
# for key in dict:
#     print(key,":",dict[key])
# for i in dict.keys():
#     print(i)
# for i in dict.values():
#     print(i)

'''python program to sort a dictonary by value'''
# dict = {"roshan":56,"suhani":18,"mahesh":12}
# sv = sorted(dict.items())
# print(sv)
# sv = sorted(dict.items(),key = lambda x:x[1])
# print(sv)
# v = sorted(dict.values())
# print(v)
# k = sorted(dict.keys())
# print(k)

'''how to check list is empty in python'''
# print(bool([]))
# print(bool([1,3,5]))

# my_list = []
# if not my_list:
#     print("list is empty")
# else:
#     print("list is filled")

# list = []
# print(len(list))
# if len(list)==0:
#     print("list is empty")
# else:
#     print("list is filled")

# my_list = []
# if my_list == []:
#     print("your list is empty")
# else:
#     print("your list is filled")

# input = "abcabcbc"
# output = 2
# "bc"

# 54321
# 4321
# 321
# 21
# 1
# for i in range(5,0,-1):
#     for j in range(i,0,-1):
#         print(j,end = "")
#     print()

# i = 5
# while i>0:
#     j = i
#     while j>0:
#         print(j,end = "")
#         j = j - 1
#     print()
#     i = i - 1

'''how to find average of any number'''
# import time
# str_time = time.time()
# num = int(input("Enter a number: "))
# sum = 0
# for i in range(num,0,-1):
#     sum = sum + i
# div = sum/num
# print(div)
# end_time = time.time()
# exec_time = end_time - str_time
# print(exec_time)

'''how to find average of N number in python'''
# num = int(input("how many number?"))
# total_sum = 0
# for i in range(num):
#     number = float(input("Enter any number: "))
#     total_sum = total_sum + number
# result = total_sum/num
# print(result)

'''how to find out the version of python you are using'''
# import sys
# print(sys.version)

'''how to print current date and time in python'''
# import time
# time = time.ctime()
# print(time)

'''how to get string format time that is strftime in python'''
# import datetime
# now = datetime.datetime.now()
# print("current date time is")
# print(now.strftime("%y-%m-%d %H:%M:%S"))

'''how to find area of circle in python'''
# radius = float(input("Enter the radius of the circle: "))
# area = 3.14 * (radius**2)
# print(area)

#using math module
# from math import pi
# r = float(input("Enter the radius of the circle: "))
# print("the radious of circle is",pi * (r**2))

'''how to reverse string in python'''
# str = input("Enter anything here to reverse: ")
# rev = str[::-1]
# print("the reverse string is ",rev)

'''how to create a list and tuple with comma separated numbers in python'''
# value =(input("Enter some numbers with comma: "))
# list = value.split(",")
# tuple = tuple(list)
# print("list:",list)
# print("tuple",tuple)

'''how to extract extension from filename in python'''
# filename = input("Enter the filename: ")
# file_extns = filename.split(".")
# # print(file_extns)
# print("the extension is",file_extns[-1])

'''display the first and last colors from a give list in python'''
# colors = ["green",'yellow',"white"]
# print(colors[0],colors[-1])

# list = [1,0,2,0]
# for item in list:
#     if item==0:
#         list.remove(item)
#         list.append(item)
# print(list)

#     *
#    * *
#   * * *
# n = 1
# while n<=3:
#     j = 6 - n
#     while j>0:
#         print(" ",end = "")
#         j = j - 1
#     k = n
#     while k>0:
#         print("*",end = " ")
#         k = k - 1
#     print()
#     n = n + 1
# n = 6
# for i in range(1,4):
#     for j in range(n-i):
#         print(" ",end = "")
#     for k in range(i):
#         print("*",end = " ")
#     print()



  