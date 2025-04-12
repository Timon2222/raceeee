from pygame import *
from random import randint
window = display.set_mode((700, 500))
display.set_caption('Гонки')
background = transform.scale(image.load('background.jpg'), (700, 500))



clock = time.Clock()
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self, player_image,  player_x, player_y,  player_width, player_height, player_speed):
         super().__init__()
         self.image = transform.scale(image.load(player_image), (player_width, player_height))
         self.speed = player_speed
         self.rect = self.image.get_rect()
         self.rect.x = player_x
         self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

    def colliderect(self, sprite):
        return self.rect.colliderect(sprite.rect)


class Player(GameSprite):
    def update(self):

        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > 5: 
            self.rect.x -= self.speed

        if keys_pressed[K_RIGHT] and self.rect.x < 660: 
            self.rect.x += self.speed

        if keys_pressed[K_UP] and self.rect.y > 5: 
            self.rect.y -= self.speed

        if keys_pressed[K_DOWN] and self.rect.y < 455: 
            self.rect.y += self.speed

class Enemy(GameSprite):
    def update_car1(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y >=  500:
            self.direction = 'down'
            self.rect.y = -60
            self.rect.x = randint(0, 635)
            
    def update_car2(self):
            self.rect.y += self.speed
            global lost
            if self.rect.y >=  500:
                self.direction = 'down'
                self.rect.y = -60
                self.rect.x = randint(0, 555)
                
    def update_car3(self):
            self.rect.y += self.speed
            global lost
            if self.rect.y >=  500:
                self.direction = 'down'
                self.rect.y = -60
                self.rect.x = randint(0, 145)
                
    def update_car4(self):
            self.rect.y += self.speed
            global lost
            if self.rect.y >=  500:
                self.direction = 'down'
                self.rect.y = -60
                self.rect.x = randint(0, 345)
                




car1 = Enemy('car1.png', 500, 100, 70, 80, 3)
car2 = Enemy('car2.png', 50, 150, 50, 90, 5)
car3 = Enemy('car3 (2).png', 110, 200, 120, 100, 3)
racer = Player('car4 (2).png', 220, 180, 120, 120, 5)

game = True
finish = False

font.init()
font2 = font.SysFont('Arial', 36)
text = font2.render('YOU LOSE!', 1, (255, 0, 0))


     



while game:
    if finish != True:
        window.blit(background,(0, 0))
        racer.update()
        racer.reset()
        car1.update_car1()
        car1.reset()
        car2.update_car2()
        car2.reset()
        car3.update_car3()
        car3.reset()
        if racer.colliderect(car1):
            finish = True
            window.blit(text,(300,200))
        if racer.colliderect(car2):
            finish = True
            window.blit(text,(300,200))
        if racer.colliderect(car3):
            finish = True
            window.blit(text,(300,200))    
    for e in event.get():
            if e.type == QUIT:
                game = False

    clock.tick(FPS)
    display.update()





