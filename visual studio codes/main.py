# import time is module that we use to find current time
# import time
# t = time.ctime()
# print('current date and time',t)
# import time
# a = time.time()
# print(a)
# b = time.localtime(1700660293.3255687)
# print(b)
# import time
# s = time.strftime("%a,%d% b %Y %H:%M:%S",gmtime(1700660293.3255687))
# print(s)
# practice of recursion method

# def f(n):
#   if (n==0):
#     return 0
#   elif (n==1):
#     return 1
#   else:1
#   return f(n-1) + f(n-2)
# n = int(input("enter the number:"))
# print(f(n))

# a= (input("enter the number:"))
# print(f"multiplication of {a} is ")
# try:
#   for i in range(1,11):
#     print(f"{int(a)} x {i} = {int(a)*i}")
# except:
#     print("invalid input")


# import os 
# os.mkdir("data")
# for i in range(0,100):
#     os.mkdir(f"data/day{i+1}")
# for i in range(0,100):
#     os.rename(f"data/tutuorial{i+1}",f"data/tutuorial {i+1}")
# folder = os.listdir("data")
# print(folder)
# for folders in folder:
#     print(os.listdir(f"data/{folders}"))
# class Animal:
#     def __init__(self,name,species):
#        self.name = name
#        self.species = species
#     def make_sound(self):
#        print("sound made by Animal")
# class Cat(Animal):
#     def __init__(self,name,breed):
#        Animal.__init__(self,name,species = "cat")
#        self.breed = breed
#     def mak_sound(self):
#        print("miyau!")   
# obj2 = Cat("cat","catgirl")
# obj2.make_sound()

# obj = Animal("cat","cat")
# obj.make_sound()
