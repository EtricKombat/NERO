import pygame as pg
import guest
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
            if action == "eat":
                eat(screen)
            elif action == "hear1":
                hear(screen)

            elif action == "see1":
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
    TextRect.center = (650,350)
    SCREEN.blit(TextSurf, TextRect)

def eat(screen):
    message_display("It has no taste", screen)

def see(screen):


    message_display("hi Iam " + c.UserDict[c.usuario][0], screen)

def touch(screen):
    message_display("It is tough and solid", screen)

def smell(screen):
    message_display("It smells like soil", screen)

def hear( screen):

        message_display("This is the AXC " , screen)

def gameMenu(screen, event):

        button("who are you?", 350, 700, 200, 50, c.COMBLUE, c.SKY_BLUE, screen, event, "see1")
        button("What room is this? ", 650, 700, 250, 50, c.COMBLUE, c.SKY_BLUE, screen, event, "hear1")

