import pygame
import random
import os
import sys
from os import path
from pygame.locals import *

image_dir = path.join(path.dirname(__file__), 'images')
sound_dir = path.join(path.dirname(__file__), 'sounds')

pygame.init()
pygame.mixer.init()

# Initializing shooting sounds
bulletSound1 = pygame.mixer.Sound(path.join(sound_dir, "fire1.wav"))
bulletSound1.set_volume(0.1)
bulletSound2 = pygame.mixer.Sound(path.join(sound_dir, "fire2.wav"))
bulletSound2.set_volume(0.1)
bulletSound3 = pygame.mixer.Sound(path.join(sound_dir, "fire3.wav"))
bulletSound3.set_volume(0.1)
bulletSound4 = pygame.mixer.Sound(path.join(sound_dir, "fire4.wav"))
bulletSound4.set_volume(0.1)
bulletSound5 = pygame.mixer.Sound(path.join(sound_dir, "fire5.wav"))
bulletSound5.set_volume(0.5)
bulletSound6 = pygame.mixer.Sound(path.join(sound_dir, "fire6.wav"))
bulletSound6.set_volume(0.5)


# Initializing bullet Images
bullet1 = path.join(image_dir, "bullet1.png")
bullet2 = path.join(image_dir, "bullet2.png")
bullet3 = path.join(image_dir, "bullet3.png")
bullet4 = path.join(image_dir, "bullet4.png")
bullet5 = path.join(image_dir, "bullet5.png")
bullet6 = path.join(image_dir, "dollar.png")

# Initializing Dan sounds
danSound1 = pygame.mixer.Sound(path.join(sound_dir, "dan1.wav"))
danSound2 = pygame.mixer.Sound(path.join(sound_dir, "dan2.wav"))
danSound3 = pygame.mixer.Sound(path.join(sound_dir, "dan3.wav"))
danSound4 = pygame.mixer.Sound(path.join(sound_dir, "dan4.wav"))
danSound5 = pygame.mixer.Sound(path.join(sound_dir, "dan5.wav"))

danSounds = [danSound1, danSound2, danSound3, danSound4, danSound5]

# Loading background music
pygame.mixer.music.load(path.join(sound_dir, "song1.wav"))
pygame.mixer.music.set_volume(0.2)

# Setting up screen size for game
display_width = 1024
display_height = 650

# Initializing colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
navy = (0, 0, 128)
cyan = (0, 255, 255)

# Initializing fonts
font = pygame.font.SysFont(None, 100)
font2 = pygame.font.SysFont(None, 50)
font3 = pygame.font.SysFont(None, 60)
font4 = pygame.font.SysFont(None, 70)
font5 = pygame.font.SysFont(None, 90)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Humans vs Aliens')
clock = pygame.time.Clock()

# Initializing pictures
level1 = path.join(image_dir, "level1.png")
level2 = path.join(image_dir, "level2.gif")
level3 = path.join(image_dir, "level3.png")
level4 = path.join(image_dir, "level4.png")
level5 = path.join(image_dir, "level5.png")
level6 = path.join(image_dir, "level6.png")

bernie = path.join(image_dir, "bernie.png")
arnold = path.join(image_dir, "arnold.png")
dan = path.join(image_dir, "dan.png")
kim = path.join(image_dir, "kim.png")
obama = path.join(image_dir, "obama.png")
dirks = path.join(image_dir, "dirks.png")

# Initializing background
background = pygame.image.load(path.join(image_dir, "background.png"))
rescaledBackground = pygame.transform.scale(background,
                                            (display_width, display_height)
                                            )
gameDisplay.blit(rescaledBackground, (0, 0))


