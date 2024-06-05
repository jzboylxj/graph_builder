from qtpy import QtWidgets

from PyGraph.ui.widgets.blueprint_canvas import BlueprintCanvas


class BlueprintCanvasWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.mainLayout = QtWidgets.QVBoxLayout(self)
        self.mainLayout.setObjectName("canvasWidgetMainLayout")
        self.mainLayout.setSpacing(1)
        self.mainLayout.setContentsMargins(1, 1, 1, 1)

        self.setContentsMargins(1, 1, 1, 1)

        self.pathLayout = QtWidgets.QHBoxLayout()
        self.mainLayout.addLayout(self.pathLayout)

        self.compoundPropertiesWidget = QtWidgets.QWidget()
        self.compoundPropertiesWidget.setContentsMargins(1, 1, 1, 1)
        self.compoundPropertiesWidget.setObjectName("compoundPropertiesWidget")
        self.compoundPropertiesLayout = QtWidgets.QHBoxLayout(
            self.compoundPropertiesWidget
        )
        self.compoundPropertiesLayout.setSpacing(1)
        self.compoundPropertiesLayout.setContentsMargins(1, 1, 1, 1)
        self.mainLayout.addWidget(self.compoundPropertiesWidget)

        self.leCompoundName = QtWidgets.QLineEdit()
        self.leCompoundName.setObjectName("leCompoundName")
        self.leCompoundCategory = QtWidgets.QLineEdit()
        self.leCompoundCategory.setObjectName("leCompoundCategory")

        compoundNameLabel = QtWidgets.QLabel("Name:")
        compoundNameLabel.setObjectName("compoundNameLabel")
        self.compoundPropertiesLayout.addWidget(compoundNameLabel)
        self.compoundPropertiesLayout.addWidget(self.leCompoundName)

        compoundCategoryLabel = QtWidgets.QLabel("Category:")
        compoundCategoryLabel.setObjectName("compoundCategoryLabel")
        self.compoundPropertiesLayout.addWidget(compoundCategoryLabel)
        self.compoundPropertiesLayout.addWidget(self.leCompoundCategory)

        self.canvas = BlueprintCanvas()
        self.mainLayout.addWidget(self.canvas)
