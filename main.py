from pygame import *
from random import randint
from time import time as timer 
font.init()
font1 = font.Font(None, 80)
font2 = font.Font(None, 30)
end = font1.render('GAME OVER', True, (255, 250, 240))
class GameSprite(sprite.Sprite):

    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        
        sprite.Sprite.__init__(self)
        
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

     
class Player1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

speed_x = 7
speed_y = 7
class ball(GameSprite):
    def update(self):
        self.rect.x += speed_x
        self.rect.y += speed_y
        

win = display.set_mode((700,500))
win_width = 700
win_height = 430
display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load('i (3).webp'), (win_width, win_height))
right = Player1('китаец-Picsart-BackgroundRemover-Picsart-BackgroundRemover.png', 650, win_height - 300, 50, 120, 7)
left = Player2('китаец-Picsart-BackgroundRemover2-Picsart-BackgroundRemover (1).png', 5, win_height - 300, 50, 120, 7)
balls = ball('i (2)-Picsart-BackgroundRemover.webp', 350, 215, 40, 40, 6)

finish = False
run = True
count1 = 0
count2 = 0

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if not finish:
        win.blit(background, (0, 0))
        right.update()
        right.reset()
        left.update()
        left.reset()
        balls.update()
        balls.reset()
        display.update()
        time.delay(50)
        #score = font2.render(' : ', str(count2), 1, (255,255,255))
        balls.rect.x += speed_x
        balls.rect.y += speed_y
        if balls.rect.y > win_height - 50 or balls.rect.y <= 20:
            speed_y *= -1
        if sprite.collide_rect(left, balls) or sprite.collide_rect(right, balls):
            speed_x *= -1
            speed_y *= -1
        if balls.rect.x < 0:
            count2 += 1
            """balls.rect.x = win_width//2
            balls.rect.y = win_height//2"""
            finish = True
            win.blit(end, (300,300))
            

        if balls.rect.x > 700:
            count1 += 1
            balls.rect.x = win_width//2
            balls.rect.y = win_height//2
        """if count1 > 2 or count2 > 2:
            finish = True
            win.blit(end, (300,300))"""

    else:
        run = False