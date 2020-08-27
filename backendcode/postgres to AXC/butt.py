import pygame as pg
import guest
import psql as p
# import room
import constants as c

def text_objects(text, font):
    textSurface = font.render(text, True, c.BLACK)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac, screen, event, action=None):
    mouse = pg.mouse.get_pos()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pg.draw.rect(screen, ac,(x,y,w,h))
        if event.type == pg.MOUSEBUTTONDOWN and action != None:
          if action == "hear":
                hear(screen)

          elif action == "see":
                see(screen)

    else:
        pg.draw.rect(screen, ic,(x,y,w,h))

    smallText = pg.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)

def message_display(text,SCREEN):
    largeText = pg.font.Font('freesansbold.ttf',20)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (650,550)
    SCREEN.blit(TextSurf, TextRect)



def see(screen):


    message_display("hi Iam Pomologist" , screen)


def hear( screen):

        message_display(p.create_database() , screen)

def gameMenu(screen, event):

        button("who are you?", 350, 700, 200, 50, c.COMBLUE, c.SKY_BLUE, screen, event, "see")
        button("which is the best apple? ", 650, 700, 250, 50, c.COMBLUE, c.SKY_BLUE, screen, event, "hear")

