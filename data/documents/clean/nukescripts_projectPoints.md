# nukescripts.projectPoints
nukescripts.projectPoints(_camera =None_, _points =None_)

projectPoint(camera, points) -> list of nuke.math.Vector2
Project the given 3D point through the camera to get 2D pixel coordinates.
Parameters

  * **camera** – The Camera node or name of the Camera node to use for projecting the point.
  * **points** – A list or tuple of either nuke.math.Vector3 or of list/tuples of three float values representing the 3D points.
Raises

**ValueError** – If camera or point is invalid.