from PySide2 import QtCore, QtGui, QtWidgets

from PyGraph import LIGHT_ICONS, initialize
from PyGraph.ui.widgets.blueprint_canvas_widget import BlueprintCanvasWidget


def winTitle():
    return "PyGraph v0.0.5"


class MainWindow(QtWidgets.QMainWindow):

    appInstance = None

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.currentSoftware = ""

        self.canvasWidget = BlueprintCanvasWidget(self)
        self.canvasWidget.setObjectName("canvasWidget")
        self.setCentralWidget(self.canvasWidget)

        self.setWindowTitle(winTitle())

        self.setContentsMargins(1, 1, 1, 1)
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.setTabPosition(
            QtCore.Qt.AllDockWidgetAreas,
            QtWidgets.QTabWidget.North,
        )
        self.setDockOptions(QtWidgets.QMainWindow.AnimatedDocks | QtWidgets.QMainWindow.AllowNestedDocks)

        self.init_menu_bar()
        self.init_tool_bar()

    def init_menu_bar(self):
        self.mainMenuBar = QtWidgets.QMenuBar(self)
        self.mainMenuBar.setGeometry(QtCore.QRect(0, 0, 863, 21))
        self.mainMenuBar.setObjectName("menuBar")
        self.setMenuBar(self.mainMenuBar)

    def init_tool_bar(self):
        self.toolBar = QtWidgets.QToolBar(self)
        self.toolBar.setObjectName("toolBar")
        self.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

    def populateMenu(self):
        fileMenu = self.mainMenuBar.addMenu("File")
        newFileAction = fileMenu.addAction("New file")
        newFileAction.setIcon(QtGui.QIcon(f"{LIGHT_ICONS}/document_add.svg"))
        newFileAction.triggered.connect(self._clickNewFile)

        loadAction = fileMenu.addAction("Load")
        loadAction.setIcon(QtGui.QIcon(f"{LIGHT_ICONS}/folder_open.svg"))
        loadAction.triggered.connect(self._clickLoadFile)

    def _clickNewFile(self):
        print("Click new file action")

    def _clickLoadFile(self):
        print("Click load file action")

    @staticmethod
    def instance(parent=None, software=""):
        assert software != "", "无效参数. 请传递你的软件名作为第二个参数的值！"

        instance = MainWindow(parent)
        instance.currentSoftware = software

        extraPackagePaths = []
        initialize(additionalPackageLocations=extraPackagePaths, software=software)

        # populate menus
        instance.populateMenu()

        MainWindow.appInstance = instance

        return instance
