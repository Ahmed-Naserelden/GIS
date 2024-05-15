import arcpy
import os
import time
import pandas as pd



land = r"C:\Users\Start\Desktop\New folder (4)\gis labs\New folder\Data\ne_10m_land.shp"
output  = r"C:\Users\Start\Desktop\New folder (4)\gis labs\New folder\Output"
lakes  =r"C:\Users\Start\Desktop\New folder (4)\gis labs\New folder\Data\ne_10m_rivers_lake_centerlines.shp"


arcpy.MakeFeatureLayer_management(lakes,'countries_layer',""" "featurecla"='Lake Centerline' """)
arcpy.FeatureClassToFeatureClass_conversion('countries_layer', output,"lakecentrlinesout")
