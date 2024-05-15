from PIL import Image, ExifTags
import os



img_folder = r'C:\Users\biruni\Pictures\Camera Roll\New folder'
img_contents = os.listdir(img_folder)

for image in img_contents:
    fullpath = os.path.join(img_folder, image)
    pillow = Image.open(fullpath)
    exif = {ExifTags.TAGS[K]: v for K, v in pillow.getexif().items() if K in ExifTags.TAGS}
    gpsall = {}
    try:
        exif is None or "GPSInfo" not in exif
        print(fullpath," Not geotagged")
        for k in exif['GPSInfo'].keys():
            dval = ExifTags.GPSTAGS.get(k)
            gpsall[dval] = exif['GPSInfo'][k]
        longref = gpsall.get('GPSLongitudeRef')
        long = gpsall.get('GPSLongitude')
        latref = gpsall.get('GPSLatitudeRef')
        lat = gpsall.get('GPSLatitude')


        print("{0}:".format(image))
        print("Longitude: {0} {1}".format(longref, long))
        print("Latitude: {0} {1}".format(latref, lat))
    except KeyError:
        print("{0}: This image has no GPS info".format(image))
