'''
-----------------------------------------------------------------------------
Program Name: (never put your personal name or information on the Internet)
Program Description:

-----------------------------------------------------------------------------
References:

(put a link to your reference here but also add a comment in the code below where you used the reference)

-----------------------------------------------------------------------------

Additional Libraries/Extensions:

(put a list of required extensions so that the user knows that they need to download extra features)

-----------------------------------------------------------------------------

Known bugs:

(put a list of known bugs here, if you have any)

----------------------------------------------------------------------------


Program Reflection:
I think this project deserves a level XXXXXX because ...

 Level 3 Requirements Met:
• 
•  
•  
•  
•  
• 

Features Added Beyond Level 3 Requirements:
• 
•  
•  
•  
•  
• 
-----------------------------------------------------------------------------
'''

# *********SETUP**********
import pygame
pygame.init()


# *********WINDOW CODE**********
WindowWidth = 1000
WindowHeight = 667

window = pygame.display.set_mode((WindowWidth, WindowHeight)) #CREATES WINDOWS
clock = pygame.time.Clock()

# *********VARIABLES**********

BLACK = (0,0,0) #CREATES COLOUR VARABLE FOR BLACK
WHITE = (250,250,250)
State = "HOME"

HomeBg = pygame.image.load("HomeBg.png")
MenuTitle =  pygame.image.load("images/title.png")
InstructionsImage =  pygame.image.load("images/instructions.png")
font = pygame.font.Font("fonts/minecraft.ttf", 46) #LOADS FONT 
InstructionsButton = pygame.image.load("images/buttonHowTo.png")
Frog = pygame.image.load("images/run01.png")
Saw = pygame.image.load("images/saw01.png")

#*********RESIZE*************

Frog_resize = pygame.transform.scale(Frog, (96, 96))

# *********MAIN LOOP**********
Running = True
while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False

    if State == "HOME": #CHECKS TO SEE IF THE CURRENT STATE IS HOME
        window.blit(HomeBg, (0,0)) #PUTS HOME PAGE BACKGROUND ON SCREEN
        window.blit(MenuTitle, (0,0))
        window.blit(InstructionsImage, (0,120))

        Instructions_Rect = pygame.Rect(120, 500, 760, 300)
        window.blit(InstructionsButton, (120, 500))


        Instructions1 = "Jump Over Obstacles"
        Instructions2 = "Collect powerups"
        RenderText1 = font.render(Instructions1,1, pygame.Color(BLACK))
        RenderText2 = font.render(Instructions2,1, pygame.Color(BLACK))
        window.blit(RenderText1, (500, 160))
        window.blit(RenderText2, (500, 260))

        StartButton = "Press to Start"
        RenderText3 = font.render(StartButton,1, pygame.Color(BLACK))
        window.blit(RenderText3, (320, 380))
        Start_Rect = pygame.Rect(0,0, 1000, 400)

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            click_pos = event.pos
            if Start_Rect.collidepoint(click_pos): #CHECKS TO SEE IF MOUSE POSITION IS COLLIDING WITH THE START BUTTON RECTANGLE 
                State = "GAME"
                print(State)

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            click_pos = event.pos
            if Instructions_Rect.collidepoint(click_pos):#CHECKS TO SEE IF MOUSE POSITION IS COLLIDING WITH THE INSTRUCTIONS BUTTON RECTANGLE 
                State = "INSTRUCTIONS"
                print(State)

    if State == "GAME": #CHECKS TO SEE IF THE CURRENT STATE IS GAME
        window.fill(BLACK)
        window.blit(HomeBg, (0,0))
        window.blit(Frog_resize, (100, 200))
        window.blit(Saw, (400, 399))


    if State == "INSTRUCTIONS":#CHECKS TO SEE IF THE CURRENT STATE IS INSTRUCTIONS
        window.fill(WHITE)
        HowToPlay1 = "Click on the space button to make" #CREATES VARIABLE TO STORE INSTRUCTIONS
        HowToPlay2 = "the player jump over the hurdles"
        HowToPlay3 = "Avoid getting hurt to survive"
        
        RenderText4 = font.render(HowToPlay1,1, pygame.Color(BLACK))
        RenderText5 = font.render(HowToPlay2,1, pygame.Color(BLACK))
        RenderText6 = font.render(HowToPlay3,1, pygame.Color(BLACK))
        window.blit(RenderText4, (120, 160)) #BLITS INSTRUCTIONS ONTOTHE INSTRUCTIONS SCREEN 
        window.blit(RenderText5, (120, 260))
        window.blit(RenderText6, (160, 360))

# *********FRAMES**********

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
