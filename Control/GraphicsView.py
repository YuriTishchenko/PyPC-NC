import math
from PySide2 import QtCore, QtGui, QtWidgets


class ControlGraphicsView(QtWidgets.QDialog):
    closed = QtCore.Signal()

    def __init__(self, mainwin, machine):
        self._mainwin = mainwin
        self._machine = machine

        super(ControlGraphicsView, self).__init__(None)

        self._ui = Ui_GraphicsViewWindow()
        self._ui.setupUi(self)

        self._ui.markOrigin.clicked.connect(self.markOrigin)
        self._ui.gotoXY.clicked.connect(self.gotoXY)
        self._ui.polarFixXY.clicked.connect(self.polarFixXY)
        self._ui.closeButton.clicked.connect(self.close)

    @QtCore.Slot()
    def markOrigin(self):
        (x, y) = self._scene.getCursorPosition()
        self._scene.setCrosshairPosition(x, y)
        self._mainwin.setOriginOffset(x, y)

    @QtCore.Slot()
    def gotoXY(self):
        if isinstance(self._machine.action(), ProgrammedMotionController):
            return
        elif not isinstance(self._machine.action(), ManualMotionController):
            self._machine.setAction(ManualMotionController(self._machine))

        (posX, posY) = self._scene.getCursorPosition()
        (orgX, orgY) = self._scene.getCrosshairPosition()

        (posR, posPhi) = toPolar(posX - orgX, posY - orgY)
        (r, deltaPhi) = self._mainwin.polarCorrection()
        (posX, posY) = fromPolar(posR * r, posPhi + deltaPhi)

        workpiecePos = self._mainwin.workpiecePos()
        self._machine.action().gotoXYZ(posX + workpiecePos[0], posY + workpiecePos[1])

    @QtCore.Slot()
    def polarFixXY(self):
        (orgX, orgY) = self._scene.getCrosshairPosition()
        (posX, posY) = self._scene.getCursorPosition()
        (r1, phi1) = toPolar(posX - orgX, posY - orgY)

        workpiecePos = self._mainwin.workpiecePos()
        posX = self._machine.machineStatus().x() - workpiecePos[0] + orgX
        posY = self._machine.machineStatus().y() - workpiecePos[1] + orgY
        (r2, phi2) = toPolar(posX - orgX, posY - orgY)
        self._mainwin.setPolarCorrection(r2 / r1, phi2 - phi1)

    def closeEvent(self, event):
        self.closed.emit()
        event.accept()

    def render(self, parser):
        self._scene = MyGraphicsScene()

        renderer = SceneRenderer(self._scene)
        renderer.render(parser)

        self._ui.graphicsView.setScene(self._scene)

        bbox = self._scene.itemsBoundingRect()
        bbox.setTop(bbox.top() - bbox.height() * 0.1)
        bbox.setBottom(bbox.bottom() + bbox.height() * 0.1)
        bbox.setLeft(bbox.left() - bbox.width() * 0.1)
        bbox.setRight(bbox.right() + bbox.width() * 0.1)
        self._scene.setSceneRect(bbox)
        self._ui.graphicsView.fitInView(bbox, QtCore.Qt.KeepAspectRatio)
        self._ui.graphicsView.autoconfSizes()  # @fixme wait for initial resize


