# flappy bird game in python 
# import pygame
# x = pygame.init() # it is initialize all modules of pygame
# # creating window
# gamewindow = pygame.display.set_mode((1000,500))
# pygame.display.set_caption("Flappy Bird Game")
# # game specific variable
# exit_game = False
# game_over = False
# #creating a game loop
# while not exit_game:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit_game = True
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_RIGHT:
#                 print("you have pressed right arrow key")
# pygame.quit()
# quit()

    


# snake game by using pygame in python 
# import pygame
# import random
# pygame.init()
# # for colors numbers of colors difine by a RGB values it is between 0 to 255 
# white = (255,255,255)
# red = (255,0,0)
# black = (0,0,0)
# screen_width = 800
# screen_height = 600
# gamewindow = pygame.display.set_mode((screen_width,screen_height))
# # game title 
# pygame.display.set_caption("Snake Game By Anurag")
# pygame.display.update()
# clock = pygame.time.Clock()
# font = pygame.font.SysFont(None,40)
# def text_screen(text,color,x,y):
#     # render is helps to put high resolution thing to low resolution than it make it better True for use it
#     screen_text = font.render(text,True,color)
#     gamewindow.blit(screen_text,[x,y])
# def plot_snake(gamewindow,color,snake_list,snake_size):
#     for x,y in snake_list:
#         pygame.draw.rect(gamewindow,black,[x,y,snake_size,snake_size])
# # game over loop 
# def game_loop():
#     # game specific variable 
#     exit_game = False
#     game_over = False
#     snake_x = 50
#     snake_y = 50
#     velocity_x = 0
#     velocity_y = 0
#     snake_list = []
#     snake_length = 1
#     hiscore = 0
#     food_x = random.randint(40,screen_width/2)
#     food_y = random.randint(40,screen_height/2)
#     score = 0
#     initialize_velocity = 5
#     snake_size = 20
#     food_size = 20
#     fps = 60
# # game loop 
#     while not exit_game:
#         if game_over:
#             if score > hiscore:
#                 hiscore = score
#             gamewindow.fill(white)
#             text_screen("Game Over!! Press Enter To Continue",red,150,250)
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     exit_game = True
#                 if event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_RETURN:
#                         game_loop()
#         else:
            
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     exit_game = True
#                 if event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_RIGHT:
#                         velocity_x = initialize_velocity
#                         velocity_y = 0
#                     if event.key == pygame.K_LEFT:
#                         velocity_x = - initialize_velocity
#                         velocity_y = 0
#                     if event.key == pygame.K_UP:
#                         velocity_y = - initialize_velocity
#                         velocity_x = 0
#                     if event.key == pygame.K_DOWN:
#                         velocity_y = initialize_velocity
#                         velocity_x = 0
                    
#             snake_x = snake_x + velocity_x
#             snake_y = snake_y + velocity_y
#         # abs gives us abselute value 
#             if abs (snake_x - food_x)<15 and abs (snake_y - food_y)<15:
#                 score = score + 10
#                 food_x = random.randint(20,screen_width/2)
#                 food_y = random.randint(20,screen_height/2)
#                 snake_length = snake_length + 5
                
#             gamewindow.fill(white)
#             text_screen(f"By Anurag and sangeeta: {score} Hiscore {hiscore}",red,5,5)
#             pygame.draw.rect(gamewindow,red,[food_x,food_y,food_size,food_size])
#             # pygame.draw.rect(gamewindow,black,[snake_x,snake_y,snake_size,snake_size])
#             head = []
#             head.append(snake_x)
#             head.append(snake_y)
#             snake_list.append(head)
#             if len(snake_list)>snake_length:
#                 del snake_list[0]
#             if head in snake_list[:-1]:
#                 game_over = True
#             if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
#                 game_over = True
#             plot_snake(gamewindow,black,snake_list,snake_size)
#         pygame.display.update()
#         clock.tick(fps)

#     pygame.quit()
#     quit()
# game_loop()

# fluppy bird game by using pygame 
# import pygame
# import random
# pygame.init()

