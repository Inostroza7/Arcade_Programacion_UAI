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

class ShipSprite(arcade.Sprite):
    """
    Sprite que representa nuestra nave

    Herencia de arcade.Sprite.
    """
    def __init__(self, filename, scale):
        """ Definimos nuestra nave. """

        # Super llama a la funcion padre
        super().__init__(filename, scale)

        # El ángulo se hereda de la funcion padre
        self.thrust = 0
        self.speed = 0
        self.max_speed = 4
        self.drag = 0.05
        self.respawning = 0

        # Marca para reaparecer o respawn.
        self.respawn()

    def respawn(self):
        """
        Llamamos a esta funcion cuando se destruye la nave y se necesita reaparecer.
        respawn o reaparecer es un tiempo de invulnerabilidad.
        """
        # Si estamos en medio de un Respawning este es 0.
        self.respawning = 1
        self.center_x = SCREEN_WIDTH / 2
        self.center_y = SCREEN_HEIGHT / 2
        self.angle = 0

    def update(self): # TODO verificar si la nave estará fija en el centro o se movera
        """
        Actualiza nuestra posición y otros partículares.
        """
        if self.respawning:
            self.respawning += 1
            self.alpha = self.respawning / 500.0
            if self.respawning > 250:
                self.respawning = 0
                self.alpha = 1
        if self.speed > 0:
            self.speed -= self.drag
            if self.speed < 0:
                self.speed = 0

        if self.speed < 0:
            self.speed += self.drag
            if self.speed > 0:
                self.speed = 0

        self.speed += self.thrust
        if self.speed > self.max_speed:
            self.speed = self.max_speed
        if self.speed < -self.max_speed:
            self.speed = -self.max_speed

        self.change_x = -math.sin(math.radians(self.angle)) * self.speed
        self.change_y = math.cos(math.radians(self.angle)) * self.speed

        self.center_x += self.change_x
        self.center_y += self.change_y

        """ Llama a la clase padre. """
        super().update()


class AsteroidSprite(arcade.Sprite): # TODO Modificar esto por naves enemigas
    """ Sprite that represents an asteroid. """

    def __init__(self, image_file_name, scale):
        super().__init__(image_file_name, scale=scale)
        self.size = 0

    def update(self):
        """ Move the asteroid around. """
        super().update()
        if self.center_x < LEFT_LIMIT:
            self.center_x = RIGHT_LIMIT
        if self.center_x > RIGHT_LIMIT:
            self.center_x = LEFT_LIMIT
        if self.center_y > TOP_LIMIT:
            self.center_y = BOTTOM_LIMIT
        if self.center_y < BOTTOM_LIMIT:
            self.center_y = TOP_LIMIT




















#############################
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