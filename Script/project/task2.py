import arcpy

# points = r"C:\Users\biruni\Desktop\GIS\Data\Datasets"

# arcpy.env.workspace = "your_workspace"  # Path to your workspace
arcpy.env.overwriteOutput = True

# Input data
elevation_points = r"C:\Users\biruni\Desktop\GIS\Data\Datasets\ne_10m_geography_regions_elevation_points.shp"
land_regions = r"C:\Users\biruni\Desktop\GIS\Data\Datasets\ne_10m_land.shp"
out_path = r"C:\Users\biruni\Desktop\GIS\Output\task2";

# Output shapefiles
elevation_points_shapefile = r"C:\Users\biruni\Desktop\GIS\Output\task2\ElevationPoints.shp"  # Elevation points shapefile
land_points_shapefile = r"C:\Users\biruni\Desktop\GIS\Output\task2\LandPoints.shp"  # Land points shapefile

# Create shapefiles
arcpy.FeatureClassToFeatureClass_conversion(elevation_points, out_path, "ElevationPoints")
arcpy.FeatureClassToFeatureClass_conversion(land_regions, out_path, "LandPoints")

# Count points
elevation_point_count = arcpy.GetCount_management(elevation_points_shapefile)
land_point_count = arcpy.GetCount_management(land_points_shapefile)

# Print the counts
print("Number of elevation points:", elevation_point_count)
print("Number of land points:", land_point_count)