# width = 900
# height = 500
# fps = 60
# black = (0,0,0)
# white = (255,255,255)
# gray = (128,128,128)
# red = (255,0,0)
# yellow = (255,255,0)
# screen = pygame.display.set_mode([width,height])
# pygame.display.set_caption("Flappy Bird By Anurag")
# time = pygame.time.Clock()
# # variable library
# player_x = 200
# player_y = 200
# y_change = 0
# jump_height = 12
# gravity = .9
# obstacles = [400,700,1000,1300,1600]
# y_positions = []
# generate_places = True
# game_over = False
# def draw_player(x_posi,y_posi):
#     global y_change
#     mouth = pygame.draw.circle(screen,gray,(x_posi + 25 , y_posi + 15),12)
#     play = pygame.draw.rect(screen,white,[x_posi,y_posi,30,30],0,12) # this two next arguments are width of player_x and player_y
#     eye = pygame.draw.circle(screen,black,(x_posi + 24, y_posi + 12),5)
#     jackpack = pygame.draw.rect(screen,white,[x_posi-20,y_posi +1,18,28],2,2)
#     if y_change < 0:
#         flame1 = pygame.draw.rect(screen,red,[x_posi -20,y_posi +29,7,20],0,2)
#         flame1_yellow = pygame.draw.rect(screen,yellow,[x_posi -18,y_posi +30,3,18],0,2)
#         flame2 = pygame.draw.rect(screen,red,[x_posi -10,y_posi +29,7,20],0,2)
#         flame2_yellow = pygame.draw.rect(screen,yellow,[x_posi -8,y_posi +30,3,18],0,2)
#     return play
# def draw_obstacles(obst,y_pos,play):
#     for i in range(len(obst)):
#         y_coord = y_pos[i]
#         top_rect = pygame.draw.rect(screen,gray,[obst[i],0,30,y_coord])
#         top2 = pygame.draw.rect(screen,gray,[obst[i]-3,y_coord-20,36,20],0,5)
#         bot_rect = pygame.draw.rect(screen,gray,[obst[i],y_coord + 200,30,height - (y_coord + 70)])
#         bot2 = pygame.draw.rect(screen,gray,[obst[i]-3,y_coord +200,36,20],0,5)
# running = True
# while running: 
#     time.tick(fps)
#     screen.fill(black)
#     if generate_places:
#         for i in range(len(obstacles)):
#             y_positions.append(random.randint(0,300))
#     player = draw_player(player_x,player_y)
#     draw_obstacles(obstacles,y_positions,player)

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_SPACE:
#                 y_change = -jump_height
#     if player_y + y_change < height - 30:
#         player_y = player_y + y_change
#         y_change = y_change  + gravity 
#     else:
#         player_y = height - 30
#     pygame.display.flip()
#     # display.flip() will update the contents of the entire display
# # display.update() allows to update a portion of the screen, instead of the entire area of the screen. Passing no arguments, updates the entire display
# pygame.quit()
# quit()

# def latter(char):
#     upp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     low = "abcdefghijklmnopqrstuvwxyz"
#     result = ""
#     for i in upp:
#         if char==i:
#             char = char.lower()
#             print(char)
#             result = result + char
#             print(ord(result))
#             break
#     else:
#         result = ""
#         for j in low:
#             if char==j:
#                 char = char.upper()
#                 print(char)
#                 result = result + char
#                 print(ord(result))
# char = input("Enter any aplhabet here in chapital small: ")
# latter(char)

# def replace_vowels(string,sign):
#     vowels = "aeiou"
#     new_str = ""
#     for i in string:
#         for j in vowels:
#             if i==j:
#                string = string.replace(i,sign)
#     print(string)
# replace_vowels("anurag is a good boy","#")

# def find_hig(list):
#     result = 0
#     current_num = 0
#     for i in list:
#         if i>current_num:
#             if result<i:
#                 result = i
#         else:
#             if current_num != 0:
#                 result = current_num
#         current_num = i
#     print(result)
# find_hig([1,5,2,3,7])

#this will return true when all elements present in list is prime number else it will return flase
# def all_prime(list):
#     new_list = []
#     check = True
#     for num in list:
#         if num<2:
#             check = False
#         elif (num>=2):
#             for i in range(2,num):
#                 if num%i==0:
#                     check = False
#                     break
#             else:
#                 check = True
#         if check == True:
#             new_list.append(num)
#     print(new_list)
#     if len(new_list)==len(list):
#         print(True)
#     else:
#         print(False)
# all_prime([2, 3, 5, 7, 13, 17, 19, 23, 4])

# it check whether string statement is right or wrong
# s = "x - 9 = 10"
# s1 = s.split()
# print(s1)
# sum = 0
# i = 0
# match = False
# if int(s1[4])<int(s1[2]) and s1[1]=="+":
#     while (match!=True):
#         sum = i + int(s1[2])
#         if sum==int(s1[4]):
#             print(i)
#             match = True
#         i = i - 1
# elif s1[1]=="+":
#     while match!=True:
#         sum = i + int(s1[2])
#         if sum==int(s1[4]):
#             print(i)
#             match = True
#         i = i + 1
# if s1[1]=="-":
#     while (match!=True):
#         if i-int(s1[2])==int(s1[4]):
#             print(i)
#             match = True
#         i = i + 1

