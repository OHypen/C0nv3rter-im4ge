from PIL import Image #pip install Pillow

img= Image.open("Images/nomeDaImagem.jpg")
blackAndWhite = img.convert("L")
blackAndWhite.save('Images/nomeDaImagem.jpeg')
blackAndWhite.show()


#To use this code it is necessary to have Python and Pillow installed.
