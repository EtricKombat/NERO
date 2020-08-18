import pygame as pg
import rr as r
import constants as c
import  butt as b

class User(pg.sprite.Sprite):
    def __init__(self,name):
        self.sheet = pg.image.load(name)
        self.sheet.set_clip(pg.Rect(0, 640, 64, 64))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.center = (400,400)
        self.frame = 0

    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]

    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pg.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pg.Rect(clipped_rect))
        return clipped_rect
    def coll(self):
        if user2.rect.colliderect(user.rect):
            if user2.rect.x > user.rect.x:
                user.clip(c.left_states)
                user.rect.x += 1

            else:

                user.rect.x -= 1
            b.gameMenu(SCREEN, event)

    def update(self, direction, AreaActual):
        if c.Room_dict[AreaActual][1] == 'roomtype1':


            if direction == 'left':
                self.clip(c.left_states)
                if self.rect.x <= 228:
                    self.rect.x += 3
                elif self.rect.x + self.rect.y <= 228 + 40 + 176:
                    self.rect.x += 3
                elif self.rect.x - self.rect.y <= 228 - 40 - 426:
                    self.rect.x += 3
                else:
                    self.rect.x -= 3
            elif direction == 'right':
                self.clip(c.right_states)
                if self.rect.x >= 821:
                    self.rect.x -= 3
                elif self.rect.x - self.rect.y >= 228 - 40 + 426:
                    self.rect.x -= 3
                elif self.rect.x + self.rect.y >= 228 + 40 + 426 + 570:
                    self.rect.x -= 3
                else:
                    self.rect.x += 3
            elif direction == 'up':
                self.clip(c.up_states)
                if self.rect.y <= 40:
                    self.rect.y += 3
                elif self.rect.x + self.rect.y <= 228 + 40 + 176:
                    self.rect.y += 3
                elif self.rect.x - self.rect.y >= 228 - 40 + 426:
                    self.rect.y += 3
                else:
                    self.rect.y -= 3
            elif direction == 'down':
                self.clip(c.down_states)
                if self.rect.y >= 623:
                    self.rect.y -= 3
                elif self.rect.x - self.rect.y <= 228 - 40 - 426:
                    self.rect.y -= 3
                elif self.rect.x + self.rect.y >= 228 + 40 + 426 + 570:
                    self.rect.y -= 3
                else:
                    self.rect.y += 3

            elif direction == 'stand_left':
                self.clip(c.left_states[0])
            elif direction == 'stand_right':
                self.clip(c.right_states[0])
            elif direction == 'stand_up':
                self.clip(c.up_states[0])
            elif direction == 'stand_down':
                self.clip(c.down_states[0])

        if c.Room_dict[AreaActual][1] == 'roomtype2':
            if direction == 'left':
                self.clip(c.left_states)
                if self.rect.x <= 228:
                    self.rect.x += 3
                elif self.rect.x + self.rect.y <= 228 + 40 + 176:
                    self.rect.x += 3
                elif self.rect.x - self.rect.y <= 228 - 40 - 426:
                    self.rect.x += 3
                else:
                    self.rect.x -= 3
            elif direction == 'right':
                self.clip(c.right_states)
                if self.rect.x >= 821:
                    self.rect.x -= 3
                elif self.rect.x - self.rect.y >= 228 - 40 + 426:
                    self.rect.x -= 3
                elif self.rect.x + self.rect.y >= 228 + 40 + 426 + 570:
                    self.rect.x -= 3
                else:
                    self.rect.x += 3
            elif direction == 'up':
                self.clip(c.up_states)
                if self.rect.y <= 40:
                    self.rect.y += 3
                elif self.rect.x + self.rect.y <= 228 + 40 + 176:
                    self.rect.y += 3
                elif self.rect.x - self.rect.y >= 228 - 40 + 426:
                    self.rect.y += 3
                else:
                    self.rect.y -= 3
            elif direction == 'down':
                self.clip(c.down_states)
                if self.rect.y >= 623:
                    self.rect.y -= 3
                elif self.rect.x - self.rect.y <= 228 - 40 - 426:
                    self.rect.y -= 3
                elif self.rect.x + self.rect.y >= 228 + 40 + 426 + 570:
                    self.rect.y -= 3
                else:
                    self.rect.y += 3

            elif direction == 'stand_left':
                self.clip(c.left_states[0])
            elif direction == 'stand_right':
                self.clip(c.right_states[0])
            elif direction == 'stand_up':
                self.clip(c.up_states[0])
            elif direction == 'stand_down':
                self.clip(c.down_states[0])



        elif c.Room_dict[AreaActual][1] == 'roomtype3':
            if direction == 'left':
                self.clip(c.left_states)
                if self.rect.x <= 0:
                    self.rect.x += 3
                else:
                    self.rect.x -= 3
            elif direction == 'right':
                self.clip(c.right_states)
                if self.rect.x >= 1100:
                    self.rect.x -= 3
                else:
                    self.rect.x += 3
            elif direction == 'up':
                self.clip(c.up_states)
                if self.rect.y <= 0:
                    self.rect.y += 3
                else:
                    self.rect.y -= 3
            elif direction == 'down':
                self.clip(c.down_states)
                if self.rect.y >= 800:
                    self.rect.y -= 3
                else:
                    self.rect.y += 3

            elif direction == 'stand_left':
                self.clip(c.left_states[0])
            elif direction == 'stand_right':
                self.clip(c.right_states[0])
            elif direction == 'stand_up':
                self.clip(c.up_states[0])
            elif direction == 'stand_down':
                self.clip(c.down_states[0])

        elif c.Room_dict[AreaActual][1] == 'roomtype4':
            if direction == 'left':
                self.clip(c.left_states)
                if self.rect.x <= 0:
                    self.rect.x += 3
                else:
                    self.rect.x -= 3
            elif direction == 'right':
                self.clip(c.right_states)
                if self.rect.x >= 1100:
                    self.rect.x -= 3
                else:
                    self.rect.x += 3
            elif direction == 'up':
                self.clip(c.up_states)
                if self.rect.y <= 0:
                    self.rect.y += 3
                else:
                    self.rect.y -= 3
            elif direction == 'down':
                self.clip(c.down_states)
                if self.rect.y >= 800:
                    self.rect.y -= 3
                else:
                    self.rect.y += 3

            elif direction == 'stand_left':
                self.clip(c.left_states[0])
            elif direction == 'stand_right':
                self.clip(c.right_states[0])
            elif direction == 'stand_up':
                self.clip(c.up_states[0])
            elif direction == 'stand_down':
                self.clip(c.down_states[0])
        elif c.Room_dict[AreaActual][1] == 'roomtype5':
            if direction == 'left':
                self.clip(c.left_states)
                if self.rect.x <= 0:
                    self.rect.x += 3
                else:
                    self.rect.x -= 3
            elif direction == 'right':
                self.clip(c.right_states)
                if self.rect.x >= 1100:
                    self.rect.x -= 3
                else:
                    self.rect.x += 3
            elif direction == 'up':
                self.clip(c.up_states)
                if self.rect.y <= 0:
                    self.rect.y += 3
                else:
                    self.rect.y -= 3
            elif direction == 'down':
                self.clip(c.down_states)
                if self.rect.y >= 800:
                    self.rect.y -= 3
                else:
                    self.rect.y += 3

            elif direction == 'stand_left':
                self.clip(c.left_states[0])
            elif direction == 'stand_right':
                self.clip(c.right_states[0])
            elif direction == 'stand_up':
                self.clip(c.up_states[0])
            elif direction == 'stand_down':
                self.clip(c.down_states[0])
        elif c.Room_dict[AreaActual][1] == 'roomtype6':
            if direction == 'left':
                self.clip(c.left_states)
                if self.rect.x <= 0:
                    self.rect.x += 3
                else:
                    self.rect.x -= 3
            elif direction == 'right':
                self.clip(c.right_states)
                if self.rect.x >= 1100:
                    self.rect.x -= 3
                else:
                    self.rect.x += 3
            elif direction == 'up':
                self.clip(c.up_states)
                if self.rect.y <= 0:
                    self.rect.y += 3
                else:
                    self.rect.y -= 3
            elif direction == 'down':
                self.clip(c.down_states)
                if self.rect.y >= 800:
                    self.rect.y -= 3
                else:
                    self.rect.y += 3

            elif direction == 'stand_left':
                self.clip(c.left_states[0])
            elif direction == 'stand_right':
                self.clip(c.right_states[0])
            elif direction == 'stand_up':
                self.clip(c.up_states[0])
            elif direction == 'stand_down':
                self.clip(c.down_states[0])
        elif c.Room_dict[AreaActual][1] == 'roomtype7':
            if direction == 'left':
                self.clip(c.left_states)
                if self.rect.x <= 0:
                    self.rect.x += 3
                else:
                    self.rect.x -= 3
            elif direction == 'right':
                self.clip(c.right_states)
                if self.rect.x >= 1100:
                    self.rect.x -= 3
                else:
                    self.rect.x += 3
            elif direction == 'up':
                self.clip(c.up_states)
                if self.rect.y <= 0:
                    self.rect.y += 3
                else:
                    self.rect.y -= 3
            elif direction == 'down':
                self.clip(c.down_states)
                if self.rect.y >= 800:
                    self.rect.y -= 3
                else:
                    self.rect.y += 3

            elif direction == 'stand_left':
                self.clip(c.left_states[0])
            elif direction == 'stand_right':
                self.clip(c.right_states[0])
            elif direction == 'stand_up':
                self.clip(c.up_states[0])
            elif direction == 'stand_down':
                self.clip(c.down_states[0])
        elif c.Room_dict[AreaActual][1] == 'roomtype8':
            if direction == 'left':
                self.clip(c.left_states)
                if self.rect.x <= 0:
                    self.rect.x += 3
                else:
                    self.rect.x -= 3
            elif direction == 'right':
                self.clip(c.right_states)
                if self.rect.x >= 1100:
                    self.rect.x -= 3
                else:
                    self.rect.x += 3
            elif direction == 'up':
                self.clip(c.up_states)
                if self.rect.y <= 0:
                    self.rect.y += 3
                else:
                    self.rect.y -= 3
            elif direction == 'down':
                self.clip(c.down_states)
                if self.rect.y >= 800:
                    self.rect.y -= 3
                else:
                    self.rect.y += 3

            elif direction == 'stand_left':
                self.clip(c.left_states[0])
            elif direction == 'stand_right':
                self.clip(c.right_states[0])
            elif direction == 'stand_up':
                self.clip(c.up_states[0])
            elif direction == 'stand_down':
                self.clip(c.down_states[0])
        self.image = self.sheet.subsurface(self.sheet.get_clip())

    def handle_event(self, event, AreaActual):
        if event.type == pg.QUIT:
            game_over = True

        if event.type == pg.KEYDOWN:

            if event.key == pg.K_LEFT:
                self.update('left', AreaActual)
            if event.key == pg.K_RIGHT:
                self.update('right', AreaActual)
            if event.key == pg.K_UP:
                self.update('up', AreaActual)
            if event.key == pg.K_DOWN:
                self.update('down', AreaActual)

        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT:
                self.update('stand_left', AreaActual)
            if event.key == pg.K_RIGHT:
                self.update('stand_right', AreaActual)
            if event.key == pg.K_UP:
                self.update('stand_up', AreaActual)
            if event.key == pg.K_DOWN:
                self.update('stand_down', AreaActual)




