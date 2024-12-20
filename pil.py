from PIL import Image, ImageTk


# Crear una imagen en blanco de 100x100 px
image = Image.new('RGB', (100, 100), color='white')

# Guardar la imagen
image.save('test_image.png')

print("La imagen se ha guardado correctamente.")
