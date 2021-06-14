import arcade

#constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Space Game"
SCALING = 0.2

class MyGame(arcade.Window):
    """
    Clase de aplicación principal.

    NOTE: Continúe y elimine los métodos que no necesita. Si necesita un método, elimine el "pass"
    y reemplácelo con su propio código. No deje "pass" en este programa.
    """
    #-------------------------------------------------------------------------------------------------#
    def _init_(self, width, height, title):
        super()._init_(width, height, title)

        arcade.set_background_color((155,33,40)) 
        #arcade.set_background_color(arcade.color.AMAZON)

        # Si tienes listas de sprites, deberías crearlas aquí,

        # Y ponlos en None
    #-------------------------------------------------------------------------------------------------#
    def setup(self):
        """ Configura las variables del juego. Llame para reiniciar el juego. """
        # Crea tus sprites y listas de sprites aquí
        pass

    def on_draw(self):
        """
        Renderizar la pantalla.
        """

        # Este comando debería ocurrir antes de comenzar a dibujar. Se despejará
        # la pantalla al color de fondo, y borramos lo que dibujamos el último fotograma.
        arcade.start_render()
        

        # llame a draw () en todas sus listas de sprites a continuación

    def on_update(self, delta_time):
        """
        Toda la lógica para moverse, y la lógica del juego va aquí. 
        Normalmente, llamará a update () en las listas de sprites que lo necesiten.
        """
        pass
    #-------------------------------------------------------------------------------------------------#
    def on_key_press(self, key, key_modifiers):
        #Called whenever a key on the keyboard is pressed.
        pass
    
    def on_key_release(self, key, key_modifiers):
        #Called whenever the user lets off a previously pressed key.
        pass
    #-------------------------------------------------------------------------------------------------#
    def on_mouse_motion(self, x, y, delta_x, delta_y):
        #Called whenever the mouse moves.
        pass
    #-------------------------------------------------------------------------------------------------#
    def on_mouse_press(self, x, y, button, key_modifiers):
        #Called when the user presses a mouse button.
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        #Called when a user releases a mouse button.
        pass
    #-------------------------------------------------------------------------------------------------#

def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if _name_ == "_main_":
    main()
