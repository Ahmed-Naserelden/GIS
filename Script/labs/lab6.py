# 6
import arcpy
import re
arcpy.env.overwriteOutput = True

points = r"C:\Users\biruni\Desktop\GIS\Data\ne_10m_populated_places.shp"
countries = r"C:\Users\biruni\Desktop\GIS\Data\ne_10m_admin_0_countries.shp"
out_path = r"C:\Users\biruni\Desktop\GIS\Output"


country_cursor = arcpy.SearchCursor(countries, ['FID', 'SOVEREIGNT', 'POP_EST'])

arcpy.MakeFeatureLayer_management(points, "points_layer")

total_count = 0
created_count = 0

for x in country_cursor:
    
    total_count += 1
    
    if x.getValue('POP_EST') > 50_000_000:
        
        created_count +=  1
        
        print(x.getValue('FID'))
        
        name = re.sub(r'[^a-zA-Z0-9\s]', '', x.getValue('SOVEREIGNT'))
        
        arcpy.MakeFeatureLayer_management(countries, 'countries_layer', """ "FID"={} """.format(x.getValue('FID')))
        
        arcpy.SelectLayerByLocation_management('points_layer', 'WITHIN', 'countries_layer')
        
        arcpy.FeatureClassToFeatureClass_conversion('points_layer', out_path, "cityin{0}{1}".format(name, x.getValue('FID')))

    else:
        print("{} didn't meet the criteria".format(name))
        

print(total_count)
print(created_count)