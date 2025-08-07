# nukescripts.widgetgroup.QPainter
_class _nukescripts.widgetgroup.QPainter(_self_)  None
_class _nukescripts.widgetgroup.QPainter(_self_ , _arg__1 : PySide6.QtGui.QPaintDevice_)  None

Bases: `Shiboken.Object`
__init__(self) -> None __init__(self, arg__1: PySide6.QtGui.QPaintDevice) -> None
Initialize self. See help(type(self)) for accurate signature.
Methods
`background` ---
`backgroundMode`
`begin`
`beginNativePainting`
`boundingRect`
`brush`
`brushOrigin`
`clipBoundingRect`
`clipPath`
`clipRegion`
`combinedTransform`
`compositionMode`
`device`
`deviceTransform`
`drawArc`
`drawChord`
`drawConvexPolygon`
`drawEllipse`
`drawGlyphRun`
`drawImage`
`drawLine`
`drawLines`
`drawPath`
`drawPicture`
`drawPie`
`drawPixmap`
`drawPixmapFragments`
`drawPoint`
`drawPoints`
`drawPointsNp`
`drawPolygon`
`drawPolyline`
`drawRect`
`drawRects`
`drawRoundedRect`
`drawStaticText`
`drawText`
`drawTextItem`
`drawTiledPixmap`
`end`
`endNativePainting`
`eraseRect`
`fillPath`
`fillRect`
`font`
`fontInfo`
`fontMetrics`
`hasClipping`
`isActive`
`layoutDirection`
`opacity`
`paintEngine`
`pen`
`renderHints`
`resetTransform`
`restore`
`rotate`
`save`
`scale`
`setBackground`
`setBackgroundMode`
`setBrush`
`setBrushOrigin`
`setClipPath`
`setClipRect`
`setClipRegion`
`setClipping`
`setCompositionMode`
`setFont`
`setLayoutDirection`
`setOpacity`
`setPen`
`setRenderHint`
`setRenderHints`
`setTransform`
`setViewTransformEnabled`
`setViewport`
`setWindow`
`setWorldMatrixEnabled`
`setWorldTransform`
`shear`
`strokePath`
`testRenderHint`
`transform`
`translate`
`viewTransformEnabled`
`viewport`
`window`
`worldMatrixEnabled`
`worldTransform`

