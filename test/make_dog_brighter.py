from PIL import Image

# open the image
img = Image.open("dog.jpg")

# get the image's pixels
pixels = img.load()

# get the number of pixels in the image
n = len(pixels.keys())

# create a list to hold the new pixel values
new_pixels = []

# loop through each pixel in the image
for i in range(n):
    # get the current pixel value
    current_pixel = pixels[i]

    # increase the pixel value by 2
    new_pixel = current_pixel + 2

    # add the new pixel value to the list
    new_pixels.append(new_pixel)

# update the image's pixels with the new pixel values
pixels.clear()
pixels.update(new_pixels)

# save the updated image
img.save("dog_brighter.jpg")
