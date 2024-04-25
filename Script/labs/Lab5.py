# 5
import arcpy
arcpy.env.overwriteOutput = True

points = r"C:\Users\biruni\Desktop\GIS\Data\ne_10m_populated_places.shp"
countries = r"C:\Users\biruni\Desktop\GIS\Data\ne_10m_admin_0_countries.shp"
out_path = r"C:\Users\biruni\Desktop\GIS\Output"

attr = ['NAME', 'POP_MAX', 'TIMEZONE']
cities_cursor = arcpy.SearchCursor(points, ['NAME', 'POP_MAX', 'TIMEZONE'])
for x in cities_cursor: 
    try:
        print(x.getValue('NAME'))
        print(x.getValue('POP_MAX'))
        print(x.getValue('TIMEZONE'))
    except:
        print(x.getValue('POP_MAX'))
        print(x.getValue('TIMEZONE'))
        
    print("")