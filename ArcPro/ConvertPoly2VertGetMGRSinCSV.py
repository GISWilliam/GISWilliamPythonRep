# Convert Polygon to Vertices and Get MGRS Coordinate in CSV
# Parameters:
# Label: Input Feature Class, Name: Input_Feature_Class, Data Type: Feature Layer, Type: Required, Direction: Input
# Label: Output Directory, Name: Output_Directory, Data Type: Folder, Type: Required, Direction: Input
# Label: Vertices File Name, Name: Vertices_File_Name, Data Type: String, Type: Required, Direction: Input
# Label: CSV File Name, Name: CSV_File_Name, Data Type: String, Type: Required, Direction: Input
# Label: Coordinate System, Name: Coordinate_System, Data Type: Coordinate System, Type: Required, Direction: Input

import arcpy
import os
# Variables to be used
InFC = arcpy.GetParameterAsText(0)
OutDIR = arcpy.GetParameterAsText(1)
VertName = arcpy.GetParameterAsText(2)
CSVFileName = arcpy.GetParameterAsText(3) + '.csv'
CoordinateSystem = arcpy.GetParameterAsText(4)  # New parameter for coordinate system
arcpy.AddMessage('Input Feature Class == {}, Output Directory == {}, Vertex File Name == {}, CSVFileName == {}, Coordinate System == {}'.format(InFC, OutDIR, VertName, CSVFileName, CoordinateSystem))
# Get Polygon Vertices to Shapefile
outVert = os.path.join(OutDIR, VertName)
arcpy.management.FeatureVerticesToPoints(
    in_features=InFC,
    out_feature_class=outVert,
    point_location="ALL"
)
arcpy.AddMessage('Created Vertices File')
# Get Vertices Projected to the User's Chosen Coordinate System
newVert = outVert + "_Projected"
arcpy.management.Project(
    in_dataset=outVert,
    out_dataset=newVert,
    out_coor_system=CoordinateSystem,
    transform_method=None,
    in_coor_system=CoordinateSystem,
    preserve_shape="NO_PRESERVE_SHAPE",
    max_deviation=None,
    vertical="NO_VERTICAL"
)
arcpy.AddMessage('Projected Vertices File')
# Calculate MGRS for Vertices
arcpy.management.AddField(newVert, 'Coordinate', 'TEXT')
arcpy.AddMessage('Added Field "Coordinate"')
# Calculate Field Geometry
arcpy.management.CalculateGeometryAttributes(
    in_features=os.path.join(OutDIR, newVert),
    geometry_property="Coordinate POINT_COORD_NOTATION",
    length_unit="",
    area_unit="",
    coordinate_system=CoordinateSystem,
    coordinate_format="MGRS"
)
arcpy.AddMessage('Coordinates Calculated in MGRS')
#Convert FeatureClass Data to CSV File
Points2Table = r'C:\Users\william.j.edwards235\OneDrive - US Army\512th ENG DET (GPC) Shared Docs\5_PLANS_AND_ANALYSIS\1_RFI\FY23\FY23_037_GTMO Tent Resize\Leeward\GeoPro\Leeward_Tent_Group_Verticie_WGS1984.shp'
toCSV = [['X', 'Y', 'NAME', 'MGRS']]
with arcpy.da.SearchCursor(Points2Table, ['SHAPE@XY', 'Name', 'Coordinate']) as curs:
    for row in curs:
        x, y = row[0]
        toCSV.append([x, y, row[1], row[2]])
print(toCSV[0])
print(toCSV[1])
#Creates a new CSV file (OVERRIDES Original File if Exists Already)
with open(os.path.join(OutDIR, CSVFileName), 'w') as file:
    for row in toCSV:
        #Removes Excess Data
        newstr = str(row).replace('[' , '')
        newstr = newstr.replace(']', '')
        newstr = newstr.replace("'", "")
        #Writes Feature information into CSV
        file.write(newstr)
        file.write('\n') #Creates a new line to properly import into CSV
