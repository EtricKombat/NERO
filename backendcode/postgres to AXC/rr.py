import pygame as pg
import constants as c
import guest as g
import time


class State(pg.sprite.Sprite):
    """project the room"""

    def __init__(self):
        self.Seccion = 'WelcomeSeccion'
        self.AreaActual = 'WelcomeArea'
        self.font = pg.font.Font('freesansbold.ttf', 32)
        self.text = self.font.render(c.Room_dict[self.AreaActual][0], True, c.WHITE, c.GREY)
        self.textRect = self.text.get_rect()
        self.textRect.center = (550, 350)

    def setup_map(self, sc):
        self.Map = pg.image.load(c.Seccion_dict[self.Seccion][0]).convert()
        self.imageMap = sc.blit(self.Map, [10, 20])

    def setup_txt(self, sc):
        self.font = pg.font.Font('freesansbold.ttf', 32)
        self.text = self.font.render(c.Room_dict[self.AreaActual][0], True, c.WHITE, c.GREY)
        self.textRect = self.text.get_rect()
        self.textRect.center = (550, 350)
        self.txt = sc.blit(self.text, self.textRect)

    def setup_Room(self, sc, user):
        ''' drawing of the type room'''

        typeroom = c.Room_dict[self.AreaActual][1]

        if typeroom == 'roomtype1':
            self.room = pg.draw.polygon(sc, c.GREY, c.coord_room[typeroom], 0)
            self.wall1 = pg.draw.line(sc, c.NAVYBLUE, (424, 70), (674, 70), 5)
            self.wall2 = pg.draw.line(sc, c.NAVYBLUE, (674, 70), (851, 246), 7)
            self.wall3 = pg.draw.line(sc, c.NAVYBLUE, (851, 246), (851, 496), 5)
            self.wall4 = pg.draw.line(sc, c.NAVYBLUE, (851, 496), (674, 673), 7)
            self.wall5 = pg.draw.line(sc, c.NAVYBLUE, (674, 673), (424, 673), 5)
            self.wall6 = pg.draw.line(sc, c.NAVYBLUE, (424, 673), (248, 496), 7)
            self.wall7 = pg.draw.line(sc, c.NAVYBLUE, (248, 496), (248, 246), 5)
            self.wall8 = pg.draw.line(sc, c.NAVYBLUE, (248, 246), (424, 70), 7)
            self.Door_Seeing_Space = pg.draw.line(sc, c.Seccion_dict['SeeingSpace'][1], (276 + 248, 70),
                                                  (326 + 248, 70), 10)
            self.Door_Food_SC = pg.draw.line(sc, c.Seccion_dict['FoodSupplyChain'][1], (248, 276 + 70), (248, 326 + 70),
                                             10)
            self.Door_Carbon_Capture = pg.draw.line(sc, c.Seccion_dict['CarbonCapture'][1], (603 + 248, 276 + 70),
                                                    (603 + 248, 326 + 70), 10)
            self.Door_Edible_Digital = pg.draw.line(sc, c.Seccion_dict['EdibleDigital'][1], (497 + 248, 532 + 70),
                                                    (532 + 248, 497 + 70), 10)
            self.Door_FoodLab = pg.draw.line(sc, c.Seccion_dict['FoodLab'][1], (106 + 248, 532 + 70),
                                             (70 + 248, 497 + 70), 10)
            self.Door_Toolshop = pg.draw.line(sc, c.Seccion_dict['Toolshop'][1], (106 + 248, 70 + 70),
                                              (70 + 248, 106 + 70), 10)
            self.Door_Building_Int = pg.draw.line(sc, c.Seccion_dict['BIA'][1], (497 + 248, 70 + 70),
                                                  (532 + 248, 106 + 70), 10)
            self.Door_Exit = pg.draw.line(sc, c.SKY_BLUE, (276 + 248, 673), (326 + 248, 673), 10)

        if typeroom == 'roomtype2':
            self.room = pg.draw.circle(sc, c.NAVYBLUE, (550, 375), 305)
            self.room = pg.draw.circle(sc, c.GREY, (550, 375), 300)
            self.Door_OUT = pg.draw.line(sc, c.Seccion_dict[self.Seccion][1], (495, 675), (595, 675), 10)

        if typeroom == 'roomtype3':

            def roomh2(x, y):
                count = 1
                while (count < 10):
                     pg.draw.rect(sc, c.GREY, [x, y, 40, 40])
                     pg.draw.rect(sc, c.BLACK, [x, y, 40, 40], 3)
                     door1 = pg.draw.line(sc, c.RED, (x, y + 10), (x, y + 30), 3)
                     door2 = pg.draw.line(sc, c.RED, (x + 40, y + 10), (x + 40, y + 30), 3)
                     if user.rect.colliderect(door1):
                         user.rect.x += 60
                     if user.rect.colliderect(door2):
                         user.rect.x -= 60
                     count = count + 1
                     x = x + 70

            roomh2(270, 120)

            def roomh3(x, y):
                count = 1
                while (count < 8):
                     pg.draw.rect(sc, c.GREY, [x, y, 40, 40])
                     pg.draw.rect(sc, c.BLACK, [x, y, 40, 40], 3)
                     door1 = pg.draw.line(sc, c.RED, (x, y + 10), (x, y + 30), 3)
                     door2 = pg.draw.line(sc, c.RED, (x + 40, y + 10), (x + 40, y + 30), 3)
                     if user.rect.colliderect(door1):
                         user.rect.x += 60
                     if user.rect.colliderect(door2):
                         user.rect.x -= 60
                     count = count + 1
                     x = x + 70

            roomh3(340, 190)

            def roomh7(x, y):
                count = 1
                while (count < 16):
                     pg.draw.rect(sc, c.GREY, [x, y, 40, 40])
                     pg.draw.rect(sc, c.BLACK, [x, y, 40, 40], 3)
                     door1 = pg.draw.line(sc, c.RED, (x, y + 10), (x, y + 30), 3)
                     door2 = pg.draw.line(sc, c.RED, (x + 40, y + 10), (x + 40, y + 30), 3)
                     if user.rect.colliderect(door1):
                         user.rect.x += 60
                     if user.rect.colliderect(door2):
                         user.rect.x -= 60
                     count = count + 1
                     x = x + 70

            roomh7(130, 470)

            def roomh8(x, y):
                count = 1
                while (count < 4):
                     pg.draw.rect(sc, c.GREY, [x, y, 40, 40])
                     pg.draw.rect(sc, c.BLACK, [x, y, 40, 40], 3)
                     door1 = pg.draw.line(sc, c.RED, (x, y + 10), (x, y + 30), 3)
                     door2 = pg.draw.line(sc, c.RED, (x + 40, y + 10), (x + 40, y + 30), 3)
                     if user.rect.colliderect(door1):
                         user.rect.x += 60
                     if user.rect.colliderect(door2):
                         user.rect.x -= 60
                     count = count + 1
                     x = x + 70

            roomh8(480, 540)

            def roomh10(x, y):
                count = 1
                while (count < 13):
                     pg.draw.rect(sc, c.GREY, [x, y, 40, 40])
                     pg.draw.rect(sc, c.BLACK, [x, y, 40, 40], 3)
                     door1 = pg.draw.line(sc, c.RED, (x, y + 10), (x, y + 30), 3)
                     door2 = pg.draw.line(sc, c.RED, (x + 40, y + 10), (x + 40, y + 30), 3)
                     if user.rect.colliderect(door1):
                         user.rect.x += 60
                     if user.rect.colliderect(door2):
                         user.rect.x -= 60
                     count = count + 1
                     x = x + 70

            roomh10(200, 680)

            def roomv(x, y):
                global user
                count = 1
                while (count < 12):
                     pg.draw.rect(sc, c.GREY, [x, y, 40, 40])
                     pg.draw.rect(sc, c.BLACK, [x, y, 40, 40], 3)
                     door1 = pg.draw.line(sc, c.RED, (x + 10, y), (x + 30, y), 3)
                     door2 = pg.draw.line(sc, c.RED, (x + 10, y + 40), (x + 30, y + 40), 3)
                     # if user.rect.colliderect(door1):
                     #     user.rect.y += 60
                     # if user.rect.colliderect(door2):
                     #     user.rect.y -= 60

                     count = count + 1
                     y = y + 70

            roomv(550, 50)

            self.Door_OUT = pg.draw.line(sc, c.PURPLE, (550+10, 790), (550+30, 790), 6)
        if typeroom == 'roomtype4':
            def roomv(x, y):
                global user
                count = 1
                while (count < 8):
                    pg.draw.rect(sc, c.GREY, [x, y, 40, 40])
                    pg.draw.rect(sc, c.BLACK, [x, y, 40, 40], 3)
                    door1 = pg.draw.line(sc, c.RED, (x + 10, y), (x + 30, y), 3)
                    door2 = pg.draw.line(sc, c.RED, (x + 10, y + 40), (x + 30, y + 40), 3)
                    # if user.rect.colliderect(door1):
                    #     user.rect.y += 60
                    # if user.rect.colliderect(door2):
                    #     user.rect.y -= 60

                    count = count + 1
                    y = y + 70

            roomv(550, 330)

            def roomh10(x, y):
                count = 1
                while (count < 13):
                    pg.draw.rect(sc, c.GREY, [x, y, 40, 40])
                    pg.draw.rect(sc, c.BLACK, [x, y, 40, 40], 3)
                    door1 = pg.draw.line(sc, c.RED, (x, y + 10), (x, y + 30), 3)
                    door2 = pg.draw.line(sc, c.RED, (x + 40, y + 10), (x + 40, y + 30), 3)
                    if user.rect.colliderect(door1):
                        user.rect.x += 60
                    if user.rect.colliderect(door2):
                        user.rect.x -= 60
                    count = count + 1
                    x = x + 70

            roomh10(200, 680)
            self.Door_OUT = pg.draw.line(sc, c.BLACK, (550 + 10, 790), (550 + 30, 790), 6)
        if typeroom == 'roomtype5':
            def roomv(x, y):
                global user
                count = 1
                while (count < 9):
                    pg.draw.rect(sc, c.GREY, [x, y, 40, 40])
                    pg.draw.rect(sc, c.BLACK, [x, y, 40, 40], 3)
                    door1 = pg.draw.line(sc, c.RED, (x + 10, y), (x + 30, y), 3)
                    door2 = pg.draw.line(sc, c.RED, (x + 10, y + 40), (x + 30, y + 40), 3)
                    # if user.rect.colliderect(door1):
                    #     user.rect.y += 60
                    # if user.rect.colliderect(door2):
                    #     user.rect.y -= 60

                    count = count + 1
                    y = y + 70

            roomv(550, 260)

            def roomh10(x, y):
                count = 1
                while (count < 13):
                    pg.draw.rect(sc, c.GREY, [x, y, 40, 40])
                    pg.draw.rect(sc, c.BLACK, [x, y, 40, 40], 3)
                    door1 = pg.draw.line(sc, c.RED, (x, y + 10), (x, y + 30), 3)
                    door2 = pg.draw.line(sc, c.RED, (x + 40, y + 10), (x + 40, y + 30), 3)
                    if user.rect.colliderect(door1):
                        user.rect.x += 60
                    if user.rect.colliderect(door2):
                        user.rect.x -= 60
                    count = count + 1
                    x = x + 70

            roomh10(200, 680)
            def roomh9(x, y):
                count = 1
                while (count < 16):
                    pg.draw.rect(sc, c.GREY, [x, y, 40, 40])
                    pg.draw.rect(sc, c.BLACK, [x, y, 40, 40], 3)
                    door1 = pg.draw.line(sc, c.RED, (x, y + 10), (x, y + 30), 3)
                    door2 = pg.draw.line(sc, c.RED, (x + 40, y + 10), (x + 40, y + 30), 3)
                    if user.rect.colliderect(door1):
                        user.rect.x += 60
                    if user.rect.colliderect(door2):
                        user.rect.x -= 60
                    count = count + 1
                    x = x + 70

            roomh9(60, 470)
            self.Door_OUT = pg.draw.line(sc, c.ORANGE, (550 + 10, 790), (550 + 30, 790), 6)
        if typeroom == 'roomtype6':
            def roomv(x, y):
                global user
                count = 1
                while (count < 9):
                    pg.draw.rect(sc, c.GREY, [x, y, 40, 40])
                    pg.draw.rect(sc, c.BLACK, [x, y, 40, 40], 3)
                    door1 = pg.draw.line(sc, c.RED, (x + 10, y), (x + 30, y), 3)
                    door2 = pg.draw.line(sc, c.RED, (x + 10, y + 40), (x + 30, y + 40), 3)
                    # if user.rect.colliderect(door1):
                    #     user.rect.y += 60
                    # if user.rect.colliderect(door2):
                    #     user.rect.y -= 60

                    count = count + 1
                    y = y + 70

            roomv(550, 260)

            def roomh10(x, y):
                count = 1
                while (count < 13):
                    pg.draw.rect(sc, c.GREY, [x, y, 40, 40])
                    pg.draw.rect(sc, c.BLACK, [x, y, 40, 40], 3)
                    door1 = pg.draw.line(sc, c.RED, (x, y + 10), (x, y + 30), 3)
                    door2 = pg.draw.line(sc, c.RED, (x + 40, y + 10), (x + 40, y + 30), 3)
                    if user.rect.colliderect(door1):
                        user.rect.x += 60
                    if user.rect.colliderect(door2):
                        user.rect.x -= 60
                    count = count + 1
                    x = x + 70

            roomh10(200, 680)

            def roomh9(x, y):
                count = 1
                while (count < 16):
                    pg.draw.rect(sc, c.GREY, [x, y, 40, 40])
                    pg.draw.rect(sc, c.BLACK, [x, y, 40, 40], 3)
                    door1 = pg.draw.line(sc, c.RED, (x, y + 10), (x, y + 30), 3)
                    door2 = pg.draw.line(sc, c.RED, (x + 40, y + 10), (x + 40, y + 30), 3)
                    if user.rect.colliderect(door1):
                        user.rect.x += 60
                    if user.rect.colliderect(door2):
                        user.rect.x -= 60
                    count = count + 1
                    x = x + 70

            roomh9(60, 470)
            self.Door_OUT = pg.draw.line(sc, c.RED, (550 + 10, 790), (550 + 30, 790), 6)
        if typeroom == 'roomtype7':
            def roomv(x, y):
                global user
                count = 1
                while (count < 9):
                    pg.draw.rect(sc, c.GREY, [x, y, 40, 40])
                    pg.draw.rect(sc, c.BLACK, [x, y, 40, 40], 3)
                    door1 = pg.draw.line(sc, c.RED, (x + 10, y), (x + 30, y), 3)
                    door2 = pg.draw.line(sc, c.RED, (x + 10, y + 40), (x + 30, y + 40), 3)
                    # if user.rect.colliderect(door1):
                    #     user.rect.y += 60
                    # if user.rect.colliderect(door2):
                    #     user.rect.y -= 60

                    count = count + 1
                    y = y + 70

            roomv(550, 260)

            def roomh10(x, y):
                count = 1
                while (count < 13):
                    pg.draw.rect(sc, c.GREY, [x, y, 40, 40])
                    pg.draw.rect(sc, c.BLACK, [x, y, 40, 40], 3)
                    door1 = pg.draw.line(sc, c.RED, (x, y + 10), (x, y + 30), 3)
                    door2 = pg.draw.line(sc, c.RED, (x + 40, y + 10), (x + 40, y + 30), 3)
                    if user.rect.colliderect(door1):
                        user.rect.x += 60
                    if user.rect.colliderect(door2):
                        user.rect.x -= 60
                    count = count + 1
                    x = x + 70

            roomh10(200, 680)

            def roomh9(x, y):
                count = 1
                while (count < 16):
                    pg.draw.rect(sc, c.GREY, [x, y, 40, 40])
                    pg.draw.rect(sc, c.BLACK, [x, y, 40, 40], 3)
                    door1 = pg.draw.line(sc, c.RED, (x, y + 10), (x, y + 30), 3)
                    door2 = pg.draw.line(sc, c.RED, (x + 40, y + 10), (x + 40, y + 30), 3)
                    if user.rect.colliderect(door1):
                        user.rect.x += 60
                    if user.rect.colliderect(door2):
                        user.rect.x -= 60
                    count = count + 1
                    x = x + 70

            roomh9(60, 470)
            self.Door_OUT = pg.draw.line(sc, c.YELLOW, (550 + 10, 790), (550 + 30, 790), 6)
        if typeroom == 'roomtype8':
            def roomv(x, y):
                global user
                count = 1
                while (count < 9):
                    pg.draw.rect(sc, c.GREY, [x, y, 40, 40])
                    pg.draw.rect(sc, c.BLACK, [x, y, 40, 40], 3)
                    door1 = pg.draw.line(sc, c.RED, (x + 10, y), (x + 30, y), 3)
                    door2 = pg.draw.line(sc, c.RED, (x + 10, y + 40), (x + 30, y + 40), 3)
                    # if user.rect.colliderect(door1):
                    #     user.rect.y += 60
                    # if user.rect.colliderect(door2):
                    #     user.rect.y -= 60

                    count = count + 1
                    y = y + 70

            roomv(550, 260)

            def roomh10(x, y):
                count = 1
                while (count < 13):
                    pg.draw.rect(sc, c.GREY, [x, y, 40, 40])
                    pg.draw.rect(sc, c.BLACK, [x, y, 40, 40], 3)
                    door1 = pg.draw.line(sc, c.RED, (x, y + 10), (x, y + 30), 3)
                    door2 = pg.draw.line(sc, c.RED, (x + 40, y + 10), (x + 40, y + 30), 3)
                    if user.rect.colliderect(door1):
                        user.rect.x += 60
                    if user.rect.colliderect(door2):
                        user.rect.x -= 60
                    count = count + 1
                    x = x + 70

            roomh10(200, 680)

            def roomh9(x, y):
                count = 1
                while (count < 16):
                    pg.draw.rect(sc, c.GREY, [x, y, 40, 40])
                    pg.draw.rect(sc, c.BLACK, [x, y, 40, 40], 3)
                    door1 = pg.draw.line(sc, c.RED, (x, y + 10), (x, y + 30), 3)
                    door2 = pg.draw.line(sc, c.RED, (x + 40, y + 10), (x + 40, y + 30), 3)
                    if user.rect.colliderect(door1):
                        user.rect.x += 60
                    if user.rect.colliderect(door2):
                        user.rect.x -= 60
                    count = count + 1
                    x = x + 70

            roomh9(60, 470)
            self.Door_OUT = pg.draw.line(sc, c.GREEN, (550 + 10, 790), (550 + 30, 790), 6)
        self.setup_txt(sc)
        self.setup_map(sc)
        self.define_room(user)

    def define_room(self, user):

        if self.Seccion == 'WelcomeSeccion':

            if user.rect.colliderect(self.Door_Seeing_Space):
                time.sleep(1)
                if self.Seccion == 'WelcomeSeccion':
                    self.count = 0
                    self.Seccion = 'SeeingSpace'
                    self.AreaActual = 'SeeingRoom'
                    self.typeroom = 'roomtype2'
                    user.rect.x = c.coord_start[self.typeroom][0]
                    user.rect.y = c.coord_start[self.typeroom][1]

            elif user.rect.colliderect(self.Door_Toolshop):
                time.sleep(1)
                if self.Seccion == 'WelcomeSeccion':
                    self.count = 0
                    self.Seccion = 'Toolshop'
                    self.AreaActual = c.Toolshop_list[0]
                    self.typeroom = c.Room_dict[self.AreaActual][1]
                    user.rect.x = c.coord_start[self.typeroom][0]
                    user.rect.y = c.coord_start[self.typeroom][1]

            elif user.rect.colliderect(self.Door_Carbon_Capture):
                time.sleep(1)
                if self.Seccion == 'WelcomeSeccion':
                    self.count = 0
                    self.Seccion = 'CarbonCapture'
                    self.AreaActual = c.CarbonCap_list[0]
                    self.typeroom = c.Room_dict[self.AreaActual][1]
                    user.rect.x = c.coord_start[self.typeroom][0]
                    user.rect.y = c.coord_start[self.typeroom][1]

            elif user.rect.colliderect(self.Door_Food_SC):
                time.sleep(1)
                if self.Seccion == 'WelcomeSeccion':
                    self.count = 0
                    self.Seccion = 'FoodSupplyChain'
                    self.AreaActual = c.FSC_list[0]
                    self.typeroom = c.Room_dict[self.AreaActual][1]
                    user.rect.x = c.coord_start[self.typeroom][0]
                    user.rect.y = c.coord_start[self.typeroom][1]

            elif user.rect.colliderect(self.Door_Edible_Digital):
                time.sleep(1)
                if self.Seccion == 'WelcomeSeccion':
                    self.count = 0
                    self.Seccion = 'EdibleDigital'
                    self.AreaActual = c.ED_list[0]
                    self.typeroom = c.Room_dict[self.AreaActual][1]
                    user.rect.x = c.coord_start[self.typeroom][0]
                    user.rect.y = c.coord_start[self.typeroom][1]

            elif user.rect.colliderect(self.Door_FoodLab):
                time.sleep(1)
                if self.Seccion == 'WelcomeSeccion':
                    self.count = 0
                    self.Seccion = 'FoodLab'
                    self.AreaActual = c.FoodLab_list[0]
                    self.typeroom = c.Room_dict[self.AreaActual][1]
                    user.rect.x = c.coord_start[self.typeroom][0]
                    user.rect.y = c.coord_start[self.typeroom][1]

            elif user.rect.colliderect(self.Door_Building_Int):
                time.sleep(1)
                if self.Seccion == 'WelcomeSeccion':
                    self.count = 0
                    self.Seccion = 'BIA'
                    self.AreaActual = c.BIA_list[0]
                    self.typeroom = c.Room_dict[self.AreaActual][1]
                    user.rect.x = c.coord_start[self.typeroom][0]
                    user.rect.y = c.coord_start[self.typeroom][1]


        # open SeeingSpace secction
        elif self.Seccion == 'SeeingSpace':
            if user.rect.colliderect(self.Door_OUT):
                time.sleep(1)
                self.Seccion = 'WelcomeSeccion'
                self.AreaActual = 'WelcomeArea'
                user.rect.x = 550
                user.rect.y = 180

        #     # open Toolshop secction
        elif self.Seccion == 'Toolshop':
            if user.rect.colliderect(self.Door_OUT):
                time.sleep(1)
                self.Seccion = 'WelcomeSeccion'
                self.AreaActual = 'WelcomeArea'
                user.rect.x = 500
                user.rect.y = 400

                # open Carbon Capture secction
        elif self.Seccion == 'CarbonCapture':
             if user.rect.colliderect(self.Door_OUT):
                 time.sleep(1)
                 self.Seccion = 'WelcomeSeccion'
                 self.AreaActual = 'WelcomeArea'
                 user.rect.x = 500
                 user.rect.y = 400


                # open Edible Digital secction
        elif self.Seccion == 'EdibleDigital':
            if user.rect.colliderect(self.Door_OUT):
                time.sleep(1)
                self.Seccion = 'WelcomeSeccion'
                self.AreaActual = 'WelcomeArea'
                user.rect.x = 500
                user.rect.y = 400


                # open FoodLab secction
        elif self.Seccion == 'FoodLab':
            if user.rect.colliderect(self.Door_OUT):
                time.sleep(1)
                self.Seccion = 'WelcomeSeccion'
                self.AreaActual = 'WelcomeArea'
                user.rect.x = 500
                user.rect.y = 400


                # open FoodSupplyChain secction
        elif self.Seccion == 'FoodSupplyChain':
            if user.rect.colliderect(self.Door_OUT):
                time.sleep(1)
                self.Seccion = 'WelcomeSeccion'
                self.AreaActual = 'WelcomeArea'
                user.rect.x = 500
                user.rect.y = 400




                # open 'BIA' Capture secction
        elif self.Seccion == 'BIA':
            if user.rect.colliderect(self.Door_OUT):
                time.sleep(1)
                self.Seccion = 'WelcomeSeccion'
                self.AreaActual = 'WelcomeArea'
                user.rect.x = 500
                user.rect.y = 400




