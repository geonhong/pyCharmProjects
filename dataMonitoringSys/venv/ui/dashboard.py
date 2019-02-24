# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dashboard.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import serial
import threading
import time
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class dashboard(object):
    date_ = []
    weight_ = []

    def __init__(self, portname):
        self.portname = portname

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1080, 720)

        self.pane_menu = QtWidgets.QFrame(Dialog)
        self.pane_menu.setGeometry(QtCore.QRect(0, 0, 250, 720))
        self.pane_menu.setStyleSheet("background-color: rgb(61, 66, 78);")
        self.pane_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pane_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pane_menu.setObjectName("pane_menu")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.pane_menu)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 30, 251, 191))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.menu_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.menu_layout.setContentsMargins(20, 0, 0, 0)
        self.menu_layout.setObjectName("menu_layout")
        self.l_menu_overview = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.l_menu_overview.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 18pt \"Helvetica Neue\";")
        self.l_menu_overview.setObjectName("l_menu_overview")
        self.menu_layout.addWidget(self.l_menu_overview)
        self.l_menu_environment = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.l_menu_environment.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 18pt \"Helvetica Neue\";")
        self.l_menu_environment.setObjectName("l_menu_environment")
        self.menu_layout.addWidget(self.l_menu_environment)
        self.l_menu_growth = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.l_menu_growth.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 18pt \"Helvetica Neue\";")
        self.l_menu_growth.setObjectName("l_menu_growth")
        self.menu_layout.addWidget(self.l_menu_growth)
        self.l_menu_activity = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.l_menu_activity.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 18pt \"Helvetica Neue\";")
        self.l_menu_activity.setObjectName("l_menu_activity")
        self.menu_layout.addWidget(self.l_menu_activity)

        self.pane_data = QtWidgets.QFrame(Dialog)
        self.pane_data.setGeometry(QtCore.QRect(250, 0, 830, 720))
        self.pane_data.setStyleSheet("background-color:white")
        self.pane_data.setFrameShape(QtWidgets.QFrame.StyledPanel)

        self.label_growthData = QtWidgets.QLabel(self.pane_data)
        self.label_growthData.setGeometry(QtCore.QRect(30, 30, 200, 30))
        self.label_growthData.setStyleSheet("font: 75 24pt \"Helvetica Neue\";")
        self.label_growthData.setObjectName("label_growthData")

        #self.growthDataViewer = QtWidgets.QGraphicsView(self.pane_data)
        #self.growthDataViewer.setGeometry(QtCore.QRect(30, 60, 780, 200))
        #self.growthDataViewer.setFrameShape(QtWidgets.QFrame.Box)
        #self.growthDataViewer.setFrameShadow(QtWidgets.QFrame.Plain)
        #self.growthDataViewer.setLineWidth(0)
        #self.growthDataViewer.setObjectName("growthDataViewer")
        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)
        self.layoutWidget = QtWidgets.QWidget(self.pane_data)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 60, 780, 200))
        self.layoutWidget.setObjectName("layoutWidget")
        self.layout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.layout.setContentsMargins(20, 0, 0, 0)
        self.layout.setObjectName("layout")
        self.layout.addWidget(self.canvas)

        self.frame = QtWidgets.QFrame(self.pane_data)
        self.frame.setGeometry(QtCore.QRect(30, 280, 240, 160))
        self.frame.setStyleSheet("background-color: rgb(249, 120, 113);")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(-1)
        self.frame.setObjectName("frame")
        self.title_DATE = QtWidgets.QLabel(self.frame)
        self.title_DATE.setGeometry(QtCore.QRect(0, 10, 240, 40))
        font = QtGui.QFont()
        font.setFamily("NanumSquare")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.title_DATE.setFont(font)
        self.title_DATE.setStyleSheet("color: rgb(255, 255, 255);")
        self.title_DATE.setAlignment(QtCore.Qt.AlignCenter)
        self.title_DATE.setObjectName("title_DATE")
        self.separator_DATE = QtWidgets.QFrame(self.frame)
        self.separator_DATE.setGeometry(QtCore.QRect(20, 50, 200, 20))
        self.separator_DATE.setStyleSheet("color: rgb(255, 255, 255);")
        self.separator_DATE.setFrameShadow(QtWidgets.QFrame.Plain)
        self.separator_DATE.setLineWidth(2)
        self.separator_DATE.setMidLineWidth(0)
        self.separator_DATE.setFrameShape(QtWidgets.QFrame.HLine)
        self.separator_DATE.setObjectName("separator_DATE")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 70, 220, 80))
        font = QtGui.QFont()
        font.setFamily("NanumSquare")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(self.pane_data)
        self.frame_2.setGeometry(QtCore.QRect(300, 280, 240, 160))
        self.frame_2.setStyleSheet("background-color:rgb(114,202,200)")
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.title_DATE_2 = QtWidgets.QLabel(self.frame_2)
        self.title_DATE_2.setGeometry(QtCore.QRect(0, 10, 240, 40))
        font = QtGui.QFont()
        font.setFamily("NanumSquare")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.title_DATE_2.setFont(font)
        self.title_DATE_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.title_DATE_2.setAlignment(QtCore.Qt.AlignCenter)
        self.title_DATE_2.setObjectName("title_DATE_2")
        self.separator_DATE_2 = QtWidgets.QFrame(self.frame_2)
        self.separator_DATE_2.setGeometry(QtCore.QRect(20, 50, 200, 20))
        self.separator_DATE_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.separator_DATE_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.separator_DATE_2.setLineWidth(2)
        self.separator_DATE_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.separator_DATE_2.setObjectName("separator_DATE_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 220, 80))
        font = QtGui.QFont()
        font.setFamily("NanumSquare")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.frame_3 = QtWidgets.QFrame(self.pane_data)
        self.frame_3.setGeometry(QtCore.QRect(570, 280, 240, 160))
        self.frame_3.setStyleSheet("background-color: rgb(253,188,95)")
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setObjectName("frame_3")
        self.title_DATE_3 = QtWidgets.QLabel(self.frame_3)
        self.title_DATE_3.setGeometry(QtCore.QRect(0, 10, 240, 40))
        font = QtGui.QFont()
        font.setFamily("NanumSquare")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.title_DATE_3.setFont(font)
        self.title_DATE_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.title_DATE_3.setAlignment(QtCore.Qt.AlignCenter)
        self.title_DATE_3.setObjectName("title_DATE_3")
        self.separator_DATE_3 = QtWidgets.QFrame(self.frame_3)
        self.separator_DATE_3.setGeometry(QtCore.QRect(20, 50, 200, 20))
        self.separator_DATE_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.separator_DATE_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.separator_DATE_3.setLineWidth(2)
        self.separator_DATE_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.separator_DATE_3.setObjectName("separator_DATE_3")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 220, 80))
        font = QtGui.QFont()
        font.setFamily("NanumSquare")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.frame_4 = QtWidgets.QFrame(self.pane_data)
        self.frame_4.setGeometry(QtCore.QRect(30, 460, 780, 240))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.pressure_T01 = QtWidgets.QFrame(self.frame_4)
        self.pressure_T01.setGeometry(QtCore.QRect(0, 0, 52, 80))
        self.pressure_T01.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pressure_T01.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pressure_T01.setObjectName("pressure_T01")
        self.pressure_T02 = QtWidgets.QFrame(self.frame_4)
        self.pressure_T02.setGeometry(QtCore.QRect(52, 0, 52, 80))
        self.pressure_T02.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pressure_T02.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pressure_T02.setObjectName("pressure_T02")
        self.pressure_T03 = QtWidgets.QFrame(self.frame_4)
        self.pressure_T03.setGeometry(QtCore.QRect(104, 0, 52, 80))
        self.pressure_T03.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pressure_T03.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pressure_T03.setObjectName("pressure_T03")
        self.pressure_T04 = QtWidgets.QFrame(self.frame_4)
        self.pressure_T04.setGeometry(QtCore.QRect(156, 0, 52, 80))
        self.pressure_T04.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pressure_T04.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pressure_T04.setObjectName("pressure_T04")
        self.pressure_T05 = QtWidgets.QFrame(self.frame_4)
        self.pressure_T05.setGeometry(QtCore.QRect(208, 0, 52, 80))
        self.pressure_T05.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pressure_T05.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pressure_T05.setObjectName("pressure_T05")
        self.pressure_T06 = QtWidgets.QFrame(self.frame_4)
        self.pressure_T06.setGeometry(QtCore.QRect(260, 0, 52, 80))
        self.pressure_T06.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pressure_T06.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pressure_T06.setObjectName("pressure_T06")
        self.pressure_T07 = QtWidgets.QFrame(self.frame_4)
        self.pressure_T07.setGeometry(QtCore.QRect(312, 0, 52, 80))
        self.pressure_T07.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pressure_T07.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pressure_T07.setObjectName("pressure_T07")
        self.pressure_T08 = QtWidgets.QFrame(self.frame_4)
        self.pressure_T08.setGeometry(QtCore.QRect(364, 0, 52, 80))
        self.pressure_T08.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pressure_T08.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pressure_T08.setObjectName("pressure_T08")
        self.pressure_T09 = QtWidgets.QFrame(self.frame_4)
        self.pressure_T09.setGeometry(QtCore.QRect(416, 0, 52, 80))
        self.pressure_T09.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pressure_T09.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pressure_T09.setObjectName("pressure_T09")
        self.pressure_T10 = QtWidgets.QFrame(self.frame_4)
        self.pressure_T10.setGeometry(QtCore.QRect(468, 0, 52, 80))
        self.pressure_T10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pressure_T10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pressure_T10.setObjectName("pressure_T10")
        self.pressure_T11 = QtWidgets.QFrame(self.frame_4)
        self.pressure_T11.setGeometry(QtCore.QRect(520, 0, 52, 80))
        self.pressure_T11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pressure_T11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pressure_T11.setObjectName("pressure_T11")
        self.pressure_T12 = QtWidgets.QFrame(self.frame_4)
        self.pressure_T12.setGeometry(QtCore.QRect(572, 0, 52, 80))
        self.pressure_T12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pressure_T12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pressure_T12.setObjectName("pressure_T12")
        self.pressure_T13 = QtWidgets.QFrame(self.frame_4)
        self.pressure_T13.setGeometry(QtCore.QRect(624, 0, 52, 80))
        self.pressure_T13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pressure_T13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pressure_T13.setObjectName("pressure_T13")
        self.pressure_T14 = QtWidgets.QFrame(self.frame_4)
        self.pressure_T14.setGeometry(QtCore.QRect(676, 0, 52, 80))
        self.pressure_T14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pressure_T14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pressure_T14.setObjectName("pressure_T14")
        self.pressure_T15 = QtWidgets.QFrame(self.frame_4)
        self.pressure_T15.setGeometry(QtCore.QRect(728, 0, 52, 80))
        self.pressure_T15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pressure_T15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pressure_T15.setObjectName("pressure_T15")
        self.pressure_M06 = QtWidgets.QFrame(self.frame_4)
        self.pressure_M06.setGeometry(QtCore.QRect(260, 80, 52, 80))
        self.pressure_M06.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pressure_M06.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pressure_M06.setObjectName("pressure_M06")
        self.pressure_M02 = QtWidgets.QFrame(self.frame_4)
        self.pressure_M02.setGeometry(QtCore.QRect(52, 80, 52, 80))
        self.pressure_M02.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pressure_M02.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pressure_M02.setObjectName("pressure_M02")
        self.pressure_M08 = QtWidgets.QFrame(self.frame_4)
        self.pressure_M08.setGeometry(QtCore.QRect(364, 80, 52, 80))
        self.pressure_M08.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pressure_M08.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pressure_M08.setObjectName("pressure_M08")
        self.pressure_M11 = QtWidgets.QFrame(self.frame_4)
        self.pressure_M11.setGeometry(QtCore.QRect(520, 80, 52, 80))
        self.pressure_M11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pressure_M11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pressure_M11.setObjectName("pressure_M11")
        self.pressure_M12 = QtWidgets.QFrame(self.frame_4)
        self.pressure_M12.setGeometry(QtCore.QRect(572, 80, 52, 80))
        self.pressure_M12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pressure_M12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pressure_M12.setObjectName("pressure_M12")
        self.pressure_M07 = QtWidgets.QFrame(self.frame_4)
        self.pressure_M07.setGeometry(QtCore.QRect(312, 80, 52, 80))
        self.pressure_M07.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pressure_M07.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pressure_M07.setObjectName("pressure_M07")
        self.pressure_M15 = QtWidgets.QFrame(self.frame_4)
        self.pressure_M15.setGeometry(QtCore.QRect(728, 80, 52, 80))
        self.pressure_M15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pressure_M15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pressure_M15.setObjectName("pressure_M15")
        self.pressure_M14 = QtWidgets.QFrame(self.frame_4)
        self.pressure_M14.setGeometry(QtCore.QRect(676, 80, 52, 80))
        self.pressure_M14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pressure_M14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pressure_M14.setObjectName("pressure_M14")
        self.pressure_M05 = QtWidgets.QFrame(self.frame_4)
        self.pressure_M05.setGeometry(QtCore.QRect(208, 80, 52, 80))
        self.pressure_M05.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pressure_M05.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pressure_M05.setObjectName("pressure_M05")
        self.pressure_M01 = QtWidgets.QFrame(self.frame_4)
        self.pressure_M01.setGeometry(QtCore.QRect(0, 80, 52, 80))
        self.pressure_M01.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pressure_M01.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pressure_M01.setObjectName("pressure_M01")
        self.pressure_M13 = QtWidgets.QFrame(self.frame_4)
        self.pressure_M13.setGeometry(QtCore.QRect(624, 80, 52, 80))
        self.pressure_M13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pressure_M13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pressure_M13.setObjectName("pressure_M13")
        self.pressure_M10 = QtWidgets.QFrame(self.frame_4)
        self.pressure_M10.setGeometry(QtCore.QRect(468, 80, 52, 80))
        self.pressure_M10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pressure_M10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pressure_M10.setObjectName("pressure_M10")
        self.pressure_M04 = QtWidgets.QFrame(self.frame_4)
        self.pressure_M04.setGeometry(QtCore.QRect(156, 80, 52, 80))
        self.pressure_M04.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pressure_M04.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pressure_M04.setObjectName("pressure_M04")
        self.pressure_M03 = QtWidgets.QFrame(self.frame_4)
        self.pressure_M03.setGeometry(QtCore.QRect(104, 80, 52, 80))
        self.pressure_M03.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pressure_M03.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pressure_M03.setObjectName("pressure_M03")
        self.pressure_M09 = QtWidgets.QFrame(self.frame_4)
        self.pressure_M09.setGeometry(QtCore.QRect(416, 80, 52, 80))
        self.pressure_M09.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pressure_M09.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pressure_M09.setObjectName("pressure_M09")
        self.pressure_B13 = QtWidgets.QFrame(self.frame_4)
        self.pressure_B13.setGeometry(QtCore.QRect(624, 160, 52, 80))
        self.pressure_B13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pressure_B13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pressure_B13.setObjectName("pressure_B13")
        self.pressure_B05 = QtWidgets.QFrame(self.frame_4)
        self.pressure_B05.setGeometry(QtCore.QRect(208, 160, 52, 80))
        self.pressure_B05.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pressure_B05.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pressure_B05.setObjectName("pressure_B05")
        self.pressure_B02 = QtWidgets.QFrame(self.frame_4)
        self.pressure_B02.setGeometry(QtCore.QRect(52, 160, 52, 80))
        self.pressure_B02.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pressure_B02.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pressure_B02.setObjectName("pressure_B02")
        self.pressure_B06 = QtWidgets.QFrame(self.frame_4)
        self.pressure_B06.setGeometry(QtCore.QRect(260, 160, 52, 80))
        self.pressure_B06.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pressure_B06.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pressure_B06.setObjectName("pressure_B06")
        self.pressure_B15 = QtWidgets.QFrame(self.frame_4)
        self.pressure_B15.setGeometry(QtCore.QRect(728, 160, 52, 80))
        self.pressure_B15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pressure_B15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pressure_B15.setObjectName("pressure_B15")
        self.pressure_B04 = QtWidgets.QFrame(self.frame_4)
        self.pressure_B04.setGeometry(QtCore.QRect(156, 160, 52, 80))
        self.pressure_B04.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pressure_B04.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pressure_B04.setObjectName("pressure_B04")
        self.pressure_B09 = QtWidgets.QFrame(self.frame_4)
        self.pressure_B09.setGeometry(QtCore.QRect(416, 160, 52, 80))
        self.pressure_B09.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pressure_B09.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pressure_B09.setObjectName("pressure_B09")
        self.pressure_B03 = QtWidgets.QFrame(self.frame_4)
        self.pressure_B03.setGeometry(QtCore.QRect(104, 160, 52, 80))
        self.pressure_B03.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pressure_B03.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pressure_B03.setObjectName("pressure_B03")
        self.pressure_B07 = QtWidgets.QFrame(self.frame_4)
        self.pressure_B07.setGeometry(QtCore.QRect(312, 160, 52, 80))
        self.pressure_B07.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pressure_B07.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pressure_B07.setObjectName("pressure_B07")
        self.pressure_B01 = QtWidgets.QFrame(self.frame_4)
        self.pressure_B01.setGeometry(QtCore.QRect(0, 160, 52, 80))
        self.pressure_B01.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pressure_B01.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pressure_B01.setObjectName("pressure_B01")
        self.pressure_B11 = QtWidgets.QFrame(self.frame_4)
        self.pressure_B11.setGeometry(QtCore.QRect(520, 160, 52, 80))
        self.pressure_B11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pressure_B11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pressure_B11.setObjectName("pressure_B11")
        self.pressure_B10 = QtWidgets.QFrame(self.frame_4)
        self.pressure_B10.setGeometry(QtCore.QRect(468, 160, 52, 80))
        self.pressure_B10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pressure_B10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pressure_B10.setObjectName("pressure_B10")
        self.pressure_B12 = QtWidgets.QFrame(self.frame_4)
        self.pressure_B12.setGeometry(QtCore.QRect(572, 160, 52, 80))
        self.pressure_B12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pressure_B12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pressure_B12.setObjectName("pressure_B12")
        self.pressure_B08 = QtWidgets.QFrame(self.frame_4)
        self.pressure_B08.setGeometry(QtCore.QRect(364, 160, 52, 80))
        self.pressure_B08.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pressure_B08.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pressure_B08.setObjectName("pressure_B08")
        self.pressure_B14 = QtWidgets.QFrame(self.frame_4)
        self.pressure_B14.setGeometry(QtCore.QRect(676, 160, 52, 80))
        self.pressure_B14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pressure_B14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pressure_B14.setObjectName("pressure_B14")

        self.pArray = \
            [
             self.pressure_T01, self.pressure_T02, self.pressure_T03, self.pressure_T04, self.pressure_T05,
             self.pressure_T06, self.pressure_T07, self.pressure_T08, self.pressure_T09, self.pressure_T10,
             self.pressure_T11, self.pressure_T12, self.pressure_T13, self.pressure_T14, self.pressure_T15,
             self.pressure_M01, self.pressure_M02, self.pressure_M03, self.pressure_M04, self.pressure_M05,
             self.pressure_M06, self.pressure_M07, self.pressure_M08, self.pressure_M09, self.pressure_M10,
             self.pressure_M11, self.pressure_M12, self.pressure_M13, self.pressure_M14, self.pressure_M15,
             self.pressure_B01, self.pressure_B02, self.pressure_B03, self.pressure_B04, self.pressure_B05,
             self.pressure_B06, self.pressure_B07, self.pressure_B08, self.pressure_B09, self.pressure_B10,
             self.pressure_B11, self.pressure_B12, self.pressure_B13, self.pressure_B14, self.pressure_B15
             ]
        self.pArrMapper = \
            [
                3 , 4 , 5 , 6 , 7 , 15, 16, 17, 18, 19, 35, 20, 36, 21, 37, 22,
                38, 23, 39, 24, 40, 25, 26, 27, 28, 29, 8 , 9 , 10, 11, 12
            ]

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.startGatheringDataThread)
        self.timer.start(10)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.l_menu_overview.setText(_translate("Dialog", "OVERVIEW"))
        self.l_menu_environment.setText(_translate("Dialog", "ENVIRONMENT"))
        self.l_menu_growth.setText(_translate("Dialog", "GROWTH"))
        self.l_menu_activity.setText(_translate("Dialog", "ACTIVITY"))
        self.label_growthData.setText(_translate("Dialog", "GROWTH DATA"))
        self.title_DATE.setText(_translate("Dialog", "DATE"))

        # Update date
        today = time.gmtime(time.time())
        datestr = str(today.tm_year) + '.' + str(today.tm_mon) + '.' + str(today.tm_mday)

        self.label.setText(_translate("Dialog", datestr))
        self.title_DATE_2.setText(_translate("Dialog", "TEMPERATURE"))
        self.label_2.setText(_translate("Dialog", "- ℃"))
        self.title_DATE_3.setText(_translate("Dialog", "HUMIDITY"))
        self.label_3.setText(_translate("Dialog", "- %"))

    def getRGBfromPressureInput(self, pValue):
        intP = min( max(int(pValue), 0), 255);

        rval = 255
        bval = 255 - intP
        gval = 255 - intP

        return 'rgb(' + str(rval) + ',' + str(gval) + ',' + str(bval) + ')'

    def getSerialData(self):
        with serial.Serial(self.portname, 9600) as s:
            while(True):
                l = s.readline()
                # print(l)
                if len(l) > 1:
                    a = l.decode("utf-8").split('\t')
                    if (a[0] == 'p' or a[0] == 'T' or a[0] == 'W'):
                        print(a)
                        break
        return a

    def setPMapColor(self, pNo, pval):
        if pNo < len(self.pArrMapper):
            self.pArray[self.pArrMapper[pNo]].setStyleSheet('background-color:' + self.getRGBfromPressureInput(pval))

    def updatePressureData(self, pDat):
        for i in range(1,len(pDat)-1):
            pValue = pDat[i]
            if pValue != '':
                self.setPMapColor(i-1, pValue)

    def updateTempHumidData(self, l):
        _translate = QtCore.QCoreApplication.translate

        tempStr = str(l[1]) + '\n℃'
        self.label_2.setText(_translate("Dialog", tempStr))

        humidStr = str(l[2]) + ' %'
        self.label_3.setText(_translate("Dialog", humidStr))

    def updateWeightData(self, weight):
        # Append weight and data list
        self.date_.append(time.time())
        self.weight_.append(float(weight))

        # Update plot
        if len(self.date_)>2:
            self.ax = self.canvas.figure.subplots()
            tickFmt = mdates.DateFormatter('%Y.%M')
            self.ax.plot(self.date_, self.weight_, ".")


    def updateData(self):
        l = self.getSerialData()

        if l[0] == 'p':
            self.updatePressureData(l)
        elif l[0] == 'T':
            self.updateTempHumidData(l)
        elif l[0] == 'W':
            self.updateWeightData(l[1])

    def startGatheringDataThread(self):
        self.t = threading.Thread(target=self.updateData())
        self.t.start()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = dashboard('/dev/tty.usbmodemFA141')
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
