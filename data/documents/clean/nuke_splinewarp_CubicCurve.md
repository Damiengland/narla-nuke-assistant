# nuke.splinewarp.CubicCurve
_class _nuke.splinewarp.CubicCurve

Bases: `object`
A baked out curve for a specific frame and view.
Use the getPoint function to get positions along the curve.
Note that some curves, such as the feather curve for a roto shape, are stored as offsets relative to another curve rather than absolute positions.
Methods
`getPoint`
param t
    The parameter value to evaluate the curve with. 0.0 is the start of the curve and 1.0 is the end. A value outside this range will throw a ValueError.---

getPoint(_t_)

Parameters

**t** – The parameter value to evaluate the curve with. 0.0 is the start of the curve and 1.0 is the end. A value outside this range will throw a ValueError.
Returns

A CVec4 containing the evalution result. If the curve has less than 4 dimension, the extra dimensions will be filled with default values.