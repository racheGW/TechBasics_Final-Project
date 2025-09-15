import pygame
from os.path import join

WINDOW_WIDTH, WINDOW_HEIGHT = 1200, 600
SIZE = {"paddle": (40,100),"ball" : (30,30) }
POS = {"player":(WINDOW_WIDTH - 50, WINDOW_HEIGHT / 2), "opponent": (50, WINDOW_HEIGHT / 2)}
SPEED = {"player": 500, "opponent": 250, "ball": 450}
COLORS = {
    "paddle" : "#ffb3ba",
    "ball": "#bae1ff",
    "bg": "#ffdfba",
    "bg detail" : "#ffd27f"
}
