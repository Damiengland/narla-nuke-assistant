# nukescripts.translateRotateScaleToPoints
nukescripts.translateRotateScaleToPoints(_nodeToSnap_)

Translate the specified node to the average position of the current vertex selection in the active viewer, rotate to the orientation of the (mean squares) best fit plane for the selection and scale to the extents of the selection. The nodeToSnap must contain ‘translate’, ‘rotate’ and ‘scale’ knobs, the transform order must be ‘SRT’ and the rotation order must be ‘ZXY’.
Parameters

**nodeToSnap** () – Node to translate, rotate and scale