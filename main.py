from pygame import *

window = display.set_mode((700, 500))
display.set_caption("Пинг Понг")
background = transform.scale(image.load("background.jpg"), (700, 500))

clock = time.Clock()
FPS = 60

win_width = 700
win_height = 500

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
            super().__init__()
            # каждый спрайт должен хранить свойство image - изображение
            self.image = transform.scale(image.load(player_image), (size_x, size_y))
            self.speed = player_speed
            # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
            self.rect = self.image.get_rect()
            self.rect.x = player_x
            self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 600:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 600:
            self.rect.y += self.speed

player_l = Player('rocket.png', 10, 210 ,60,150,5)
player_r = Player('rocket.png', 640, 210 ,60 ,150,5)

ball = GameSprite('ball.png', 330, 230, 20,20, 6)

speed_x = 4
speed_y = 6

game = True
finish = False
 
font.init()
font2 = font.SysFont('Arial', 36)
font = font.SysFont('Arial',70)
win1 = font.render('WIN_P1', True, (209, 247, 255))   
win2 = font.render('WIN_P2', True, (209, 247, 255))   


while game:
    for e in event.get():
        if e.type == QUIT:
           game = False
    if finish != True:
        window.blit(background,(0, 0))
        player_r.update_r()
        player_r.reset()
        player_l.update_l()
        player_l.reset()
        ball.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y < 10:
            speed_y *= -1
        if ball.rect.y > 480:
            speed_y *= -1
        if sprite.collide_rect(player_l, ball) or sprite.collide_rect(player_r, ball):
            speed_x *= -1
        if ball.rect.x < 0:
            window.blit(win2,(200,200))
        if ball.rect.x > 680:
            window.blit(win1,(200,200))
        display.update()
    time.delay(50)