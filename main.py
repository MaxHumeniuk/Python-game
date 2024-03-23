import pygame
from sound import sound_Eve
from sound import sound_Max
from random import randrange
import random

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('./sound/song18.mp3')
pygame.mixer.music.play(-1)  # -1 означає відтворювати безкінечно (повторювати)
pygame.mixer.music.set_volume(0.08)  # Гучність 8%

#screen
screen = pygame.display.set_mode((800, 432))
clock = pygame.time.Clock()
speed_1 = 2
speed_2 = 2

scroll = 0

#Ground images
flying_ground = pygame.image.load('./images/ground_2.png')
flying_ground_width = flying_ground.get_width()
flying_ground_height = flying_ground.get_height()
ground_image = pygame.image.load("./images/ground.png").convert_alpha()
ground_width = ground_image.get_width()
ground_height = ground_image.get_height()

#background 
background_imgs = []
for i in range(1, 6):
    back_ground_img = pygame.image.load(f'./images/plx-{i}.png').convert_alpha()
    background_imgs.append(back_ground_img)
background_width = background_imgs[0].get_width()

def draw_background():
    for x in range(1000):
        speed = 0.3
        for i in background_imgs:
            screen.blit(i, ((x * background_width) - scroll * speed, 0))
            speed += 0.2

#draw ground
def draw_ground():
    for x in range(1000):
        screen.blit(ground_image, ((x * ground_width) - scroll * 2.2, 432 - ground_height))


#main characters
main_character = pygame.image.load('./character/green_little_bug.png')
main_character_2 = pygame.image.load('./character/frame_1.png')
resized_character_2 = pygame.transform.scale(main_character_2, (35, 30))
resized_character = pygame.transform.scale(main_character, (35, 30))
character = pygame.transform.flip(resized_character, True, False)
character_2 = pygame.transform.flip(resized_character_2, True, False)


#settings for postion
character_position_x = 1
character_position_y = 355
character_position_x_2 = 2
character_position_y_2 = 355
last_move_time = 0
move_delay = 850  # Затримка в мілісекундах (0.7 секунди)
move_direction = None  # Напрямок руху персонажа
jump_distance = 85  # Висота стрибка персонажа
is_jump_pressed = False 
last_move_time_2 = 0
move_delay_2 = 850  # Затримка в мілісекундах (0.7 секунди)
move_direction_2 = None  # Напрямок руху персонажа
jump_distance_2 = 85  # Висота стрибка персонажа
is_jump_pressed_2 = False # Прапорець, що вказує на те, чи була натиснута кнопка вгору





running = True
while running:
    draw_background()
    draw_ground()
    
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and not is_jump_pressed:
                sound_Max()
                is_jump_pressed = True
                move_direction = "up"
                last_move_time = pygame.time.get_ticks()
    
    
    screen.blit(character, (character_position_x, character_position_y))
    screen.blit(character_2, (character_position_x_2, character_position_y_2))

    

    current_time = pygame.time.get_ticks()
    current_time_2 = pygame.time.get_ticks()
    
    # Рух першого персонажа
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        character_position_x -= speed_1
    if character_position_x < 0:
        character_position_x = 0
    if keys[pygame.K_RIGHT]:
        character_position_x += speed_1
        


    if keys[pygame.K_UP] and not is_jump_pressed:
        sound_Max()
        is_jump_pressed = True
        move_direction = "up"
        last_move_time = pygame.time.get_ticks()
            
    if move_direction == "up":
        if character_position_y > 355 - jump_distance:
            character_position_y -= 3
        
            
        else:
            move_direction = "down"
            last_move_time = current_time
        

    if move_direction == "down":
        if character_position_y < 355:
            character_position_y += 3
        else:
            move_direction = None
            is_jump_pressed = False


    


    
    

    # Рух другого персонажа
    keys_ = pygame.key.get_pressed()
    if keys_[pygame.K_a]:
        character_position_x_2 -= speed_2
    if character_position_x_2 < 0:
        character_position_x_2 = 0
    if keys_[pygame.K_d]:
        character_position_x_2 += speed_2

    if keys_[pygame.K_w] and not is_jump_pressed_2:
        sound_Eve()
        is_jump_pressed_2 = True
        move_direction_2 = "up"
        last_move_time_2 = pygame.time.get_ticks()
        

    if move_direction_2 == "up":
        if character_position_y_2 > 355 - jump_distance_2:
            character_position_y_2 -= 3
        
            
        else:
            move_direction_2 = "down"
            last_move_time_2 = current_time_2
        

    if move_direction_2 == "down":
        if character_position_y_2 < 355:
            character_position_y_2 += 3
        else:
            move_direction_2 = None
            is_jump_pressed_2 = False



    

    
    

    pygame.display.flip()
    clock.tick(60)

pygame.quit()