# n = 5
# i = 1
# l = 1
# while n >0:
#     j = 1
#     while j <= 5-i:
#         print(" ",end= "")
#         j = j + 1
#     k = 1
#     while k <= l:
#         print("*",end = "")
#         k = k + 1
#     print()
#     i = i + 1
#     n = n -1
#     l = l + 2

# i = 1
# l = 1
# while i <= 5:
#     j = 1
#     while j <= 5-i:
#         print(" ",end = "")
#         j = j + 1
#     k = 1
#     while k <= l:
#         print("*",end = "")
#         k = k+1
#     print()
#     l = l + 2
#     i = i + 1

# n = 5
# i = 1
# l = 9
# while n >0:
#     j = 1
#     while j < i:
#         print(" ",end = "")
#         j = j + 1
#     k = 1
#     while k <= l:
#         print("*",end = "")
#         k = k + 1
#     print()
#     l = l - 2
#     i = i + 1
#     n = n - 1

# i = 1
# while i <= 5:
#     j = 1
#     while j <= i:
#         print("*",end = "")
#         j = j + 1
#     print()
#     i = i + 1

# n = 1
# i = 1
# while i <=5:
#     j = 1
#     while j <= 5-i:
#         print(" ",end = "")
#         j = j + 1
#     k = 1
#     while k <= n:
#         print("*",end = "")
#         k = k + 1
#     print()
#     n = n + 1
#     i = i + 1

# n = 4
# while n > 0:
#     k = 1
#     while k <= n:
#         print("*",end = "")
#         k = k+1
#     print()
#     n = n-1

# n = 4
# i = 1
# while n > 0:
#     j = 1
#     while j < i:
#         print(" ",end = "")
#         j = j+1
#     k = 1
#     while k <= n:
#         print("*",end = "")
#         k = k+1
#     print()
#     n = n-1
#     i = i+1

# ********
# ***  ***
# **    **
# *      *

# for i in range(1,5):
#     for j in range(1,8):
#         if j<=5-i or j>=3+i:
#             print("*",end = "")
#         else:
#             print(" ",end = "")
#     print()

# array = ['datascience','AI','ML']
# for i in range(len(array)):
    # if array[i]== "ML":
    #     print(array[i])
    # else:
    #     print("none")
    # print(array[i])

# *****
# *****
# *****
# *****
# *****
# i = 5
# while i>0:
#     j = 1
#     while j<=5:
#         print("*",end = "")
#         j = j+1
#     print()
#     i = i-1

# *****
# *****
# *****
# *****
# *****
# for i in range(1,6):
#     for j in range(1,6):
#         print("*",end = "")
#     print()

# *
# **
# ***
# ****
# *****
# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print("*",end = "")
#     print()

# *****
# ****
# ***
# **
# *
# for i in range(0,5):
#     for j in range(5-i):
#         print("*",end = "")
#     print()
# one more way to write this by using for loop 
# n = 5
# for i in range(n):
#     for j in range(i,n):
#         print("*",end = "")
#     print()

# *
# **
# ***
# ****
# *****
# for i in range(1,6):
#     for j in range(1,6):
#         if j<=i:
#             print("*",end = "")
#             j = j+1
#     print()

# *
# ***
# *****
# for i in range(1,6,2):
#     for j in range(i):
#         print("*",end = "")
#     print()


# for i in range(1,5):
#     for j in range(1,5-i):
#         print(" ",end = "")
#     for j in range(i):
#         print("*",end = " ")
#     print()

# num = 4
# for i in range(0,num):
#     for j in range(0,num-i-1):
#         print(end =" ")
#     for j in range(0,i+1):
#         print("*",end = " ")
#     print()

# num = 5
# for i in range(0,5):
#     for j in range(i):
#         print(end = " ")
#     for j in range(num-i):
#         print("*",end = " ")
#     print()

# i = 1
# l = 5
# while i<=5:
#     j = 1
#     while j<i:
#         print(end = " ")
#         j = j + 1
#     k = 1
#     while k <= l:
#         print("*",end = " ")
#         k = k + 1
#     print()
#     l = l - 1
#     i = i + 1

# for i in range(0,5):
#     for j in range(i):
#         print(" ",end = "")
#     for j in range(5-i):
#         print("*",end = " ")
#     print()

