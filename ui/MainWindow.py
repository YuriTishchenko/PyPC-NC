# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(889, 414)
        self.gotoXY = QAction(MainWindow)
        self.gotoXY.setObjectName(u"gotoXY")
        self.gotoXYZ = QAction(MainWindow)
        self.gotoXYZ.setObjectName(u"gotoXYZ")
        self.gotoX = QAction(MainWindow)
        self.gotoX.setObjectName(u"gotoX")
        self.gotoY = QAction(MainWindow)
        self.gotoY.setObjectName(u"gotoY")
        self.gotoZ = QAction(MainWindow)
        self.gotoZ.setObjectName(u"gotoZ")
        self.storeXY = QAction(MainWindow)
        self.storeXY.setObjectName(u"storeXY")
        self.storeXYZ = QAction(MainWindow)
        self.storeXYZ.setObjectName(u"storeXYZ")
        self.storeX = QAction(MainWindow)
        self.storeX.setObjectName(u"storeX")
        self.storeY = QAction(MainWindow)
        self.storeY.setObjectName(u"storeY")
        self.storeZ = QAction(MainWindow)
        self.storeZ.setObjectName(u"storeZ")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(200, 0))
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.labelX = QLabel(self.groupBox)
        self.labelX.setObjectName(u"labelX")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.labelX)

        self.statusX = QLabel(self.groupBox)
        self.statusX.setObjectName(u"statusX")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.statusX)

        self.labelPx = QLabel(self.groupBox)
        self.labelPx.setObjectName(u"labelPx")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.labelPx)

        self.statusPx = QLabel(self.groupBox)
        self.statusPx.setObjectName(u"statusPx")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.statusPx)

        self.labelPy = QLabel(self.groupBox)
        self.labelPy.setObjectName(u"labelPy")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.labelPy)

        self.statusPy = QLabel(self.groupBox)
        self.statusPy.setObjectName(u"statusPy")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.statusPy)

        self.labelPz = QLabel(self.groupBox)
        self.labelPz.setObjectName(u"labelPz")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.labelPz)

        self.statusPz = QLabel(self.groupBox)
        self.statusPz.setObjectName(u"statusPz")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.statusPz)

        self.labelPu = QLabel(self.groupBox)
        self.labelPu.setObjectName(u"labelPu")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.labelPu)

        self.statusPu = QLabel(self.groupBox)
        self.statusPu.setObjectName(u"statusPu")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.statusPu)


        self.verticalLayout_5.addWidget(self.groupBox)

        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.invertZ = QCheckBox(self.groupBox_4)
        self.invertZ.setObjectName(u"invertZ")
        self.invertZ.setChecked(True)

        self.verticalLayout_4.addWidget(self.invertZ)

        self.verticalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_6)

        self.label_2 = QLabel(self.groupBox_4)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_4.addWidget(self.label_2)

        self.feedRateOverride = QSpinBox(self.groupBox_4)
        self.feedRateOverride.setObjectName(u"feedRateOverride")
        self.feedRateOverride.setSuffix(u" %")
        self.feedRateOverride.setMinimum(10)
        self.feedRateOverride.setMaximum(200)
        self.feedRateOverride.setSingleStep(5)
        self.feedRateOverride.setValue(100)

        self.verticalLayout_4.addWidget(self.feedRateOverride)

        self.label_4 = QLabel(self.groupBox_4)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_4.addWidget(self.label_4)

        self.progress = QProgressBar(self.groupBox_4)
        self.progress.setObjectName(u"progress")

        self.verticalLayout_4.addWidget(self.progress)


        self.verticalLayout_5.addWidget(self.groupBox_4)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_5)


        self.horizontalLayout_3.addLayout(self.verticalLayout_5)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(220, 0))
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label = QLabel(self.groupBox_3)
        self.label.setObjectName(u"label")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label)

        self.relX = QLabel(self.groupBox_3)
        self.relX.setObjectName(u"relX")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.relX.sizePolicy().hasHeightForWidth())
        self.relX.setSizePolicy(sizePolicy)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.relX)

        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.relY = QLabel(self.groupBox_3)
        self.relY.setObjectName(u"relY")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.relY)

        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_5)

        self.relZ = QLabel(self.groupBox_3)
        self.relZ.setObjectName(u"relZ")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.relZ)


        self.horizontalLayout_2.addLayout(self.formLayout_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gotoOther = QToolButton(self.groupBox_3)
        self.gotoOther.setObjectName(u"gotoOther")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.gotoOther.sizePolicy().hasHeightForWidth())
        self.gotoOther.setSizePolicy(sizePolicy1)
        self.gotoOther.setMinimumSize(QSize(90, 0))
        self.gotoOther.setPopupMode(QToolButton.InstantPopup)

        self.verticalLayout_2.addWidget(self.gotoOther)

        self.storeOther = QToolButton(self.groupBox_3)
        self.storeOther.setObjectName(u"storeOther")
        sizePolicy1.setHeightForWidth(self.storeOther.sizePolicy().hasHeightForWidth())
        self.storeOther.setSizePolicy(sizePolicy1)
        self.storeOther.setPopupMode(QToolButton.InstantPopup)

        self.verticalLayout_2.addWidget(self.storeOther)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout_3.addWidget(self.groupBox_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.driveDirections = QGridLayout()
        self.driveDirections.setObjectName(u"driveDirections")
        self.driveXDown = QPushButton(self.groupBox_2)
        self.driveXDown.setObjectName(u"driveXDown")
        self.driveXDown.setEnabled(True)
        self.driveXDown.setMinimumSize(QSize(32, 32))
        self.driveXDown.setMaximumSize(QSize(32, 32))

        self.driveDirections.addWidget(self.driveXDown, 1, 0, 1, 1, Qt.AlignRight)

        self.driveXUp = QPushButton(self.groupBox_2)
        self.driveXUp.setObjectName(u"driveXUp")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.driveXUp.sizePolicy().hasHeightForWidth())
        self.driveXUp.setSizePolicy(sizePolicy2)
        self.driveXUp.setMinimumSize(QSize(32, 32))
        self.driveXUp.setMaximumSize(QSize(32, 32))

        self.driveDirections.addWidget(self.driveXUp, 1, 2, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalSpacer = QSpacerItem(32, 32, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.driveDirections.addItem(self.horizontalSpacer, 0, 3, 1, 1)

        self.driveUUp = QPushButton(self.groupBox_2)
        self.driveUUp.setObjectName(u"driveUUp")
        sizePolicy2.setHeightForWidth(self.driveUUp.sizePolicy().hasHeightForWidth())
        self.driveUUp.setSizePolicy(sizePolicy2)
        self.driveUUp.setMinimumSize(QSize(32, 32))
        self.driveUUp.setMaximumSize(QSize(32, 32))

        self.driveDirections.addWidget(self.driveUUp, 3, 4, 1, 1, Qt.AlignTop)

        self.driveUDown = QPushButton(self.groupBox_2)
        self.driveUDown.setObjectName(u"driveUDown")
        sizePolicy2.setHeightForWidth(self.driveUDown.sizePolicy().hasHeightForWidth())
        self.driveUDown.setSizePolicy(sizePolicy2)
        self.driveUDown.setMinimumSize(QSize(32, 32))
        self.driveUDown.setMaximumSize(QSize(32, 32))

        self.driveDirections.addWidget(self.driveUDown, 3, 3, 1, 1, Qt.AlignTop)

        self.fillBelow = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.driveDirections.addItem(self.fillBelow, 4, 3, 1, 1)

        self.driveYUp = QPushButton(self.groupBox_2)
        self.driveYUp.setObjectName(u"driveYUp")
        sizePolicy2.setHeightForWidth(self.driveYUp.sizePolicy().hasHeightForWidth())
        self.driveYUp.setSizePolicy(sizePolicy2)
        self.driveYUp.setMinimumSize(QSize(32, 32))
        self.driveYUp.setMaximumSize(QSize(32, 32))

        self.driveDirections.addWidget(self.driveYUp, 0, 1, 1, 1)

        self.driveYDown = QPushButton(self.groupBox_2)
        self.driveYDown.setObjectName(u"driveYDown")
        sizePolicy2.setHeightForWidth(self.driveYDown.sizePolicy().hasHeightForWidth())
        self.driveYDown.setSizePolicy(sizePolicy2)
        self.driveYDown.setMinimumSize(QSize(32, 32))
        self.driveYDown.setMaximumSize(QSize(32, 32))

        self.driveDirections.addWidget(self.driveYDown, 3, 1, 1, 1)

        self.driveZUp = QPushButton(self.groupBox_2)
        self.driveZUp.setObjectName(u"driveZUp")
        sizePolicy2.setHeightForWidth(self.driveZUp.sizePolicy().hasHeightForWidth())
        self.driveZUp.setSizePolicy(sizePolicy2)
        self.driveZUp.setMinimumSize(QSize(32, 32))
        self.driveZUp.setMaximumSize(QSize(32, 32))

        self.driveDirections.addWidget(self.driveZUp, 1, 4, 1, 1)

        self.driveZDown = QPushButton(self.groupBox_2)
        self.driveZDown.setObjectName(u"driveZDown")
        sizePolicy2.setHeightForWidth(self.driveZDown.sizePolicy().hasHeightForWidth())
        self.driveZDown.setSizePolicy(sizePolicy2)
        self.driveZDown.setMinimumSize(QSize(32, 32))
        self.driveZDown.setMaximumSize(QSize(32, 32))

        self.driveDirections.addWidget(self.driveZDown, 0, 4, 1, 1)


        self.horizontalLayout.addLayout(self.driveDirections)

        self.horizontalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.driveDistance = QVBoxLayout()
        self.driveDistance.setObjectName(u"driveDistance")
        self.drive1Step = QRadioButton(self.groupBox_2)
        self.driveDistanceGroup = QButtonGroup(MainWindow)
        self.driveDistanceGroup.setObjectName(u"driveDistanceGroup")
        self.driveDistanceGroup.addButton(self.drive1Step)
        self.drive1Step.setObjectName(u"drive1Step")
        self.drive1Step.setChecked(True)

        self.driveDistance.addWidget(self.drive1Step)

        self.drive001mm = QRadioButton(self.groupBox_2)
        self.driveDistanceGroup.addButton(self.drive001mm)
        self.drive001mm.setObjectName(u"drive001mm")

        self.driveDistance.addWidget(self.drive001mm)

        self.drive01mm = QRadioButton(self.groupBox_2)
        self.driveDistanceGroup.addButton(self.drive01mm)
        self.drive01mm.setObjectName(u"drive01mm")

        self.driveDistance.addWidget(self.drive01mm)

        self.drive1mm = QRadioButton(self.groupBox_2)
        self.driveDistanceGroup.addButton(self.drive1mm)
        self.drive1mm.setObjectName(u"drive1mm")

        self.driveDistance.addWidget(self.drive1mm)

        self.drive10mm = QRadioButton(self.groupBox_2)
        self.driveDistanceGroup.addButton(self.drive10mm)
        self.drive10mm.setObjectName(u"drive10mm")

        self.driveDistance.addWidget(self.drive10mm)

        self.drive100mm = QRadioButton(self.groupBox_2)
        self.driveDistanceGroup.addButton(self.drive100mm)
        self.drive100mm.setObjectName(u"drive100mm")

        self.driveDistance.addWidget(self.drive100mm)

        self.verticalSpacer_4 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.driveDistance.addItem(self.verticalSpacer_4)


        self.horizontalLayout.addLayout(self.driveDistance)

        self.horizontalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_6)

        self.driveSpeed = QVBoxLayout()
        self.driveSpeed.setObjectName(u"driveSpeed")
        self.driveFast = QRadioButton(self.groupBox_2)
        self.driveSpeedGroup = QButtonGroup(MainWindow)
        self.driveSpeedGroup.setObjectName(u"driveSpeedGroup")
        self.driveSpeedGroup.addButton(self.driveFast)
        self.driveFast.setObjectName(u"driveFast")
        self.driveFast.setChecked(True)

        self.driveSpeed.addWidget(self.driveFast)

        self.driveSlow = QRadioButton(self.groupBox_2)
        self.driveSpeedGroup.addButton(self.driveSlow)
        self.driveSlow.setObjectName(u"driveSlow")

        self.driveSpeed.addWidget(self.driveSlow)

        self.verticalSpacer_2 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.driveSpeed.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addLayout(self.driveSpeed)


        self.verticalLayout_3.addWidget(self.groupBox_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stop = QPushButton(self.centralwidget)
        self.stop.setObjectName(u"stop")
        self.stop.setStyleSheet(u"background-color:red")

        self.verticalLayout.addWidget(self.stop)

        self.refMovement = QPushButton(self.centralwidget)
        self.refMovement.setObjectName(u"refMovement")

        self.verticalLayout.addWidget(self.refMovement)

        self.importGCode = QPushButton(self.centralwidget)
        self.importGCode.setObjectName(u"importGCode")

        self.verticalLayout.addWidget(self.importGCode)

        self.run = QPushButton(self.centralwidget)
        self.run.setObjectName(u"run")

        self.verticalLayout.addWidget(self.run)

        self.resume = QPushButton(self.centralwidget)
        self.resume.setObjectName(u"resume")

        self.verticalLayout.addWidget(self.resume)

        self.showGraphicsView = QPushButton(self.centralwidget)
        self.showGraphicsView.setObjectName(u"showGraphicsView")

        self.verticalLayout.addWidget(self.showGraphicsView)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 889, 25))
        self.menuGoto = QMenu(self.menuBar)
        self.menuGoto.setObjectName(u"menuGoto")
        self.menuStore = QMenu(self.menuBar)
        self.menuStore.setObjectName(u"menuStore")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuGoto.menuAction())
        self.menuBar.addAction(self.menuStore.menuAction())
        self.menuGoto.addAction(self.gotoXY)
        self.menuGoto.addAction(self.gotoXYZ)
        self.menuGoto.addSeparator()
        self.menuGoto.addAction(self.gotoX)
        self.menuGoto.addAction(self.gotoY)
        self.menuGoto.addAction(self.gotoZ)
        self.menuStore.addAction(self.storeXY)
        self.menuStore.addAction(self.storeXYZ)
        self.menuStore.addSeparator()
        self.menuStore.addAction(self.storeX)
        self.menuStore.addAction(self.storeY)
        self.menuStore.addAction(self.storeZ)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PyPC-NC", None))
        self.gotoXY.setText(QCoreApplication.translate("MainWindow", u"Goto XY", None))
        self.gotoXYZ.setText(QCoreApplication.translate("MainWindow", u"Goto XYZ", None))
        self.gotoX.setText(QCoreApplication.translate("MainWindow", u"Goto X", None))
        self.gotoY.setText(QCoreApplication.translate("MainWindow", u"Goto Y", None))
        self.gotoZ.setText(QCoreApplication.translate("MainWindow", u"Goto Z", None))
        self.storeXY.setText(QCoreApplication.translate("MainWindow", u"Store XY", None))
        self.storeXYZ.setText(QCoreApplication.translate("MainWindow", u"Store XYZ", None))
        self.storeX.setText(QCoreApplication.translate("MainWindow", u"Store X", None))
        self.storeY.setText(QCoreApplication.translate("MainWindow", u"Store Y", None))
        self.storeZ.setText(QCoreApplication.translate("MainWindow", u"Store Z", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Status Info", None))
        self.labelX.setText(QCoreApplication.translate("MainWindow", u"@X", None))
        self.statusX.setText(QCoreApplication.translate("MainWindow", u"04 (ready)", None))
        self.labelPx.setText(QCoreApplication.translate("MainWindow", u"@PX", None))
        self.statusPx.setText(QCoreApplication.translate("MainWindow", u"123", None))
        self.labelPy.setText(QCoreApplication.translate("MainWindow", u"@PY", None))
        self.statusPy.setText(QCoreApplication.translate("MainWindow", u"123", None))
        self.labelPz.setText(QCoreApplication.translate("MainWindow", u"@PZ", None))
        self.statusPz.setText(QCoreApplication.translate("MainWindow", u"123", None))
        self.labelPu.setText(QCoreApplication.translate("MainWindow", u"@PU", None))
        self.statusPu.setText(QCoreApplication.translate("MainWindow", u"123", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Options", None))
        self.invertZ.setText(QCoreApplication.translate("MainWindow", u"Invert Z-axis", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Feed rate override", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Work progress", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Workpiece Relative Location", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.relX.setText(QCoreApplication.translate("MainWindow", u"123", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.relY.setText(QCoreApplication.translate("MainWindow", u"123", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.relZ.setText(QCoreApplication.translate("MainWindow", u"123", None))
        self.gotoOther.setText(QCoreApplication.translate("MainWindow", u"Goto ...", None))
        self.storeOther.setText(QCoreApplication.translate("MainWindow", u"Store ...", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Manual Movement", None))
        self.driveXDown.setText(QCoreApplication.translate("MainWindow", u"X-", None))
        self.driveXUp.setText(QCoreApplication.translate("MainWindow", u"X+", None))
        self.driveUUp.setText(QCoreApplication.translate("MainWindow", u"U+", None))
        self.driveUDown.setText(QCoreApplication.translate("MainWindow", u"U-", None))
        self.driveYUp.setText(QCoreApplication.translate("MainWindow", u"Y+", None))
        self.driveYDown.setText(QCoreApplication.translate("MainWindow", u"Y-", None))
        self.driveZUp.setText(QCoreApplication.translate("MainWindow", u"Z+", None))
        self.driveZDown.setText(QCoreApplication.translate("MainWindow", u"Z-", None))
        self.drive1Step.setText(QCoreApplication.translate("MainWindow", u"1 Step", None))
        self.drive001mm.setText(QCoreApplication.translate("MainWindow", u"0.01 mm", None))
        self.drive01mm.setText(QCoreApplication.translate("MainWindow", u"0.1 mm", None))
        self.drive1mm.setText(QCoreApplication.translate("MainWindow", u"1 mm", None))
        self.drive10mm.setText(QCoreApplication.translate("MainWindow", u"10 mm", None))
        self.drive100mm.setText(QCoreApplication.translate("MainWindow", u"100 mm", None))
        self.driveFast.setText(QCoreApplication.translate("MainWindow", u"fast", None))
        self.driveSlow.setText(QCoreApplication.translate("MainWindow", u"slow", None))
        self.stop.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
        self.refMovement.setText(QCoreApplication.translate("MainWindow", u"Ref. Movement", None))
        self.importGCode.setText(QCoreApplication.translate("MainWindow", u"Import G-Code ...", None))
        self.run.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.resume.setText(QCoreApplication.translate("MainWindow", u"Continue", None))
        self.showGraphicsView.setText(QCoreApplication.translate("MainWindow", u"Graphics View ...", None))
        self.menuGoto.setTitle(QCoreApplication.translate("MainWindow", u"Goto", None))
        self.menuStore.setTitle(QCoreApplication.translate("MainWindow", u"Store", None))
    # retranslateUi

