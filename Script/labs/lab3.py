# 3

import arcpy

# arcpy.env.workspace(r"C:\Users\biruni\Desktop\GIS\Data")

points = r"C:\Users\biruni\Desktop\GIS\Data\ne_10m_populated_places.shp"
countries = r"C:\Users\biruni\Desktop\GIS\Data\ne_10m_admin_0_countries.shp"


arcpy.MakeFeatureLayer_management(points, 'points_layer')
arcpy.MakeFeatureLayer_management(countries, 'countries_layer', """ "NAME"='United States of America'  """)


arcpy.SelectLayerByLocation_management('points_layer', 'WITHIN', 'countries_layer')

out_path = r"C:\Users\biruni\Desktop\GIS\Output"
arcpy.conversion.FeatureClassToFeatureClass("points_layer", out_path, "ThirdLabOUTPUT")

