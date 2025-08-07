# nukescripts.udim.TableDelegate
_class _nukescripts.udim.TableDelegate(_self_ , _parent : Optional[PySide6.QtCore.QObject] = None_)  None

Bases: `PySide6.QtWidgets.QStyledItemDelegate`
Initialize self. See help(type(self)) for accurate signature.
Methods
`blockSignals` ---
`childEvent`
`children`
`connect`
`connectNotify`
`createEditor`
`customEvent`
`deleteLater`
`destroyEditor`
`disconnect`
`disconnectNotify`
`displayText`
`dumpObjectInfo`
`dumpObjectTree`
`dynamicPropertyNames`
`editorEvent`
`emit`
`event`
`eventFilter`
`findChild`
`findChildren`
`helpEvent`
`inherits`
`initStyleOption`
`installEventFilter`
`isQuickItemType`
`isSignalConnected`
`isWidgetType`
`isWindowType`
`itemEditorFactory`
`killTimer`
`metaObject`
`moveToThread`
`objectName`
`paint`
`paintingRoles`
`parent`
`property`
`receivers`
`removeEventFilter`
`sender`
`senderSignalIndex`
`setEditorData`
`setItemEditorFactory`
`setModelData`
`setObjectName`
`setParent`
`setProperty`
`signalsBlocked`
`sizeHint`
`startTimer`
`thread`
`timerEvent`
`tr`
`updateEditorGeometry`

Attributes
`closeEditor` ---
`commitData`
`destroyed`
`objectNameChanged`
`sizeHintChanged`
`staticMetaObject`

_class _EndEditHint(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Enum`
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

createEditor(_self_ , _parent :_, _option : PySide6.QtWidgets.QStyleOptionViewItem_, _index : Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex]_)

customEvent(_self_ , _event : PySide6.QtCore.QEvent_)  None

deleteLater(_self_)  None

destroyEditor(_self_ , _editor :_, _index : Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex]_)  None

_static _disconnect(_arg__1 : PySide6.QtCore.QMetaObject.Connection_)  bool
_static _disconnect(_arg__1 : PySide6.QtCore.QObject_, _arg__2 : bytes_, _arg__3 : Callable_)  bool
_static _disconnect(_self_ , _arg__1 : bytes_, _arg__2 : Callable_)  bool
_static _disconnect(_self_ , _receiver : PySide6.QtCore.QObject_, _member : Optional[bytes] = None_)  bool
_static _disconnect(_self_ , _signal : bytes_, _receiver : PySide6.QtCore.QObject_, _member : bytes_)  bool
_static _disconnect(_sender : PySide6.QtCore.QObject_, _signal : PySide6.QtCore.QMetaMethod_, _receiver : PySide6.QtCore.QObject_, _member : PySide6.QtCore.QMetaMethod_)  bool
_static _disconnect(_sender : PySide6.QtCore.QObject_, _signal : bytes_, _receiver : PySide6.QtCore.QObject_, _member : bytes_)  bool

disconnectNotify(_self_ , _signal : PySide6.QtCore.QMetaMethod_)  None

displayText(_self_ , _value : Any_, _locale : Union[PySide6.QtCore.QLocale, PySide6.QtCore.QLocale.Language]_)  str

dumpObjectInfo(_self_)  None

dumpObjectTree(_self_)  None

dynamicPropertyNames(_self_)  List[PySide6.QtCore.QByteArray]

editorEvent(_self_ , _event : PySide6.QtCore.QEvent_, _model : PySide6.QtCore.QAbstractItemModel_, _option : PySide6.QtWidgets.QStyleOptionViewItem_, _index : Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex]_)  bool

emit(_self_ , _arg__1 : bytes_, _* args: None_)  bool

event(_self_ , _event : PySide6.QtCore.QEvent_)  bool

eventFilter(_self_ , _object : PySide6.QtCore.QObject_, _event : PySide6.QtCore.QEvent_)  bool

findChild(_self_ , _type : type_, _name : str = {}_, _options : = Instance(Qt.FindChildrenRecursively)_)  object

findChildren(_self_ , _type : type_, _name : str = {}_, _options : = Instance(Qt.FindChildrenRecursively)_)
findChildren(_self_ , _type : type_, _pattern : Union[PySide6.QtCore.QRegularExpression, str]_, _options : = Instance(Qt.FindChildrenRecursively)_)

helpEvent(_self_ , _event : PySide6.QtGui.QHelpEvent_, _view : PySide6.QtWidgets.QAbstractItemView_, _option : PySide6.QtWidgets.QStyleOptionViewItem_, _index : Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex]_)  bool

inherits(_self_ , _classname : bytes_)  bool

initStyleOption(_self_ , _option : PySide6.QtWidgets.QStyleOptionViewItem_, _index : Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex]_)  None

installEventFilter(_self_ , _filterObj : PySide6.QtCore.QObject_)  None

isQuickItemType(_self_)  bool

isSignalConnected(_self_ , _signal : PySide6.QtCore.QMetaMethod_)  bool

isWidgetType(_self_)  bool

isWindowType(_self_)  bool

itemEditorFactory(_self_)  PySide6.QtWidgets.QItemEditorFactory

killTimer(_self_ , _id : int_)  None

metaObject(_self_)  PySide6.QtCore.QMetaObject

moveToThread(_self_ , _thread : PySide6.QtCore.QThread_)  None

objectName(_self_)  str

paint(_self_ , _painter :_, _option : PySide6.QtWidgets.QStyleOptionViewItem_, _index : Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex]_)  None

paintingRoles(_self_)  List[int]

parent(_self_)  PySide6.QtCore.QObject

property(_self_ , _name : str_)  Any

receivers(_self_ , _signal : bytes_)  int

removeEventFilter(_self_ , _obj : PySide6.QtCore.QObject_)  None

sender(_self_)  PySide6.QtCore.QObject

senderSignalIndex(_self_)  int

setEditorData(_self_ , _editor :_, _index : Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex]_)  None

setItemEditorFactory(_self_ , _factory : PySide6.QtWidgets.QItemEditorFactory_)  None

setModelData(_self_ , _editor :_, _model : PySide6.QtCore.QAbstractItemModel_, _index : Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex]_)  None

setObjectName(_self_ , _name : str_)  None

setParent(_self_ , _parent : Optional[PySide6.QtCore.QObject]_)  None

setProperty(_self_ , _name : str_, _value : Any_)  bool

signalsBlocked(_self_)  bool

sizeHint(_self_ , _option : PySide6.QtWidgets.QStyleOptionViewItem_, _index : Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex]_)  PySide6.QtCore.QSize

startTimer(_self_ , _interval : int_, _timerType : = Instance(Qt.CoarseTimer)_)  int

thread(_self_)  PySide6.QtCore.QThread

timerEvent(_self_ , _event : PySide6.QtCore.QTimerEvent_)  None

tr(_self_ , _sourceText : str_, _disambiguation : Optional[str]_, _n : int = - 1_)  str

updateEditorGeometry(_self_ , _editor :_, _option : PySide6.QtWidgets.QStyleOptionViewItem_, _index : Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex]_)  None