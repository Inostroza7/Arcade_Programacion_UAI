import arcade
import random
import time
import os


# Dimensiones pantalla
SCREEN_WIDTH = 1300
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Space Jam"
OFFSCREEN_SPACE = 300
LEFT_LIMIT = -OFFSCREEN_SPACE
RIGHT_LIMIT = SCREEN_WIDTH + OFFSCREEN_SPACE
BOTTOM_LIMIT = -OFFSCREEN_SPACE
TOP_LIMIT = SCREEN_HEIGHT + OFFSCREEN_SPACE

# Escalas para los distintos Sprites
SCALE_SPACESHIP = 1 # Player
SCALE_ENEMY = 1 # Enemigo
SCALE_LIFE = 1 # Vida
SCALE_TIME = 1 # Tiempo
SCALE_SCORE = 1  # Puntaje

class TurningSprite(arcade.Sprite):
    """ Sprite que establece su ángulo en la dirección en la que viaja la nave. """
    def update(self):
        super().update()
        self.angle = math.degrees(math.atan2(self.change_y, self.change_x))




arcade.open_window(ancho,alto,"SPACE JAM", True,True)

colorLetras = arcade.color.SKY_BLUE
mainWallpaper = arcade.Sprite("main_Wallpaper.jpeg",scale= 1.0)
mainSpaceShip = arcade.Sprite("SpaceShip_Sprite.png",scale= 1.0)

arcade.start_render()

# Main Wallpaper
mainWallpaper.center_y = alto//2
mainWallpaper.left = 0
mainWallpaperList = arcade.SpriteList()
mainWallpaperList.append(mainWallpaper)
mainWallpaperList.draw()

# SpaceShip Wallpaper
mainSpaceShip.center_y = alto//2+50
mainSpaceShip.left = ancho//2
mainSpaceShipList = arcade.SpriteList()
mainSpaceShipList.append(mainSpaceShip)
mainSpaceShipList.draw()

arcade.draw_text('SPACE JAM', ancho//2-500, alto-300 , arcade.color.DEEP_LEMON, 70)
arcade.draw_text('Nuevo Juego', ancho//2-500, alto//2 , colorLetras, 32)
arcade.draw_text('Mejores Puntajes', ancho//2-500, alto//2-50 , colorLetras, 32)
arcade.draw_text('Salir del Juego', ancho//2-500, alto//2-100 , colorLetras, 32)

arcade.finish_render()

arcade.run()