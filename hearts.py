
#pygame hearts
#gets you started to draw a valentine's day card

import pygame #gaming module (aka library) 
pygame.init() #initializes Pygame
pygame.display.set_caption("Valentine's day card") #sets the window title
screen = pygame.display.set_mode((800, 800)) #creates game screen
font = pygame.font.Font('freesansbold.ttf', 32) #load font
img = pygame.image.load("dog.jpg") #make sure this is saved to the same folder as your code


#first Heart
pygame.draw.circle(screen, (250,0,0), (180, 200), 20) #top left circle
pygame.draw.circle(screen, (250,0,0), (220, 200), 20) #top right circle
pygame.draw.polygon(screen, (250,0,0), ((160, 205),(239, 205), (200, 250))) #triangle to form base

#text
text1 = font.render('I Love You!', True, (250, 100, 100)) #numbers give color
text2 = font.render('Happy Valentines Day', True, (250, 0, 0), (200,150,150)) #this one includes background color
screen.blit(text1, (200, 100)) #numbers give position
screen.blit(text2, (400, 300))

#image
screen.blit(img, (0, 400))#draw pic

pygame.display.flip() #this flips all those shapes onto the game screen (needed for every game)
pygame.time.wait(5000) #pause so screen stays up (no game loop)



