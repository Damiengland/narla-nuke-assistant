# nukescripts.scripteditorknob.QVBoxLayout
_class _nukescripts.scripteditorknob.QVBoxLayout(_self_)  None
_class _nukescripts.scripteditorknob.QVBoxLayout(_self_ , _parent :_)  None

Bases: `PySide6.QtWidgets.QBoxLayout`
__init__(self) -> None __init__(self, parent: PySide6.QtWidgets.QWidget) -> None
Initialize self. See help(type(self)) for accurate signature.
Methods
`activate` ---
`addChildLayout`
`addChildWidget`
`addItem`
`addLayout`
`addSpacerItem`
`addSpacing`
`addStretch`
`addStrut`
`addWidget`
`adoptLayout`
`alignment`
`alignmentRect`
`blockSignals`
`childEvent`
`children`
`closestAcceptableSize`
`connect`
`connectNotify`
`contentsMargins`
`contentsRect`
`controlTypes`
`count`
`customEvent`
`deleteLater`
`direction`
`disconnect`
`disconnectNotify`
`dumpObjectInfo`
`dumpObjectTree`
`dynamicPropertyNames`
`emit`
`event`
`eventFilter`
`expandingDirections`
`findChild`
`findChildren`
`geometry`
`getContentsMargins`
`hasHeightForWidth`
`heightForWidth`
`indexOf`
`inherits`
`insertItem`
`insertLayout`
`insertSpacerItem`
`insertSpacing`
`insertStretch`
`insertWidget`
`installEventFilter`
`invalidate`
`isEmpty`
`isEnabled`
`isQuickItemType`
`isSignalConnected`
`isWidgetType`
`isWindowType`
`itemAt`
`killTimer`
`layout`
`maximumSize`
`menuBar`
`metaObject`
`minimumHeightForWidth`
`minimumSize`
`moveToThread`
`objectName`
`parent`
`parentWidget`
`property`
`receivers`
`removeEventFilter`
`removeItem`
`removeWidget`
`replaceWidget`
`sender`
`senderSignalIndex`
`setAlignment`
`setContentsMargins`
`setDirection`
`setEnabled`
`setGeometry`
`setMenuBar`
`setObjectName`
`setParent`
`setProperty`
`setSizeConstraint`
`setSpacing`
`setStretch`
`setStretchFactor`
`signalsBlocked`
`sizeConstraint`
`sizeHint`
`spacerItem`
`spacing`
`startTimer`
`stretch`
`takeAt`
`thread`
`timerEvent`
`totalHeightForWidth`
`totalMaximumSize`
`totalMinimumHeightForWidth`
`totalMinimumSize`
`totalSizeHint`
`tr`
`unsetContentsMargins`
`update`
`widget`
`widgetEvent`

Attributes
`align` ---
`destroyed`
`objectNameChanged`
`staticMetaObject`

