from matplotlib import contour
import os
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

folder = "images\\cat"

for i in os.listdir(folder):

    image = Image.open(os.path.join(folder, i))
    image =  image.resize((200,200))
    pixels = np.array(image)

    # this is give informations about image
    print("File:", i)
    print("Size:", image.size)
    print("Shape:", pixels.shape)

    print()

    print("Pixel:", pixels[100, 100])
    
    ## this is tell us that first channel is red, second channel is green, third channel is blue 
    # or it gives vallue for a one pixel in colour code
    print("Red:", pixels[100, 100, 0])
    print("Green:", pixels[100, 100, 1])
    print("Blue:", pixels[100, 100, 2])
    print("Top-left pixel:", pixels[0, 0])
    print("Center pixel:", pixels[100, 100])
    print("Last pixel:", pixels[198, 198])

    # find total pixels in the image 
    print("Total pixels:", pixels.shape[0] * pixels.shape[1])

    # normalize the pixel values 
    normalized = pixels / 255.0
    print("Normalized:", normalized[100, 100])
    print("Minimum:", normalized.min())
    print("Maximum:", normalized.max())

    plt.imshow(normalized)
    plt.title("Normalized Image")
    plt.show()



    