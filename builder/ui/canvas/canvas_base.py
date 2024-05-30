from qtpy import QtCore, QtGui, QtWidgets

from builder.core.common import GetRangePct, lerp


class CanvasBase(QtWidgets.QGraphicsView):
    _mouseWheelZoomRate = 0.0005

    def __init__(self):
        super(CanvasBase, self).__init__()

        # settings
        self.factor = 1
        self._minimum_scale = 0.2
        self._maximum_scale = 3.0

        self.CanvasBgColor = QtGui.QColor(35, 35, 35)
        self.CanvasGridColor = QtGui.QColor(20, 20, 20, 100)
        self.CanvasGridColorDarker = QtGui.QColor(20, 20, 20)
        self.DrawGrid = True
        self.GridSizeFine = 10
        self.GridSizeHuge = 100

        self.LOD_Number = 4
        self.CanvasSwitch = 3

        self.setScene(self.createScene())

    def createScene(self):
        scene = QtWidgets.QGraphicsScene(self)
        scene.setItemIndexMethod(QtWidgets.QGraphicsScene.NoIndex)
        scene.setSceneRect(QtCore.QRectF(0, 0, 10, 10))
        return scene

    def wheelEvent(self, event):
        zoomFactor = 1.0 + event.angleDelta().y() * self._mouseWheelZoomRate

        self.zoom(zoomFactor)

    def zoom(self, scale_factor):
        self.factor = self.transform().m22()
        futureScale = self.factor * scale_factor
        if futureScale <= self._minimum_scale:
            scale_factor = self._minimum_scale / self.factor
        if futureScale >= self._maximum_scale:
            scale_factor = (self._maximum_scale - 0.1) / self.factor
        self.scale(scale_factor, scale_factor)

    def resetScale(self):
        self.resetMatrix()

    def viewMinimumScale(self):
        return self._minimum_scale

    def viewMaximumScale(self):
        return self._maximum_scale

    def currentViewScale(self):
        return self.transform().m22()

    def getLodValueFromScale(self, numLods=5, scale=1.0):
        lod = lerp(
            numLods,
            1,
            GetRangePct(
                self.viewMinimumScale(),
                self.viewMaximumScale(),
                scale,
            ),
        )
        return int(round(lod))

    def getCanvasLodValueFromCurrentScale(self):
        return self.getLodValueFromScale(
            self.LOD_Number,
            self.currentViewScale(),
        )

    def getLodValueFromCurrentScale(self, numLods=5):
        return self.getLodValueFromScale(numLods, self.currentViewScale())

    def drawBackground(self, painter, rect):
        super(CanvasBase, self).drawBackground(painter, rect)
        lod = self.getCanvasLodValueFromCurrentScale()
        self.boundingRect = rect

        painter.fillRect(rect, QtGui.QBrush(self.CanvasBgColor))

        left = int(rect.left()) - (int(rect.left()) % self.GridSizeFine)
        top = int(rect.top()) - (int(rect.top()) % self.GridSizeFine)

        if self.DrawGrid:
            self.draw_background_grid(painter, rect, lod, left, top)

    def draw_background_grid(self, painter, rect, lod, left, top):
        if lod < self.CanvasSwitch:
            # Draw horizontal fine lines
            gridLines = []
            y = float(top)
            while y < float(rect.bottom()):
                gridLines.append(
                    QtCore.QLineF(rect.left(), y, rect.right(), y),
                )
                y += self.GridSizeFine
            painter.setPen(QtGui.QPen(self.CanvasGridColor, 1))
            painter.drawLines(gridLines)

            # Draw vertical fine lines
            gridLines = []
            x = float(left)
            while x < float(rect.right()):
                gridLines.append(
                    QtCore.QLineF(x, rect.top(), x, rect.bottom()),
                )
                x += self.GridSizeFine
            painter.setPen(QtGui.QPen(self.CanvasGridColor, 1))
            painter.drawLines(gridLines)

        # Draw thick grid
        left = int(rect.left()) - (int(rect.left()) % self.GridSizeHuge)
        top = int(rect.top()) - (int(rect.top()) % self.GridSizeHuge)

        # Draw vertical thick lines
        gridLines = []
        painter.setPen(QtGui.QPen(self.CanvasGridColorDarker, 1.5))
        x = left
        while x < rect.right():
            gridLines.append(
                QtCore.QLineF(x, rect.top(), x, rect.bottom()),
            )
            x += self.GridSizeHuge
        painter.drawLines(gridLines)

        # Draw horizontal thick lines
        gridLines = []
        painter.setPen(QtGui.QPen(self.CanvasGridColorDarker, 1.5))
        y = top
        while y < rect.bottom():
            gridLines.append(
                QtCore.QLineF(rect.left(), y, rect.right(), y),
            )
            y += self.GridSizeHuge
        painter.drawLines(gridLines)