# Human Object
class Human(pygame.sprite.Sprite):
    def __init__(self, image, speed, bulletSpeed, bulletImg):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.left = 0
        self.speedy = speed
        self.radius = 57
        self.bulletSpeed = bulletSpeed
        self.bulletImg = bulletImg
        # pygame.draw.circle(self.image, red, self.rect.center, self.radius)

    def update(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP] or keystate[pygame.K_w]:
            self.rect.y -= self.speedy
        if keystate[pygame.K_DOWN] or keystate[pygame.K_s]:
            self.rect.y += self.speedy
        if self.rect.top < 30:
            self.rect.top = 30
        if self.rect.bottom > display_height - 10:
            self.rect.bottom = display_height - 10

    def shoot(self):
        bullet = Bullet(self.rect.centerx,
                        self.rect.centery - 20, self.bulletSpeed,
                        self.bulletImg)
        bullets.add(bullet)


# Alien Object
class Alien(pygame.sprite.Sprite):
    def __init__(self, image, speed):  # (image type, speed)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.radius = 41
        # pygame.draw.circle(self.image, red, self.rect.center, self.radius)
        self.rect.x = random.randint(display_width + 20, display_width + 2000)
        self.rect.y = random.randrange(40,
                                       display_height - self.rect.height, 100)
        self.speedx = speed
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.x -= self.speedx
        if self.rect.left < -90:
            self.kill()


# Bullet Object
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, bullet):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(bullet)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedx = speed
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.x += self.speedx
        if self.rect.right > display_width + 10:
            self.kill()


# Putting sprites into their corresponding groups
enemies = pygame.sprite.Group()
enemies2 = pygame.sprite.Group()
enemies3 = pygame.sprite.Group()
enemies4 = pygame.sprite.Group()
enemies5 = pygame.sprite.Group()
enemies6 = pygame.sprite.Group()
bullets = pygame.sprite.Group()
human1 = pygame.sprite.Group()
human2 = pygame.sprite.Group()
human3 = pygame.sprite.Group()
human4 = pygame.sprite.Group()
human5 = pygame.sprite.Group()
human6 = pygame.sprite.Group()

# Making instaces of objects
h1 = Human(bernie, 10, 10, bullet1)
h2 = Human(arnold, 12, 15, bullet2)
h3 = Human(dan, 14, 20, bullet3)
h4 = Human(kim, 16, 25, bullet4)
h5 = Human(obama, 18, 30, bullet5)
h6 = Human(dirks, 20, 35, bullet6)

human1.add(h1)
human2.add(h2)
human3.add(h3)
human4.add(h4)
human5.add(h5)
human6.add(h6)

# Spawning Alines for different levels
# Bernie
for i in range(25):
    a = Alien(level1, 6)
    enemies.add(a)

# Arnold
for i in range(30):
    b = Alien(level2, 8)
    enemies2.add(b)

# Dan
for i in range(35):
    c = Alien(level3, 10)
    enemies3.add(c)

# Kim
for i in range(32):
    d = Alien(level4, 10.5)
    enemies4.add(d)

# Obama
for i in range(33):
    e = Alien(level5, 11)
    enemies5.add(e)

# Dirks
for i in range(34):
    f = Alien(level6, 11.5)
    enemies6.add(f)


# Drawing Lives
def Live(health):
    font = pygame.font.SysFont(None, 30, bold=True)
    text = font.render("LIVES: " + str(health) + "/10", True, white)
    gameDisplay.blit(text, (10, 10))


# Drawing Score
def score(score):
    font = pygame.font.SysFont(None, 30, bold=True)
    text = font.render("SCORE: " + str(score),
                       True, white)
    gameDisplay.blit(text, (470, 10))


def draw_pause():
    font = pygame.font.SysFont(None, 30, bold=True)
    text = font.render("'P' = PAUSE",
                       True, cyan)
    text2 = font.render("'R' = RESTART",
                        True, cyan)
    gameDisplay.blit(text, (850, 10))
    gameDisplay.blit(text2, (850, 30))


# Drawing High Score
def high_score(lastScore):
    font = pygame.font.SysFont("None", 30, bold=True)
    text = font.render("HIGH SCORE: " + lastScore,
                       True, white)
    gameDisplay.blit(text, (620, 10))


