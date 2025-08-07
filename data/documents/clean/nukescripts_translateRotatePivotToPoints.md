# nukescripts.translateRotatePivotToPoints
nukescripts.translateRotatePivotToPoints(_nodeToSnap_)

Translate the specified node’s Pivot Point to the average position of the current vertex selection and rotate the pivot to align Z to match the average normals in the active viewer. The nodeToSnap must contain ‘translate’, ‘rotate’, ‘pivot_translate’, ‘pivot_rotate’ and ‘pivot_translate’ knobs, the transform order must be ‘SRT’ and the rotation order must be ‘ZXY’.
Parameters

**nodeToSnap** () – Node to translate its Pivot Point