# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GraphicsView.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Control.GraphicsView import MyGraphicsView


class Ui_GraphicsViewWindow(object):
    def setupUi(self, GraphicsViewWindow):
        if not GraphicsViewWindow.objectName():
            GraphicsViewWindow.setObjectName(u"GraphicsViewWindow")
        GraphicsViewWindow.resize(699, 387)
        self.verticalLayout = QVBoxLayout(GraphicsViewWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.graphicsView = MyGraphicsView(GraphicsViewWindow)
        self.graphicsView.setObjectName(u"graphicsView")

        self.verticalLayout.addWidget(self.graphicsView)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.markOrigin = QPushButton(GraphicsViewWindow)
        self.markOrigin.setObjectName(u"markOrigin")

        self.horizontalLayout.addWidget(self.markOrigin)

        self.gotoXY = QPushButton(GraphicsViewWindow)
        self.gotoXY.setObjectName(u"gotoXY")

        self.horizontalLayout.addWidget(self.gotoXY)

        self.polarFixXY = QPushButton(GraphicsViewWindow)
        self.polarFixXY.setObjectName(u"polarFixXY")

        self.horizontalLayout.addWidget(self.polarFixXY)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.closeButton = QPushButton(GraphicsViewWindow)
        self.closeButton.setObjectName(u"closeButton")

        self.horizontalLayout.addWidget(self.closeButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(GraphicsViewWindow)

        QMetaObject.connectSlotsByName(GraphicsViewWindow)
    # setupUi

    def retranslateUi(self, GraphicsViewWindow):
        GraphicsViewWindow.setWindowTitle(QCoreApplication.translate("GraphicsViewWindow", u"PyPC-NC Graphics View", None))
        self.markOrigin.setText(QCoreApplication.translate("GraphicsViewWindow", u"Mark Origin", None))
        self.gotoXY.setText(QCoreApplication.translate("GraphicsViewWindow", u"Goto XY", None))
        self.polarFixXY.setText(QCoreApplication.translate("GraphicsViewWindow", u"Polar Fix XY", None))
        self.closeButton.setText(QCoreApplication.translate("GraphicsViewWindow", u"&Close", None))
    # retranslateUi

