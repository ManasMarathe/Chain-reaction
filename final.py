import pygame   # Library To Build the Game
import sys
from math import *   # To Import mathematical Functions
import pickle        # To Load game Settings from File
 
flag=0
 
# Initialization of Pygame
pygame.init()
 
# Block = Size of each block
blocks = 60              # Height = Width of each Block
# Order of the matrix
sqFactor = int(input("Enter grid size: "))         # No of sqFactor = No. of Columns
noPlayers = int(input("Enter No. of Players: "))         # No. of Players
noPlayers=noPlayers if noPlayers<=8 else 8
 
mode = int(input("Select Mode: Elimination(1) or Non-Elimination(0): "))            # Mode of the Game (1- Battle Royale and 0 - Rebirth)
sqFactor = sqFactor if sqFactor<=12 else 12
width = blocks * sqFactor   # Calculate Required Width of Game window
height = blocks * sqFactor  # Calculate Required Height of Game Window
display = pygame.display.set_mode((width, height))   # Set Heigth and Width
 
# Sets the title of the game screen.
pygame.display.set_caption("Chain Reaction %dP Mode" % noPlayers)
 
# Define the clock.
clock = pygame.time.Clock()
# Define a standard font
font = pygame.font.SysFont("Calibri", 30)
 
# Predefine all Colors
background = (21, 67, 96)
border = (208, 211, 212)
red = (231, 76, 60)
white = (244, 246, 247)
violet = (255, 0, 255)
yellow = (204, 204, 0)
green = (88, 214, 141)
orange = (255, 153, 0)
darkBlue = (26, 26, 255)
lnm_green = (102, 255, 51)
blue = (102, 204, 255)
 
