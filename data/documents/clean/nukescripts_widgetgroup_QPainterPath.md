# nukescripts.widgetgroup.QPainterPath
_class _nukescripts.widgetgroup.QPainterPath(_self_)  None
_class _nukescripts.widgetgroup.QPainterPath(_self_ , _other : PySide6.QtGui.QPainterPath_)  None
_class _nukescripts.widgetgroup.QPainterPath(_self_ , _startPoint : Union[PySide6.QtCore.QPointF, PySide6.QtCore.QPoint, PySide6.QtGui.QPainterPath.Element]_)  None

Bases: `Shiboken.Object`
__init__(self) -> None __init__(self, other: PySide6.QtGui.QPainterPath) -> None __init__(self, startPoint: Union[PySide6.QtCore.QPointF, PySide6.QtCore.QPoint, PySide6.QtGui.QPainterPath.Element]) -> None
Initialize self. See help(type(self)) for accurate signature.
Methods
`addEllipse` ---
`addPath`
`addPolygon`
`addRect`
`addRegion`
`addRoundedRect`
`addText`
`angleAtPercent`
`arcMoveTo`
`arcTo`
`boundingRect`
`capacity`
`clear`
`closeSubpath`
`connectPath`
`contains`
`controlPointRect`
`cubicTo`
`currentPosition`
`elementAt`
`elementCount`
`fillRule`
`intersected`
`intersects`
`isEmpty`
`length`
`lineTo`
`moveTo`
`percentAtLength`
`pointAtPercent`
`quadTo`
`reserve`
`setElementPositionAt`
`setFillRule`
`simplified`
`slopeAtPercent`
`subtracted`
`swap`
`toFillPolygon`
`toFillPolygons`
`toReversed`
`toSubpathPolygons`
`translate`
`translated`
`united`

_class _Element(_self_)  None
_class _Element(_self_ , _Element : PySide6.QtGui.QPainterPath.Element_)  None

Bases: `Shiboken.Object`
__init__(self) -> None __init__(self, Element: PySide6.QtGui.QPainterPath.Element) -> None
Initialize self. See help(type(self)) for accurate signature.
isCurveTo(_self_)  bool

isLineTo(_self_)  bool

isMoveTo(_self_)  bool

