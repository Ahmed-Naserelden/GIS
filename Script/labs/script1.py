#
# # LAB 1
# import arcpy
#
# arcpy.env.workspace = r"C:\Users\biruni\Desktop\GIS\Data"
#
# # LAB 2
# feature_list = arcpy.ListFeatureClasses()
# print(feature_list)
#
# # LAB 3
#
# countries = r"C:\Users\biruni\Desktop\GIS\Data\ne_10m_admin_0_countries.shp"
# points = r"C:\Users\biruni\Desktop\GIS\Data\ne_10m_populated_places.shp"
#
# arcpy.MakeFeatureLayer_management(points, 'points_layer')
# arcpy.MakeFeatureLayer_management(countries, 'countries_layer')
#
# out_path = r"C:\Users\biruni\Desktop\GIS\Output"
# arcpy.FeatureClassesToFeatureClass_conversion('points_layer', out_path, 'thirdLabOutput')
#
#
# # LAB 4
# countries = r"C:\Users\biruni\Desktop\GIS\Data\ne_10m_admin_0_countries.shp"
# points = r"C:\Users\biruni\Desktop\GIS\Data\ne_10m_populated_places.shp"
#
# countries_list = ["Egypt", "Barzil"]
# arcpy.MakeFeatureLayer_management(points, "points_layer")
# for x in countries_list:
#     print(x)
#     arcpy.MakeFeatureLayer_management(countries, "countries_Layer", f"Name = {x}")
#     arcpy.SelectLayerByLocation_mangement("pints_layer", "WITHIN", "countries_layer")
#     arcpy.ListFeatureClassesToFeatureClass_conversion('points_layer', out_path, f"cities_in_{x}")
#
# # LAB 5
# cities_cursor = arcpy.SearchCursor(points, ['NAME', 'POP_MAX', 'TIMEZONE'])
# for x in cities_cursor:
#     print(x.getValue('Name'))
#     print(x.getValue('POP_MAX'))
#     print(x.getValue('TIMEZONE'))
#     print("")
#
# # LAB 6
# countries_cursor = arcpy.SearchCursor(countries, ['FID', 'SOVEREIGNT'])
# arcpy.MakeFeatureLayer_management(points, 'points_layer')
#
# for x in countries_cursor:
#     name = str(x.getValue('SOVEREIGNT')).replace('(', '').replace(')', '').replace(' ', '_')
#     print(name)
#
#
#     arcpy.MakeFeatureLayer_management(countries, 'countries_layer', f"FID = { x.getValue('FID') }")
#     arcpy.SelectLayerByLocation_mangement("points_layar", "WITHIN", "countries_layer")
#     arcpy.FeatureClassesToFeatureClass_conversion('points_layer', out_path, f'cityin{name},{x.getValue("FID")}')
#
# # LAB 7
# ================================================================================================================================
# ================================================================================================================================
# ================================================================================================================================
# ================================================================================================================================
# ================================================================================================================================
# ================================================================================================================================
# ================================================================================================================================
# ================================================================================================================================
# ================================================================================================================================
# ================================================================================================================================
# ================================================================================================================================
# ================================================================================================================================






























