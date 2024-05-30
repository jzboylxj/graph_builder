from qtpy import QtWidgets


class GraphBuilder(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(GraphBuilder, self).__init__(parent)

        self.setWindowTitle("Graph Builder v0.0.1")
        self.setContentsMargins(1, 1, 1, 1)
