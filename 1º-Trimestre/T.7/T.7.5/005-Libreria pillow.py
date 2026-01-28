from PIL import Image

imagen = Image.open("Tortuga.jpg")

pixel1 = imagen.getpixel((0, 0))

print(pixel1)