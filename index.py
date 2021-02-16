from PIL import Image #pip install Pillow

img= Image.open("Images/nomeDaImagem.jpg")
blackAndWhite = img.convert("L")
blackAndWhite.save('Images/nomeDaImagem.jpeg')
blackAndWhite.show()
