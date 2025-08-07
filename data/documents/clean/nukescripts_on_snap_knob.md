# nukescripts.on_snap_knob
nukescripts.on_snap_knob(_origin_knob_ , _command_)

Called by the snap knobs to perform a pivot_to_selection/pivot_to_bbox/geo_to_selection operation.
Parameters

  * **origin_knob** () – Knob that was used to start this operation. This is used to determine the operation to perform as well as finding the parameters for the operation from other related snap knobs on the node.
  * **command** (_str_) – An additional command string currently used by the pivot_to_bbox operation specifying the side of the bounding box to snap to. This must be one of: Center/Top/Bottom/Left/Right/Front/Back if pivot_to_bbox operation, otherwise this parameter is ignored.