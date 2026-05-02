# By DarkSATHI

from PIL import Image

# Un exemple de filtre
contraste = [
[0, -1, 0],
[-1, 5, -1],
[0, -1, 0]
]

flou = [
[1, 1, 1],
[1, 1, 1],
[1, 1, 1]
]

detectionBord = [
[0, 1, 0],
[1, -4, 1],
[0, 1, 0]
]

detectionBord2 = [
[-1, -1, -1],
[-1, 8, -1],
[-1, -1, -1]
]

sobel = [
[-1, 0, 1],
[-2, 0, 2],
[-1, 0, 0]
]

repoussage = [
    [-2, -1, 0],
    [-1, 1, 1],
    [0, 1, 2]
    ]


def convolutionComposante(photo, position, filtre, composante):
    i, j = position
    intensite =  photo.getpixel((i-1, j-1))[composante]*filtre[0][0] \
                    + photo.getpixel((i-1, j))[composante]*filtre[1][0] \
                    + photo.getpixel((i-1, j+1))[composante]*filtre[2][0] \
                    + photo.getpixel((i, j-1))[composante]*filtre[0][1] \
                    + photo.getpixel((i, j))[composante]*filtre[1][1] \
                    + photo.getpixel((i, j+1))[composante]*filtre[2][1] \
                    + photo.getpixel((i+1, j-1))[composante]*filtre[0][2] \
                    + photo.getpixel((i+1, j))[composante]*filtre[1][2] \
                    + photo.getpixel((i+1, j+1))[composante]*filtre[2][2]
    return intensite

def convolution(photo, position, filtre):
    i, j = position
    return (convolutionComposante(photo, position, filtre, 0),
            convolutionComposante(photo, position, filtre, 1),
            convolutionComposante(photo, position, filtre, 2))

def filtrage(addresseImage, filtre, nomImagefiltree):
    photo = Image.open(addresseImage)
    width, height = photo.size
    imagearrivee = Image.new('RGB',(width, height))
    for i in range(1, width-1):
        for j in range(1, height-1):
            pixel = convolution(photo, (i,j), filtre)
            imagearrivee.putpixel((i,j),pixel)
    imagearrivee.save(nomImagefiltree)
