import random
import pygame
import os

pygame.mixer.init()
pygame.init()


print("THIS IS MADE BY RAJA SINGH")

#display
game_window = pygame.display.set_mode((700,400))
pygame.display.set_caption("MADE BY - RAGHAV ROY -")
pygame.display.update()

#colour
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
new = (3,0,9)

#variable

init_vilocity = 5
d_writh = 390
d_hight = 690
#g bg
bgimg = pygame.image.load("wallpaper/wallpaper1.jpg")
bgimg = pygame.transform.scale(bgimg,(700,400)).convert_alpha()
#w gb
bgimg1 = pygame.image.load("wallpaper/wallpaper2.jpg")
bgimg1 = pygame.transform.scale(bgimg1,(700,400)).convert_alpha()
#game over
bgimg2 = pygame.image.load("wallpaper/wallpaper3.jpg")
bgimg2 = pygame.transform.scale(bgimg2,(700,400)).convert_alpha()
time = pygame.time.Clock()
font = pygame.font.SysFont(None,17)
font1 = pygame.font.SysFont(None,32)
font2 = pygame.font.SysFont(None,22)
#functions
def display_score(text,colour,x,y):
    screen_txt = font.render(text,True,colour)
    game_window.blit(screen_txt, [x,y])
    game_window.blit(screen_txt, [x,y])

def display_score1(text,colour,x,y):
    screen_txt = font1.render(text,True,colour)
    game_window.blit(screen_txt, [x,y])
    game_window.blit(screen_txt, [x,y])

def display_score2(text,colour,x,y):
    screen_txt = font2.render(text,True,colour)
    game_window.blit(screen_txt, [x,y])
    game_window.blit(screen_txt, [x,y])

def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def welcome():
    exit_game = False
    while not exit_game:
        game_window.blit(bgimg1, (0, 0))
        #game_window.fill((3,0,9))
        display_score2("MADE BY -( RAGHAV ROY )-", white, 10, 10)
        display_score1("  \n W_ELCOME \n", white, 260, 160)
        display_score1("- - { THUNDER SNAKE } - -", white, 210, 200)
        display_score1("\n\n\n\n\n\n\n\n\n\n\n\n  \n", white, 220, 240)
        display_score2("           press space - \n\n\n\n\n\n -bar to play", white, 400, 360)
        # display_score("\Press Space Bar To Play", black, 220, 240)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop()
                exit_game = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('sounds/tap.mp3')
                    pygame.mixer.music.play(5)
                    pygame.mixer.music.load('sounds/tap.mp3')
                    pygame.mixer.music.play(5)
                    pygame.mixer.music.load('sounds/tap.mp3')
                    pygame.mixer.music.play(5)
                    pygame.mixer.music.load('sounds/tap.mp3')
                    pygame.mixer.music.play(5)
                    loop()


        pygame.display.update()
        time.tick(60)
#game_data
def loop():
#variabales
    snack_list = []
    snack_length = 1
    exit_game = False
    game_over = False
    game_score = 0
    snack_x = 85
    snack_y = 99
#check file hiscore

    if(not os.path.exists("snake_score.txt")):
        with open("snake_score.txt","w") as f:
            f.write("0")
    with open("snake_score.txt","r") as f:
             hiscore = f.read()
    snack_size = 10
    fps = 30
    vilocity_x = 0
    vilocity_y = 0
    food_x = random.randint(20,650)
    food_y = random.randint(20,350)
# loop
    while not exit_game:

        if game_over:

            with open("snake_score.txt", "w") as f:
                f.write(str(hiscore))

            game_window.fill(new)
            game_window.blit(bgimg2, (0, 0))
            display_score1("\n Game Over! \n", white, 250, 160 )
            display_score1("\n-\n-\n-\n-\n-\n-\n-\n-\n-\n-\n-\n-\n-\n-\n-\n-\n-\n", white, 190, 200)
            display_score1(f"SCORE - {game_score}",white,220, 250)
            display_score2("\n press | ENTER | to Continue! \n", white, 400,360)


            for event in pygame.event.get():


                 if event.type == pygame.QUIT:
                    exit_game = True

                 if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.mixer.music.load('sounds/tap.mp3')
                        pygame.mixer.music.play()
                        loop()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN :
                        if event.key == pygame.K_RIGHT:
                            #pygame.mixer.music.load('play_key.wav')
                            #pygame.mixer.music.play()
                            vilocity_x = init_vilocity
                            vilocity_y = 0

                        if event.key == pygame.K_LEFT:
                            #pygame.mixer.music.load('play_key.wav')
                            #pygame.mixer.music.play()
                            vilocity_x = - init_vilocity
                            vilocity_y = 0

                        if event.key == pygame.K_DOWN:
                            #pygame.mixer.music.load('play_key.wav')
                            #pygame.mixer.music.play()
                            vilocity_y = + init_vilocity
                            vilocity_x = 0

                        if event.key == pygame.K_UP:
                            # pygame.mixer.music.load('play_key.wav')
                            # pygame.mixer.music.play()
                            vilocity_y = - init_vilocity
                            vilocity_x = 0

                        if event.key == pygame.K_s:
                            # pygame.mixer.music.load('play_key.wav')
                            # pygame.mixer.music.play()
                            game_score += 10

                        if event.key == pygame.K_l:
                            snack_length += 5

            snack_x = snack_x + vilocity_x
            snack_y = snack_y + vilocity_y

            #eat and score
            if abs(snack_x -food_x)<8 and abs(snack_y - food_y)<8:
                game_score += 10
                #pygame.mixer.music.load('eat_food.mp3')
                #pygame.mixer.music.play()
                food_x = random.randint(20, 670 )
                food_y = random.randint(20,370)
                snack_length +=5

            if game_score>int(hiscore):
                    hiscore = game_score
        #display details
            game_window.fill(black)
            game_window.blit(bgimg, (0,0))
            display_score("score: " + str(game_score),white, 5, 5)
            display_score("Lenght: " + str(snack_length),white,5,20)
            display_score("( Hi-score ) -  " + str(hiscore),white, 5, 35)
            head = []
            head.append(snack_x)
            head.append(snack_y)
            snack_list.append(head)

            if len(snack_list)>snack_length:
                del snack_list[0]
            if head in snack_list[:-1]:
                game_over = True
                pygame.mixer.music.load('sounds/eate.mp3')
                pygame.mixer.music.play()

            if snack_x < 0 or snack_x > d_hight or snack_y < 0 or snack_y > d_writh:
                game_over = True
                pygame.mixer.music.load('sounds/eate.mp3')
                pygame.mixer.music.play()
            plot_snake(game_window, white, snack_list, snack_size)
        pygame.draw.rect(game_window,red,[food_x,food_y,snack_size,snack_size])
        plot_snake(game_window, white, snack_list, snack_size)


        pygame.display.update()
        time.tick(fps)



    pygame.quit()
    quit()

welcome()
a = input()
