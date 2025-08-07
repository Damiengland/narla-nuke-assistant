# nukescripts.readviewscheck.QTimer
_class _nukescripts.readviewscheck.QTimer(_self_ , _parent : Optional[PySide6.QtCore.QObject] = None_)  None

Bases: `PySide6.QtCore.QObject`
__init__(self, parent: Optional[PySide6.QtCore.QObject] = None) -> None
Initialize self. See help(type(self)) for accurate signature.
Methods
`blockSignals` ---
`childEvent`
`children`
`connect`
`connectNotify`
`customEvent`
`deleteLater`
`disconnect`
`disconnectNotify`
`dumpObjectInfo`
`dumpObjectTree`
`dynamicPropertyNames`
`emit`
`event`
`eventFilter`
`findChild`
`findChildren`
`inherits`
`installEventFilter`
`interval`
`isActive`
`isQuickItemType`
`isSignalConnected`
`isSingleShot`
`isWidgetType`
`isWindowType`
`killTimer`
`metaObject`
`moveToThread`
`objectName`
`parent`
`property`
`receivers`
`remainingTime`
`removeEventFilter`
`sender`
`senderSignalIndex`
`setInterval`
`setObjectName`
`setParent`
`setProperty`
`setSingleShot`
`setTimerType`
`signalsBlocked`
`singleShot`
`start`
`startTimer`
`stop`
`thread`
`timerEvent`
`timerId`
`timerType`
`tr`

Attributes
`destroyed` ---
`objectNameChanged`
`staticMetaObject`
`timeout`

blockSignals(_self_ , _b : bool_)  bool

childEvent(_self_ , _event : PySide6.QtCore.QChildEvent_)  None

children(_self_)  List[PySide6.QtCore.QObject]

_static _connect(_arg__1 : PySide6.QtCore.QObject_, _arg__2 : bytes_, _arg__3 : Callable_, _type : = Instance(Qt.AutoConnection)_)  PySide6.QtCore.QMetaObject.Connection
_static _connect(_self_ , _arg__1 : bytes_, _arg__2 : Callable_, _type : = Instance(Qt.AutoConnection)_)  PySide6.QtCore.QMetaObject.Connection
_static _connect(_self_ , _arg__1 : bytes_, _arg__2 : PySide6.QtCore.QObject_, _arg__3 : bytes_, _type : = Instance(Qt.AutoConnection)_)  PySide6.QtCore.QMetaObject.Connection
_static _connect(_self_ , _sender : PySide6.QtCore.QObject_, _signal : bytes_, _member : bytes_, _type : = Instance(Qt.AutoConnection)_)  PySide6.QtCore.QMetaObject.Connection
_static _connect(_sender : PySide6.QtCore.QObject_, _signal : PySide6.QtCore.QMetaMethod_, _receiver : PySide6.QtCore.QObject_, _method : PySide6.QtCore.QMetaMethod_, _type : = Instance(Qt.AutoConnection)_)  PySide6.QtCore.QMetaObject.Connection
_static _connect(_sender : PySide6.QtCore.QObject_, _signal : bytes_, _receiver : PySide6.QtCore.QObject_, _member : bytes_, _type : = Instance(Qt.AutoConnection)_)  PySide6.QtCore.QMetaObject.Connection

connectNotify(_self_ , _signal : PySide6.QtCore.QMetaMethod_)  None

customEvent(_self_ , _event : PySide6.QtCore.QEvent_)  None

deleteLater(_self_)  None

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

findChild(_self_ , _type : type_, _name : str = {}_, _options : = Instance(Qt.FindChildrenRecursively)_)  object

findChildren(_self_ , _type : type_, _name : str = {}_, _options : = Instance(Qt.FindChildrenRecursively)_)
findChildren(_self_ , _type : type_, _pattern : Union[PySide6.QtCore.QRegularExpression, str]_, _options : = Instance(Qt.FindChildrenRecursively)_)

inherits(_self_ , _classname : bytes_)  bool

installEventFilter(_self_ , _filterObj : PySide6.QtCore.QObject_)  None

interval(_self_)  int

isActive(_self_)  bool

isQuickItemType(_self_)  bool

isSignalConnected(_self_ , _signal : PySide6.QtCore.QMetaMethod_)  bool

isSingleShot(_self_)  bool

isWidgetType(_self_)  bool

isWindowType(_self_)  bool

killTimer(_self_ , _arg__1 : int_)  None

metaObject(_self_)  PySide6.QtCore.QMetaObject

moveToThread(_self_ , _thread : PySide6.QtCore.QThread_)  None

objectName(_self_)  str

parent(_self_)  PySide6.QtCore.QObject

property(_self_ , _name : str_)  Any

receivers(_self_ , _signal : bytes_)  int

remainingTime(_self_)  int

removeEventFilter(_self_ , _obj : PySide6.QtCore.QObject_)  None

sender(_self_)  PySide6.QtCore.QObject

senderSignalIndex(_self_)  int

setInterval(_self_ , _msec : int_)  None

setObjectName(_self_ , _name : str_)  None

setParent(_self_ , _parent : Optional[PySide6.QtCore.QObject]_)  None

setProperty(_self_ , _name : str_, _value : Any_)  bool

setSingleShot(_self_ , _singleShot : bool_)  None

setTimerType(_self_ , _atype :_)  None

signalsBlocked(_self_)  bool

_static _singleShot(_arg__1 : int_, _arg__2 : Callable_)  None
_static _singleShot(_msec : int_, _receiver : PySide6.QtCore.QObject_, _member : bytes_)  None
_static _singleShot(_msec : int_, _timerType :_, _receiver : PySide6.QtCore.QObject_, _member : bytes_)  None

start(_self_)  None
start(_self_ , _msec : int_)  None

startTimer(_self_ , _interval : int_, _timerType : = Instance(Qt.CoarseTimer)_)  int

stop(_self_)  None

thread(_self_)  PySide6.QtCore.QThread

timerEvent(_self_ , _arg__1 : PySide6.QtCore.QTimerEvent_)  None

timerId(_self_)  int

timerType(_self_)

tr(_self_ , _sourceText : str_, _disambiguation : Optional[str]_, _n : int = - 1_)  str