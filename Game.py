import arcade  # Importamos Arcade

ancho = 1080
alto = 720
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