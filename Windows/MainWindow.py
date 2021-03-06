# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow_lowres.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1137, 746)
        MainWindow.setStyleSheet("background-color: #FFF")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1131, 681))
        self.tabWidget.setObjectName("tabWidget")
        self.tabMain = QtWidgets.QWidget()
        self.tabMain.setObjectName("tabMain")
        self.plotSensor = MplWidget(self.tabMain)
        self.plotSensor.setGeometry(QtCore.QRect(20, 20, 500, 500))
        self.plotSensor.setObjectName("plotSensor")
        self.btnTakeImage = QtWidgets.QPushButton(self.tabMain)
        self.btnTakeImage.setGeometry(QtCore.QRect(10, 550, 171, 61))
        self.btnTakeImage.setStyleSheet("color: #fff;\n"
"background-color: #337ab7;\n"
"border-color: #2e6da4;\n"
"background-image: none;\n"
"border: 1px solid transparent;\n"
"border-radius: 4px;")
        self.btnTakeImage.setObjectName("btnTakeImage")
        self.plotSensor_2 = MplWidget(self.tabMain)
        self.plotSensor_2.setGeometry(QtCore.QRect(590, 20, 500, 500))
        self.plotSensor_2.setObjectName("plotSensor_2")
        self.btnShow = QtWidgets.QPushButton(self.tabMain)
        self.btnShow.setGeometry(QtCore.QRect(590, 550, 171, 61))
        self.btnShow.setStyleSheet("color: #fff;\n"
"background-color: #337ab7;\n"
"border-color: #2e6da4;\n"
"background-image: none;\n"
"border: 1px solid transparent;\n"
"border-radius: 4px;")
        self.btnShow.setObjectName("btnShow")
        self.btnSavePDF = QtWidgets.QPushButton(self.tabMain)
        self.btnSavePDF.setGeometry(QtCore.QRect(770, 550, 171, 61))
        self.btnSavePDF.setStyleSheet("color: #fff;\n"
"background-color: #337ab7;\n"
"border-color: #2e6da4;\n"
"background-image: none;\n"
"border: 1px solid transparent;\n"
"border-radius: 4px;")
        self.btnSavePDF.setObjectName("btnSavePDF")
        self.btnSave_2 = QtWidgets.QPushButton(self.tabMain)
        self.btnSave_2.setGeometry(QtCore.QRect(950, 550, 171, 61))
        self.btnSave_2.setStyleSheet("color: #fff;\n"
"background-color: #337ab7;\n"
"border-color: #2e6da4;\n"
"background-image: none;\n"
"border: 1px solid transparent;\n"
"border-radius: 4px;")
        self.btnSave_2.setObjectName("btnSave_2")
        self.spinBox = QtWidgets.QSpinBox(self.tabMain)
        self.spinBox.setGeometry(QtCore.QRect(590, 620, 71, 24))
        self.spinBox.setMinimum(1)
        self.spinBox.setProperty("value", 6)
        self.spinBox.setObjectName("spinBox")
        self.label_2 = QtWidgets.QLabel(self.tabMain)
        self.label_2.setGeometry(QtCore.QRect(660, 620, 61, 21))
        self.label_2.setObjectName("label_2")
        self.horizontalSlider = QtWidgets.QSlider(self.tabMain)
        self.horizontalSlider.setGeometry(QtCore.QRect(590, 520, 251, 22))
        self.horizontalSlider.setMaximum(1000)
        self.horizontalSlider.setProperty("value", 200)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.btnCreateGrid = QtWidgets.QPushButton(self.tabMain)
        self.btnCreateGrid.setGeometry(QtCore.QRect(190, 550, 171, 61))
        self.btnCreateGrid.setStyleSheet("color: #fff;\n"
"background-color: #337ab7;\n"
"border-color: #2e6da4;\n"
"background-image: none;\n"
"border: 1px solid transparent;\n"
"border-radius: 4px;")
        self.btnCreateGrid.setObjectName("btnCreateGrid")
        self.btnFindSpots = QtWidgets.QPushButton(self.tabMain)
        self.btnFindSpots.setGeometry(QtCore.QRect(370, 550, 171, 61))
        self.btnFindSpots.setStyleSheet("color: #fff;\n"
"background-color: #337ab7;\n"
"border-color: #2e6da4;\n"
"background-image: none;\n"
"border: 1px solid transparent;\n"
"border-radius: 4px;")
        self.btnFindSpots.setObjectName("btnFindSpots")
        self.checkBoxAutomatic = QtWidgets.QCheckBox(self.tabMain)
        self.checkBoxAutomatic.setGeometry(QtCore.QRect(10, 620, 111, 21))
        self.checkBoxAutomatic.setObjectName("checkBoxAutomatic")
        self.tabWidget.addTab(self.tabMain, "")
        self.tabCalibration = QtWidgets.QWidget()
        self.tabCalibration.setObjectName("tabCalibration")
        self.plotAnalyse = MplWidget(self.tabCalibration)
        self.plotAnalyse.setGeometry(QtCore.QRect(20, 10, 500, 500))
        self.plotAnalyse.setObjectName("plotAnalyse")
        self.btnPlotZernike = QtWidgets.QPushButton(self.tabCalibration)
        self.btnPlotZernike.setGeometry(QtCore.QRect(530, 100, 221, 71))
        self.btnPlotZernike.setStyleSheet("color: #fff;\n"
"background-color: #337ab7;\n"
"border-color: #2e6da4;\n"
"cursor: pointer;\n"
"background-image: none;\n"
"border: 1px solid transparent;\n"
"border-radius: 4px;")
        self.btnPlotZernike.setObjectName("btnPlotZernike")
        self.spinNumFoci = QtWidgets.QSpinBox(self.tabCalibration)
        self.spinNumFoci.setGeometry(QtCore.QRect(1270, 30, 111, 31))
        self.spinNumFoci.setObjectName("spinNumFoci")
        self.label = QtWidgets.QLabel(self.tabCalibration)
        self.label.setGeometry(QtCore.QRect(1400, 30, 151, 31))
        self.label.setObjectName("label")
        self.btnFindSpotsCali = QtWidgets.QPushButton(self.tabCalibration)
        self.btnFindSpotsCali.setGeometry(QtCore.QRect(530, 180, 221, 71))
        self.btnFindSpotsCali.setStyleSheet("color: #fff;\n"
"background-color: #337ab7;\n"
"border-color: #2e6da4;\n"
"cursor: pointer;\n"
"background-image: none;\n"
"border: 1px solid transparent;\n"
"border-radius: 4px;")
        self.btnFindSpotsCali.setObjectName("btnFindSpotsCali")
        self.spinBoxSingleZernike = QtWidgets.QSpinBox(self.tabCalibration)
        self.spinBoxSingleZernike.setGeometry(QtCore.QRect(760, 110, 71, 24))
        self.spinBoxSingleZernike.setMinimum(1)
        self.spinBoxSingleZernike.setProperty("value", 6)
        self.spinBoxSingleZernike.setObjectName("spinBoxSingleZernike")
        self.label_3 = QtWidgets.QLabel(self.tabCalibration)
        self.label_3.setGeometry(QtCore.QRect(830, 110, 61, 21))
        self.label_3.setObjectName("label_3")
        self.sliderAnalyse = QtWidgets.QSlider(self.tabCalibration)
        self.sliderAnalyse.setGeometry(QtCore.QRect(30, 520, 251, 22))
        self.sliderAnalyse.setMaximum(1000)
        self.sliderAnalyse.setProperty("value", 200)
        self.sliderAnalyse.setOrientation(QtCore.Qt.Horizontal)
        self.sliderAnalyse.setObjectName("sliderAnalyse")
        self.tabWidget.addTab(self.tabCalibration, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1137, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ZerFit"))
        self.btnTakeImage.setText(_translate("MainWindow", "Take Image"))
        self.btnShow.setText(_translate("MainWindow", "Reconstruct Wavefront"))
        self.btnSavePDF.setText(_translate("MainWindow", "Save PDF"))
        self.btnSave_2.setText(_translate("MainWindow", "Save TXT"))
        self.label_2.setText(_translate("MainWindow", "Order"))
        self.btnCreateGrid.setText(_translate("MainWindow", "Create Grid"))
        self.btnFindSpots.setText(_translate("MainWindow", "Find Spots"))
        self.checkBoxAutomatic.setText(_translate("MainWindow", "Automatic "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabMain), _translate("MainWindow", "Main"))
        self.btnPlotZernike.setText(_translate("MainWindow", "Plot Zernike"))
        self.label.setText(_translate("MainWindow", "Number of Foci"))
        self.btnFindSpotsCali.setText(_translate("MainWindow", "Open Exported TXT"))
        self.label_3.setText(_translate("MainWindow", "Degree"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabCalibration), _translate("MainWindow", "Analyse"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Camera"))

from mplwidget import MplWidget