class MyGraphicsScene(QtWidgets.QGraphicsScene):
    def __init__(self):
        super(MyGraphicsScene, self).__init__()

        pen = QtGui.QPen(QtCore.Qt.GlobalColor.blue)
        self._crossHairV = self.addLine(0, 0, 0, 0, pen)
        self._crossHairH = self.addLine(0, 0, 0, 0, pen)

        pen = QtGui.QPen(QtCore.Qt.GlobalColor.red)
        brush = QtGui.QBrush(QtCore.Qt.GlobalColor.red)
        self._cursor = self.addEllipse(0, 0, 0, 0, pen, brush)

    def mousePressEvent(self, event):
        super(MyGraphicsScene, self).mousePressEvent(event)
        self._mousePressPos = event.screenPos()

    def mouseReleaseEvent(self, event):
        super(MyGraphicsScene, self).mouseReleaseEvent(event)
        if event.button() != QtCore.Qt.LeftButton: return
        if self._mousePressPos.x() != event.screenPos().x(): return
        if self._mousePressPos.y() != event.screenPos().y(): return

        clickPos = event.buttonDownScenePos(QtCore.Qt.LeftButton)
        items = self.items(clickPos.x() - 1000, clickPos.y() - 1000, 2000, 2000, QtCore.Qt.IntersectsItemShape)
        if not len(items): return

        maxDist = None
        selPos = None
        for item in items:
            if isinstance(item, QtGui.QGraphicsLineItem):
                points = [item.line().p1(), item.line().p2()]
            elif isinstance(item, ClickableEllipseItem):
                points = item.points()
            else:
                continue

            for point in points:
                dist = math.sqrt((point.x() - clickPos.x()) ** 2 + (point.y() - clickPos.y()) ** 2)

                if maxDist == None or dist < maxDist:
                    maxDist = dist
                    selPos = point

        self.setCursorPosition(selPos.x(), -selPos.y())

    def setCursorPosition(self, x, y):
        d = self._cursor.rect().width()
        self._cursor.setRect(x - d / 2, -y - d / 2, d, d)

    def getCursorPosition(self):
        oldr = self._cursor.rect().width() / 2
        return (self._cursor.rect().x() + oldr, -(self._cursor.rect().y() + oldr))

    def setCursorRadius(self, newr):
        oldr = self._cursor.rect().width() / 2
        x = self._cursor.rect().x() + oldr
        y = self._cursor.rect().y() + oldr
        self._cursor.setRect(x - newr, y - newr, newr * 2, newr * 2)

    def setCrosshairPosition(self, x, y):
        newr = self._crossHairH.line().dx() / 2
        self._crossHairH.setLine(x - newr, -y, x + newr, -y)
        self._crossHairV.setLine(x, -y - newr, x, -y + newr)

    def getCrosshairPosition(self):
        r = self._crossHairH.line().dx() / 2
        return (self._crossHairH.line().x1() + r, -(self._crossHairV.line().y1() + r))

    def setCrosshairSize(self, newr, linew):
        oldr = self._crossHairH.line().dx() / 2
        x = self._crossHairH.line().x1() + oldr
        y = self._crossHairV.line().y1() + oldr

        pen = QtGui.QPen(QtCore.Qt.GlobalColor.blue)
        pen.setWidth(linew)

        self._crossHairH.setLine(x - newr, y, x + newr, y)
        self._crossHairH.setPen(pen)
        self._crossHairV.setLine(x, y - newr, x, y + newr)
        self._crossHairV.setPen(pen)


class MyGraphicsView(QtWidgets.QGraphicsView):
    def __init__(self, parent):
        super(MyGraphicsView, self).__init__(parent)

    def mousePressEvent(self, event):
        self.setDragMode(QtGui.QGraphicsView.ScrollHandDrag)
        super(MyGraphicsView, self).mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        self.setDragMode(QtGui.QGraphicsView.NoDrag)
        super(MyGraphicsView, self).mouseReleaseEvent(event)

    def wheelEvent(self, event):
        factor = 1.2;
        if event.delta() < 0:
            factor = 1.0 / factor
        self.scale(factor, factor)
        self.autoconfSizes()

    def autoconfSizes(self):
        bbox = self.mapToScene(self.viewport().geometry()).boundingRect()
        r = 4 * bbox.width() / self.rect().width()
        self.scene().setCursorRadius(r)

        r = 20 * bbox.width() / self.rect().width()
        lw = 3 * bbox.width() / self.rect().width()
        self.scene().setCrosshairSize(r, lw)


class ClickableEllipseItem(QtWidgets.QGraphicsEllipseItem):
    _points = []

    def addPoint(self, point):
        self._points.append(point)

    def points(self):
        return self._points


