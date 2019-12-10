#################################################
"""
Create and solve a service analysis layer for ArcPro
Current ArcPro 2.3.2 NA
Author: Andrew Makowicki
"""
#################################################

try:
    # Import libraries
    import arcpy
    from arcpy import env
    import arcpy.na
    import os
    
    # Check for NA Extension
    if arcpy.CheckExtension("network") == "Available":
        arcpy.CheckOutExtension("network")
    else:
        raise arcpy.ExecuteError("Network Analyst Extension not available.")

    # Environment settings
    output_dir = r'D:\Cases\CarWash\CarWash' # switch out with your workspace file path
    env.workspace = os.path.join(output_dir, "CarWash.gdb")
    env.overwriteOutput = True

    # Set network route feature dataset and input data -- set local envrionment parameters
    na_network_data_source = r'C:\ArcGIS\Business Analyst\US_2018\Data\Streets Data\NorthAmerica.gdb\Routing\Routing_ND' # point to Routing_ND feature dataset
    input_gdb = r'D:\Cases\CarWash\CarWash\CarWash.gdb' # point to user geodatabase file path
    
    layer_name = str('Service_Area_Analysis') # create layer name for OD Cost Matrix
    travel_mode = "Driving Time" # call travel mode for analysis
           
    origin = os.path.join(input_gdb, "Feature_Dataset", "Facilities_PointShapefile") # point to assigned origins shapefile, currently file structure pointing to database --> feature dataset --> point shapefile
    
    output_layer_file = os.path.join(output_dir, layer_name + ".lyrx") # out directory and file type for OD Cost Matrix, lyrx Pro layer file type


    # Create Service Area layer
    result_object = arcpy.MakeServiceAreaAnalysisLayer_na(na_network_data_source, layer_name, travel_mode, "FROM_FACILITIES", [10, 15, 20, 30], output_type="POLYGONS", geometry_at_overlaps="OVERLAP", geometry_at_cutoffs="DISKS") # creating Service Area layer with 10, 15, 20 and 30 minute drive time catchments
    layer_object = result_object.getOutput(0)
    print("Service area analysis layer successfully created")

    sub_layers = arcpy.na.GetNAClassNames(layer_object)
    print("Sublayer names: ", sub_layers)

    origin_layer_name = sub_layers["Facilities"]
    print("Facilities layer name: ", origin_layer_name)

    field_mapping_origin = arcpy.na.NAClassFieldMappings(layer_object, origin_layer_name)
    field_mapping_origin["Name"].mappedFieldName = "RecordID" # establish DC_ID as the "Name" primary key to rectify origin location data after analysis
    arcpy.na.AddLocations(layer_object, origin_layer_name, origin, field_mapping_origin)
    print("Facilities field mapping: ", field_mapping_origin, "Facilities added to layer")

    # Solve Service Area
    arcpy.na.Solve(layer_object)

    # Save the solved Service area layer
    layer_object.saveACopy(output_layer_file)

    print("Service area layer solved.")

except Exception as e:
    # If error occured print line number
    import traceback, sys
    tb = sys.exc_info()[2]
    print("An error has occured at line %i" % tb.tb_lineno)
    print(str(e))