_class _Direction(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Enum`
_class _SizeConstraint(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Enum`
activate(_self_)  bool

addChildLayout(_self_ , _l : PySide6.QtWidgets.QLayout_)  None

addChildWidget(_self_ , _w :_)  None

addItem(_self_ , _arg__1 : PySide6.QtWidgets.QLayoutItem_)  None

addLayout(_self_ , _layout : PySide6.QtWidgets.QLayout_, _stretch : int = 0_)  None

addSpacerItem(_self_ , _spacerItem : PySide6.QtWidgets.QSpacerItem_)  None

addSpacing(_self_ , _size : int_)  None

addStretch(_self_ , _stretch : int = 0_)  None

addStrut(_self_ , _arg__1 : int_)  None

addWidget(_self_ , _arg__1 :_, _stretch : int = 0_, _alignment : = Default(Qt.Alignment)_)  None

adoptLayout(_self_ , _layout : PySide6.QtWidgets.QLayout_)  bool

alignment(_self_)

alignmentRect(_self_ , _arg__1 : PySide6.QtCore.QRect_)  PySide6.QtCore.QRect

blockSignals(_self_ , _b : bool_)  bool

childEvent(_self_ , _e : PySide6.QtCore.QChildEvent_)  None

children(_self_)  List[PySide6.QtCore.QObject]

_static _closestAcceptableSize(_w :_, _s : PySide6.QtCore.QSize_)  PySide6.QtCore.QSize

_static _connect(_arg__1 : PySide6.QtCore.QObject_, _arg__2 : bytes_, _arg__3 : Callable_, _type : = Instance(Qt.AutoConnection)_)  PySide6.QtCore.QMetaObject.Connection
_static _connect(_self_ , _arg__1 : bytes_, _arg__2 : Callable_, _type : = Instance(Qt.AutoConnection)_)  PySide6.QtCore.QMetaObject.Connection
_static _connect(_self_ , _arg__1 : bytes_, _arg__2 : PySide6.QtCore.QObject_, _arg__3 : bytes_, _type : = Instance(Qt.AutoConnection)_)  PySide6.QtCore.QMetaObject.Connection
_static _connect(_self_ , _sender : PySide6.QtCore.QObject_, _signal : bytes_, _member : bytes_, _type : = Instance(Qt.AutoConnection)_)  PySide6.QtCore.QMetaObject.Connection
_static _connect(_sender : PySide6.QtCore.QObject_, _signal : PySide6.QtCore.QMetaMethod_, _receiver : PySide6.QtCore.QObject_, _method : PySide6.QtCore.QMetaMethod_, _type : = Instance(Qt.AutoConnection)_)  PySide6.QtCore.QMetaObject.Connection
_static _connect(_sender : PySide6.QtCore.QObject_, _signal : bytes_, _receiver : PySide6.QtCore.QObject_, _member : bytes_, _type : = Instance(Qt.AutoConnection)_)  PySide6.QtCore.QMetaObject.Connection

connectNotify(_self_ , _signal : PySide6.QtCore.QMetaMethod_)  None

contentsMargins(_self_)  PySide6.QtCore.QMargins

contentsRect(_self_)  PySide6.QtCore.QRect

controlTypes(_self_)

count(_self_)  int

customEvent(_self_ , _event : PySide6.QtCore.QEvent_)  None

deleteLater(_self_)  None

direction(_self_)

_static _disconnect(_arg__1 : PySide6.QtCore.QMetaObject.Connection_)  bool
_static _disconnect(_arg__1 : PySide6.QtCore.QObject_, _arg__2 : bytes_, _arg__3 : Callable_)  bool
_static _disconnect(_self_ , _arg__1 : bytes_, _arg__2 : Callable_)  bool
_static _disconnect(_self_ , _receiver : PySide6.QtCore.QObject_, _member : Optional[bytes] = None_)  bool
_static _disconnect(_self_ , _signal : bytes_, _receiver : PySide6.QtCore.QObject_, _member : bytes_)  bool
_static _disconnect(_sender : PySide6.QtCore.QObject_, _signal : PySide6.QtCore.QMetaMethod_, _receiver : PySide6.QtCore.QObject_, _member : PySide6.QtCore.QMetaMethod_)  bool
_static _disconnect(_sender : PySide6.QtCore.QObject_, _signal : bytes_, _receiver : PySide6.QtCore.QObject_, _member : bytes_)  bool

disconnectNotify(_self_ , _signal : PySide6.QtCore.QMetaMethod_)  None

dumpObjectInfo(_self_)  None

dumpObjectTree(_self_)  None

dynamicPropertyNames(_self_)  List[PySide6.QtCore.QByteArray]

emit(_self_ , _arg__1 : bytes_, _* args: None_)  bool

event(_self_ , _event : PySide6.QtCore.QEvent_)  bool

eventFilter(_self_ , _watched : PySide6.QtCore.QObject_, _event : PySide6.QtCore.QEvent_)  bool

expandingDirections(_self_)

findChild(_self_ , _type : type_, _name : str = {}_, _options : = Instance(Qt.FindChildrenRecursively)_)  object

findChildren(_self_ , _type : type_, _name : str = {}_, _options : = Instance(Qt.FindChildrenRecursively)_)
findChildren(_self_ , _type : type_, _pattern : Union[PySide6.QtCore.QRegularExpression, str]_, _options : = Instance(Qt.FindChildrenRecursively)_)

geometry(_self_)  PySide6.QtCore.QRect

getContentsMargins(_self_)  object

hasHeightForWidth(_self_)  bool

heightForWidth(_self_ , _arg__1 : int_)  int

indexOf(_self_ , _arg__1 : PySide6.QtWidgets.QLayoutItem_)  int
indexOf(_self_ , _arg__1 :_)  int

inherits(_self_ , _classname : bytes_)  bool

insertItem(_self_ , _index : int_, _arg__2 : PySide6.QtWidgets.QLayoutItem_)  None

insertLayout(_self_ , _index : int_, _layout : PySide6.QtWidgets.QLayout_, _stretch : int = 0_)  None

insertSpacerItem(_self_ , _index : int_, _spacerItem : PySide6.QtWidgets.QSpacerItem_)  None

insertSpacing(_self_ , _index : int_, _size : int_)  None

insertStretch(_self_ , _index : int_, _stretch : int = 0_)  None

insertWidget(_self_ , _index : int_, _widget :_, _stretch : int = 0_, _alignment : = Default(Qt.Alignment)_)  None

installEventFilter(_self_ , _filterObj : PySide6.QtCore.QObject_)  None

invalidate(_self_)  None

isEmpty(_self_)  bool

isEnabled(_self_)  bool

isQuickItemType(_self_)  bool

isSignalConnected(_self_ , _signal : PySide6.QtCore.QMetaMethod_)  bool

isWidgetType(_self_)  bool

isWindowType(_self_)  bool

itemAt(_self_ , _arg__1 : int_)  PySide6.QtWidgets.QLayoutItem

killTimer(_self_ , _id : int_)  None

layout(_self_)  PySide6.QtWidgets.QLayout

maximumSize(_self_)  PySide6.QtCore.QSize

menuBar(_self_)

metaObject(_self_)  PySide6.QtCore.QMetaObject

minimumHeightForWidth(_self_ , _arg__1 : int_)  int

minimumSize(_self_)  PySide6.QtCore.QSize

moveToThread(_self_ , _thread : PySide6.QtCore.QThread_)  None

objectName(_self_)  str

parent(_self_)  PySide6.QtCore.QObject

parentWidget(_self_)

property(_self_ , _name : str_)  Any

receivers(_self_ , _signal : bytes_)  int

removeEventFilter(_self_ , _obj : PySide6.QtCore.QObject_)  None

removeItem(_self_ , _arg__1 : PySide6.QtWidgets.QLayoutItem_)  None

removeWidget(_self_ , _w :_)  None

replaceWidget(_self_ , _from_ :_, _to :_, _options : = Instance(Qt.FindChildrenRecursively)_)  PySide6.QtWidgets.QLayoutItem

sender(_self_)  PySide6.QtCore.QObject

senderSignalIndex(_self_)  int

setAlignment(_self_ , _arg__1 :_)  None
setAlignment(_self_ , _l : PySide6.QtWidgets.QLayout_, _alignment :_)  bool
setAlignment(_self_ , _w :_, _alignment :_)  bool

setContentsMargins(_self_ , _left : int_, _top : int_, _right : int_, _bottom : int_)  None
setContentsMargins(_self_ , _margins : PySide6.QtCore.QMargins_)  None

setDirection(_self_ , _arg__1 :_)  None

setEnabled(_self_ , _arg__1 : bool_)  None

setGeometry(_self_ , _arg__1 : PySide6.QtCore.QRect_)  None

setMenuBar(_self_ , _w :_)  None

setObjectName(_self_ , _name : str_)  None

setParent(_self_ , _parent : Optional[PySide6.QtCore.QObject]_)  None

setProperty(_self_ , _name : str_, _value : Any_)  bool

setSizeConstraint(_self_ , _arg__1 :_)  None

setSpacing(_self_ , _spacing : int_)  None

setStretch(_self_ , _index : int_, _stretch : int_)  None

setStretchFactor(_self_ , _l : PySide6.QtWidgets.QLayout_, _stretch : int_)  bool
setStretchFactor(_self_ , _w :_, _stretch : int_)  bool

signalsBlocked(_self_)  bool

sizeConstraint(_self_)

sizeHint(_self_)  PySide6.QtCore.QSize

spacerItem(_self_)  PySide6.QtWidgets.QSpacerItem

spacing(_self_)  int

startTimer(_self_ , _interval : int_, _timerType : = Instance(Qt.CoarseTimer)_)  int

stretch(_self_ , _index : int_)  int

takeAt(_self_ , _arg__1 : int_)  PySide6.QtWidgets.QLayoutItem

thread(_self_)  PySide6.QtCore.QThread

timerEvent(_self_ , _event : PySide6.QtCore.QTimerEvent_)  None

totalHeightForWidth(_self_ , _w : int_)  int

totalMaximumSize(_self_)  PySide6.QtCore.QSize

totalMinimumHeightForWidth(_self_ , _w : int_)  int

totalMinimumSize(_self_)  PySide6.QtCore.QSize

totalSizeHint(_self_)  PySide6.QtCore.QSize

tr(_self_ , _sourceText : str_, _disambiguation : Optional[str]_, _n : int = - 1_)  str

unsetContentsMargins(_self_)  None

update(_self_)  None

widget(_self_)

widgetEvent(_self_ , _arg__1 : PySide6.QtCore.QEvent_)  None