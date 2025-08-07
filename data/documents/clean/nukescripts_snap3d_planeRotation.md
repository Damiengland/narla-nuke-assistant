# nukescripts.snap3d.planeRotation
nukescripts.snap3d.planeRotation(_tri_ , _norm =None_)

Calculate the rotations around the X, Y and Z axes that will align a plane perpendicular to the Z axis with the given triangle.
Parameters

**tri** – A list or tuple of 3 _nukemath.Vector3 objects. The 3 points must describe the plane (i.e. they must not be collinear).
Returns

A _nukemath.Vector3 object where the x coordinate is the angle of rotation around the x axis and so on.
Raises

**ValueError** – if the three points are collinear.