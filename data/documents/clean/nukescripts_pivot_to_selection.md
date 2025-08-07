# nukescripts.pivot_to_selection
nukescripts.pivot_to_selection(_node_to_snap_ , _frames_ , _translate_enabled_ , _rotate_enabled_ , _animate_single_frame =False_, _stage =None_, _task =None_)

Translate and/or rotate the specified node’s Pivot Point to the average position/rotation of the current vertex selection on the stage.
Parameters

  * **node_to_snap** () – Node to translate/rotate
  * **frames** (_int_ _or_ _int array_) – The frame or array of frames to affect
  * **translate_enabled** (_boolean_) – Whether to apply the translation to the node
  * **rotate_enabled** (_boolean_) – Whether to apply the rotation to the node
  * **animate_single_frame** (_boolean_) – If true, will set key for animation if affecting 1 frame. Always will set keys for animation if affecting multiple frames
  * **stage** (_pxr.Usd.Stage_) – The stage to get the selected vertex info from. If None, this method will attempt to get the stage from the active viewer.
  * **task** () – An optional progress task that will update as frames are processed.
Returns

True if this method was successful, False otherwise.