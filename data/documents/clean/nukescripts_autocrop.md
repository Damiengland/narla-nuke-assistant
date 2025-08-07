# nukescripts.autocrop
nukescripts.autocrop(_first =None_, _last =None_, _inc =None_, _layer ='rgba'_)

Run the CurveTool’s AutoCrop function on each selected node over the specified frame range and channels. If the range values are None, the project first_frame and last_frame are used; if inc is None, 1 is used. After execution, the CurveTool AutoCrop results are copied into a Crop node attached to each selected node.