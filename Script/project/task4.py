import arcpy


arcpy.env.workspace = r"C:\Users\biruni\Desktop\GIS\Data\Datasets"
arcpy.env.overwriteOutput = True

geography_regions = "ne_10m_geography_regions_elevation_points.shp" 
glaciated_areas = "ne_10m_glaciated_areas.shp"

out_path = r"C:\Users\biruni\Desktop\GIS\Output\task4"


arcpy.MakeFeatureLayer_management(geography_regions, "geography_regions_elevation_layer")
glaciated_areas_cursor = arcpy.SearchCursor(glaciated_areas, ['FID', 'scalerank'])

cnt = 0
vis = []

for i in range(0, 100):
    vis.append(False)

for x in glaciated_areas_cursor:
    
    if vis[x.getValue('scalerank')]:
        continue

    vis[x.getValue('scalerank')] = True
    
    cnt += 1
    
    arcpy.MakeFeatureLayer_management(glaciated_areas, 'glaciated_areas_layer', """ "scalerank"={} """.format(x.getValue('scalerank')))
        
    arcpy.SelectLayerByLocation_management('geography_regions_elevation_layer', 'WITHIN', 'glaciated_areas_layer')
    
    arcpy.FeatureClassToFeatureClass_conversion('geography_regions_elevation_layer', out_path, "area{0}_{1}".format(cnt, x.getValue('FID')))


print(cnt)