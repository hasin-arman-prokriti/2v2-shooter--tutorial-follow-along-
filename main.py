import pygame
import os

W, H = 900, 500
COLOR = (25, 25, 155)
FPS = 60
DISPLACEMENT = 5
BULLET_VEL = 10
BG = pygame.image.load(os.path.join('Assets', 'space.png'))
BG = pygame.transform.scale(BG, (W, H))

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))

YELLOW_SPACESHIP = pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (55,40))
YELLOW_SPACESHIP = pygame.transform.rotate(YELLOW_SPACESHIP, -90)

RED_SPACESHIP = pygame.transform.scale(RED_SPACESHIP_IMAGE, (55,40))
RED_SPACESHIP = pygame.transform.rotate(RED_SPACESHIP, 90)

WIN = pygame.display.set_mode((W, H))  # setting constant variables in capital
BORDER = pygame.Rect(W/2-5, 0, 10, H)

RED_HIT =  pygame.USEREVENT + 1
YELLOW_HIT = pygame.USEREVENT + 2
pygame.display.set_caption("2v2 Shooter")


def draw_window(red, yellow, red_bullets, yellow_bullets):  # this will make sure whatever is going on with the display
    WIN.blit(BG,(0,0))
    pygame.draw.rect(WIN, (0,0,0), BORDER)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    for bullet in red_bullets:
        pygame.draw.rect(WIN, (255,0,0), bullet)
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, (255,255,0), bullet)
    pygame.display.update()

def red_movement(key_pressed, red):
    if key_pressed[pygame.K_a] and red.x - DISPLACEMENT > 0:     #Left player left movement
        red.x -= DISPLACEMENT
    if key_pressed[pygame.K_d] and red.x + DISPLACEMENT + red.width < BORDER.x:     #Left player rignt movement
        red.x += DISPLACEMENT
    if key_pressed[pygame.K_w] and red.y - DISPLACEMENT > 0:     #Left player up movement
        red.y -= DISPLACEMENT
    if key_pressed[pygame.K_s] and red.y + DISPLACEMENT + red.height < H:     #Left player down movement
        red.y += DISPLACEMENT    

def yellow_movement(key_pressed, yellow):
    if key_pressed[pygame.K_LEFT] and yellow.x - DISPLACEMENT > BORDER.x:     #right player left movement and border
        yellow.x -= DISPLACEMENT
    if key_pressed[pygame.K_RIGHT] and yellow.x + DISPLACEMENT + yellow.width < W:     #right player rignt movement
        yellow.x += DISPLACEMENT
    if key_pressed[pygame.K_UP] and yellow.y - DISPLACEMENT > 0:     #right player up movement
        yellow.y -= DISPLACEMENT
    if key_pressed[pygame.K_DOWN] and yellow.y + DISPLACEMENT + yellow.height < H:     #right player down movement
        yellow.y += DISPLACEMENT 

def bullet_movement(red_bullets, yellow_bullets, red, yellow):
    for bullet in red_bullets:
        bullet.x += BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x == W:
            red_bullets.remove(bullet)
    for bullet in yellow_bullets:
        bullet.x -= BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x == 0:
            yellow_bullets.remove(bullet)

def main():  # this is the main function. will run per frame and update scores and others etc.
    WIN.blit(BG,(0,0))
    red = pygame.Rect(100, 300, 40, 40)
    yellow = pygame.Rect(700, 300, 40, 40)
    red_bullets = []
    yellow_bullets = []

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)     # this will make sure this while loop only runs for 60 times a second, not more, not less
        
        for event in pygame.event.get():  # this loops through each event happening in pygame like pressing anybuttons
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL:
                    bullet = pygame.Rect(red.x, red.y+red.height//2, 10, 5)
                    red_bullets.append(bullet)
                if event.key == pygame.K_RCTRL:
                    bullet = pygame.Rect(yellow.x, yellow.y+yellow.width//2, 10,5)
                    yellow_bullets.append(bullet)

        key_pressed = pygame.key.get_pressed()
        red_movement(key_pressed, red)
        yellow_movement(key_pressed, yellow)
        bullet_movement(red_bullets, yellow_bullets, red, yellow)
        draw_window(red, yellow, red_bullets, yellow_bullets)

    pygame.quit()


if __name__ == '__main__':  # this part will only run if this file is run, otherwise
    # if it is imported then it will not run but if we didn't use this then if we imported
    main()  # the file then the main() function will automatically run which is not good
