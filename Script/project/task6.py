import arcpy
arcpy.env.overwriteOutput = True
arcpy.env.workspace = r'F:\lec\gis\project\dataset'
output = r'F:\lec\gis\project\output'
disputed_areas = r'F:\lec\gis\project\dataset\ne_10m_admin_0_disputed_areas.shp'


arcpy.MakeFeatureLayer_management(disputed_areas, 'disputed')
disputedcursor = arcpy.SearchCursor(disputed_areas,['INCOME_GRP', 'NAME'])
for i in disputedcursor:
    if i.getValue('INCOME_GRP') < 4:
        arcpy.FeatureClassToFeatureClass_conversion('disputed', output, 'Income GRP')
        print(i.getValue('NAME'))