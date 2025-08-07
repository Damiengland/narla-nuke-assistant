# nukescripts.readviewscheck.QApplication
_class _nukescripts.readviewscheck.QApplication(_self_)  None
_class _nukescripts.readviewscheck.QApplication(_self_ , _arg__1 : Sequence[str]_)  None

Bases: `PySide6.QtGui.QGuiApplication`
__init__(self) -> None __init__(self, arg__1: Sequence[str]) -> None
Initialize self. See help(type(self)) for accurate signature.
Methods
`aboutQt` ---
`activeModalWidget`
`activePopupWidget`
`activeWindow`
`addLibraryPath`
`alert`
`allWidgets`
`allWindows`
`applicationDirPath`
`applicationDisplayName`
`applicationFilePath`
`applicationName`
`applicationPid`
`applicationState`
`applicationVersion`
`arguments`
`autoSipEnabled`
`beep`
`blockSignals`
`changeOverrideCursor`
`childEvent`
`children`
`clipboard`
`closeAllWindows`
`closingDown`
`connect`
`connectNotify`
`cursorFlashTime`
`customEvent`
`deleteLater`
`desktopFileName`
`desktopSettingsAware`
`devicePixelRatio`
`disconnect`
`disconnectNotify`
`doubleClickInterval`
`dumpObjectInfo`
`dumpObjectTree`
`dynamicPropertyNames`
`emit`
`event`
`eventDispatcher`
`eventFilter`
`exec`
`exec_`
`exit`
`findChild`
`findChildren`
`focusObject`
`focusWidget`
`focusWindow`
`font`
`fontMetrics`
`highDpiScaleFactorRoundingPolicy`
`inherits`
`inputMethod`
`installEventFilter`
`installNativeEventFilter`
`installTranslator`
`instance`
`isEffectEnabled`
`isLeftToRight`
`isQuickItemType`
`isQuitLockEnabled`
`isRightToLeft`
`isSavingSession`
`isSessionRestored`
`isSetuidAllowed`
`isSignalConnected`
`isWidgetType`
`isWindowType`
`keyboardInputInterval`
`keyboardModifiers`
`killTimer`
`layoutDirection`
`libraryPaths`
`metaObject`
`modalWindow`
`mouseButtons`
`moveToThread`
`notify`
`objectName`
`organizationDomain`
`organizationName`
`overrideCursor`
`palette`
`parent`
`platformFunction`
`platformName`
`postEvent`
`primaryScreen`
`processEvents`
`property`
`queryKeyboardModifiers`
`quit`
`quitOnLastWindowClosed`
`receivers`
`removeEventFilter`
`removeLibraryPath`
`removeNativeEventFilter`
`removePostedEvents`
`removeTranslator`
`resolveInterface`
`restoreOverrideCursor`
`screenAt`
`screens`
`sendEvent`
`sendPostedEvents`
`sender`
`senderSignalIndex`
`sessionId`
`sessionKey`
`setActiveWindow`
`setApplicationDisplayName`
`setApplicationName`
`setApplicationVersion`
`setAttribute`
`setAutoSipEnabled`
`setBadgeNumber`
`setCursorFlashTime`
`setDesktopFileName`
`setDesktopSettingsAware`
`setDoubleClickInterval`
`setEffectEnabled`
`setEventDispatcher`
`setFont`
`setHighDpiScaleFactorRoundingPolicy`
`setKeyboardInputInterval`
`setLayoutDirection`
`setLibraryPaths`
`setObjectName`
`setOrganizationDomain`
`setOrganizationName`
`setOverrideCursor`
`setPalette`
`setParent`
`setProperty`
`setQuitLockEnabled`
`setQuitOnLastWindowClosed`
`setSetuidAllowed`
`setStartDragDistance`
`setStartDragTime`
`setStyle`
`setStyleSheet`
`setWheelScrollLines`
`setWindowIcon`
`shutdown`
`signalsBlocked`
`startDragDistance`
`startDragTime`
`startTimer`
`startingUp`
`style`
`styleHints`
`styleSheet`
`sync`
`testAttribute`
`thread`
`timerEvent`
`topLevelAt`
`topLevelWidgets`
`topLevelWindows`
`tr`
`translate`
`wheelScrollLines`
`widgetAt`
`windowIcon`

Attributes
`ApplicationFlags` ---
`aboutToQuit`
`applicationDisplayNameChanged`
`applicationNameChanged`
`applicationStateChanged`
`applicationVersionChanged`
`commitDataRequest`
`destroyed`
`focusChanged`
`focusObjectChanged`
`focusWindowChanged`
`fontChanged`
`fontDatabaseChanged`
`lastWindowClosed`
`layoutDirectionChanged`
`objectNameChanged`
`organizationDomainChanged`
`organizationNameChanged`
`paletteChanged`
`primaryScreenChanged`
`saveStateRequest`
`screenAdded`
`screenRemoved`
`staticMetaObject`

