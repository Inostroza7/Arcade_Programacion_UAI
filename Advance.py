import arcade
import random
import time
import os


# Dimensiones pantalla
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_TITLE = "Space Jam"

# Margen entre el borde de la pantalla
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

# Características de la Física del Juego
MOVEMENT_SPEED = 5
ENEMY_SPEED = 2
EMEMY2_SPEED = 2.5

# Musica
MUSIC_VOLUME = 0.03
MUSIC_VOLUMEHIGH = 0.25

class InstructionView(arcade.View):

    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture("img/wall/introWallpaper.png")
        # Restablecer la ventana gráfica, necesaria si tenemos un juego de desplazamiento y necesitamos
        # para restablecer la ventana gráfica al inicio para que podamos ver lo que dibujamos.
        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

    def on_draw(self):
        """ Dibuja esta vista """
        arcade.start_render()
        self.texture.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                                SCREEN_WIDTH, SCREEN_HEIGHT)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ Si el usuario presiona el botón del mouse, inicia el juego. """
        game_view = MyGame()
        game_view.setup()
        self.window.show_view(game_view)

class Enemy(arcade.Sprite):

    def follow_sprite(self, player_sprite):
        # Esta función es para que el Enemy (self) se mueva hacia el personaje (player.sprite).

        if self.center_y < player_sprite.center_y:
            self.center_y += min(ENEMY_SPEED, player_sprite.center_y - self.center_y)
        elif self.center_y > player_sprite.center_y:
            self.center_y -= min(ENEMY_SPEED, self.center_y - player_sprite.center_y)

        if self.center_x < player_sprite.center_x:
            self.center_x += min(ENEMY_SPEED, player_sprite.center_x - self.center_x)
        elif self.center_x > player_sprite.center_x:
            self.center_x -= min(ENEMY_SPEED_SPEED, self.center_x - player_sprite.center_x)

class Enemy2(arcade.Sprite):

    def follow_sprite(self, player_sprite):
        # Esta función es para que el Enemy2 (self) se mueva hacia el personaje (player.sprite).

        if self.center_y < player_sprite.center_y:
            self.center_y += min(ENEMY2_SPEED, player_sprite.center_y - self.center_y)
        elif self.center_y > player_sprite.center_y:
            self.center_y -= min(ENEMY2_SPEED, self.center_y - player_sprite.center_y)

        if self.center_x < player_sprite.center_x:
            self.center_x += min(ENEMYw_SPEED, player_sprite.center_x - self.center_x)
        elif self.center_x > player_sprite.center_x:
            self.center_x -= min(ENEMY2_SPEED_SPEED, self.center_x - player_sprite.center_x)

def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = InstructionView()
    window.show_view(start_view)
    arcade.run()

if __name__ == "__main__":
    main()
