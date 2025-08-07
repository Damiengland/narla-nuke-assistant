# nukescripts.snap3d.anySelectedPoint
nukescripts.snap3d.anySelectedPoint(_selectionThreshold_)  _nukemath.Vector3

Return a selected point from the active viewer or the first viewer with a selection. The selectionThreshold parameter is used when working with a soft selection. Only points with a selection level >= the selection threshold will be returned by this function.