_static _aboutQt()  None

_static _activeModalWidget()

_static _activePopupWidget()

_static _activeWindow()

_static _addLibraryPath(_arg__1 : str_)  None

_static _alert(_widget :_, _duration : int = 0_)  None

_static _allWidgets()  List]

_static _allWindows()  List[PySide6.QtGui.QWindow]

_static _applicationDirPath()  str

_static _applicationDisplayName()  str

_static _applicationFilePath()  str

_static _applicationName()  str

_static _applicationPid()  int

_static _applicationState()

_static _applicationVersion()  str

_static _arguments()  List[str]

autoSipEnabled(_self_)  bool

_static _beep()  None

blockSignals(_self_ , _b : bool_)  bool

_static _changeOverrideCursor(_arg__1 : Union, PySide6.QtGui.QPixmap]_)  None

childEvent(_self_ , _event : PySide6.QtCore.QChildEvent_)  None

children(_self_)  List[PySide6.QtCore.QObject]

_static _clipboard()  PySide6.QtGui.QClipboard

_static _closeAllWindows()  None

_static _closingDown()  bool

_static _connect(_arg__1 : PySide6.QtCore.QObject_, _arg__2 : bytes_, _arg__3 : Callable_, _type : = Instance(Qt.AutoConnection)_)  PySide6.QtCore.QMetaObject.Connection
_static _connect(_self_ , _arg__1 : bytes_, _arg__2 : Callable_, _type : = Instance(Qt.AutoConnection)_)  PySide6.QtCore.QMetaObject.Connection
_static _connect(_self_ , _arg__1 : bytes_, _arg__2 : PySide6.QtCore.QObject_, _arg__3 : bytes_, _type : = Instance(Qt.AutoConnection)_)  PySide6.QtCore.QMetaObject.Connection
_static _connect(_self_ , _sender : PySide6.QtCore.QObject_, _signal : bytes_, _member : bytes_, _type : = Instance(Qt.AutoConnection)_)  PySide6.QtCore.QMetaObject.Connection
_static _connect(_sender : PySide6.QtCore.QObject_, _signal : PySide6.QtCore.QMetaMethod_, _receiver : PySide6.QtCore.QObject_, _method : PySide6.QtCore.QMetaMethod_, _type : = Instance(Qt.AutoConnection)_)  PySide6.QtCore.QMetaObject.Connection
_static _connect(_sender : PySide6.QtCore.QObject_, _signal : bytes_, _receiver : PySide6.QtCore.QObject_, _member : bytes_, _type : = Instance(Qt.AutoConnection)_)  PySide6.QtCore.QMetaObject.Connection

connectNotify(_self_ , _signal : PySide6.QtCore.QMetaMethod_)  None

_static _cursorFlashTime()  int

customEvent(_self_ , _event : PySide6.QtCore.QEvent_)  None

deleteLater(_self_)  None

_static _desktopFileName()  str

_static _desktopSettingsAware()  bool

devicePixelRatio(_self_)  float

_static _disconnect(_arg__1 : PySide6.QtCore.QMetaObject.Connection_)  bool
_static _disconnect(_arg__1 : PySide6.QtCore.QObject_, _arg__2 : bytes_, _arg__3 : Callable_)  bool
_static _disconnect(_self_ , _arg__1 : bytes_, _arg__2 : Callable_)  bool
_static _disconnect(_self_ , _receiver : PySide6.QtCore.QObject_, _member : Optional[bytes] = None_)  bool
_static _disconnect(_self_ , _signal : bytes_, _receiver : PySide6.QtCore.QObject_, _member : bytes_)  bool
_static _disconnect(_sender : PySide6.QtCore.QObject_, _signal : PySide6.QtCore.QMetaMethod_, _receiver : PySide6.QtCore.QObject_, _member : PySide6.QtCore.QMetaMethod_)  bool
_static _disconnect(_sender : PySide6.QtCore.QObject_, _signal : bytes_, _receiver : PySide6.QtCore.QObject_, _member : bytes_)  bool

disconnectNotify(_self_ , _signal : PySide6.QtCore.QMetaMethod_)  None

_static _doubleClickInterval()  int

dumpObjectInfo(_self_)  None

dumpObjectTree(_self_)  None

dynamicPropertyNames(_self_)  List[PySide6.QtCore.QByteArray]

