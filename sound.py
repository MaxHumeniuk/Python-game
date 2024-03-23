import pygame 


def sound_Eve():
    pygame.mixer.init()
    s_e = pygame.mixer.Sound('./sound/Євусик_1.mp3')
    s_e.play()

def sound_Max():
    pygame.mixer.init()
    s_m = pygame.mixer.Sound('./sound/Максим_1.mp3')
    
    s_m.play()
