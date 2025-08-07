# nukescripts.projectSelectedPoints
nukescripts.projectSelectedPoints(_cameraName ='Camera1'_)  iterator yielding nuke.math.Vector2

Using the specified camera, project all of the selected points into 2D pixel coordinates and return their locations.
Parameters

**cameraName** – Optional name of the Camera node to use for projecting the points. If omitted, will look for a node called Camera1.