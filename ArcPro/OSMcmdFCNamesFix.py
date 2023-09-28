# Convert OSM(CMD) Feature Class Names to Readable
# Parameters:
# Label: Input Geodatabase, Data Type: Workspace, Type: Required, Direction: Input
# Description:
# Uses a provided Geodatabase of the OpenStreetMap pull from AGC's CMB Online and converts the feature names into readble format.

import arcpy
import os
inGD = arcpy.GetParameterAsText(0) # Used for changing into toolbox item
#inGD = r'C:\Users\william.j.edwards235\Downloads\CO_colombia\CO_colombia.gdb'
arcpy.env.workspace = inGD
featureclasses = arcpy.ListFeatureClasses()
# List of Names for Feature Classes to be Renamed to.
osmCMDfc = [['osm_aero', 'Aeronautical'],
            ['osm_aero_l', 'Aeronautical_L'],
            ['osm_aero_a', 'Aeronautical_A'],
            ['osm_boundaries_l', 'Boundaries_L'],
            ['osm_boundaries_a','Boundaries_A'],
            ['osm_buildings', 'Buildings'],
            ['osm_landuse', 'Landuse'],
            ['osm_natural', 'Natural'],
            ['osm_natural_l', 'Natural_L'],
            ['osm_natural_a', 'Natural_A'],
            ['osm_places','Places'],
            ['osm_places_l', 'Places_L'],
            ['osm_places_a', 'Places_A'],
            ['osm_pofw', 'PlaceOfWorship'],
            ['osm_pofw_a', 'PlaceOfWorship_A'],
            ['osm_pois', 'PointsOfInterest'],
            ['osm_pois_a', 'PointsOfInterest_A'],
            ['osm_power', 'Power'],
            ['osm_power_l', 'Power_L'],
            ['osm_power_a', 'Power_A'],
            ['osm_railways', 'Railways'],
            ['osm_roads', 'Roads'],
            ['osm_routes', 'Routes'],
            ['osm_traffic', 'Traffic'],
            ['osm_traffic_a', 'Traffic_A'],
            ['osm_transport', 'Transport'],
            ['osm_transport_a', 'Transport_A'],
            ['osm_utility_markers', 'Utility_Markers'],
            ['osm_utilities_l', 'Utilities_L'],
            ['osm_utilities_a', 'Utilities_A'],
            ['osm_water', 'Water'],
            ['osm_waterways', 'Waterways'],
            ['osm_waterways_a', 'Waterways_A']]
for fc in featureclasses:
    for row in osmCMDfc:
        if fc == row[0]:
            newIn = os.path.join(inGD, fc)
            newOut = os.path.join(inGD,row[1])
            arcpy.management.Rename(in_data=newIn, out_data=newOut, data_type="FeatureClass")
