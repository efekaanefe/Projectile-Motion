import pygame, os
import random


class Ball():
    def __init__(self, x, y, win, WIDTH, HEIGHT):
        self.width = WIDTH
        self.height = HEIGHT
        self.size = 15
        self.image = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "ball.png")),(self.size,self.size))
        self.win = win
        self.x = x
        self.y = y
        self.x_vel = 0
        self.y_vel = 0
        self.moving = True
        self.acceleration_y = 9.8
        self.acceleration_x = 0
        self.time_passed = 0 # since the last frame


    def move(self):
        if self.moving == True:
            self.x += self.x_vel*self.time_passed
            #self.y += self.y_vel*self.time_passed+0.5*self.acceleration_y*self.time_passed**2
            self.y += self.y_vel*self.time_passed

           
    def draw(self):
        self.win.blit(self.image, (self.x, self.y))
    
    def accelerate(self):
        if self.moving == True:
            self.y_vel += self.acceleration_y*self.time_passed
            self.x_vel += self.acceleration_x*self.time_passed

    def get_velocity(self, delta_x, delta_y):
        multiplier = 0.2
        self.x_vel = delta_x * multiplier
        self.y_vel = delta_y * multiplier
        self.moving = True

    def bounce(self): #bounces when touching left or right only for now
        multiplier = 0.65
        self.y_vel = self.y_vel*multiplier
        self.x_vel = -self.x_vel*multiplier


    def stop(self):
        self.y_vel = 0
        self.x_vel = 0
        self.moving = False 
        self.y = self.height - self.size


    def bounce_when_touching_sides(self):
        if self.x+(self.x_vel*self.time_passed)<0:
            self.bounce()
        elif self.x+self.size+(self.x_vel*self.time_passed)>self.width:
            self.bounce()

    def stop_when_touching_ground(self):
        if self.y_vel >0:
            if self.y+self.size+(self.y_vel*self.time_passed+0.5*self.acceleration_y*self.time_passed**2) > self.height:
                self.stop()

        
