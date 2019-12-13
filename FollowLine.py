
import sys, platform
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import math

class MainWindow(QGraphicsView):

    def __init__(self):

        super(MainWindow, self).__init__()
        self.setWindowTitle("PID Control Demo")

        w, h = 1300, 500

        self.scene = QGraphicsScene(self)
        self.scene.setSceneRect(QRectF(0.0, -h / 2.0, w, h))
        self.scene.addLine(0.0, 0.0, float(w), 0.0)
        self.setScene(self.scene)
        self.resize(w, h)

        self.car = self.scene.addPixmap(QPixmap("./images/ico_car.png"))
        self.car.setOffset(-self.car.pixmap().width() / 2, -self.car.pixmap().height() / 2)
        self.car.setPos(0, -200)

        self.errors = []
        self.integral = 0
        self.v = 100.0
        self.dt = 60 / 1000

        self.timer = QTimer(self)
        self.timer.setInterval(self.dt * 1000)
        self.timer.timeout.connect(self.onTimeout)
        self.timer.start()

    def onTimeout(self):

        e = self.car.scenePos().y() / 10
        self.errors.append(e)
        self.integral += e

        if len(self.errors) % 2 == 0:
            itemPoint = self.scene.addRect(QRectF(self.car.scenePos().x() - 1, self.car.scenePos().y() - 1, 2, 2));
            itemPoint.setZValue(-1)

        P = e * -5
        I = -1.0 * self.integral * self.dt
        D = (0 if len(self.errors) < 2 else (self.errors[len(self.errors) - 1] - self.errors[len(self.errors) - 2]) / self.dt) * -5.0
        w = P + I + D
        dw = w * self.dt
        dx = self.v * self.dt
        print("pos=(%d, %d); w = %d" % (self.car.scenePos().x() / 10, self.car.scenePos().y() / 10, w))

        matrix = QTransform()
        matrix.rotate(dw).translate(dx, 0.0)
        self.car.setTransform(matrix, True)
