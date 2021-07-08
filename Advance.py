import arcade
import math
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
SCALE = 0.5
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

class InstructionView(arcade.View): # Definimos el menú inicial

    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture("img/introWallpaper.png")
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

class TurningSprite(arcade.Sprite): # Sprite que establece su angulo en direccion en la que viaja la nave

    def update(self):
        super().update()
        self.angle = math.degrees(math.atan2(self.change_y, self.change_x))

class ShipSprite(arcade.Sprite): # Sprite que representa nuestra nave

    def __init__(self, filename, scale):

        super().__init__(filename, scale) # Super llama a la funcion padre

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

class AsteroidSprite(arcade.Sprite):
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


class BulletSprite(TurningSprite):
    """
    Class that represents a bullet.

    Derives from arcade.TurningSprite which is just a Sprite
    that aligns to its direction.
    """

    def update(self):
        super().update()
        if self.center_x < -100 or self.center_x > 1500 or \
                self.center_y > 1100 or self.center_y < -100:
            self.kill()

class MyGame(arcade.View):
    """ Main application class. """
    def __init__(self):
        super().__init__()

        self.frame_count = 0

        self.game_over = False

        # Sprite lists
        self.all_sprites_list = None
        self.asteroid_list = None
        self.bullet_list = None
        self.ship_life_list = None

        # Set up the player
        self.score = 0
        self.player_sprite = None
        self.lives = 3

        # Sounds
        self.laser_sound = arcade.load_sound("sound/blaster.mp3")

        # Esta variable guarda el background
        self.background = None

        # Set the background color
        #arcade.set_background_color(arcade.color.BLACK)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Cargamos el background
        self.background = arcade.load_texture("img/gameWallpaper.jpg")

        self.frame_count = 0
        self.game_over = False

        # Sprite lists
        self.all_sprites_list = arcade.SpriteList()
        self.asteroid_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.ship_life_list = arcade.SpriteList()

        # Set up the player
        self.score = 0
        self.player_sprite = ShipSprite("img/SpaceShip_Sprite.png", SCALE)
        self.all_sprites_list.append(self.player_sprite)
        self.lives = 3

        # Set up the little icons that represent the player lives. todo config vidas
        cur_pos = 10
        for i in range(self.lives):
            life = arcade.Sprite("img/SpaceShip_Life.png",SCALE)
            life.center_x = cur_pos + life.width
            life.center_y = life.height
            cur_pos += life.width
            self.all_sprites_list.append(life)
            self.ship_life_list.append(life)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw the background texture
        arcade.draw_lrwh_rectangle_textured(0, 0,SCREEN_WIDTH, SCREEN_HEIGHT,self.background)

    # Draw all the sprites.
        self.all_sprites_list.draw()


        # Put the text on the screen.
        output = "Score: {}".format(self.score)
        arcade.draw_text(output, 1200, 700, arcade.color.AMBER, 14)


    def on_key_press(self, symbol, modifiers):
        """ Called whenever a key is pressed. """
        # Shoot if the player hit the space bar and we aren't respawning.
        if not self.player_sprite.respawning and symbol == arcade.key.SPACE:
            bullet_sprite = BulletSprite("img/laser.png", SCALE)

            bullet_speed = 13
            bullet_sprite.change_y = \
                math.cos(math.radians(self.player_sprite.angle)) * bullet_speed
            bullet_sprite.change_x = \
                -math.sin(math.radians(self.player_sprite.angle)) \
                * bullet_speed

            bullet_sprite.center_x = self.player_sprite.center_x
            bullet_sprite.center_y = self.player_sprite.center_y
            bullet_sprite.update()

            self.all_sprites_list.append(bullet_sprite)
            self.bullet_list.append(bullet_sprite)

            arcade.play_sound(self.laser_sound)

        if symbol == arcade.key.LEFT:
            self.player_sprite.change_angle = 3
        elif symbol == arcade.key.RIGHT:
            self.player_sprite.change_angle = -3
        elif symbol == arcade.key.UP:
            self.player_sprite.thrust = 0.15
        elif symbol == arcade.key.DOWN:
            self.player_sprite.thrust = -.2

    def on_key_release(self, symbol, modifiers):
        """ Called whenever a key is released. """
        if symbol == arcade.key.LEFT:
            self.player_sprite.change_angle = 0
        elif symbol == arcade.key.RIGHT:
            self.player_sprite.change_angle = 0
        elif symbol == arcade.key.UP:
            self.player_sprite.thrust = 0
        elif symbol == arcade.key.DOWN:
            self.player_sprite.thrust = 0

    def update(self, x):
        """ Move everything """

        self.frame_count += 1

        if not self.game_over:
            self.all_sprites_list.update()

            for bullet in self.bullet_list:
                asteroids = \
                    arcade.check_for_collision_with_list(bullet, self.asteroid_list)
                for asteroid in asteroids:
                    self.split_asteroid(asteroid)
                    asteroid.kill()
                    bullet.kill()

            if not self.player_sprite.respawning:
                asteroids = \
                    arcade.check_for_collision_with_list(self.player_sprite,self.asteroid_list)
                if len(asteroids) > 0:
                    if self.lives > 0:
                        self.lives -= 1
                        self.player_sprite.respawn()
                        self.split_asteroid(asteroids[0])
                        asteroids[0].kill()
                        self.ship_life_list.pop().kill()
                        print("Crash")
                    else:
                        self.game_over = True
                        print("Game over")



# Final
def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = InstructionView()
    window.show_view(start_view)
    arcade.run()

if __name__ == "__main__":
    main()
