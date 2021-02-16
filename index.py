from PIL import Image

img= Image.open("Images/nomeDaImagem.jpg")
blackAndWhite = img.convert("L")
blackAndWhite.save('Images/nomeDaImagem.jpeg')
blackAndWhite.show()