emit(_self_ , _arg__1 : bytes_, _* args: None_)  bool

event(_self_ , _arg__1 : PySide6.QtCore.QEvent_)  bool

_static _eventDispatcher()  PySide6.QtCore.QAbstractEventDispatcher

eventFilter(_self_ , _watched : PySide6.QtCore.QObject_, _event : PySide6.QtCore.QEvent_)  bool

_static _exec()  int

exec_(_self_)  int

_static _exit(_retcode : int = 0_)  None

findChild(_self_ , _type : type_, _name : str = {}_, _options : = Instance(Qt.FindChildrenRecursively)_)  object

findChildren(_self_ , _type : type_, _name : str = {}_, _options : = Instance(Qt.FindChildrenRecursively)_)
findChildren(_self_ , _type : type_, _pattern : Union[PySide6.QtCore.QRegularExpression, str]_, _options : = Instance(Qt.FindChildrenRecursively)_)

_static _focusObject()  PySide6.QtCore.QObject

_static _focusWidget()

_static _focusWindow()  PySide6.QtGui.QWindow

_static _font()  PySide6.QtGui.QFont
_static _font(_arg__1 :_)  PySide6.QtGui.QFont
_static _font(_className : bytes_)  PySide6.QtGui.QFont

_static _fontMetrics()  PySide6.QtGui.QFontMetrics

_static _highDpiScaleFactorRoundingPolicy()

inherits(_self_ , _classname : bytes_)  bool

_static _inputMethod()  PySide6.QtGui.QInputMethod

installEventFilter(_self_ , _filterObj : PySide6.QtCore.QObject_)  None

installNativeEventFilter(_self_ , _filterObj : PySide6.QtCore.QAbstractNativeEventFilter_)  None

_static _installTranslator(_messageFile : PySide6.QtCore.QTranslator_)  bool

_static _instance()  Optional[PySide6.QtCore.QCoreApplication]

_static _isEffectEnabled(_arg__1 :_)  bool

_static _isLeftToRight()  bool

isQuickItemType(_self_)  bool

_static _isQuitLockEnabled()  bool

_static _isRightToLeft()  bool

isSavingSession(_self_)  bool

isSessionRestored(_self_)  bool

_static _isSetuidAllowed()  bool

isSignalConnected(_self_ , _signal : PySide6.QtCore.QMetaMethod_)  bool

isWidgetType(_self_)  bool

isWindowType(_self_)  bool

_static _keyboardInputInterval()  int

_static _keyboardModifiers()

killTimer(_self_ , _id : int_)  None

_static _layoutDirection()

_static _libraryPaths()  List[str]

metaObject(_self_)  PySide6.QtCore.QMetaObject

_static _modalWindow()  PySide6.QtGui.QWindow

_static _mouseButtons()

moveToThread(_self_ , _thread : PySide6.QtCore.QThread_)  None

notify(_self_ , _arg__1 : PySide6.QtCore.QObject_, _arg__2 : PySide6.QtCore.QEvent_)  bool

objectName(_self_)  str

_static _organizationDomain()  str

_static _organizationName()  str

_static _overrideCursor()  PySide6.QtGui.QCursor

_static _palette()
_static _palette(_arg__1 :_)
_static _palette(_className : bytes_)

parent(_self_)  PySide6.QtCore.QObject

_static _platformFunction(_function : Union[PySide6.QtCore.QByteArray, bytes]_)  int

_static _platformName()  str

_static _postEvent(_receiver : PySide6.QtCore.QObject_, _event : PySide6.QtCore.QEvent_, _priority : int = Instance(Qt.NormalEventPriority)_)  None

_static _primaryScreen()  PySide6.QtGui.QScreen

_static _processEvents(_flags : PySide6.QtCore.QEventLoop.ProcessEventsFlag_, _maxtime : int_)  None
_static _processEvents(_flags : PySide6.QtCore.QEventLoop.ProcessEventsFlag = Instance(PySide6.QtCore.QEventLoop.AllEvents)_)  None

property(_self_ , _name : str_)  Any

_static _queryKeyboardModifiers()

_static _quit()  None

_static _quitOnLastWindowClosed()  bool

receivers(_self_ , _signal : bytes_)  int

removeEventFilter(_self_ , _obj : PySide6.QtCore.QObject_)  None

_static _removeLibraryPath(_arg__1 : str_)  None

removeNativeEventFilter(_self_ , _filterObj : PySide6.QtCore.QAbstractNativeEventFilter_)  None

_static _removePostedEvents(_receiver : PySide6.QtCore.QObject_, _eventType : int = 0_)  None

