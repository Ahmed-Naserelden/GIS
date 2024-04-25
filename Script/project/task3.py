import arcpy

# Set environment settings
arcpy.env.workspace = "your_workspace"  # Path to your workspace
arcpy.env.overwriteOutput = True

# Input data
elevation_points = r"C:\Users\biruni\Desktop\GIS\Data\Datasets\ne_10m_geography_regions_elevation_points.shp"  # Elevation points feature class

# # Search for mountain with no name
# cursor =  arcpy.SearchCursor(elevation_points, ["name", "lat_y", "long_x", "comment"])
# g, cnt = 0, 0
# for row in cursor:
#     g += 1
#     # Print latitude and longitude
#     if row.getValue('name') == ' ':
#         cnt += 1
#         # print(row.getValue('name'))
#         print("Latitude:", row.getValue('lat_y'))
#         print("Longitude:", row.getValue('long_x'))
        
#         new_name = row.getValue('comment')
#         # # Update the feature
#         with arcpy.da.UpdateCursor(elevation_points, ["name"]) as update_cursor:
#             for update_row in update_cursor:
#                 update_row[0] = new_name
#                 update_cursor.updateRow(update_row)
# print(g, cnt)

cnt = 0
ncomment = 0

no_name_query = "name = ' '"  # Assuming "Name" is the field containing mountain names
cursor = arcpy.da.SearchCursor(elevation_points, ["name", "lat_y", "long_x", "comment"], no_name_query)
for row in cursor:
    cnt += 1
    # Print latitude and longitude
    # if row[3] == ' ':
        # ncomment += 1
    print("Latitude:", row[1])
    print("Longitude:", row[2])
    
    # Update name with comment
    new_name = row[3]  # Assuming "Comment" contains the new name
    # Update the feature
    update_cursor = arcpy.da.UpdateCursor(elevation_points, ["name", "comment"], no_name_query)
    for update_row in update_cursor:
        if update_cursor[1] == row[3]:
            update_row[0] = new_name
            update_cursor.updateRow(update_row)
    print("Updated mountain name to:", new_name)
print(cnt)
print(ncomment)