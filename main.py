import pygame as pg
import guest as g
import rr as r
import constants as c

import butt as b
''' 
    In this file we will crea the scren, insert the image of the AXC campus, the logo and the icon which does not mutate.
    the second part is the look and here we insert the room and the user

'''

user2 = g.User2('imagenes/Alex.png')
user = g.User('imagenes/Dirk.png')

pg.init()
pg.display.set_caption(c.ORIGINAL_CAPTION)
SCREEN = pg.display.set_mode(c.SCREEN_SIZE)
Logo = pg.image.load("imagenes/Logo.png").convert()
icon = pg.image.load("imagenes/logo_ICO.png")
pg.display.set_icon(icon)
clock = pg.time.Clock()

roomActual = r.State()
access = True




while access == True:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            access = False

    SCREEN.fill(c.WHITE)
    SCREEN.blit(Logo,[900,25])



    # user.handle_event(event, roomActual.AreaActual)
    # roomActual.setup_Room(SCREEN, user)



    user.handle_event(event, roomActual.AreaActual)
    roomActual.setup_Room(SCREEN,user2)
    SCREEN.blit(user.image, user.rect)
    SCREEN.blit(user2.image, user2.rect)

    if user2.rect.colliderect(user):
        b.gameMenu(SCREEN, event)



    pg.display.flip()
    clock.tick(60)

pg.quit ()