class User2(pg.sprite.Sprite):
    def __init__(self, name):
        self.sheet = pg.image.load(name)
        self.sheet.set_clip(pg.Rect(0, 640, 64, 64))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.center = c.Start_position
        self.frame = 0

    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]

    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pg.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pg.Rect(clipped_rect))
        return clipped_rect

    def update(self, direction, AreaActual):
        if c.Room_dict[AreaActual][1] == 'roomtype1':
            if direction == 'left':
                self.clip(c.left_states)
                if self.rect.x <= 228:
                    self.rect.x += 3
                elif self.rect.x + self.rect.y <= 228 + 40 + 176:
                    self.rect.x += 3
                elif self.rect.x - self.rect.y <= 228 - 40 - 426:
                    self.rect.x += 3
                else:
                    self.rect.x -= 3
            elif direction == 'right':
                self.clip(c.right_states)
                if self.rect.x >= 821:
                    self.rect.x -= 3
                elif self.rect.x - self.rect.y >= 228 - 40 + 426:
                    self.rect.x -= 3
                elif self.rect.x + self.rect.y >= 228 + 40 + 426 + 570:
                    self.rect.x -= 3
                else:
                    self.rect.x += 3
            elif direction == 'up':
                self.clip(c.up_states)
                if self.rect.y <= 40:
                    self.rect.y += 3
                elif self.rect.x + self.rect.y <= 228 + 40 + 176:
                    self.rect.y += 3
                elif self.rect.x - self.rect.y >= 228 - 40 + 426:
                    self.rect.y += 3
                else:
                    self.rect.y -= 3
            elif direction == 'down':
                self.clip(c.down_states)
                if self.rect.y >= 623:
                    self.rect.y -= 3
                elif self.rect.x - self.rect.y <= 228 - 40 - 426:
                    self.rect.y -= 3
                elif self.rect.x + self.rect.y >= 228 + 40 + 426 + 570:
                    self.rect.y -= 3
                else:
                    self.rect.y += 3

            elif direction == 'stand_left':
                self.clip(c.left_states[0])
            elif direction == 'stand_right':
                self.clip(c.right_states[0])
            elif direction == 'stand_up':
                self.clip(c.up_states[0])
            elif direction == 'stand_down':
                self.clip(c.down_states[0])

        if c.Room_dict[AreaActual][1] == 'roomtype2':
            if direction == 'left':
                self.clip(c.left_states)
                if self.rect.x <= 228:
                    self.rect.x += 3
                elif self.rect.x + self.rect.y <= 228 + 40 + 176:
                    self.rect.x += 3
                elif self.rect.x - self.rect.y <= 228 - 40 - 426:
                    self.rect.x += 3
                else:
                    self.rect.x -= 3
            elif direction == 'right':
                self.clip(c.right_states)
                if self.rect.x >= 821:
                    self.rect.x -= 3
                elif self.rect.x - self.rect.y >= 228 - 40 + 426:
                    self.rect.x -= 3
                elif self.rect.x + self.rect.y >= 228 + 40 + 426 + 570:
                    self.rect.x -= 3
                else:
                    self.rect.x += 3
            elif direction == 'up':
                self.clip(c.up_states)
                if self.rect.y <= 40:
                    self.rect.y += 3
                elif self.rect.x + self.rect.y <= 228 + 40 + 176:
                    self.rect.y += 3
                elif self.rect.x - self.rect.y >= 228 - 40 + 426:
                    self.rect.y += 3
                else:
                    self.rect.y -= 3
            elif direction == 'down':
                self.clip(c.down_states)
                if self.rect.y >= 623:
                    self.rect.y -= 3
                elif self.rect.x - self.rect.y <= 228 - 40 - 426:
                    self.rect.y -= 3
                elif self.rect.x + self.rect.y >= 228 + 40 + 426 + 570:
                    self.rect.y -= 3
                else:
                    self.rect.y += 3

            elif direction == 'stand_left':
                self.clip(c.left_states[0])
            elif direction == 'stand_right':
                self.clip(c.right_states[0])
            elif direction == 'stand_up':
                self.clip(c.up_states[0])
            elif direction == 'stand_down':
                self.clip(c.down_states[0])



        elif c.Room_dict[AreaActual][1] == 'roomtype3':
            if direction == 'left':
                self.clip(c.left_states)
                if self.rect.x <= 0:
                    self.rect.x += 3
                else:
                    self.rect.x -= 3
            elif direction == 'right':
                self.clip(c.right_states)
                if self.rect.x >= 1100:
                    self.rect.x -= 3
                else:
                    self.rect.x += 3
            elif direction == 'up':
                self.clip(c.up_states)
                if self.rect.y <= 0:
                    self.rect.y += 3
                else:
                    self.rect.y -= 3
            elif direction == 'down':
                self.clip(c.down_states)
                if self.rect.y >= 800:
                    self.rect.y -= 3
                else:
                    self.rect.y += 3

            elif direction == 'stand_left':
                self.clip(c.left_states[0])
            elif direction == 'stand_right':
                self.clip(c.right_states[0])
            elif direction == 'stand_up':
                self.clip(c.up_states[0])
            elif direction == 'stand_down':
                self.clip(c.down_states[0])

        elif c.Room_dict[AreaActual][1] == 'roomtype4':
            if direction == 'left':
                self.clip(c.left_states)
                if self.rect.x <= 0:
                    self.rect.x += 3
                else:
                    self.rect.x -= 3
            elif direction == 'right':
                self.clip(c.right_states)
                if self.rect.x >= 1100:
                    self.rect.x -= 3
                else:
                    self.rect.x += 3
            elif direction == 'up':
                self.clip(c.up_states)
                if self.rect.y <= 0:
                    self.rect.y += 3
                else:
                    self.rect.y -= 3
            elif direction == 'down':
                self.clip(c.down_states)
                if self.rect.y >= 800:
                    self.rect.y -= 3
                else:
                    self.rect.y += 3

            elif direction == 'stand_left':
                self.clip(c.left_states[0])
            elif direction == 'stand_right':
                self.clip(c.right_states[0])
            elif direction == 'stand_up':
                self.clip(c.up_states[0])
            elif direction == 'stand_down':
                self.clip(c.down_states[0])
        elif c.Room_dict[AreaActual][1] == 'roomtype5':
            if direction == 'left':
                self.clip(c.left_states)
                if self.rect.x <= 0:
                    self.rect.x += 3
                else:
                    self.rect.x -= 3
            elif direction == 'right':
                self.clip(c.right_states)
                if self.rect.x >= 1100:
                    self.rect.x -= 3
                else:
                    self.rect.x += 3
            elif direction == 'up':
                self.clip(c.up_states)
                if self.rect.y <= 0:
                    self.rect.y += 3
                else:
                    self.rect.y -= 3
            elif direction == 'down':
                self.clip(c.down_states)
                if self.rect.y >= 800:
                    self.rect.y -= 3
                else:
                    self.rect.y += 3

            elif direction == 'stand_left':
                self.clip(c.left_states[0])
            elif direction == 'stand_right':
                self.clip(c.right_states[0])
            elif direction == 'stand_up':
                self.clip(c.up_states[0])
            elif direction == 'stand_down':
                self.clip(c.down_states[0])
        elif c.Room_dict[AreaActual][1] == 'roomtype6':
            if direction == 'left':
                self.clip(c.left_states)
                if self.rect.x <= 0:
                    self.rect.x += 3
                else:
                    self.rect.x -= 3
            elif direction == 'right':
                self.clip(c.right_states)
                if self.rect.x >= 1100:
                    self.rect.x -= 3
                else:
                    self.rect.x += 3
            elif direction == 'up':
                self.clip(c.up_states)
                if self.rect.y <= 0:
                    self.rect.y += 3
                else:
                    self.rect.y -= 3
            elif direction == 'down':
                self.clip(c.down_states)
                if self.rect.y >= 800:
                    self.rect.y -= 3
                else:
                    self.rect.y += 3

            elif direction == 'stand_left':
                self.clip(c.left_states[0])
            elif direction == 'stand_right':
                self.clip(c.right_states[0])
            elif direction == 'stand_up':
                self.clip(c.up_states[0])
            elif direction == 'stand_down':
                self.clip(c.down_states[0])
        elif c.Room_dict[AreaActual][1] == 'roomtype7':
            if direction == 'left':
                self.clip(c.left_states)
                if self.rect.x <= 0:
                    self.rect.x += 3
                else:
                    self.rect.x -= 3
            elif direction == 'right':
                self.clip(c.right_states)
                if self.rect.x >= 1100:
                    self.rect.x -= 3
                else:
                    self.rect.x += 3
            elif direction == 'up':
                self.clip(c.up_states)
                if self.rect.y <= 0:
                    self.rect.y += 3
                else:
                    self.rect.y -= 3
            elif direction == 'down':
                self.clip(c.down_states)
                if self.rect.y >= 800:
                    self.rect.y -= 3
                else:
                    self.rect.y += 3

            elif direction == 'stand_left':
                self.clip(c.left_states[0])
            elif direction == 'stand_right':
                self.clip(c.right_states[0])
            elif direction == 'stand_up':
                self.clip(c.up_states[0])
            elif direction == 'stand_down':
                self.clip(c.down_states[0])
        elif c.Room_dict[AreaActual][1] == 'roomtype8':
            if direction == 'left':
                self.clip(c.left_states)
                if self.rect.x <= 0:
                    self.rect.x += 3
                else:
                    self.rect.x -= 3
            elif direction == 'right':
                self.clip(c.right_states)
                if self.rect.x >= 1100:
                    self.rect.x -= 3
                else:
                    self.rect.x += 3
            elif direction == 'up':
                self.clip(c.up_states)
                if self.rect.y <= 0:
                    self.rect.y += 3
                else:
                    self.rect.y -= 3
            elif direction == 'down':
                self.clip(c.down_states)
                if self.rect.y >= 800:
                    self.rect.y -= 3
                else:
                    self.rect.y += 3

            elif direction == 'stand_left':
                self.clip(c.left_states[0])
            elif direction == 'stand_right':
                self.clip(c.right_states[0])
            elif direction == 'stand_up':
                self.clip(c.up_states[0])
            elif direction == 'stand_down':
                self.clip(c.down_states[0])
        self.image = self.sheet.subsurface(self.sheet.get_clip())

    def handle_event(self, event, AreaActual):
        if event.type == pg.QUIT:
            game_over = True

        if event.type == pg.KEYDOWN:

            if event.key == pg.K_LEFT:
                self.update('left', AreaActual)
            if event.key == pg.K_RIGHT:
                self.update('right', AreaActual)
            if event.key == pg.K_UP:
                self.update('up', AreaActual)
            if event.key == pg.K_DOWN:
                self.update('down', AreaActual)

        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT:
                self.update('stand_left', AreaActual)
            if event.key == pg.K_RIGHT:
                self.update('stand_right', AreaActual)
            if event.key == pg.K_UP:
                self.update('stand_up', AreaActual)
            if event.key == pg.K_DOWN:
                self.update('stand_down', AreaActual)