# Drawing Aliens passed
def aliens_passed(passed):
    font = pygame.font.SysFont(None, 30, bold=True)
    text = font.render("ALIENS PASSED: " + str(passed) + "/10", True, white)
    gameDisplay.blit(text, (185, 10))


def drawText(text, font, surface, x, y, color):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


# Pause Function
def paused():
    pygame.mixer.music.pause()
    pause = True
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_RETURN:
                    pygame.mixer.music.unpause()
                    return

        gameDisplay.blit(rescaledBackground, (0, 0))
        drawText('PAUSED', font, gameDisplay, 370, 200, black)
        drawText('PRESS ENTER TO CONTINUE', font2,
                 gameDisplay, 260, 400, black)
        Live(lives)
        score(scoreCount)
        aliens_passed(aliensPassed)
        high_score(lastScore)
        pygame.display.update()
        clock.tick(15)


# Game Intro screen
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_RETURN:
                    return
        gameDisplay.blit(rescaledBackground, (0, 0))
        drawText('HUMANS vs. ALIENS', font, gameDisplay, (170), (90), black)
        drawText('CS10 FINAL PROJECT', font2, gameDisplay,
                 (display_width / 3) - 10, 230, blue)
        drawText('PRESS ENTER TO START', font3, gameDisplay,
                 (display_width / 3) - 80, (display_height / 3) + 150, white)
        drawText('Space => Shoot                 Arrow Keys => Move',
                 font2, gameDisplay, 150, 500, navy)
        pygame.display.update()


# Game Over screen
def gameOver():
    pygame.mixer.music.stop()
    gameDisplay.blit(rescaledBackground, (0, 0))
    drawText("HUMANS vs. ALIENS", font, gameDisplay, 170, 70, black)
    drawText("Oh no! Aliens have invaded your land!", font2,
             gameDisplay, 200, display_height / 2 - 120, black)
    drawText("PRESS ENTER TO RESTART OR ESCAPE TO EXIT",
             font2, gameDisplay, 90, 550, white)
    drawText("SCORE: " + str(scoreCount), font5, gameDisplay, 350, 300, black)
    drawText("HIGH SCORE: " + str(lastScore), font4, gameDisplay,
             300, 430, navy)
    pygame.display.update()
    waiting = True
    while waiting:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_RETURN:
                    pygame.mixer.music.play(-1)
                    waiting = False


# WINNING SCREEN
def winning():
    pygame.mixer.music.stop()
    gameDisplay.blit(rescaledBackground, (0, 0))
    drawText("HUMANS vs. ALIENS", font, gameDisplay, 170, 70, black)
    drawText("Congratulation! You have defeated the Aliens!", font2,
             gameDisplay, 150, display_height / 2 - 120, blue)
    drawText("Your land is safe now.", font2,
             gameDisplay, 340, display_height / 2 - 60, blue)
    drawText("PRESS ENTER TO RESTART OR ESCAPE TO EXIT",
             font2, gameDisplay, 90, 550, white)
    drawText("SCORE: " + str(scoreCount), font5, gameDisplay, 350, 350, black)
    drawText("HIGH SCORE: " + str(lastScore), font4, gameDisplay,
             300, 450, navy)
    pygame.display.update()
    waiting = True
    while waiting:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_RETURN:
                    pygame.mixer.music.play(-1)
                    waiting = False


# Initializing variables and game_intro script
game_intro()
game_over = False
win = False
restarted = False
global aliensPassed
aliensPassed = 0
global killed
killed = 0
global scoreCount
scoreCount = 0
global lives
lives = 10

