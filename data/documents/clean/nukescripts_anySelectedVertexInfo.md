# nukescripts.anySelectedVertexInfo
nukescripts.anySelectedVertexInfo(_selectionThreshold_)

Returns a single VertexInfo for a selected point. If more than one point is selected, one of them will be chosen arbitrarily.
The selectionThreshold parameter is used when working with a soft selection. Only points with a selection level >= the selection threshold will be returned by this function.