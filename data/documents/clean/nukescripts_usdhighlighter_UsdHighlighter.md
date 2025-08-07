# nukescripts.usdhighlighter.UsdHighlighter
_class _nukescripts.usdhighlighter.UsdHighlighter(_self_ , _parent : PySide6.QtCore.QObject_)  None
_class _nukescripts.usdhighlighter.UsdHighlighter(_self_ , _parent : PySide6.QtGui.QTextDocument_)  None

Bases: `PySide6.QtGui.QSyntaxHighlighter`
Initialize self. See help(type(self)) for accurate signature.
Methods
`blockSignals` ---
`childEvent`
`children`
`connect`
`connectNotify`
`currentBlock`
`currentBlockState`
`currentBlockUserData`
`customEvent`
`deleteLater`
`disconnect`
`disconnectNotify`
`document`
`dumpObjectInfo`
`dumpObjectTree`
`dynamicPropertyNames`
`emit`
`event`
`eventFilter`
`findChild`
`findChildren`
`format`
`highlightBlock`
`inherits`
`installEventFilter`
`isQuickItemType`
`isSignalConnected`
`isWidgetType`
`isWindowType`
`killTimer`
`metaObject`
`moveToThread`
`objectName`
`parent`
`previousBlockState`
`property`
`receivers`
`rehighlight`
`rehighlightBlock`
`removeEventFilter`
`sender`
`senderSignalIndex`
`setCurrentBlockState`
`setCurrentBlockUserData`
`setDocument`
`setFormat`
`setObjectName`
`setParent`
`setProperty`
`signalsBlocked`
`startTimer`
`thread`
`timerEvent`
`tr`

Attributes
`destroyed` ---
`objectNameChanged`
`staticMetaObject`

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

currentBlock(_self_)  PySide6.QtGui.QTextBlock

currentBlockState(_self_)  int

currentBlockUserData(_self_)  PySide6.QtGui.QTextBlockUserData

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

document(_self_)  PySide6.QtGui.QTextDocument

dumpObjectInfo(_self_)  None

dumpObjectTree(_self_)  None

dynamicPropertyNames(_self_)  List[PySide6.QtCore.QByteArray]

emit(_self_ , _arg__1 : bytes_, _* args: None_)  bool

event(_self_ , _event : PySide6.QtCore.QEvent_)  bool

eventFilter(_self_ , _watched : PySide6.QtCore.QObject_, _event : PySide6.QtCore.QEvent_)  bool

findChild(_self_ , _type : type_, _name : str = {}_, _options : = Instance(Qt.FindChildrenRecursively)_)  object

findChildren(_self_ , _type : type_, _name : str = {}_, _options : = Instance(Qt.FindChildrenRecursively)_)
findChildren(_self_ , _type : type_, _pattern : Union[PySide6.QtCore.QRegularExpression, str]_, _options : = Instance(Qt.FindChildrenRecursively)_)

format(_self_ , _pos : int_)  PySide6.QtGui.QTextCharFormat

highlightBlock(_self_ , _text : str_)  None

inherits(_self_ , _classname : bytes_)  bool

installEventFilter(_self_ , _filterObj : PySide6.QtCore.QObject_)  None

isQuickItemType(_self_)  bool

isSignalConnected(_self_ , _signal : PySide6.QtCore.QMetaMethod_)  bool

isWidgetType(_self_)  bool

isWindowType(_self_)  bool

killTimer(_self_ , _id : int_)  None

metaObject(_self_)  PySide6.QtCore.QMetaObject

moveToThread(_self_ , _thread : PySide6.QtCore.QThread_)  None

objectName(_self_)  str

parent(_self_)  PySide6.QtCore.QObject

previousBlockState(_self_)  int

property(_self_ , _name : str_)  Any

receivers(_self_ , _signal : bytes_)  int

rehighlight(_self_)  None

rehighlightBlock(_self_ , _block : PySide6.QtGui.QTextBlock_)  None

removeEventFilter(_self_ , _obj : PySide6.QtCore.QObject_)  None

sender(_self_)  PySide6.QtCore.QObject

senderSignalIndex(_self_)  int

setCurrentBlockState(_self_ , _newState : int_)  None

setCurrentBlockUserData(_self_ , _data : PySide6.QtGui.QTextBlockUserData_)  None

setDocument(_self_ , _doc : Optional[PySide6.QtGui.QTextDocument]_)  None

setFormat(_self_ , _start : int_, _count : int_, _color : Union, str, int]_)  None
setFormat(_self_ , _start : int_, _count : int_, _font : Union[PySide6.QtGui.QFont, str, Sequence[str]]_)  None
setFormat(_self_ , _start : int_, _count : int_, _format : PySide6.QtGui.QTextCharFormat_)  None

setObjectName(_self_ , _name : str_)  None

setParent(_self_ , _parent : Optional[PySide6.QtCore.QObject]_)  None

setProperty(_self_ , _name : str_, _value : Any_)  bool

signalsBlocked(_self_)  bool

startTimer(_self_ , _interval : int_, _timerType : = Instance(Qt.CoarseTimer)_)  int

thread(_self_)  PySide6.QtCore.QThread

timerEvent(_self_ , _event : PySide6.QtCore.QTimerEvent_)  None

tr(_self_ , _sourceText : str_, _disambiguation : Optional[str]_, _n : int = - 1_)  str