# Game Loop
while True:
    pygame.mixer.music.play(-1)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_p:
                    paused()
                if event.key == pygame.K_r:
                    restarted = True
                if event.key == K_SPACE:
                    if killed < 50:
                        h1.shoot()
                        bulletSound1.play()
                    if killed >= 50 and killed < 120:
                        h2.shoot()
                        bulletSound2.play()
                    if killed >= 120 and killed < 200:
                        h3.shoot()
                        bulletSound3.play()
                    if killed >= 200 and killed < 300:
                        h4.shoot()
                        bulletSound4.play()
                    if killed >= 300 and killed < 420:
                        h5.shoot()
                        bulletSound5.play()
                    if killed >= 420 and killed < 550:
                        h6.shoot()
                        bulletSound6.play()

        bullets.update()
        enemies.update()
        human1.update()
        gameDisplay.blit(rescaledBackground, (0, 0))
        bullets.draw(gameDisplay)
        enemies.draw(gameDisplay)
        human1.draw(gameDisplay)

        # Read high score text file; if the file is empty, write 0
        with open("high_score.txt", "r+") as f:
            if os.stat("high_score.txt").st_size == 0:
                f.write("0")
            global lastScore
            lastScore = f.read()

        # LEVEL1
        hits = pygame.sprite.groupcollide(enemies, bullets, True, True,
                                          pygame.sprite.collide_mask)
        for hit in hits:
            a1 = Alien(level1, 6)
            enemies.add(a1)
            killed += 1
            scoreCount += 1

        hits = pygame.sprite.spritecollide(h1, enemies, True,
                                           pygame.sprite.collide_circle)
        for hit in hits:
            lives -= 1
            a1 = Alien(level1, 6)
            enemies.add(a1)
            if lives <= 0:
                game_over = True

        for i in enemies:
            if i.rect.right < 0:
                aliensPassed += 1

        # LEVEL2
        if killed >= 50 and killed < 120:
            enemies.remove()
            enemies.empty()
            human1.remove()
            human1.empty()
            enemies2.update()
            human2.update()
            enemies2.draw(gameDisplay)
            human2.draw(gameDisplay)

        hits = pygame.sprite.groupcollide(enemies2, bullets, True, True,
                                          pygame.sprite.collide_mask)
        for hit in hits:
            a2 = Alien(level2, 8)
            enemies2.add(a2)
            killed += 1
            scoreCount += 1

        hits = pygame.sprite.spritecollide(h2, enemies2, True,
                                           pygame.sprite.collide_circle)
        for hit in hits:
            lives -= 1
            a2 = Alien(level2, 8)
            enemies2.add(a2)
            if lives <= 0:
                game_over = True

        for i in enemies2:
            if i.rect.right < 0:
                aliensPassed += 1

        # LEVEL3
        if killed >= 120 and killed < 200:
            enemies2.remove()
            enemies2.empty()
            human2.remove()
            human2.empty()
            enemies3.update()
            human3.update()
            enemies3.draw(gameDisplay)
            human3.draw(gameDisplay)

        hits = pygame.sprite.groupcollide(enemies3, bullets, True, True,
                                          pygame.sprite.collide_mask)
        for hit in hits:
            a3 = Alien(level3, 10)
            enemies3.add(a3)
            killed += 1
            scoreCount += 1

        hits = pygame.sprite.spritecollide(h3, enemies3, True,
                                           pygame.sprite.collide_circle)
        for hit in hits:
            random.choice(danSounds).play()
            lives -= 1
            a3 = Alien(level3, 10)
            enemies3.add(a3)
            if lives <= 0:
                game_over = True

        for i in enemies3:
            if i.rect.right < 0:
                aliensPassed += 1

        # Level 4
        if killed >= 200 and killed < 300:
            enemies3.remove()
            enemies3.empty()
            human3.remove()
            human3.empty()
            enemies4.update()
            human4.update()
            enemies4.draw(gameDisplay)
            human4.draw(gameDisplay)

        hits = pygame.sprite.groupcollide(enemies4, bullets, True, True,
                                          pygame.sprite.collide_mask)
        for hit in hits:
            a4 = Alien(level4, 10.5)
            enemies4.add(a4)
            killed += 1
            scoreCount += 1

        hits = pygame.sprite.spritecollide(h4, enemies4, True,
                                           pygame.sprite.collide_circle)
        for hit in hits:
            lives -= 1
            a4 = Alien(level4, 10.5)
            enemies4.add(a4)
            if lives <= 0:
                game_over = True

        for i in enemies4:
            if i.rect.right < 0:
                aliensPassed += 1

        # Level 5
        if killed >= 300 and killed < 420:
            enemies4.remove()
            enemies4.empty()
            human4.remove()
            human4.empty()
            enemies5.update()
            human5.update()
            enemies5.draw(gameDisplay)
            human5.draw(gameDisplay)

        hits = pygame.sprite.groupcollide(enemies5, bullets, True, True,
                                          pygame.sprite.collide_mask)
        for hit in hits:
            a5 = Alien(level5, 11)
            enemies5.add(a5)
            killed += 1
            scoreCount += 1

        hits = pygame.sprite.spritecollide(h5, enemies5, True,
                                           pygame.sprite.collide_circle)
        for hit in hits:
            lives -= 1
            a5 = Alien(level5, 11)
            enemies5.add(a5)
            if lives <= 0:
                game_over = True

        for i in enemies5:
            if i.rect.right < 0:
                aliensPassed += 1

        # Final Level
        if killed >= 420:
            enemies5.remove()
            enemies5.empty()
            human5.remove()
            human5.empty()
            enemies6.update()
            human6.update()
            enemies6.draw(gameDisplay)
            human6.draw(gameDisplay)

        hits = pygame.sprite.groupcollide(enemies6, bullets, True, True,
                                          pygame.sprite.collide_mask)
        for hit in hits:
            a6 = Alien(level6, 11.5)
            enemies6.add(a6)
            killed += 1
            scoreCount += 1

        hits = pygame.sprite.spritecollide(h6, enemies6, True,
                                           pygame.sprite.collide_circle)
        for hit in hits:
            lives -= 1
            a6 = Alien(level6, 11.5)
            enemies6.add(a6)
            if lives <= 0:
                game_over = True

        for i in enemies6:
            if i.rect.right < 0:
                aliensPassed += 1

        if scoreCount > int(lastScore):
            with open("high_score.txt", "w") as g:
                g.write(str(scoreCount))

        # If 10 Aliens pass, the player loses
        if aliensPassed >= 10:
            game_over = True

        if killed >= 550:
            win = True

        # GAME OVER SCREEN AND RESTARTING
        if game_over:
            gameOver()
            game_over = False
            enemies = pygame.sprite.Group()
            enemies2 = pygame.sprite.Group()
            enemies3 = pygame.sprite.Group()
            enemies4 = pygame.sprite.Group()
            enemies5 = pygame.sprite.Group()
            enemies6 = pygame.sprite.Group()
            bullets = pygame.sprite.Group()
            human1 = pygame.sprite.Group()
            human2 = pygame.sprite.Group()
            human3 = pygame.sprite.Group()
            human4 = pygame.sprite.Group()
            human5 = pygame.sprite.Group()
            human6 = pygame.sprite.Group()
            h1 = Human(bernie, 10, 10, bullet1)
            h2 = Human(arnold, 12, 15, bullet2)
            h3 = Human(dan, 14, 20, bullet3)
            h4 = Human(kim, 16, 25, bullet4)
            h5 = Human(obama, 18, 30, bullet5)
            h6 = Human(dirks, 20, 35, bullet6)
            human1.add(h1)
            human2.add(h2)
            human3.add(h3)
            human4.add(h4)
            human5.add(h5)
            human6.add(h6)
            for i in range(25):
                a = Alien(level1, 6)
                enemies.add(a)
            for i in range(30):
                b = Alien(level2, 8)
                enemies2.add(b)
            for i in range(35):
                c = Alien(level3, 10)
                enemies3.add(c)
            for i in range(32):
                d = Alien(level4, 10.5)
                enemies4.add(d)
            for i in range(33):
                e = Alien(level5, 11)
                enemies5.add(e)
            for i in range(34):
                f = Alien(level6, 11.5)
                enemies6.add(f)
            aliensPassed = 0
            killed = 0
            scoreCount = 0
            lives = 10
            with open("high_score.txt", "r") as f:
                lastScore = f.read()

        # WINNING SCREEN AND RESTARTING
        if win:
            winning()
            win = False
            enemies = pygame.sprite.Group()
            enemies2 = pygame.sprite.Group()
            enemies3 = pygame.sprite.Group()
            enemies4 = pygame.sprite.Group()
            enemies5 = pygame.sprite.Group()
            enemies6 = pygame.sprite.Group()
            bullets = pygame.sprite.Group()
            human1 = pygame.sprite.Group()
            human2 = pygame.sprite.Group()
            human3 = pygame.sprite.Group()
            human4 = pygame.sprite.Group()
            human5 = pygame.sprite.Group()
            human6 = pygame.sprite.Group()
            h1 = Human(bernie, 10, 10, bullet1)
            h2 = Human(arnold, 12, 15, bullet2)
            h3 = Human(dan, 14, 20, bullet3)
            h4 = Human(kim, 16, 25, bullet4)
            h5 = Human(obama, 18, 30, bullet5)
            h6 = Human(dirks, 20, 35, bullet6)
            human1.add(h1)
            human2.add(h2)
            human3.add(h3)
            human4.add(h4)
            human5.add(h5)
            human6.add(h6)
            for i in range(25):
                a = Alien(level1, 6)
                enemies.add(a)
            for i in range(30):
                b = Alien(level2, 8)
                enemies2.add(b)
            for i in range(35):
                c = Alien(level3, 10)
                enemies3.add(c)
            for i in range(32):
                d = Alien(level4, 10.5)
                enemies4.add(d)
            for i in range(33):
                e = Alien(level5, 11)
                enemies5.add(e)
            for i in range(34):
                f = Alien(level6, 11.5)
                enemies6.add(f)
            aliensPassed = 0
            killed = 0
            scoreCount = 0
            lives = 10
            with open("high_score.txt", "r") as f:
                lastScore = f.read()

        # RESTART
        if restarted:
            restarted = False
            pygame.mixer.music.play(-1)
            enemies = pygame.sprite.Group()
            enemies2 = pygame.sprite.Group()
            enemies3 = pygame.sprite.Group()
            enemies4 = pygame.sprite.Group()
            enemies5 = pygame.sprite.Group()
            enemies6 = pygame.sprite.Group()
            bullets = pygame.sprite.Group()
            human1 = pygame.sprite.Group()
            human2 = pygame.sprite.Group()
            human3 = pygame.sprite.Group()
            human4 = pygame.sprite.Group()
            human5 = pygame.sprite.Group()
            human6 = pygame.sprite.Group()
            h1 = Human(bernie, 10, 10, bullet1)
            h2 = Human(arnold, 12, 15, bullet2)
            h3 = Human(dan, 14, 20, bullet3)
            h4 = Human(kim, 16, 25, bullet4)
            h5 = Human(obama, 18, 30, bullet5)
            h6 = Human(dirks, 20, 35, bullet6)
            human1.add(h1)
            human2.add(h2)
            human3.add(h3)
            human4.add(h4)
            human5.add(h5)
            human6.add(h6)
            for i in range(25):
                a = Alien(level1, 6)
                enemies.add(a)
            for i in range(30):
                b = Alien(level2, 8)
                enemies2.add(b)
            for i in range(35):
                c = Alien(level3, 10)
                enemies3.add(c)
            for i in range(32):
                d = Alien(level4, 10.5)
                enemies4.add(d)
            for i in range(33):
                e = Alien(level5, 11)
                enemies5.add(e)
            for i in range(34):
                f = Alien(level6, 11.5)
                enemies6.add(f)
            aliensPassed = 0
            killed = 0
            scoreCount = 0
            lives = 10
            with open("high_score.txt", "r") as f:
                lastScore = f.read()

        score(scoreCount)
        aliens_passed(aliensPassed)
        Live(lives)
        high_score(lastScore)
        draw_pause()
        pygame.display.update()
        clock.tick(60)
pygame.quit()
sys.exit()
