# nukescripts.pivot_to_bbox
nukescripts.pivot_to_bbox(_node_to_snap_ , _frames_ , _rotate_enabled_ , _command_ , _animate_single_frame =False_, _stage =None_, _task =None_)

Translate and optionally rotate the specified node’s Pivot Point to a chosen point on the currently selected prim’s bounding box.
Parameters

  * **node_to_snap** () – Node to translate and optionally rotate
  * **frames** (_int_ _or_ _int array_) – The frame or array of frames to affect
  * **rotate_enabled** (_boolean_) – Whether to apply the rotation to the node
  * **command** (_str_) – The side of the bounding box to snap to. This must be one of: Center/Top/Bottom/Left/Right/Front/Back
  * **animate_single_frame** (_boolean_) – If true, will set key for animation if affecting 1 frame. Always will set keys for animation if affecting multiple frames
  * **stage** (_pxr.Usd.Stage_) – The stage to get the selected prim from. If None, this method will attempt to get the stage from the active viewer.
  * **task** () – An optional progress task that will update as frames are processed.
Returns

True if this method was successful, False otherwise.