_static _removeTranslator(_messageFile : PySide6.QtCore.QTranslator_)  bool

resolveInterface(_self_ , _name : bytes_, _revision : int_)  int

_static _restoreOverrideCursor()  None

_static _screenAt(_point : PySide6.QtCore.QPoint_)  PySide6.QtGui.QScreen

_static _screens()  List[PySide6.QtGui.QScreen]

_static _sendEvent(_receiver : PySide6.QtCore.QObject_, _event : PySide6.QtCore.QEvent_)  bool

_static _sendPostedEvents(_receiver : Optional[PySide6.QtCore.QObject] = None_, _event_type : int = 0_)  None

sender(_self_)  PySide6.QtCore.QObject

senderSignalIndex(_self_)  int

sessionId(_self_)  str

sessionKey(_self_)  str

_static _setActiveWindow(_act :_)  None

_static _setApplicationDisplayName(_name : str_)  None

_static _setApplicationName(_application : str_)  None

_static _setApplicationVersion(_version : str_)  None

_static _setAttribute(_attribute :_, _on : bool = True_)  None

setAutoSipEnabled(_self_ , _enabled : bool_)  None

setBadgeNumber(_self_ , _number : int_)  None

_static _setCursorFlashTime(_arg__1 : int_)  None

_static _setDesktopFileName(_name : str_)  None

_static _setDesktopSettingsAware(_on : bool_)  None

_static _setDoubleClickInterval(_arg__1 : int_)  None

_static _setEffectEnabled(_arg__1 :_, _enable : bool = True_)  None

_static _setEventDispatcher(_eventDispatcher : PySide6.QtCore.QAbstractEventDispatcher_)  None

_static _setFont(_arg__1 : Union[PySide6.QtGui.QFont, str, Sequence[str]]_, _className : Optional[bytes] = None_)  None

_static _setHighDpiScaleFactorRoundingPolicy(_policy :_)  None

_static _setKeyboardInputInterval(_arg__1 : int_)  None

_static _setLayoutDirection(_direction :_)  None

_static _setLibraryPaths(_arg__1 : Sequence[str]_)  None

setObjectName(_self_ , _name : str_)  None

_static _setOrganizationDomain(_orgDomain : str_)  None

_static _setOrganizationName(_orgName : str_)  None

_static _setOverrideCursor(_arg__1 : Union, PySide6.QtGui.QPixmap]_)  object

_static _setPalette(_arg__1 : Union,, PySide6.QtGui.QColor]_, _className : Optional[bytes] = None_)  None

setParent(_self_ , _parent : Optional[PySide6.QtCore.QObject]_)  None

setProperty(_self_ , _name : str_, _value : Any_)  bool

_static _setQuitLockEnabled(_enabled : bool_)  None

_static _setQuitOnLastWindowClosed(_quit : bool_)  None

_static _setSetuidAllowed(_allow : bool_)  None

_static _setStartDragDistance(_l : int_)  None

_static _setStartDragTime(_ms : int_)  None

_static _setStyle(_arg__1 :_)  None
_static _setStyle(_arg__1 : str_)

setStyleSheet(_self_ , _sheet : str_)  None

_static _setWheelScrollLines(_arg__1 : int_)  None

_static _setWindowIcon(_icon : Union[PySide6.QtGui.QIcon, PySide6.QtGui.QPixmap]_)  None

shutdown(_self_)  None

signalsBlocked(_self_)  bool

_static _startDragDistance()  int

_static _startDragTime()  int

startTimer(_self_ , _interval : int_, _timerType : = Instance(Qt.CoarseTimer)_)  int

_static _startingUp()  bool

_static _style()

_static _styleHints()  PySide6.QtGui.QStyleHints

styleSheet(_self_)  str

_static _sync()  None

_static _testAttribute(_attribute :_)  bool

thread(_self_)  PySide6.QtCore.QThread

timerEvent(_self_ , _event : PySide6.QtCore.QTimerEvent_)  None

_static _topLevelAt(_p : PySide6.QtCore.QPoint_)
_static _topLevelAt(_x : int_, _y : int_)

_static _topLevelWidgets()  List]

_static _topLevelWindows()  List[PySide6.QtGui.QWindow]

tr(_self_ , _sourceText : str_, _disambiguation : Optional[str]_, _n : int = - 1_)  str

_static _translate(_context : str_, _key : str_, _disambiguation : Optional[str]_, _n : int = - 1_)  str

_static _wheelScrollLines()  int

_static _widgetAt(_p : PySide6.QtCore.QPoint_)
_static _widgetAt(_x : int_, _y : int_)

_static _windowIcon()  PySide6.QtGui.QIcon