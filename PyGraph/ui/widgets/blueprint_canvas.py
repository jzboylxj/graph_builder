from qtpy import QtCore, QtWidgets

from PyGraph.ui.canvas.canvas_base import CanvasBase


class BlueprintCanvas(CanvasBase):
    def __init__(self):
        super(BlueprintCanvas, self).__init__()
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        self.installEventFilter(self)