_class _CompositionMode(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Enum`
_class _PixmapFragment(_self_)  None
_class _PixmapFragment(_self_ , _PixmapFragment : PySide6.QtGui.QPainter.PixmapFragment_)  None

Bases: `Shiboken.Object`
__init__(self) -> None __init__(self, PixmapFragment: PySide6.QtGui.QPainter.PixmapFragment) -> None
Initialize self. See help(type(self)) for accurate signature.
_static _create(_pos : Union]_, _sourceRect : Union[PySide6.QtCore.QRectF, PySide6.QtCore.QRect]_, _scaleX : float = 1_, _scaleY : float = 1_, _rotation : float = 0_, _opacity : float = 1_)  PySide6.QtGui.QPainter.PixmapFragment

_class _PixmapFragmentHint(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Flag`
_class _RenderHint(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Flag`
background(_self_)  PySide6.QtGui.QBrush

backgroundMode(_self_)

begin(_self_ , _arg__1 : PySide6.QtGui.QPaintDevice_)  bool

beginNativePainting(_self_)  None

boundingRect(_self_ , _rect : PySide6.QtCore.QRect_, _flags : int_, _text : str_)  PySide6.QtCore.QRect
boundingRect(_self_ , _rect : Union[PySide6.QtCore.QRectF, PySide6.QtCore.QRect]_, _flags : int_, _text : str_)  PySide6.QtCore.QRectF
boundingRect(_self_ , _rect : Union[PySide6.QtCore.QRectF, PySide6.QtCore.QRect]_, _text : str_, _o : Union] = Default(QTextOption)_)  PySide6.QtCore.QRectF
boundingRect(_self_ , _x : int_, _y : int_, _w : int_, _h : int_, _flags : int_, _text : str_)  PySide6.QtCore.QRect

brush(_self_)  PySide6.QtGui.QBrush

brushOrigin(_self_)  PySide6.QtCore.QPoint

clipBoundingRect(_self_)  PySide6.QtCore.QRectF

clipPath(_self_)

clipRegion(_self_)  PySide6.QtGui.QRegion

combinedTransform(_self_)  PySide6.QtGui.QTransform

compositionMode(_self_)  PySide6.QtGui.QPainter.CompositionMode

device(_self_)  PySide6.QtGui.QPaintDevice

deviceTransform(_self_)  PySide6.QtGui.QTransform

drawArc(_self_ , _arg__1 : PySide6.QtCore.QRect_, _a : int_, _alen : int_)  None
drawArc(_self_ , _rect : Union[PySide6.QtCore.QRectF, PySide6.QtCore.QRect]_, _a : int_, _alen : int_)  None
drawArc(_self_ , _x : int_, _y : int_, _w : int_, _h : int_, _a : int_, _alen : int_)  None

drawChord(_self_ , _arg__1 : PySide6.QtCore.QRect_, _a : int_, _alen : int_)  None
drawChord(_self_ , _rect : Union[PySide6.QtCore.QRectF, PySide6.QtCore.QRect]_, _a : int_, _alen : int_)  None
drawChord(_self_ , _x : int_, _y : int_, _w : int_, _h : int_, _a : int_, _alen : int_)  None

drawConvexPolygon(_self_ , _arg__1 : Sequence[PySide6.QtCore.QPointF]_)  None
drawConvexPolygon(_self_ , _arg__1 : Sequence[PySide6.QtCore.QPoint]_)  None
drawConvexPolygon(_self_ , _polygon : Union[PySide6.QtGui.QPolygon, Sequence[PySide6.QtCore.QPoint], PySide6.QtCore.QRect]_)  None
drawConvexPolygon(_self_ , _polygon : Union[PySide6.QtGui.QPolygonF, Sequence[PySide6.QtCore.QPointF], PySide6.QtGui.QPolygon, PySide6.QtCore.QRectF]_)  None

drawEllipse(_self_ , _center : PySide6.QtCore.QPoint_, _rx : int_, _ry : int_)  None
drawEllipse(_self_ , _center : Union]_, _rx : float_, _ry : float_)  None
drawEllipse(_self_ , _r : PySide6.QtCore.QRect_)  None
drawEllipse(_self_ , _r : Union[PySide6.QtCore.QRectF, PySide6.QtCore.QRect]_)  None
drawEllipse(_self_ , _x : int_, _y : int_, _w : int_, _h : int_)  None

drawGlyphRun(_self_ , _position : Union]_, _glyphRun : PySide6.QtGui.QGlyphRun_)  None

drawImage(_self_ , _p : PySide6.QtCore.QPoint_, _image : Union[PySide6.QtGui.QImage, str]_)  None
drawImage(_self_ , _p : PySide6.QtCore.QPoint_, _image : Union[PySide6.QtGui.QImage, str]_, _sr : PySide6.QtCore.QRect_, _flags : = Instance(Qt.AutoColor)_)  None
drawImage(_self_ , _p : Union]_, _image : Union[PySide6.QtGui.QImage, str]_)  None
drawImage(_self_ , _p : Union]_, _image : Union[PySide6.QtGui.QImage, str]_, _sr : Union[PySide6.QtCore.QRectF, PySide6.QtCore.QRect]_, _flags : = Instance(Qt.AutoColor)_)  None
drawImage(_self_ , _r : PySide6.QtCore.QRect_, _image : Union[PySide6.QtGui.QImage, str]_)  None
drawImage(_self_ , _r : Union[PySide6.QtCore.QRectF, PySide6.QtCore.QRect]_, _image : Union[PySide6.QtGui.QImage, str]_)  None
drawImage(_self_ , _targetRect : PySide6.QtCore.QRect_, _image : Union[PySide6.QtGui.QImage, str]_, _sourceRect : PySide6.QtCore.QRect_, _flags : = Instance(Qt.AutoColor)_)  None
drawImage(_self_ , _targetRect : Union[PySide6.QtCore.QRectF, PySide6.QtCore.QRect]_, _image : Union[PySide6.QtGui.QImage, str]_, _sourceRect : Union[PySide6.QtCore.QRectF, PySide6.QtCore.QRect]_, _flags : = Instance(Qt.AutoColor)_)  None
drawImage(_self_ , _x : int_, _y : int_, _image : Union[PySide6.QtGui.QImage, str]_, _sx : int = 0_, _sy : int = 0_, _sw : int = - 1_, _sh : int = - 1_, _flags : = Instance(Qt.AutoColor)_)  None

drawLine(_self_ , _line : PySide6.QtCore.QLine_)  None
drawLine(_self_ , _line : Union[PySide6.QtCore.QLineF, PySide6.QtCore.QLine]_)  None
drawLine(_self_ , _p1 : PySide6.QtCore.QPoint_, _p2 : PySide6.QtCore.QPoint_)  None
drawLine(_self_ , _p1 : Union]_, _p2 : Union]_)  None
drawLine(_self_ , _x1 : int_, _y1 : int_, _x2 : int_, _y2 : int_)  None

drawLines(_self_ , _lines : Sequence[PySide6.QtCore.QLineF]_)  None
drawLines(_self_ , _lines : Sequence[PySide6.QtCore.QLine]_)  None
drawLines(_self_ , _lines : Union[PySide6.QtCore.QLineF, PySide6.QtCore.QLine]_, _lineCount : int_)  None
drawLines(_self_ , _pointPairs : Sequence[PySide6.QtCore.QPointF]_)  None
drawLines(_self_ , _pointPairs : Sequence[PySide6.QtCore.QPoint]_)  None

drawPath(_self_ , _path :_)  None

drawPicture(_self_ , _p : PySide6.QtCore.QPoint_, _picture : Union[PySide6.QtGui.QPicture, int]_)  None
drawPicture(_self_ , _p : Union]_, _picture : Union[PySide6.QtGui.QPicture, int]_)  None
drawPicture(_self_ , _x : int_, _y : int_, _picture : Union[PySide6.QtGui.QPicture, int]_)  None

drawPie(_self_ , _arg__1 : PySide6.QtCore.QRect_, _a : int_, _alen : int_)  None
drawPie(_self_ , _rect : Union[PySide6.QtCore.QRectF, PySide6.QtCore.QRect]_, _a : int_, _alen : int_)  None
drawPie(_self_ , _x : int_, _y : int_, _w : int_, _h : int_, _a : int_, _alen : int_)  None

drawPixmap(_self_ , _p : PySide6.QtCore.QPoint_, _pm : Union[PySide6.QtGui.QPixmap, PySide6.QtGui.QImage, str]_)  None
drawPixmap(_self_ , _p : PySide6.QtCore.QPoint_, _pm : Union[PySide6.QtGui.QPixmap, PySide6.QtGui.QImage, str]_, _sr : PySide6.QtCore.QRect_)  None
drawPixmap(_self_ , _p : Union]_, _pm : Union[PySide6.QtGui.QPixmap, PySide6.QtGui.QImage, str]_)  None
drawPixmap(_self_ , _p : Union]_, _pm : Union[PySide6.QtGui.QPixmap, PySide6.QtGui.QImage, str]_, _sr : Union[PySide6.QtCore.QRectF, PySide6.QtCore.QRect]_)  None
drawPixmap(_self_ , _r : PySide6.QtCore.QRect_, _pm : Union[PySide6.QtGui.QPixmap, PySide6.QtGui.QImage, str]_)  None
drawPixmap(_self_ , _targetRect : PySide6.QtCore.QRect_, _pixmap : Union[PySide6.QtGui.QPixmap, PySide6.QtGui.QImage, str]_, _sourceRect : PySide6.QtCore.QRect_)  None
drawPixmap(_self_ , _targetRect : Union[PySide6.QtCore.QRectF, PySide6.QtCore.QRect]_, _pixmap : Union[PySide6.QtGui.QPixmap, PySide6.QtGui.QImage, str]_, _sourceRect : Union[PySide6.QtCore.QRectF, PySide6.QtCore.QRect]_)  None
drawPixmap(_self_ , _x : int_, _y : int_, _pm : Union[PySide6.QtGui.QPixmap, PySide6.QtGui.QImage, str]_)  None
drawPixmap(_self_ , _x : int_, _y : int_, _pm : Union[PySide6.QtGui.QPixmap, PySide6.QtGui.QImage, str]_, _sx : int_, _sy : int_, _sw : int_, _sh : int_)  None
drawPixmap(_self_ , _x : int_, _y : int_, _w : int_, _h : int_, _pm : Union[PySide6.QtGui.QPixmap, PySide6.QtGui.QImage, str]_)  None
drawPixmap(_self_ , _x : int_, _y : int_, _w : int_, _h : int_, _pm : Union[PySide6.QtGui.QPixmap, PySide6.QtGui.QImage, str]_, _sx : int_, _sy : int_, _sw : int_, _sh : int_)  None

drawPixmapFragments(_self_ , _fragments : PySide6.QtGui.QPainter.PixmapFragment_, _fragmentCount : int_, _pixmap : Union[PySide6.QtGui.QPixmap, PySide6.QtGui.QImage, str]_, _hints : PySide6.QtGui.QPainter.PixmapFragmentHint = Default(QPainter.PixmapFragmentHints)_)  None

drawPoint(_self_ , _p : PySide6.QtCore.QPoint_)  None
drawPoint(_self_ , _pt : Union]_)  None
drawPoint(_self_ , _x : int_, _y : int_)  None

drawPoints(_self_ , _arg__1 : Sequence[PySide6.QtCore.QPointF]_)  None
drawPoints(_self_ , _arg__1 : Sequence[PySide6.QtCore.QPoint]_)  None
drawPoints(_self_ , _points : Union]_, _pointCount : int_)  None
drawPoints(_self_ , _points : Union[PySide6.QtGui.QPolygon, Sequence[PySide6.QtCore.QPoint], PySide6.QtCore.QRect]_)  None
drawPoints(_self_ , _points : Union[PySide6.QtGui.QPolygonF, Sequence[PySide6.QtCore.QPointF], PySide6.QtGui.QPolygon, PySide6.QtCore.QRectF]_)  None

drawPointsNp(_self_ , _x : shibokensupport.signature.mapping.ArrayLikeVariable_, _y : shibokensupport.signature.mapping.ArrayLikeVariable_)  None

drawPolygon(_self_ , _arg__1 : Sequence[PySide6.QtCore.QPointF]_, _arg__2 :_)  None
drawPolygon(_self_ , _arg__1 : Sequence[PySide6.QtCore.QPoint]_, _arg__2 :_)  None
drawPolygon(_self_ , _polygon : Union[PySide6.QtGui.QPolygon, Sequence[PySide6.QtCore.QPoint], PySide6.QtCore.QRect]_, _fillRule : = Instance(Qt.OddEvenFill)_)  None
drawPolygon(_self_ , _polygon : Union[PySide6.QtGui.QPolygonF, Sequence[PySide6.QtCore.QPointF], PySide6.QtGui.QPolygon, PySide6.QtCore.QRectF]_, _fillRule : = Instance(Qt.OddEvenFill)_)  None

drawPolyline(_self_ , _arg__1 : Sequence[PySide6.QtCore.QPointF]_)  None
drawPolyline(_self_ , _arg__1 : Sequence[PySide6.QtCore.QPoint]_)  None
drawPolyline(_self_ , _polygon : Union[PySide6.QtGui.QPolygon, Sequence[PySide6.QtCore.QPoint], PySide6.QtCore.QRect]_)  None
drawPolyline(_self_ , _polyline : Union[PySide6.QtGui.QPolygonF, Sequence[PySide6.QtCore.QPointF], PySide6.QtGui.QPolygon, PySide6.QtCore.QRectF]_)  None

drawRect(_self_ , _rect : PySide6.QtCore.QRect_)  None
drawRect(_self_ , _rect : Union[PySide6.QtCore.QRectF, PySide6.QtCore.QRect]_)  None
drawRect(_self_ , _x1 : int_, _y1 : int_, _w : int_, _h : int_)  None

drawRects(_self_ , _rectangles : Sequence[PySide6.QtCore.QRectF]_)  None
drawRects(_self_ , _rectangles : Sequence[PySide6.QtCore.QRect]_)  None
drawRects(_self_ , _rects : Union[PySide6.QtCore.QRectF, PySide6.QtCore.QRect]_, _rectCount : int_)  None

drawRoundedRect(_self_ , _rect : PySide6.QtCore.QRect_, _xRadius : float_, _yRadius : float_, _mode : = Instance(Qt.AbsoluteSize)_)  None
drawRoundedRect(_self_ , _rect : Union[PySide6.QtCore.QRectF, PySide6.QtCore.QRect]_, _xRadius : float_, _yRadius : float_, _mode : = Instance(Qt.AbsoluteSize)_)  None
drawRoundedRect(_self_ , _x : int_, _y : int_, _w : int_, _h : int_, _xRadius : float_, _yRadius : float_, _mode : = Instance(Qt.AbsoluteSize)_)  None

drawStaticText(_self_ , _left : int_, _top : int_, _staticText : PySide6.QtGui.QStaticText_)  None
drawStaticText(_self_ , _topLeftPosition : PySide6.QtCore.QPoint_, _staticText : PySide6.QtGui.QStaticText_)  None
drawStaticText(_self_ , _topLeftPosition : Union]_, _staticText : PySide6.QtGui.QStaticText_)  None

drawText(_self_ , _p : PySide6.QtCore.QPoint_, _s : str_)  None
drawText(_self_ , _p : Union]_, _s : str_)  None
drawText(_self_ , _r : PySide6.QtCore.QRect_, _flags : int_, _text : str_)  PySide6.QtCore.QRect
drawText(_self_ , _r : Union[PySide6.QtCore.QRectF, PySide6.QtCore.QRect]_, _flags : int_, _text : str_)  PySide6.QtCore.QRectF
drawText(_self_ , _r : Union[PySide6.QtCore.QRectF, PySide6.QtCore.QRect]_, _text : str_, _o : Union] = Default(QTextOption)_)  None
drawText(_self_ , _x : int_, _y : int_, _s : str_)  None
drawText(_self_ , _x : int_, _y : int_, _w : int_, _h : int_, _flags : int_, _text : str_)  None

drawTextItem(_self_ , _p : PySide6.QtCore.QPoint_, _ti : PySide6.QtGui.QTextItem_)  None
drawTextItem(_self_ , _p : Union]_, _ti : PySide6.QtGui.QTextItem_)  None
drawTextItem(_self_ , _x : int_, _y : int_, _ti : PySide6.QtGui.QTextItem_)  None

drawTiledPixmap(_self_ , _arg__1 : PySide6.QtCore.QRect_, _arg__2 : Union[PySide6.QtGui.QPixmap, PySide6.QtGui.QImage, str]_, _pos : PySide6.QtCore.QPoint = Default(QPoint)_)  None
drawTiledPixmap(_self_ , _rect : Union[PySide6.QtCore.QRectF, PySide6.QtCore.QRect]_, _pm : Union[PySide6.QtGui.QPixmap, PySide6.QtGui.QImage, str]_, _offset : Union] = Default(QPointF)_)  None
drawTiledPixmap(_self_ , _x : int_, _y : int_, _w : int_, _h : int_, _arg__5 : Union[PySide6.QtGui.QPixmap, PySide6.QtGui.QImage, str]_, _sx : int = 0_, _sy : int = 0_)  None

end(_self_)  bool

endNativePainting(_self_)  None

eraseRect(_self_ , _arg__1 : PySide6.QtCore.QRect_)  None
eraseRect(_self_ , _arg__1 : Union[PySide6.QtCore.QRectF, PySide6.QtCore.QRect]_)  None
eraseRect(_self_ , _x : int_, _y : int_, _w : int_, _h : int_)  None

fillPath(_self_ , _path :_, _brush : Union,, PySide6.QtGui.QColor, PySide6.QtGui.QGradient, PySide6.QtGui.QImage, PySide6.QtGui.QPixmap]_)  None

fillRect(_self_ , _arg__1 : PySide6.QtCore.QRect_, _arg__2 : Union,, PySide6.QtGui.QColor, PySide6.QtGui.QGradient, PySide6.QtGui.QImage, PySide6.QtGui.QPixmap]_)  None
fillRect(_self_ , _arg__1 : PySide6.QtCore.QRect_, _color : Union, str, int]_)  None
fillRect(_self_ , _arg__1 : Union[PySide6.QtCore.QRectF, PySide6.QtCore.QRect]_, _arg__2 : Union,, PySide6.QtGui.QColor, PySide6.QtGui.QGradient, PySide6.QtGui.QImage, PySide6.QtGui.QPixmap]_)  None
fillRect(_self_ , _arg__1 : Union[PySide6.QtCore.QRectF, PySide6.QtCore.QRect]_, _color : Union, str, int]_)  None
fillRect(_self_ , _r : PySide6.QtCore.QRect_, _c :_)  None
fillRect(_self_ , _r : PySide6.QtCore.QRect_, _preset : PySide6.QtGui.QGradient.Preset_)  None
fillRect(_self_ , _r : PySide6.QtCore.QRect_, _style :_)  None
fillRect(_self_ , _r : Union[PySide6.QtCore.QRectF, PySide6.QtCore.QRect]_, _c :_)  None
fillRect(_self_ , _r : Union[PySide6.QtCore.QRectF, PySide6.QtCore.QRect]_, _preset : PySide6.QtGui.QGradient.Preset_)  None
fillRect(_self_ , _r : Union[PySide6.QtCore.QRectF, PySide6.QtCore.QRect]_, _style :_)  None
fillRect(_self_ , _x : int_, _y : int_, _w : int_, _h : int_, _arg__5 : Union,, PySide6.QtGui.QColor, PySide6.QtGui.QGradient, PySide6.QtGui.QImage, PySide6.QtGui.QPixmap]_)  None
fillRect(_self_ , _x : int_, _y : int_, _w : int_, _h : int_, _c :_)  None
fillRect(_self_ , _x : int_, _y : int_, _w : int_, _h : int_, _color : Union, str, int]_)  None
fillRect(_self_ , _x : int_, _y : int_, _w : int_, _h : int_, _preset : PySide6.QtGui.QGradient.Preset_)  None
fillRect(_self_ , _x : int_, _y : int_, _w : int_, _h : int_, _style :_)  None

font(_self_)  PySide6.QtGui.QFont

fontInfo(_self_)  PySide6.QtGui.QFontInfo

fontMetrics(_self_)  PySide6.QtGui.QFontMetrics

hasClipping(_self_)  bool

isActive(_self_)  bool

layoutDirection(_self_)

opacity(_self_)  float

paintEngine(_self_)  PySide6.QtGui.QPaintEngine

pen(_self_)  PySide6.QtGui.QPen

renderHints(_self_)  PySide6.QtGui.QPainter.RenderHint

resetTransform(_self_)  None

restore(_self_)  None

rotate(_self_ , _a : float_)  None

save(_self_)  None

scale(_self_ , _sx : float_, _sy : float_)  None

setBackground(_self_ , _bg : Union,, PySide6.QtGui.QColor, PySide6.QtGui.QGradient, PySide6.QtGui.QImage, PySide6.QtGui.QPixmap]_)  None

setBackgroundMode(_self_ , _mode :_)  None

setBrush(_self_ , _brush : Union,, PySide6.QtGui.QColor, PySide6.QtGui.QGradient, PySide6.QtGui.QImage, PySide6.QtGui.QPixmap]_)  None
setBrush(_self_ , _style :_)  None

setBrushOrigin(_self_ , _arg__1 : PySide6.QtCore.QPoint_)  None
setBrushOrigin(_self_ , _arg__1 : Union]_)  None
setBrushOrigin(_self_ , _x : int_, _y : int_)  None

setClipPath(_self_ , _path :_, _op : = Instance(Qt.ReplaceClip)_)  None

setClipRect(_self_ , _arg__1 : PySide6.QtCore.QRect_, _op : = Instance(Qt.ReplaceClip)_)  None
setClipRect(_self_ , _arg__1 : Union[PySide6.QtCore.QRectF, PySide6.QtCore.QRect]_, _op : = Instance(Qt.ReplaceClip)_)  None
setClipRect(_self_ , _x : int_, _y : int_, _w : int_, _h : int_, _op : = Instance(Qt.ReplaceClip)_)  None

setClipRegion(_self_ , _arg__1 : Union[PySide6.QtGui.QRegion, PySide6.QtGui.QBitmap, PySide6.QtGui.QPolygon, PySide6.QtCore.QRect]_, _op : = Instance(Qt.ReplaceClip)_)  None

setClipping(_self_ , _enable : bool_)  None

setCompositionMode(_self_ , _mode : PySide6.QtGui.QPainter.CompositionMode_)  None

setFont(_self_ , _f : Union[PySide6.QtGui.QFont, str, Sequence[str]]_)  None

setLayoutDirection(_self_ , _direction :_)  None

setOpacity(_self_ , _opacity : float_)  None

setPen(_self_ , _color : Union, str, int]_)  None
setPen(_self_ , _pen : Union, PySide6.QtGui.QColor]_)  None
setPen(_self_ , _style :_)  None

setRenderHint(_self_ , _hint : PySide6.QtGui.QPainter.RenderHint_, _on : bool = True_)  None

setRenderHints(_self_ , _hints : PySide6.QtGui.QPainter.RenderHint_, _on : bool = True_)  None

setTransform(_self_ , _transform : PySide6.QtGui.QTransform_, _combine : bool = False_)  None

setViewTransformEnabled(_self_ , _enable : bool_)  None

setViewport(_self_ , _viewport : PySide6.QtCore.QRect_)  None
setViewport(_self_ , _x : int_, _y : int_, _w : int_, _h : int_)  None

setWindow(_self_ , _window : PySide6.QtCore.QRect_)  None
setWindow(_self_ , _x : int_, _y : int_, _w : int_, _h : int_)  None

setWorldMatrixEnabled(_self_ , _enabled : bool_)  None

setWorldTransform(_self_ , _matrix : PySide6.QtGui.QTransform_, _combine : bool = False_)  None

shear(_self_ , _sh : float_, _sv : float_)  None

strokePath(_self_ , _path :_, _pen : Union, PySide6.QtGui.QColor]_)  None

testRenderHint(_self_ , _hint : PySide6.QtGui.QPainter.RenderHint_)  bool

transform(_self_)  PySide6.QtGui.QTransform

translate(_self_ , _dx : float_, _dy : float_)  None
translate(_self_ , _offset : PySide6.QtCore.QPoint_)  None
translate(_self_ , _offset : Union]_)  None

viewTransformEnabled(_self_)  bool

viewport(_self_)  PySide6.QtCore.QRect

window(_self_)  PySide6.QtCore.QRect

worldMatrixEnabled(_self_)  bool

worldTransform(_self_)  PySide6.QtGui.QTransform