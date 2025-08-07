# nukescripts.snap3d.rotatePivotToPoints
nukescripts.snap3d.rotatePivotToPoints(_nodeToSnap_)

Rotate the specified node’s Pivot Point to the average of the current vertex selection normals in the active viewer. The nodeToSnap must contain ‘translate’, ‘rotate’, ‘pivot_translate’ and ‘pivot_rotate’ knobs, the transform order must be ‘SRT’ and the rotation order must be ‘ZXY’.
Parameters

**nodeToSnap** () – Node to translate its Pivot Point