# i = 1
# while i<=5:
#     j = 1
#     while j<i:
#         print(" ",end = "")
#         j = j + 1
#     k = 1
#     while k <=(6-i):
#         print("*",end = " ")
#         k = k + 1
#     print()
#     i = i + 1
    
#    *
#   * *
#  * * *
# * * * *
#  * * *
#   * *
#    *
# r = int(input("enter the number of rows:\n"))
# i = 1
# while r>=i:
#     s = r-i
#     while s>0:
#         print(" ",end = "")
#         s = s - 1
#     st = i
#     while st>0:
#         print("* ",end = "")
#         st = st - 1
#     print()
#     i = i + 1
# i = r - 1
# while i>0:
#     s = r - i
#     while s>0:
#         print(" ",end = "")
#         s = s - 1
#     st = i
#     while st>0:
#         print("* ",end = "")
#         st = st - 1 
#     print()
#     i = i - 1

#    * 
#   * * 
#  * * * 
# * * * * 
#  * * * 
#   * * 
#    * 
# rows = 4
# for i in range(1,rows + 1):
#     space = rows - i
#     print(" "*space + "* "*i)
# for j in range(rows-1,0,-1):
#     space = rows - j 
#     print(" "*space + "* "*j)

# *****
# ****
# ***
# **
# *
# num = int(input("enter the number of rows:\n"))
# for i in range(num,0,-1):
#     for j in range(i):
#         print("*",end = "")
#     print()

# for i in range(1,6):
#     for j in range(6-i):
#         print("*",end = "")
#     print()

#  ***
# *   *
# *   *
# *****
# *   *
# *   *
# *   *


# *****
#  ****
#   ***
#    **
#     *
# n = 5
# for i in range(0,n):
#     for j in range(i):
#         print(" ",end = "")
#     for j in range(n-i):
#         print("*",end = "")
#     print()

# n = 5
# i = 1
# while n>0:
#     j = i - 1
#     while j>0:
#         print(" ",end = "")
#         j = j - 1
#     j = n 
#     while j>0:
#         print("*",end = "")
#         j = j - 1
#     print()
#     n = n - 1
#     i = i + 1

#      *
#     ***
#    *****
#   *******
#  *********
# n = 5
# for i in range(n):
#     for j in range(i,n):
#         print("  ",end = "")
#     for j in range(i+1):
#         print("* ",end = "")
#     for j in range(i):
#         print("* ",end = "")
#     print()

# n = 5
# i = 1
# while n>0:
#     j = n - 1
#     while j>0:
#         print("  ",end = "")
#         j = j - 1
#     k = i 
#     while k>0:
#         print("* ",end = "")
#         k = k - 1
#     j = i - 1
#     while j>0:
#         print("* ",end = "")
#         j = j - 1
#     print()
#     n = n - 1
#     i = i + 1

# * * * * * * * * * 
#   * * * * * * * 
#     * * * * * 
#       * * * 
#         * 
# n = 5
# for i in range(5):
#     for j in range(i):
#         print("  ",end = "")
#     for j in range(n-i):
#         print("* ",end = "")
#     for j in range(n-i-1):
#         print("* ",end = "")
#     print()

# n = 5
# i = 0
# while n>0:
#     j = i
#     while j>0:
#         print("  ",end = "")
#         j = j - 1
#     k = n
#     while k>0:
#         print("* ",end = "")
#         k = k - 1
#     j = n - 1
#     while j>0:
#         print("* ",end = "")
#         j = j - 1
#     print()
#     n = n - 1
#     i = i + 1

# ****
# *  *
# *  *
# ****
# for i in range(4):
#     for j in range(4):
#         if ((j==0 or j==3) or (i==0 or i==3)):
#             print("*",end = "")
#         else:
#             print(" ",end = "")
#     print()

# *
# **
# ***
# ****
# ***
# **
# *
# row = int(input("enter the number of rows:\n"))
# for i in range(1,row+1):
#     print("*"*i)
# for i in range(row-1,0,-1):
#     print("*"*i)

# i = 1
# while i<=4:
#     print("*"*i)
#     i = i + 1
# i = 3
# while i>0:
#     print("*"*i)
#     i = i - 1

# *
# **
# * *
# *  *  
# *   *  
# ******
# row = 6
# for i in range(0,row):
#     for j in range(row):
#         if i==5 or j==0 or i==j:
#             print("*",end = "")
#         else:
#             print(" ",end = "")
#     print()