#this is as same as privious code but the only change is it's deal with a list
# s = ["1 + 1 = 2", "2 + 2 = 3", "5 * 5 = 25", "3 / 3 = 1"]
# new_list = []
# for i in s:
#     s2 = i.split()
#     a = int(s2[0])
#     b = int(s2[2])
#     if s2[1]=="+":
#         sum = a+b
#     if s2[1]=="-":
#         sum = a-b
#     if s2[1]=="*":
#         sum = a*b
#     if s2[1]=="/":
#         sum = a/b
#     if sum==int(s2[4]):
#         new_list.append(i)
# print(new_list)

#legendre's formula in python
# def legendre(p,n):
#     i = 1
#     sum = 0
#     while i!=0:
#         add = p**i
#         if n>add:
#             sum = sum + (n/add)
#             i = i+1
#         else:
#             print(sum)
#             return i == 0
# legendre(2,128)

#this function give colour of squares in chess board 
# def chess_board(str):
#     a = int(str[1])
#     b = str[0]
#     print(b)
#     print(a)
#     list = ["a","b","c","d","e","f","g","h"]
#     for i in range(len(list)):
#         if list[i]==b:
#             c = i+1
#     if c%2!=0 and a%2!=0 or c%2==0 and a%2==0:
#         print("black")
#     else:
#         print("white")
# chess_board("f5")
            
#it gives sum of three values
# def simple_equation(a, b, c):
#     list = [a,b,c]
#     new_list = []
#     sum = []
#     temp = []
#     for i in range(len(list)):
#         sum.append(list[i])
#         for index,j in enumerate(range(len(list))):
#             if i==index:
#                 new_list.append(list[j])
#             else:
#                 temp.append(list[j])
#         if temp[0]+temp[1]==sum[0]:
#             print(f"{temp[0]}+{temp[1]}={sum[0]}")
#         if temp[1]-temp[0]==sum[0]:
#             print(f"{temp[0]}-{temp[1]}={sum[0]}")
#         if temp[1]/temp[0]==sum[0]:
#             print(f"{temp[0]}/{temp[1]}={sum[0]}")
#         if temp[0]*temp[1]==sum[0]:
#             print(f"{temp[0]}*{temp[1]}={sum[0]}")
#         # print(sum)
#         # print(temp)
#         sum.clear()
#         temp.clear()
# simple_equation(2,2,4)
            
#it gives highest number of the list
# def find_high(list):
#     max = list[0]
#     current = list[0]
#     for i in range(len(list)):
#         if (list[i]>=current):
#             if list[i]>=max:
#                 max = list[i]
#             current = list[i]
#     print(max)
# find_high([87])

#this return max alphabet count in a list or every alphabet has a equal value then it return's None
# def majority_vote(list):
#     count = 0
#     dict = {}
#     match = []
#     set_list = set()
#     for i in list:
#         set_list.add(i)
#     for i in set_list:
#         for j in list:
#             if i==j:
#                 count = count + 1
#         dict[i]=count
#         count = 0
#     current = -float("inf")
#     max_value = -float("inf")
#     max_key = None
#     for key,value in dict.items():
#         if value>current:
#             current = value
#             if max_value<value:
#                 max_value = value
#                 max_key = key
#     for value in dict.values():
#         match.append(value)
#     if match==[]:
#         print(None)
#     else:
#         current_min = match[0]
#         min_key = match[0]
#         for i in range(len(match)):
#             if current_min>match[i]:
#                 current_min = match[i]
#                 if min_key>current_min:
#                     min_key = current_min
#         if min_key==max_value:
#             print(None)
#         else:
#             print(max_key)  
# majority_vote(["A", "B", "B", "A", "C", "C"]) # this will return None
# majority_vote(["A", "A", "B", "B", "A", "C", "C"]) # this will return A

#this return the number powerfull or not using prime factor prime factor is prime number and factor means that number come in the prime numbers table.
# def is_powerful(n):
#     temp = []
#     valid = []
#     n_count = 0
#     s = str(n)
#     for i in s:
#         n_count += 1
#     for i in range(1,n):
#         if i>1:
#             for j in range(2,i):
#                 if i%j==0:
#                     break
#             else:
#                 if n%i==0:
#                     temp.append(i)
#                     check = i**n_count
#                     if n%check==0:
#                         valid.append(True)
#     if (len(temp)==len(valid)):
#         return True
#     else:
#         return False
# a = is_powerful(674)
# print(a)

#code to create box in box
# def rep_set(n):
#     final = []
#     for i in range(n):
#         temp1 = []
#         temp2 = []
#         for j in range(i):
#             for k in range(j):
#                 temp1.append([])
#             temp2.append(temp1)
#             temp1 = []
#         final.append(temp2)
#         temp2 = []
#     return final
# a = rep_set(3)
# print(a)
            
                    
