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

class BulletSprite(TurningSprite): #Definimos las balas
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

class MyWindow(arcade.Window):
    """ Main application class. """

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT)

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
        self.laser_sound = arcade.load_sound("sounds/laser1.ogg")

    def start_new_game(self):
        """ Set up the game and initialize the variables. """

        self.frame_count = 0
        self.game_over = False

        # Sprite lists
        self.all_sprites_list = arcade.SpriteList()
        self.asteroid_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.ship_life_list = arcade.SpriteList()

        # Set up the player
        self.score = 0
        self.player_sprite = ShipSprite("images/playerShip1_orange.png", SCALE)
        self.all_sprites_list.append(self.player_sprite)
        self.lives = 3

        # Set up the little icons that represent the player lives.
        cur_pos = 10
        for i in range(self.lives):
            life = arcade.Sprite("images/playerLife1_orange.png", SCALE)
            life.center_x = cur_pos + life.width
            life.center_y = life.height
            cur_pos += life.width
            self.all_sprites_list.append(life)
            self.ship_life_list.append(life)

        # Make the asteroids
        image_list = ("images/meteorGrey_big1.png",
                      "images/meteorGrey_big2.png",
                      "images/meteorGrey_big3.png",
                      "images/meteorGrey_big4.png")
        for i in range(3):
            image_no = random.randrange(4)
            enemy_sprite = AsteroidSprite(image_list[image_no], SCALE)

            enemy_sprite.center_y = random.randrange(BOTTOM_LIMIT, TOP_LIMIT)
            enemy_sprite.center_x = random.randrange(LEFT_LIMIT, RIGHT_LIMIT)

            enemy_sprite.change_x = random.random() * 2 - 1
            enemy_sprite.change_y = random.random() * 2 - 1

            enemy_sprite.change_angle = (random.random() - 0.5) * 2
            enemy_sprite.size = 4
            self.all_sprites_list.append(enemy_sprite)
            self.asteroid_list.append(enemy_sprite)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self.all_sprites_list.draw()

        # Put the text on the screen.
        output = "Score: {}".format(self.score)
        arcade.draw_text(output, 10, 70, arcade.color.WHITE, 14)

        output = "Asteroid Count: {}".format(len(self.asteroid_list))
        arcade.draw_text(output, 10, 50, arcade.color.WHITE, 14)

    def on_key_press(self, symbol, modifiers):
        """ Called whenever a key is pressed. """
        # Shoot if the player hit the space bar and we aren't respawning.
        if not self.player_sprite.respawning and symbol == arcade.key.SPACE:
            bullet_sprite = BulletSprite("images/laserBlue01.png", SCALE)

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

    def split_asteroid(self, asteroid: AsteroidSprite):
        """ Split an asteroid into chunks. """
        x = asteroid.center_x
        y = asteroid.center_y
        self.score += 1

        if asteroid.size == 4:
            for i in range(3):
                image_no = random.randrange(2)
                image_list = ["images/meteorGrey_med1.png",
                              "images/meteorGrey_med2.png"]

                enemy_sprite = AsteroidSprite(image_list[image_no],
                                              SCALE * 1.5)

                enemy_sprite.center_y = y
                enemy_sprite.center_x = x

                enemy_sprite.change_x = random.random() * 2.5 - 1.25
                enemy_sprite.change_y = random.random() * 2.5 - 1.25

                enemy_sprite.change_angle = (random.random() - 0.5) * 2
                enemy_sprite.size = 3

                self.all_sprites_list.append(enemy_sprite)
                self.asteroid_list.append(enemy_sprite)
        elif asteroid.size == 3:
            for i in range(3):
                image_no = random.randrange(2)
                image_list = ["images/meteorGrey_small1.png",
                              "images/meteorGrey_small2.png"]

                enemy_sprite = AsteroidSprite(image_list[image_no],
                                              SCALE * 1.5)

                enemy_sprite.center_y = y
                enemy_sprite.center_x = x

                enemy_sprite.change_x = random.random() * 3 - 1.5
                enemy_sprite.change_y = random.random() * 3 - 1.5

                enemy_sprite.change_angle = (random.random() - 0.5) * 2
                enemy_sprite.size = 2

                self.all_sprites_list.append(enemy_sprite)
                self.asteroid_list.append(enemy_sprite)
        elif asteroid.size == 2:
            for i in range(3):
                image_no = random.randrange(2)
                image_list = ["images/meteorGrey_tiny1.png",
                              "images/meteorGrey_tiny2.png"]

                enemy_sprite = AsteroidSprite(image_list[image_no],
                                              SCALE * 1.5)

                enemy_sprite.center_y = y
                enemy_sprite.center_x = x

                enemy_sprite.change_x = random.random() * 3.5 - 1.75
                enemy_sprite.change_y = random.random() * 3.5 - 1.75

                enemy_sprite.change_angle = (random.random() - 0.5) * 2
                enemy_sprite.size = 1

                self.all_sprites_list.append(enemy_sprite)
                self.asteroid_list.append(enemy_sprite)

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
                    arcade.check_for_collision_with_list(self.player_sprite,
                                                         self.asteroid_list)
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


def main():
    window = MyWindow()
    window.start_new_game()
    arcade.run()


if __name__ == "__main__":
    main()












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