# row = 1
# while row<=6:
#     j = 1
#     while j<=row:
#         if j==1 or j==row or row==6:
#             print("*",end = "")
#         else:
#             print(" ",end = "")
#         j = j + 1
#     print()
#     row = row + 1

# * * * * * 
#   *     * 
#     *   * 
#       * * 
#         * 
# for i in range(5):
#     for j in range(5):
#         if i ==0 or j==4 or i==j:
#             print("* ",end = "")
#         else:
#             print("  ",end = "")
#     print()

#   * *   * *   
# *     *     * 
# *           * 
#   *       *   
#     *   *     
#       *          
# for row in range(6):
#     for col in range(7):
#         if (row==0 and col%3!=0) or (row==1 and col%3==0) or (row-col==2) or (row+col==8):
#             print("* ",end = "")
#         else:
#             print("  ",end = "")
#     print()

# row = 0
# while row<=5:
#     col = 0
#     while col<=6:
#         if (row==0 and col%3!=0) or (row==1 and col%3==0) or (row-col==2) or (row+col==8):
#             print("* ",end = "")
#         else:
#             print("  ",end = "")
#         col =  col + 1
#     print()
#     row = row + 1

# def sum(a,b,c):
#     return a + b + c
# def printboard(x_state,z_state):
#     zero = "X" if x_state[0] else "O" if z_state[0] else 0
#     one = "X" if x_state[1] else "O" if z_state[1] else 1
#     two = "X" if x_state[2] else "O" if z_state[2] else 2
#     three = "X" if x_state[3] else "O" if z_state[3] else 3
#     four = "X" if x_state[4] else "O" if z_state[4] else 4
#     five = "X" if x_state[5] else "O" if z_state[5] else 5
#     six = "X" if x_state[6] else "O" if z_state[6] else 6
#     seven = "X" if x_state[7] else "O" if z_state[7] else 7
#     eight = "X" if x_state[8] else "O" if z_state[8] else 8
#     print(f"{zero} | {one} | {two}")
#     print("--|---|--")
#     print(f"{three} | {four} | {five}")
#     print("--|---|--")
#     print(f"{six} | {seven} | {eight}")
# def checkwin(x_state,z_state):
#     wins = [[0,1,2],[3,4,5],[6,7,8],[0,4,8],[2,4,6],[0,3,6],[1,4,7],[2,5,8]]
#     for win in wins:
#         if (sum(x_state[win[0]],x_state[win[1]],x_state[win[2]])==3):
#             print("X win's")
#             return 1 
#         if  (sum(z_state[win[0]],z_state[win[1]],z_state[win[2]])==3):
#             print("O win's")
#             return 0
#     return -1
# if __name__ == "__main__":
#     x_state = [0,0,0,0,0,0,0,0,0]
#     z_state = [0,0,0,0,0,0,0,0,0]
#     turn = 1
#     while True:
#         printboard(x_state,z_state)
#         if turn == 1:
#             print("X's turn")
#             value = (int(input("Enter number between from 0 to 8 to mark :\n")))
#             x_state[value] = 1
#         else: 
#             print("O's turn")
#             value = (int(input("Enter number between from 0 to 8 to mark :\n")))
#             z_state[value] = 1
#         cwin = checkwin(x_state,z_state)
#         if (cwin != -1):
#             print("Game Over!")
#             break
#         turn = turn - 1

# *****
#  ***
#   *
# i = 0
# l = 5
# while i<=2:
#     j = i
#     while j>=0:
#         print(" ",end = "")
#         j = j - 1
#     k = l
#     while k>0:
#         print("*",end = "")
#         k = k - 1
#     print()
#     i = i + 1
#     l = l - 2

# for i in range(3):
#     for j in range(5):
#         if i==0 or i==1 and j%4!=0 or i+j==4:
#             print("*",end = "")
#         else:
#             print(" ",end = "")
#     print()

# def sum_common(lst1,lst2,lst3):
#     temp = []
#     temp1 = []
#     result = []
#     for i in lst1:
#         for j in lst2:
#             if i==j:
#                 temp.append(i)
#                 break
#     for i in lst2:
#         for j in lst3:
#             if i==j:
#                 temp1.append(i)
#                 break
#     for i in temp:
#         for j in temp1:
#             if i==j:
#                 result.append(i)
#                 break
#     print(temp)
#     print(temp1)
#     print(result)
# sum_common([1, 2, 2, 3], [5, 3, 2, 2], [7, 3, 2, 2])