_class _ElementType(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Enum`
__add__(_self_ , _other : PySide6.QtGui.QPainterPath_)  PySide6.QtGui.QPainterPath

Return self+value.
__mul__(_self_ , _m : PySide6.QtGui.QTransform_)  PySide6.QtGui.QPainterPath

Return self*value.
addEllipse(_self_ , _center : Union[PySide6.QtCore.QPointF, PySide6.QtCore.QPoint, PySide6.QtGui.QPainterPath.Element]_, _rx : float_, _ry : float_)  None
addEllipse(_self_ , _rect : Union[PySide6.QtCore.QRectF, PySide6.QtCore.QRect]_)  None
addEllipse(_self_ , _x : float_, _y : float_, _w : float_, _h : float_)  None

addPath(_self_ , _path : PySide6.QtGui.QPainterPath_)  None

addPolygon(_self_ , _polygon : Union[PySide6.QtGui.QPolygonF, Sequence[PySide6.QtCore.QPointF], PySide6.QtGui.QPolygon, PySide6.QtCore.QRectF]_)  None

addRect(_self_ , _rect : Union[PySide6.QtCore.QRectF, PySide6.QtCore.QRect]_)  None
addRect(_self_ , _x : float_, _y : float_, _w : float_, _h : float_)  None

addRegion(_self_ , _region : Union[PySide6.QtGui.QRegion, PySide6.QtGui.QBitmap, PySide6.QtGui.QPolygon, PySide6.QtCore.QRect]_)  None

addRoundedRect(_self_ , _rect : Union[PySide6.QtCore.QRectF, PySide6.QtCore.QRect]_, _xRadius : float_, _yRadius : float_, _mode : = Instance(Qt.AbsoluteSize)_)  None
addRoundedRect(_self_ , _x : float_, _y : float_, _w : float_, _h : float_, _xRadius : float_, _yRadius : float_, _mode : = Instance(Qt.AbsoluteSize)_)  None

addText(_self_ , _point : Union[PySide6.QtCore.QPointF, PySide6.QtCore.QPoint, PySide6.QtGui.QPainterPath.Element]_, _f : Union[PySide6.QtGui.QFont, str, Sequence[str]]_, _text : str_)  None
addText(_self_ , _x : float_, _y : float_, _f : Union[PySide6.QtGui.QFont, str, Sequence[str]]_, _text : str_)  None

angleAtPercent(_self_ , _t : float_)  float

arcMoveTo(_self_ , _rect : Union[PySide6.QtCore.QRectF, PySide6.QtCore.QRect]_, _angle : float_)  None
arcMoveTo(_self_ , _x : float_, _y : float_, _w : float_, _h : float_, _angle : float_)  None

arcTo(_self_ , _rect : Union[PySide6.QtCore.QRectF, PySide6.QtCore.QRect]_, _startAngle : float_, _arcLength : float_)  None
arcTo(_self_ , _x : float_, _y : float_, _w : float_, _h : float_, _startAngle : float_, _arcLength : float_)  None

boundingRect(_self_)  PySide6.QtCore.QRectF

capacity(_self_)  int

clear(_self_)  None

closeSubpath(_self_)  None

connectPath(_self_ , _path : PySide6.QtGui.QPainterPath_)  None

contains(_self_ , _p : PySide6.QtGui.QPainterPath_)  bool
contains(_self_ , _pt : Union[PySide6.QtCore.QPointF, PySide6.QtCore.QPoint, PySide6.QtGui.QPainterPath.Element]_)  bool
contains(_self_ , _rect : Union[PySide6.QtCore.QRectF, PySide6.QtCore.QRect]_)  bool

controlPointRect(_self_)  PySide6.QtCore.QRectF

cubicTo(_self_ , _ctrlPt1 : Union[PySide6.QtCore.QPointF, PySide6.QtCore.QPoint, PySide6.QtGui.QPainterPath.Element]_, _ctrlPt2 : Union[PySide6.QtCore.QPointF, PySide6.QtCore.QPoint, PySide6.QtGui.QPainterPath.Element]_, _endPt : Union[PySide6.QtCore.QPointF, PySide6.QtCore.QPoint, PySide6.QtGui.QPainterPath.Element]_)  None
cubicTo(_self_ , _ctrlPt1x : float_, _ctrlPt1y : float_, _ctrlPt2x : float_, _ctrlPt2y : float_, _endPtx : float_, _endPty : float_)  None

currentPosition(_self_)  PySide6.QtCore.QPointF

elementAt(_self_ , _i : int_)  PySide6.QtGui.QPainterPath.Element

elementCount(_self_)  int

fillRule(_self_)

intersected(_self_ , _r : PySide6.QtGui.QPainterPath_)  PySide6.QtGui.QPainterPath

intersects(_self_ , _p : PySide6.QtGui.QPainterPath_)  bool
intersects(_self_ , _rect : Union[PySide6.QtCore.QRectF, PySide6.QtCore.QRect]_)  bool

isEmpty(_self_)  bool

length(_self_)  float

lineTo(_self_ , _p : Union[PySide6.QtCore.QPointF, PySide6.QtCore.QPoint, PySide6.QtGui.QPainterPath.Element]_)  None
lineTo(_self_ , _x : float_, _y : float_)  None

moveTo(_self_ , _p : Union[PySide6.QtCore.QPointF, PySide6.QtCore.QPoint, PySide6.QtGui.QPainterPath.Element]_)  None
moveTo(_self_ , _x : float_, _y : float_)  None

percentAtLength(_self_ , _t : float_)  float

pointAtPercent(_self_ , _t : float_)  PySide6.QtCore.QPointF

quadTo(_self_ , _ctrlPt : Union[PySide6.QtCore.QPointF, PySide6.QtCore.QPoint, PySide6.QtGui.QPainterPath.Element]_, _endPt : Union[PySide6.QtCore.QPointF, PySide6.QtCore.QPoint, PySide6.QtGui.QPainterPath.Element]_)  None
quadTo(_self_ , _ctrlPtx : float_, _ctrlPty : float_, _endPtx : float_, _endPty : float_)  None

reserve(_self_ , _size : int_)  None

setElementPositionAt(_self_ , _i : int_, _x : float_, _y : float_)  None

setFillRule(_self_ , _fillRule :_)  None

simplified(_self_)  PySide6.QtGui.QPainterPath

slopeAtPercent(_self_ , _t : float_)  float

subtracted(_self_ , _r : PySide6.QtGui.QPainterPath_)  PySide6.QtGui.QPainterPath

swap(_self_ , _other : PySide6.QtGui.QPainterPath_)  None

toFillPolygon(_self_ , _matrix : PySide6.QtGui.QTransform = Default(QTransform)_)  PySide6.QtGui.QPolygonF

toFillPolygons(_self_ , _matrix : PySide6.QtGui.QTransform = Default(QTransform)_)  List[PySide6.QtGui.QPolygonF]

toReversed(_self_)  PySide6.QtGui.QPainterPath

toSubpathPolygons(_self_ , _matrix : PySide6.QtGui.QTransform = Default(QTransform)_)  List[PySide6.QtGui.QPolygonF]

translate(_self_ , _dx : float_, _dy : float_)  None
translate(_self_ , _offset : Union[PySide6.QtCore.QPointF, PySide6.QtCore.QPoint, PySide6.QtGui.QPainterPath.Element]_)  None

translated(_self_ , _dx : float_, _dy : float_)  PySide6.QtGui.QPainterPath
translated(_self_ , _offset : Union[PySide6.QtCore.QPointF, PySide6.QtCore.QPoint, PySide6.QtGui.QPainterPath.Element]_)  PySide6.QtGui.QPainterPath

united(_self_ , _r : PySide6.QtGui.QPainterPath_)  PySide6.QtGui.QPainterPath