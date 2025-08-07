# nukescripts.panels.registerWidgetAsPanel
nukescripts.panels.registerWidgetAsPanel(_widget_ , _name_ , _id_ , _create_)

Wraps and registers a widget to be used in a Nuke panel.
widget - should be a string of the class for the widget name - is is the name as it will appear on the Pane menu id - should the the unique ID for this widget panel create - if this is set to true a new NukePanel will be returned that wraps this widget
Example ( using PySide6 )
import nuke from PySide6 import QtCore, QtWidgets from nukescripts import panels
class NukeTestWindow( QtWidgets.QWidget ):

def __init__(self, parent=None):

QtWidgets.QWidget.__init__(self, parent) self.setLayout( QtWidgets.QVBoxLayout() )
self.myTable = QtWidgets.QTableWidget() headers = [‘Date’, ‘Files’, ‘Size’, ‘Path’ ] self.myTable.setColumnCount( len( headers ) ) self.myTable.setHorizontalHeaderLabels( headers ) self.layout().addWidget( self.myTable )
nukescripts.registerWidgetAsPanel(‘NukeTestWindow’, ‘NukeTestWindow’, ‘uk.co.thefoundry.NukeTestWindow’ )