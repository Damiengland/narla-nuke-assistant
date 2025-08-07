# nukescripts.selected_vertex_infos
nukescripts.selected_vertex_infos(_stage_ , _current_frame_ , _selection_threshold =0.5_)

selectedVertexInfos(selectionThreshold) -> iterator
Return an iterator which yields a tuple of the index and position of each point currently selected in the Viewer in turn.
The selectionThreshold parameter is used when working with a soft selection. Only points with a selection level >= the selection threshold will be returned by this function.