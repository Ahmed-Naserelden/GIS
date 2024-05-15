import arcpy
import os
from PIL import Image, ExifTags

img_folder = r'C:\Users\biruni\Pictures\Camera Roll\New folder'
img_contents = os.listdir(img_folder)

for image in img_contents:
    fullpath = os.path.join(img_folder, image)
    pillow = Image.open(fullpath)
    exif = { ExifTags.TAGS[K]: v for K, v in pillow.getexif().items() if K in ExifTags.TAGS }
    print(exif)