# nukescripts.snap3d.selectedPoints
nukescripts.snap3d.selectedPoints(_selectionThreshold_)  iterator

Return an iterator which yields the position of every point currently selected in the Viewer in turn.
The selectionThreshold parameter is used when working with a soft selection. Only points with a selection level >= the selection threshold will be returned by this function.