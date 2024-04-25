# Geographic Data Analysis Project

This project aims to perform various spatial analyses using geographic datasets available in the attached folder. The analysis will be conducted using ArcMap GIS software, and the results will be documented in this README file. Additionally, a toolbox will be created to automate the processes outlined below.

## Datasets

The following datasets are included in the project folder:

1. "Land"
2. "geography region points"
3. "geography regions polys"
4. "geography region elevation points"
5. "glaciated areas"
6. "rivers_lake_centerlines"

**Note:** Before starting the analysis, extract the contents of the provided folder to ensure all datasets are accessible within your ArcMap environment.

## Tasks

1. **Data Exploration and Visualization**
   - List all datasets and visualize them in ArcMap.

2. **Shapefile Creation for Geography Region Elevation Points**
   - Create a shapefile for all geography region elevation points on land.
   - Create another shapefile for geography region points on land.
   - Print the number of points in each shapefile.

3. **Identification and Update of Unnamed Mountain**
   - Search for the mountain with no name in the elevation points.
   - Print its latitude and longitude.
   - Update its name with the value written in the comment field.

4. **Shapefile Creation for Glaciated Areas**
   - Create shapefiles for each region in geography region elevation points that are in glaciated areas.

5. **Shapefile Creation for Geographic Region Points**
   - Create shapefiles for geographic region points in the Indian Ocean, North Pacific Ocean, and South Pacific Ocean.
   - Print the names of these subregions.

6. **Shapefile Creation for Rivers and Lake Centerlines**
   - Create shapefiles for rivers and lake centerlines based on scalerank.

7. **Extraction of Geographic Regions Polys Information**
   - Using Search Cursor, print the name, region, and WIKIDATAID for all geography regions polys.

8. **Shapefile Creation for Lake Centerlines**
   - Create a shapefile for all Lake Centerline in river_Lake_centerline using only one condition.

9. **Shapefile Creation based on Elevation and Region**
   - Using Search Cursor, create shapefiles for geography region elevation points based on the condition that elevation > 1500 & region is “Africa”.

10. **Update of Empty Fields in Geography Region Points**
    - Using Update Cursor for multiple fields, update empty fields that are of string datatype in geography region points.

11. **Toolbox Development**
    - Create a toolbox implementing all the requirements above.
    - Ensure to print the logs in ArcGIS as well.

12. **Image Processing**
    - Print full path for a bunch of images.

13. **Exif Tags Extraction**
    - Print Exif Tags for the images.

14. **GPS Tags Extraction**
    - Print GPS Tags/Info for each image indicating which is geotagged & which is not.

15. **Geotagged Image Analysis**
    - Print latitude & longitude for each geotagged image.

## Conclusion

This README provides an overview of the tasks to be performed in the project. Each task will be executed using ArcMap and documented accordingly. The toolbox will facilitate automation of these tasks for efficient analysis of geographic data.
