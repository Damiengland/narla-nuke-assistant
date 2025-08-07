# nukescripts.snap3d.projectPoint
nukescripts.snap3d.projectPoint(_camera_ , _point_)  nuke.math.Vector2

Project the given 3D point through the camera to get 2D pixel coordinates.
Parameters

  * **camera** – The Camera node or name of the Camera node to use for projecting the point.
  * **point** – A nuke.math.Vector3 or of list/tuple of three float values representing the 3D point.
Raises

**ValueError** – If camera or point is invalid.