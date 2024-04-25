# 4
import arcpy
arcpy.env.overwriteOutput = True

points = r"C:\Users\biruni\Desktop\GIS\Data\ne_10m_populated_places.shp"
countries = r"C:\Users\biruni\Desktop\GIS\Data\ne_10m_admin_0_countries.shp"
out_path = r"C:\Users\biruni\Desktop\GIS\Output"
 
arcpy.MakeFeatureLayer_management(points, "points_layer")

for country in ['Egypt', 'Brazil']:
    print(country)
    
    arcpy.MakeFeatureLayer_management(countries, "countries_layer", """ "name"='{}' """.format(country))
    arcpy.SelectLayerByLocation_management('points_layer', 'WITHIN', 'countries_layer')
    arcpy.FeatureClassToFeatureClass_conversion('points_layer', out_path, 'cities_in_{}'.format(country))


