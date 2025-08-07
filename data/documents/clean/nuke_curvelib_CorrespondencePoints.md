# nuke.curvelib.CorrespondencePoints
_class _nuke.curvelib.CorrespondencePoints

Bases: `object`
Correspondence points add a relation to the interpolation of two curves. These points are made up of two values; a t-value on the source curve and a corresponding t-value on the destination curve T-values should be in the range [0-1], where 0 is the start of the curve, and 1 is the end of the curve
Methods
`addPoint`  Adds a correspondence point :param time: Time at which to t_src and t_dest will be set :param t_src: Position on the source curve (where 0=start and 1=end) :param t_dest: Position on the destination curve Note that the correspondence point is not animated.---
`getAnimCurve`
param index
    Index to the point to get the associated AnimCurve
`getNumPoints`
return
    Returns the number of correspondence points in the object
`getPointValues`
param time
    Time at which to evaluate point's values
`modifyPoint`
param time
    Time at which to t_in and t_out will be set
`removePoint`
param index
    Index to the point to remove
`reset`  cps->reset() Resets the correspondence points object to empty

addPoint(_time_ , _t_src_ , _t_dest_)

Adds a correspondence point :param time: Time at which to t_src and t_dest will be set :param t_src: Position on the source curve (where 0=start and 1=end) :param t_dest: Position on the destination curve Note that the correspondence point is not animated. Animation must be set manually to avoid conflicting with existing points.
getAnimCurve(_index_ , _which_)

Parameters

**index** – Index to the point to get the associated AnimCurve
object for :param which: Whether the source (0) or destination (1) t-value is being modified :return: An AnimCurve object for the timeline of the specified point and src/dest value
getNumPoints()

Returns

Returns the number of correspondence points in the object
getPointValues(_time_ , _index_)

Parameters

  * **time** – Time at which to evaluate point’s values
  * **index** – Index to the point to evaluate
Returns

A tuple containing source and destionation t-values
modifyPoint(_time_ , _index_ , _which_ , _t_)

Parameters

  * **time** – Time at which to t_in and t_out will be set
  * **index** – Index to the point to modify
  * **which** – Whether the source (0) or destination (1) t-value is
being modified :param t: Position on the curve specified in by ‘which’
removePoint(_index_)

Parameters

**index** – Index to the point to remove
reset()

cps->reset() Resets the correspondence points object to empty