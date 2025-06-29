from pygame import *

window = display.set_mode((700, 500))
display.set_caption('Лабиринт')
background = transform.scale(image.load('background.jpg'), (700, 500))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 425:
            self.rect.y += self.speed
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < 625:
            self.rect.x += self.speed

class Enemy(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y, player_speed)
        self.direction = 'left'
    def update(self):
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
        if self.rect.x <= 520:
            self.direction = 'right'
        if self.rect.x >= 650:
            self.direction = 'left'

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

clock = time.Clock()
FPS = 60

hero = Player('hero.png', 50, 400, 5)
cyborg = Enemy('cyborg.png', 600, 300, 2)
cyborg2 = Enemy('cyborg.png', 600, 120, 3)
gold = GameSprite('treasure.png', 600, 430, 0)
wall1 = Wall(97, 88, 199, 400, 85, 10, 325)
wall2 = Wall(97, 88, 199, 310, 400, 100, 10)
wall3 = Wall(97, 88, 199, 195, 480, 325, 10)
wall4 = Wall(97, 88, 199, 190, 110, 10, 380)
wall5 = Wall(97, 88, 199, 510, 100, 10, 380)
wall6 = Wall(97, 88, 199, 200, 300, 110, 10)
wall7 = Wall(97, 88, 199, 300, 170, 10, 130)
wall8 = Wall(97, 88, 199, 0, 0, 700, 10)
wall9 = Wall(97, 88, 199, 300, 80, 110, 10)
wall10 = Wall(97, 88, 199, 300, 0, 10, 90)
wall11 = Wall(97, 88, 199, 80, 0, 10, 380)
wall12 = Wall(97, 88, 199, 0, 490, 700, 10)

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.set_volume(0.2)
mixer.music.play()
money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')

font.init()
font = font.SysFont('Comic Sans MS', 70)
win = font.render('YOU WIN! :D', True, (255, 237, 100))
lose = font.render('YOU LOSE :(', True, (215, 4, 74))

finish = False
game = True
while game:
    if finish != True:
        window.blit(background, (0, 0))
        hero.reset()
        cyborg.reset()
        cyborg2.reset()
        gold.reset()
        wall1.draw_wall()
        wall2.draw_wall()
        wall4.draw_wall()
        wall5.draw_wall()
        wall6.draw_wall()
        wall7.draw_wall()
        wall8.draw_wall()
        wall9.draw_wall()
        wall10.draw_wall()
        wall11.draw_wall()
        wall12.draw_wall()
        hero.update()
        cyborg.update()
        cyborg2.update()
        if sprite.collide_rect(hero, gold):
            finish = True
            window.blit(win, (200, 200))
            money.play()
        if sprite.collide_rect(hero, cyborg) or sprite.collide_rect(hero, cyborg2):
            finish = True
            window.blit(lose, (200, 200))
            kick.play()
        if sprite.collide_rect(hero, wall1):
            hero.rect.x = 50
            hero.rect.y = 400
            kick.play()
        if sprite.collide_rect(hero, wall2):
            hero.rect.x = 50
            hero.rect.y = 400
            kick.play()
        if sprite.collide_rect(hero, wall4):
            hero.rect.x = 50
            hero.rect.y = 400
            kick.play()
        if sprite.collide_rect(hero, wall5):
            hero.rect.x = 50
            hero.rect.y = 400
            kick.play()
        if sprite.collide_rect(hero, wall6):
            hero.rect.x = 50
            hero.rect.y = 400
            kick.play()
        if sprite.collide_rect(hero, wall7):
            hero.rect.x = 50
            hero.rect.y = 400
            kick.play()
        if sprite.collide_rect(hero, wall8):
            hero.rect.x = 50
            hero.rect.y = 400
            kick.play()
        if sprite.collide_rect(hero, wall9):
            hero.rect.x = 50
            hero.rect.y = 400
            kick.play()
        if sprite.collide_rect(hero, wall10):
            hero.rect.x = 50
            hero.rect.y = 400
            kick.play()
        if sprite.collide_rect(hero, wall11):
            hero.rect.x = 50
            hero.rect.y = 400
            kick.play()
        if sprite.collide_rect(hero, wall12):
            hero.rect.x = 50
            hero.rect.y = 400
            kick.play()

    for e in event.get():
        if e.type == KEYDOWN:
            if e.key == K_v and finish == True:
                finish = False
                hero.rect.x = 50
                hero.rect.y = 400
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(FPS)