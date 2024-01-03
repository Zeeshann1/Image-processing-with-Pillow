from PIL import Image
from PIL import Image, ImageEnhance, ImageDraw
import os

#PIL : Pillow library is fork of PIL (python image library) 

path = "C:/Users/zeeshan/Desktop/Result"

# Check whether the specified path exists or not
isExist = os.path.exists(path)
print(isExist)

# Create a new directory because it does not exist
if not isExist:
    os.makedirs(path)
    print("The new directory is created!")


#Load&open image
image = Image.open('demo_image.jpg')
image.show()


# The file format of the source file.
print(image.format) # Output: JPEG

# The pixel format used by the image. Typical values are "1", "L", "RGB", or "CMYK."
print(image.mode) # Output: RGB

# Image size, in pixels. The size is given as a 2-tuple (width, height).
print(image.size) # Output: (1920, 1280)

# Colour palette table, if any.
print(image.palette) # Output: None

image.save('C:/Users/zeeshan/Desktop/Result/new_image.png')


#Resizing Images
new_image = image.resize((400, 400))
new_image.save('C:/Users/zeeshan/Desktop/Result/image_400.jpg')
print(image.size) # Output: (1920, 1280)
print(new_image.size) # Output: (400, 400)
image.thumbnail((400, 400))
image.save('C:/Users/zeeshan/Desktop/Result/image_thumbnail.jpg')
print(image.size) # Output: (400, 267)


#Cropping
box = (200, 300, 700, 600)
cropped_image = image.crop(box)
cropped_image.save('C:/Users/zeeshan/Desktop/Result/cropped_image.jpg')

# Print size of cropped image
print(cropped_image.size) # Output: (500, 300)


#Pasting an Image onto Another Image
# logo = Image.open('logo.png')
# image_copy = image.copy()
# position = ((image_copy.width - logo.width), (image_copy.height - logo.height))
# image_copy.paste(logo, position)
# image_copy.save('C:/Users/zeeshan/Desktop/Result/pasted_image.jpg')
# image_copy.paste(logo, position, logo)
# image_copy.save('C:/Users/zeeshan/Desktop/Result/pasted_image.jpg')


#Rotating Images

image_rot_90 = image.rotate(90)
image_rot_90.save('C:/Users/zeeshan/Desktop/Result/image_rot_90.jpg')

image_rot_180 = image.rotate(180)
image_rot_180.save('C:/Users/zeeshan/Desktop/Result/image_rot_180.jpg')
image.rotate(18).save('C:/Users/zeeshan/Desktop/Result/image_rot_18.jpg')
image.rotate(18, expand=True).save('C:/Users/zeeshan/Desktop/Result/image_rot_18.jpg')


#Flipping Images
image_flip = image.transpose(Image.FLIP_LEFT_RIGHT)
image_flip.save('C:/Users/zeeshan/Desktop/Result/image_flip.jpg')


# Drawing on Images

canvas = Image.new('RGB', (400, 300), 'white')
img_draw = ImageDraw.Draw(canvas)
img_draw.rectangle((70, 50, 270, 200), outline='red', fill='blue')
img_draw.text((70, 250), 'Hello World', fill='green')
canvas.save('C:/Users/zeeshan/Desktop/Result/drawn_image.jpg')


#Color Transforms
greyscale_image = image.convert('L')
greyscale_image.save('C:/Users/zeeshan/Desktop/Result/greyscale_image.jpg')
print(image.mode) # Output: RGB
print(greyscale_image.mode) # Output: L


#Splitting and Merging Bands
red, green, blue = image.split()
print(image.mode) # Output: RGB
print(red.mode) # Output: L
print(green.mode) # Output: L
print(blue.mode) # Output: L
new_image = Image.merge("RGB", (green, red, blue))
new_image.save('C:/Users/zeeshan/Desktop/Result/new_image.jpg')
print(new_image.mode) # Output: RGB


#Image enhancements
contrast = ImageEnhance.Contrast(image)
contrast.enhance(1.5).save('C:/Users/zeeshan/Desktop/Result/contrast.jpg')

color = ImageEnhance.Color(image)
color.enhance(1.5).save('C:/Users/zeeshan/Desktop/Result/color.jpg')

brightness = ImageEnhance.Brightness(image)
brightness.enhance(1.5).save('C:/Users/zeeshan/Desktop/Result/brightness.jpg')

sharpness = ImageEnhance.Sharpness(image)
sharpness.enhance(1.5).save('C:/Users/zeeshan/Desktop/Result/sharpness.jpg')