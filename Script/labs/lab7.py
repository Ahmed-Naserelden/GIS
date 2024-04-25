# LAB 7
import arcpy
import re
arcpy.env.overwriteOutput = True
arcpy.env.workspace = r""
points = arcpy.GetParameterAsText(0)

countries = arcpy.GetParameterAsText(1)
out_path = arcpy.GetParameterAsText(2)


country_cursor = arcpy.SearchCursor(countries, ['FID', 'SOVEREIGNT', 'POP_EST'])
country_cursor = arcpy.UpdateCursor()
arcpy.MakeFeatureLayer_management(points, "points_layer")

total_count = 0
created_count = 0

# with arcpy.da.SearchCursor(countries, ['FID', 'SOVEREIGNT', 'POP_EST']):
for x in country_cursor:
    total_count += 1
    if x.getValue('POP_EST') > int(arcpy.GetParameterAsText(3)):
        created_count +=  1
        print(x.getValue('FID'))
        
        name = re.sub(r'[^a-zA-Z0-9\s]', '', x.getValue('SOVEREIGNT'))
        # re.sub(r'^a-zA-Z0-9\s', '', x.getValue('SOVEREIGNT'))
        arcpy.MakeFeatureLayer_management(countries, 'countries_layer', """ "FID"={} """.format(x.getValue('FID')))
        arcpy.SelectLayerByLocation_management('points_layer', 'WITHIN', 'countries_layer')
        arcpy.FeatureClassToFeatureClass_conversion('points_layer', out_path, "cityin{0}{1}".format(name, x.getValue('FID')))

    else:
        print("{} didn't meet the criteria".format(name))
    

print(total_count)
print(created_count)