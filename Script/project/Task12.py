import arcpy
import os
arcpy.env.overwriteOutput = True
img_folder = r'C:\Users\biruni\Pictures\Camera Roll\New folder'
img_contents = os.listdir(img_folder)
for image in img_contents:
 print(image)
 fullpath = os.path.join(img_folder,image)
 print (fullpath)