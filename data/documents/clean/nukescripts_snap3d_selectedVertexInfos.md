# nukescripts.snap3d.selectedVertexInfos
nukescripts.snap3d.selectedVertexInfos(_selectionThreshold_)  iterator

Return an iterator which yields a tuple of the index and position of each point currently selected in the Viewer in turn.
The selectionThreshold parameter is used when working with a soft selection. Only points with a selection level >= the selection threshold will be returned by this function.