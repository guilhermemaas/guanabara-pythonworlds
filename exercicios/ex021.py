"""
Faca um programa que abra e execute um arquivo .mp3
"""

import pygame

pygame.init()
pygame.mixer.music.load('Real_Folk_Blues.mp3')
pygame.mixer.music.play()
pygame.mixer.music.stop()
pygame.event.wait()


