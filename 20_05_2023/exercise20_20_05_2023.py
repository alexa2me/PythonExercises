# TODO: CHECK IF IT CAN WORK WITH AN URL

import pygame

pygame.init()
pygame.mixer.music.load('https://file-examples.com/storage/fea9880a616463cab9f1575/2017/11/file_example_MP3_700KB.mp3')
pygame.mixer.music.play()
pygame.event.wait()
