import time
import pygame
import sys
import os
pygame.init()
screen=pygame.display.set_mode((250,150))
pygame.display.set_caption('Message from admin')
font=pygame.font.SysFont("Lucida Console",20)
label=font.render("Hello there",1,(0,0,0))
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            time.sleep(0.10)
            screen=pygame.display.set_mode((250,150))
            pygame.display.set_caption('New Message')
    screen.fill((255,255,255))
    screen.blit(label,(50,50))
    pygame.display.update()
    
