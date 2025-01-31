def sum(a,b,c):
    return a + b + c
def printboard(xstate , zstate):
    zero = "X" if xstate[0] else ("O" if zstate[0] else 0) 
    one = "X" if xstate[1] else ("O" if zstate[1] else 1) 
    two = "X" if xstate[2] else ("O" if zstate[2] else 2) 
    three = "X" if xstate[3] else ("O" if zstate[3] else 3) 
    four = "X" if xstate[4] else ("O" if zstate[4] else 4) 
    five = "X" if xstate[5] else ("O" if zstate[5] else 5) 
    six = "X" if xstate[6] else ("O" if zstate[6] else 6) 
    seven = "X" if xstate[7] else ("O" if zstate[7] else 7) 
    eight = "X" if xstate[8] else ("O" if zstate[8] else 8) 
    print(f" {zero} | {one} | {two} ")
    print(f"---|---|---")
    print(f" {three} | {four} | {five} ")
    print(f"---|---|---")
    print(f" {six} | {seven} | {eight} ")
def checkwins(xstate,zstate):
    wins = [[0,1,2],[3,4,5],[6,7,8],[0,4,8],[2,4,6],[0,3,6],[1,4,7],[2,5,8]]
    for win in wins:
        if (sum(xstate[win[0]],xstate[win[1]],xstate[win[2]])==3):
            print("X Won the match")
            return 1
        if (sum(zstate[win[0]],zstate[win[1]],zstate[win[2]])==3):
            print("O Won the match")
            return 0
    return -1
if __name__ == "__main__":
    xstate = [0,0,0,0,0,0,0,0,0]
    zstate = [0,0,0,0,0,0,0,0,0]
    turn = 1
    print("Welcome to tic tac toe")
    while True:
         printboard(xstate , zstate)
         if (turn == 1):
            print("X's chance")
            value = int(input("please enter a value:-"))
            xstate[value] = 1
         else:
            print("O's chance")
            value = int(input("please enter a value:-"))
            zstate[value] = 1
         cwin = checkwins(xstate,zstate)
         if (cwin != -1):
            print("Game Over!")
            break
        
         turn = 1-turn

'''quick password generator in python'''
# import random
# char = ("abcdefghijklmnopqrstuvwxyz")#you can add more charactor in this for more security
# length = int(input("enter length of password:-"))
# password = ""
# for i in range(length):
#     password+=random.choice(char)
# print(password)

'''grocery shop calculator'''
# sum = 0
# while True:
#     UserInput = input("enter the price \npress 'q' for quit:-")
#     if UserInput != "q":
#         sum = sum + int(UserInput)
#         print(f"order total so far {sum}")
#     else:
#         print(f"your total bill is {sum}")
#         break

'''factorial of any number by python'''
# def factorial(number):
#     if number == 0 or number == 1:
#         return 1
#     else:
#         return number * factorial(number-1)
# if __name__ == "__main__":
#     number= int(input("enter the number for factorial:-"))
#     fac = factorial(number)
#     print(f"the factorial of {number} is {fac}")

# fibonacci series in python
# def fibonacci(n):
#     if n <=1:
#         return n 
#     else:
#        return fibonacci(n-1) + fibonacci(n+2)
# num = int(input("enter a number:"))
# if num <0:
#     print("enter a positive value!")
# else:
#     result = fibonacci(num)
#     print(result)

