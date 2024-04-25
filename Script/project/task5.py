import arcpy

arcpy.env.workspace = r"C:\Users\biruni\Desktop\GIS\Data\Datasets"
arcpy.env.overwriteOutput = True

geography_regions = r"C:\Users\biruni\Desktop\GIS\Data\Datasets\ne_10m_geography_regions_points.shp" 
land = r"C:\Users\biruni\Desktop\GIS\Data\Datasets\ne_10m_land.shp";

glaciated_areas = "ne_10m_glaciated_areas.shp"

out_path = r"C:\Users\biruni\Desktop\GIS\Output\task5";
 
 
for x in ['Indian Ocean', 'North Pacific Ocean', 'South Pacific Ocean']:
    arcpy.MakeFeatureLayer_management(geography_regions, "geography_regions_points_layer", """ "subregion"='{}' """.format(x))
    arcpy.FeatureClassToFeatureClass_conversion('geography_regions_points_layer', out_path, 'cities_in_{}'.format(x))

