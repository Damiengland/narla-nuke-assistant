# nukescripts.connect_selected_to_viewer
nukescripts.connect_selected_to_viewer(_inputIndex_)

Connect the selected node to the given input index of the active viewer.
This method has various outcomes determined by order of fallback:
1\. Attempt to connect the active viewer within the current DAG window (excludes viewers in a group with a closed group view). If no node is selected, only select the active viewer.
2\. If no active viewer is found, connect any viewer in the selected node’s parent group. If there are none, create a viewer within the group and connect it.
3\. If no node is selected, select any viewer in nuke.lastHitGroup. If there are none, create a viewer within lastHitGroup and select it.
Parameters

**inputIndex** (_int_) – the input index of the viewer.