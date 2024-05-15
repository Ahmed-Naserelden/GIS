import arcpy
import os
import time
import pandas as pd


arcpy.env.workspace = r"C:\Users\Start\Desktop\New folder (4)\gis labs\New folder\Data"
arcpy.env.overwriteOutput = True
# Input dataset
land = r"C:\Users\Start\Desktop\New folder (4)\gis labs\New folder\Data\ne_10m_land.shp"
output  = r"C:\Users\Start\Desktop\New folder (4)\gis labs\New folder\Output"

geography_rpoints=r"C:\Users\Start\Desktop\New folder (4)\gis labs\New folder\Data\ne_10m_geography_regions_points.shp"



update2=arcpy.UpdateCursor(geography_rpoints,['name_alt','comment','label','subregion'])
updated_records = 0
for x in update2:
    if x.getValue('name_alt') == ' ':
        x.setValue('name_alt', 'hello')
        update2.updateRow(x)
        updated_records += 1
    elif x.getValue('comment') == ' ':
        x.setValue('comment', 'hello')
        update2.updateRow(x)
        updated_records += 1
    elif x.getValue('label') == ' ':
        x.setValue('label', 'hello')
        update2.updateRow(x)
        updated_records += 1
    elif x.getValue('subregion') == ' ':
        x.setValue('subregion', 'hello')
        update2.updateRow(x)
        updated_records += 1

arcpy.AddMessage("Number of records updated: {}".format(updated_records))


