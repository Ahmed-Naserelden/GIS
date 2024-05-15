import arcpy
import os
import time
import pandas as pd


arcpy.env.workspace = r"C:\Users\Start\Desktop\New folder (4)\gis labs\New folder\Data"
arcpy.env.overwriteOutput = True
# Input dataset
land = r"C:\Users\Start\Desktop\New folder (4)\gis labs\New folder\Data\ne_10m_land.shp"
output  = r"C:\Users\Start\Desktop\New folder (4)\gis labs\New folder\Output"
geography_epoints=r"C:\Users\Start\Desktop\New folder (4)\gis labs\New folder\Data\ne_10m_geography_regions_elevation_points.shp"
# task 9
selected_features = []


searchh=arcpy.SearchCursor(geography_epoints,['Shape','featurecla','elevation','region'])

for r in searchh:
    if r.getValue("elevation") >1500 and r.getValue("region") == "Africa":
        selected_features.append(r.getValue("Shape"))

# Create a new shapefile for the selected features
output_shapefile = os.path.join(output, "elevation_gt_1500_in_Africa.shp")
arcpy.CopyFeatures_management(selected_features, output_shapefile)
arcpy.AddMessage("New shapefile created with features having elevation > 1500 in Africa:")
arcpy.AddMessage(output_shapefile)
