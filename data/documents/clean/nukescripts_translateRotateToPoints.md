# nukescripts.translateRotateToPoints
nukescripts.translateRotateToPoints(_nodeToSnap_)

Translate the specified node to the average position of the current vertex selection in the active viewer and rotate to the orientation of the (mean squares) best fit plane for the selection. The nodeToSnap must contain ‘translate’ and ‘rotate’ knobs, the transform order must be ‘SRT’ and the rotation order must be ‘ZXY’.
Parameters

**nodeToSnap** () – Node to translate and rotate