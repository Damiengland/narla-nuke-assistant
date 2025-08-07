# nukescripts.translate_rotate_pivot
nukescripts.translate_rotate_pivot(_node_to_snap_ , _translate_ , _rotate_ , _current_frame_)

Pivot translation and rotation must keep the object stationary and in order to do that compensation values must be placed in the geometry translate and rotate.
Parameters

  * **node_to_snap** () – Node to translate and rotate
  * **translate** (__nukemath.Vector3_) – Target position for the pivot point.
  * **rotate** (__nukemath.Vector3_) – Target rotation for the pivot point.
Return type

`tuple`
Returns

A tuple with the new geometry translation and rotation respectively (_nukemath.Vector3, _nukemath.Vector3).