class ClickableArcItem(ClickableEllipseItem):
    def __init__(self, x, y, w, h, parent=None):
        super(ClickableArcItem, self).__init__(x, y, w, h, parent)

    def paint(self, painter, option, widget):
        painter.setPen(self.pen())
        painter.setBrush(self.brush())
        painter.drawArc(self.rect(), self.startAngle(), self.spanAngle())


class SceneRenderer:
    axes = ['X', 'Y', 'Z']
    _x = 0
    _y = 0

    def __init__(self, scene):
        self._scene = scene

    def appendPreamble(self):
        pass

    def appendPostamble(self):
        pass

    def setFeedRate(self, fr):
        pass

    def setSpindleSpeed(self, speed):
        pass

    def appendEmptyStep(self):
        pass

    def setCoolantMist(self):
        pass

    def setCoolantOff(self):
        pass

    def setSpindleConfig(self, spindleCCW, spindleEnable, speed):
        pass

    def setSpeed(self, rapid):
        pass

    def render(self, parser):
        self._inter = GCode.GCodeInterpreter(self)
        self._inter.offsets = [0, 0, 0]
        self._inter.position = [0, 0, 0]
        self._inter.incrPosition = [0, 0, 0]
        self._inter.run(parser)

        while not self._inter.end:
            self._inter.resume(parser)

    def currentToolPen(self):
        tool = self._inter.currentTool

        if tool == 2:
            color = QtCore.Qt.GlobalColor.blue
        elif tool == 3:
            color = QtCore.Qt.GlobalColor.cyan
        elif tool == 4:
            color = QtCore.Qt.GlobalColor.green
        elif tool == 5:
            color = QtCore.Qt.GlobalColor.magenta
        elif tool == 6:
            color = QtCore.Qt.GlobalColor.red
        elif tool == 7:
            color = QtCore.Qt.GlobalColor.yellow
        elif tool == 8:
            color = QtCore.Qt.GlobalColor.lightGray
        elif tool == 9:
            color = QtCore.Qt.GlobalColor.darkYellow
        else:
            color = QtCore.Qt.GlobalColor.black

        return QtGui.QPen(color)

    def straightMotion(self, rapid, longMoveAxe, machinePos):
        newx = self._x if machinePos[0] == None else machinePos[0]
        newy = self._y if machinePos[1] == None else machinePos[1]

        if not rapid:
            if self._x == newx and self._y == newy:
                e = ClickableEllipseItem(newx - 250, -newy - 250, 500, 500)
                e.setPen(QtGui.QPen(QtCore.Qt.GlobalColor.magenta))
                e.addPoint(QtCore.QPointF(newx, -newy))
                self._scene.addItem(e)
            else:
                self._scene.addLine(self._x, -self._y, newx, -newy, self.currentToolPen())

        self._x = newx
        self._y = newy

    def circleMotion(self, x, y, p):
        # x and y is the relative position of the circle center relative to _lastPos.
        centerX = self._x + x
        centerY = self._y + y

        (radius, phi) = toPolar(-x, -y)
        (newX, newY) = fromPolar(radius, phi + p / 1000000)

        phi = (phi + math.pi * 2) % (math.pi * 2)
        # phi = 0 -> right; ccw up to math.pi * 2
        # p is radiansE6

        e = ClickableArcItem(centerX - radius, -centerY - radius, 2 * radius, 2 * radius)
        e.setSpanAngle(p * 360 * 16 / math.pi / 2 / 1000000)
        e.setStartAngle(phi * 360 * 16 / math.pi / 2)
        e.setPen(self.currentToolPen())
        e.addPoint(QtCore.QPointF(self._x, -self._y))
        e.addPoint(QtCore.QPointF(newX + centerX, -(newY + centerY)))

        self._x = newX + centerX
        self._y = newY + centerY

        self._scene.addItem(e)


from ui.GraphicsView import Ui_GraphicsViewWindow
from Converters import GCode
from Control.MachineStatus import *
from util.polar import *
