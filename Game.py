import arcade # Importamos Arcade

#definimos la ventana de Arcade
arcade.open_window(800,600, 'Titulo Arcade',True,True) #(weight,lenth,titulo,reconfigurable,antialiasing)

arcade.start_render() # Comenzar a dibujar en pantalla

#dibujo

arcade.finish_render() # Finaliza el dibujo

arcade.run # Mostrar todo en ventana