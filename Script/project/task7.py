import arcpy
arcpy.env.overwriteOutput = True
arcpy.env.workspace = r'F:\lec\gis\project\dataset'
airports = r'F:\lec\gis\project\dataset\ne_10m_airports.shp'

airportcursor = arcpy.SearchCursor(airports, ['Location','name','wikipedia'])
for i in airportcursor :
    if 'ramp' == i.getValue('Location'):
        print (i.getValue('name'), i.getValue('Location'),i.getValue('wikipedia'))



