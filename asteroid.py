#Asteroid Class and Collector.
import pygame
import random
import circleshape
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y,radius)  # Call parent constructor
        #self.radius = radius

    def draw(self,screen):
         pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self,dt):
        self.position += self.velocity*dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20,50)
            old_radius = self.radius 
            new_radius = old_radius- ASTEROID_MIN_RADIUS
            start_angle1 = self.velocity.rotate(angle)
            start_angle2 = self.velocity.rotate(-angle)
            Asteroid1 = Asteroid(self.position.x,self.position.y,new_radius)
            Asteroid1.velocity = start_angle1*1.2
            Asteroid2 = Asteroid(self.position.x,self.position.y,new_radius)
            Asteroid2.velocity = start_angle2*1.2
            return Asteroid1,Asteroid2






