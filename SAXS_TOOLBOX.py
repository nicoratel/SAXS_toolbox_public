from PyQt5 import QtWidgets
import hdf5plugin
import h5py
import sys
import os
import fabio
import numpy as np
from pathlib import Path
import math
from matplotlib import pyplot as plt
from PyQt5.QtGui import QColor
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SAXS_TOOLBOX(object):
    def setupUi(self, SAXS_TOOLBOX):
        SAXS_TOOLBOX.setObjectName("SAXS_TOOLBOX")
        SAXS_TOOLBOX.resize(1106, 740)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SAXS_TOOLBOX.sizePolicy().hasHeightForWidth())
        SAXS_TOOLBOX.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        SAXS_TOOLBOX.setFont(font)
        self.centralwidget = QtWidgets.QWidget(SAXS_TOOLBOX)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_7.addWidget(self.label_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.mask_file_lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.mask_file_lineEdit.setObjectName("mask_file_lineEdit")
        self.horizontalLayout_8.addWidget(self.mask_file_lineEdit)
        self.mask_file_pushButton = QtWidgets.QPushButton(self.tab_2)
        self.mask_file_pushButton.setObjectName("mask_file_pushButton")
        self.horizontalLayout_8.addWidget(self.mask_file_pushButton)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.verticalLayout_7.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_6.addWidget(self.label_2)
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab_2)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.tab_5)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(0, 0, 1061, 281))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_14.addItem(spacerItem)
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_14.addWidget(self.label_15)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_11.addWidget(self.label_14)
        self.key_wl_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.key_wl_lineEdit.setObjectName("key_wl_lineEdit")
        self.horizontalLayout_11.addWidget(self.key_wl_lineEdit)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem1)
        self.label_18 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_11.addWidget(self.label_18)
        self.key_distance_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.key_distance_lineEdit.setObjectName("key_distance_lineEdit")
        self.horizontalLayout_11.addWidget(self.key_distance_lineEdit)
        self.verticalLayout_14.addLayout(self.horizontalLayout_11)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_14.addItem(spacerItem2)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_19 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_12.addWidget(self.label_19)
        self.key_X_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.key_X_lineEdit.setObjectName("key_X_lineEdit")
        self.horizontalLayout_12.addWidget(self.key_X_lineEdit)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem3)
        self.label_20 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_12.addWidget(self.label_20)
        self.key_Y_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.key_Y_lineEdit.setObjectName("key_Y_lineEdit")
        self.horizontalLayout_12.addWidget(self.key_Y_lineEdit)
        self.verticalLayout_14.addLayout(self.horizontalLayout_12)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_14.addItem(spacerItem4)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_22 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_13.addWidget(self.label_22)
        self.key_dim1_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.key_dim1_lineEdit.setObjectName("key_dim1_lineEdit")
        self.horizontalLayout_13.addWidget(self.key_dim1_lineEdit)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem5)
        self.label_24 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_13.addWidget(self.label_24)
        self.key_dim2_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.key_dim2_lineEdit.setObjectName("key_dim2_lineEdit")
        self.horizontalLayout_13.addWidget(self.key_dim2_lineEdit)
        self.verticalLayout_14.addLayout(self.horizontalLayout_13)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_14.addItem(spacerItem6)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_26 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_15.addWidget(self.label_26)
        self.key_sizeX_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.key_sizeX_lineEdit.setObjectName("key_sizeX_lineEdit")
        self.horizontalLayout_15.addWidget(self.key_sizeX_lineEdit)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem7)
        self.label_30 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_30.setObjectName("label_30")
        self.horizontalLayout_15.addWidget(self.label_30)
        self.key_sizeY_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.key_sizeY_lineEdit.setObjectName("key_sizeY_lineEdit")
        self.horizontalLayout_15.addWidget(self.key_sizeY_lineEdit)
        self.verticalLayout_14.addLayout(self.horizontalLayout_15)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_14.addItem(spacerItem8)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_31 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_31.setObjectName("label_31")
        self.horizontalLayout_3.addWidget(self.label_31)
        self.image_header_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.image_header_lineEdit.setObjectName("image_header_lineEdit")
        self.horizontalLayout_3.addWidget(self.image_header_lineEdit)
        self.image_header_pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.image_header_pushButton.setObjectName("image_header_pushButton")
        self.horizontalLayout_3.addWidget(self.image_header_pushButton)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem9)
        self.verticalLayout_14.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.verticalLayout_14.addLayout(self.horizontalLayout_16)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.tab_5)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(0, 290, 1061, 41))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem10)
        self.calibframe_header_pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.calibframe_header_pushButton.setObjectName("calibframe_header_pushButton")
        self.horizontalLayout_10.addWidget(self.calibframe_header_pushButton)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem11)
        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.tab_4)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 1061, 241))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem12)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.poniFile_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.poniFile_lineEdit.setObjectName("poniFile_lineEdit")
        self.horizontalLayout_6.addWidget(self.poniFile_lineEdit)
        self.poniFile_pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.poniFile_pushButton.setObjectName("poniFile_pushButton")
        self.horizontalLayout_6.addWidget(self.poniFile_pushButton)
        self.verticalLayout_13.addLayout(self.horizontalLayout_6)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem13)
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_13.addWidget(self.label_13)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.number_X_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.number_X_lineEdit.setObjectName("number_X_lineEdit")
        self.horizontalLayout_7.addWidget(self.number_X_lineEdit)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem14)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.label_8)
        self.number_Y_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.number_Y_lineEdit.setObjectName("number_Y_lineEdit")
        self.horizontalLayout_7.addWidget(self.number_Y_lineEdit)
        self.verticalLayout_13.addLayout(self.horizontalLayout_7)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem15)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_9.addWidget(self.label_10)
        self.pixsizeH_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.pixsizeH_lineEdit.setObjectName("pixsizeH_lineEdit")
        self.horizontalLayout_9.addWidget(self.pixsizeH_lineEdit)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem16)
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_9.addWidget(self.label_11)
        self.pixsizeV_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.pixsizeV_lineEdit.setObjectName("pixsizeV_lineEdit")
        self.horizontalLayout_9.addWidget(self.pixsizeV_lineEdit)
        self.verticalLayout_13.addLayout(self.horizontalLayout_9)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab_4)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 280, 1061, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem17)
        self.calibframe_pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.calibframe_pushButton.setObjectName("calibframe_pushButton")
        self.horizontalLayout.addWidget(self.calibframe_pushButton)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem18)
        self.tabWidget_2.addTab(self.tab_4, "")
        self.verticalLayout_6.addWidget(self.tabWidget_2)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        self.verticalLayout_3.addLayout(self.verticalLayout_7)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 1081, 461))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        spacerItem19 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem19)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.transmission_I_sample_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.transmission_I_sample_lineEdit.setText("")
        self.transmission_I_sample_lineEdit.setObjectName("transmission_I_sample_lineEdit")
        self.gridLayout_5.addWidget(self.transmission_I_sample_lineEdit, 7, 2, 1, 1)
        self.label_54 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_54.setObjectName("label_54")
        self.gridLayout_5.addWidget(self.label_54, 1, 5, 1, 1)
        self.I0_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.I0_lineEdit.setObjectName("I0_lineEdit")
        self.gridLayout_5.addWidget(self.I0_lineEdit, 1, 6, 1, 1)
        self.label_51 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_51.setObjectName("label_51")
        self.gridLayout_5.addWidget(self.label_51, 2, 1, 1, 1)
        self.label_60 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_60.setObjectName("label_60")
        self.gridLayout_5.addWidget(self.label_60, 3, 1, 1, 1)
        self.Itrans_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.Itrans_lineEdit.setObjectName("Itrans_lineEdit")
        self.gridLayout_5.addWidget(self.Itrans_lineEdit, 7, 6, 1, 1)
        self.label_56 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_56.setObjectName("label_56")
        self.gridLayout_5.addWidget(self.label_56, 7, 5, 1, 1)
        self.transmission_I_ref_calc_pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.transmission_I_ref_calc_pushButton.setObjectName("transmission_I_ref_calc_pushButton")
        self.gridLayout_5.addWidget(self.transmission_I_ref_calc_pushButton, 6, 4, 1, 1)
        self.transmission_I0_calc_pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.transmission_I0_calc_pushButton.setObjectName("transmission_I0_calc_pushButton")
        self.gridLayout_5.addWidget(self.transmission_I0_calc_pushButton, 1, 4, 1, 1)
        self.transmission_I_calib_ref_Browse_pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.transmission_I_calib_ref_Browse_pushButton.setObjectName("transmission_I_calib_ref_Browse_pushButton")
        self.gridLayout_5.addWidget(self.transmission_I_calib_ref_Browse_pushButton, 3, 3, 1, 1)
        self.Iref_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.Iref_lineEdit.setObjectName("Iref_lineEdit")
        self.gridLayout_5.addWidget(self.Iref_lineEdit, 6, 6, 1, 1)
        self.label_61 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_61.setObjectName("label_61")
        self.gridLayout_5.addWidget(self.label_61, 5, 1, 1, 1)
        self.transmission_I0_Browse_pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.transmission_I0_Browse_pushButton.setObjectName("transmission_I0_Browse_pushButton")
        self.gridLayout_5.addWidget(self.transmission_I0_Browse_pushButton, 1, 3, 1, 1)
        self.label_49 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_49.setObjectName("label_49")
        self.gridLayout_5.addWidget(self.label_49, 1, 1, 1, 1)
        self.transmission_I_sample_calc_pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.transmission_I_sample_calc_pushButton.setObjectName("transmission_I_sample_calc_pushButton")
        self.gridLayout_5.addWidget(self.transmission_I_sample_calc_pushButton, 7, 4, 1, 1)
        self.transmission_I_calib_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.transmission_I_calib_lineEdit.setText("")
        self.transmission_I_calib_lineEdit.setObjectName("transmission_I_calib_lineEdit")
        self.gridLayout_5.addWidget(self.transmission_I_calib_lineEdit, 4, 2, 1, 1)
        self.label_57 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_57.setObjectName("label_57")
        self.gridLayout_5.addWidget(self.label_57, 6, 1, 1, 1)
        self.transmission_I_calib_ref_calc_pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.transmission_I_calib_ref_calc_pushButton.setObjectName("transmission_I_calib_ref_calc_pushButton")
        self.gridLayout_5.addWidget(self.transmission_I_calib_ref_calc_pushButton, 3, 4, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem20, 3, 0, 1, 1)
        self.transmission_I0_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.transmission_I0_lineEdit.setObjectName("transmission_I0_lineEdit")
        self.gridLayout_5.addWidget(self.transmission_I0_lineEdit, 1, 2, 1, 1)
        self.label_50 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_50.setObjectName("label_50")
        self.gridLayout_5.addWidget(self.label_50, 0, 1, 1, 1)
        self.label_52 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_52.setObjectName("label_52")
        self.gridLayout_5.addWidget(self.label_52, 4, 5, 1, 1)
        self.label_59 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_59.setObjectName("label_59")
        self.gridLayout_5.addWidget(self.label_59, 4, 1, 1, 1)
        self.window_width_trans_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.window_width_trans_lineEdit.setObjectName("window_width_trans_lineEdit")
        self.gridLayout_5.addWidget(self.window_width_trans_lineEdit, 0, 2, 1, 1)
        self.transmission_I_calib_Browse_pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.transmission_I_calib_Browse_pushButton.setObjectName("transmission_I_calib_Browse_pushButton")
        self.gridLayout_5.addWidget(self.transmission_I_calib_Browse_pushButton, 4, 3, 1, 1)
        self.transmission_I_ref_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.transmission_I_ref_lineEdit.setText("")
        self.transmission_I_ref_lineEdit.setObjectName("transmission_I_ref_lineEdit")
        self.gridLayout_5.addWidget(self.transmission_I_ref_lineEdit, 6, 2, 1, 1)
        self.I_water_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.I_water_lineEdit.setObjectName("I_water_lineEdit")
        self.gridLayout_5.addWidget(self.I_water_lineEdit, 4, 6, 1, 1)
        self.transmission_I_calib_ref_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.transmission_I_calib_ref_lineEdit.setObjectName("transmission_I_calib_ref_lineEdit")
        self.gridLayout_5.addWidget(self.transmission_I_calib_ref_lineEdit, 3, 2, 1, 1)
        self.label_58 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_58.setObjectName("label_58")
        self.gridLayout_5.addWidget(self.label_58, 3, 5, 1, 1)
        self.transmission_I_ref_Browse_pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.transmission_I_ref_Browse_pushButton.setObjectName("transmission_I_ref_Browse_pushButton")
        self.gridLayout_5.addWidget(self.transmission_I_ref_Browse_pushButton, 6, 3, 1, 1)
        self.transmission_I_calib_calc_pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.transmission_I_calib_calc_pushButton.setObjectName("transmission_I_calib_calc_pushButton")
        self.gridLayout_5.addWidget(self.transmission_I_calib_calc_pushButton, 4, 4, 1, 1)
        self.label_55 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_55.setObjectName("label_55")
        self.gridLayout_5.addWidget(self.label_55, 7, 1, 1, 1)
        self.label_53 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_53.setObjectName("label_53")
        self.gridLayout_5.addWidget(self.label_53, 6, 5, 1, 1)
        self.transmission_I_sample_Browse_pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.transmission_I_sample_Browse_pushButton.setObjectName("transmission_I_sample_Browse_pushButton")
        self.gridLayout_5.addWidget(self.transmission_I_sample_Browse_pushButton, 7, 3, 1, 1)
        self.I_ref_water_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.I_ref_water_lineEdit.setObjectName("I_ref_water_lineEdit")
        self.gridLayout_5.addWidget(self.I_ref_water_lineEdit, 3, 6, 1, 1)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem21, 3, 7, 1, 1)
        self.verticalLayout_10.addLayout(self.gridLayout_5)
        spacerItem22 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem22)
        self.tabWidget.addTab(self.tab, "")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.tab_1)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.groupBox = QtWidgets.QGroupBox(self.tab_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.water_checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.water_checkBox.setObjectName("water_checkBox")
        self.verticalLayout_18.addWidget(self.water_checkBox)
        self.hexane_checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.hexane_checkBox.setObjectName("hexane_checkBox")
        self.verticalLayout_18.addWidget(self.hexane_checkBox)
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_18.addWidget(self.label_12)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_18.addWidget(self.lineEdit)
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.label_21 = QtWidgets.QLabel(self.groupBox_2)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_25.addWidget(self.label_21)
        self.water_ref_calib_file_lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.water_ref_calib_file_lineEdit.setObjectName("water_ref_calib_file_lineEdit")
        self.horizontalLayout_25.addWidget(self.water_ref_calib_file_lineEdit)
        self.water_ref_calib_file_pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.water_ref_calib_file_pushButton.setObjectName("water_ref_calib_file_pushButton")
        self.horizontalLayout_25.addWidget(self.water_ref_calib_file_pushButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_25)
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.label_23 = QtWidgets.QLabel(self.groupBox_2)
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_27.addWidget(self.label_23)
        self.water_calib_file_lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.water_calib_file_lineEdit.setObjectName("water_calib_file_lineEdit")
        self.horizontalLayout_27.addWidget(self.water_calib_file_lineEdit)
        self.water_calib_file_pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.water_calib_file_pushButton.setObjectName("water_calib_file_pushButton")
        self.horizontalLayout_27.addWidget(self.water_calib_file_pushButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_27)
        self.verticalLayout_17.addLayout(self.verticalLayout_4)
        self.verticalLayout_18.addWidget(self.groupBox_2)
        spacerItem23 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_18.addItem(spacerItem23)
        self.label_27 = QtWidgets.QLabel(self.groupBox)
        self.label_27.setObjectName("label_27")
        self.verticalLayout_18.addWidget(self.label_27)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_14.addWidget(self.label_9)
        self.x_center_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.x_center_lineEdit.setObjectName("x_center_lineEdit")
        self.horizontalLayout_14.addWidget(self.x_center_lineEdit)
        self.label_16 = QtWidgets.QLabel(self.groupBox)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_14.addWidget(self.label_16)
        self.y_center_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.y_center_lineEdit.setObjectName("y_center_lineEdit")
        self.horizontalLayout_14.addWidget(self.y_center_lineEdit)
        self.label_17 = QtWidgets.QLabel(self.groupBox)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_14.addWidget(self.label_17)
        self.window_width_calib_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.window_width_calib_lineEdit.setObjectName("window_width_calib_lineEdit")
        self.horizontalLayout_14.addWidget(self.window_width_calib_lineEdit)
        self.verticalLayout_18.addLayout(self.horizontalLayout_14)
        spacerItem24 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_18.addItem(spacerItem24)
        self.horizontalLayout_32 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        spacerItem25 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_31.addItem(spacerItem25)
        self.calib_pushButton = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calib_pushButton.sizePolicy().hasHeightForWidth())
        self.calib_pushButton.setSizePolicy(sizePolicy)
        self.calib_pushButton.setObjectName("calib_pushButton")
        self.horizontalLayout_31.addWidget(self.calib_pushButton)
        spacerItem26 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_31.addItem(spacerItem26)
        self.horizontalLayout_32.addLayout(self.horizontalLayout_31)
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.label_25 = QtWidgets.QLabel(self.groupBox)
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_30.addWidget(self.label_25)
        self.calculated_calibration_coeflineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.calculated_calibration_coeflineEdit.setObjectName("calculated_calibration_coeflineEdit")
        self.horizontalLayout_30.addWidget(self.calculated_calibration_coeflineEdit)
        spacerItem27 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_30.addItem(spacerItem27)
        self.horizontalLayout_32.addLayout(self.horizontalLayout_30)
        self.verticalLayout_18.addLayout(self.horizontalLayout_32)
        self.verticalLayout_19.addWidget(self.groupBox)
        spacerItem28 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_19.addItem(spacerItem28)
        self.tabWidget.addTab(self.tab_1, "")
        self.Page = QtWidgets.QWidget()
        self.Page.setObjectName("Page")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.Page)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(380, 10, 380, 441))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_35 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_35.setObjectName("label_35")
        self.verticalLayout_8.addWidget(self.label_35)
        spacerItem29 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem29)
        self.browse_ref_1D_pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.browse_ref_1D_pushButton.setObjectName("browse_ref_1D_pushButton")
        self.verticalLayout_8.addWidget(self.browse_ref_1D_pushButton)
        spacerItem30 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem30)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_8.addWidget(self.pushButton)
        self.label_29 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_29.setObjectName("label_29")
        self.verticalLayout_8.addWidget(self.label_29)
        self.spec_trans_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.spec_trans_lineEdit.setObjectName("spec_trans_lineEdit")
        self.verticalLayout_8.addWidget(self.spec_trans_lineEdit)
        spacerItem31 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem31)
        self.calc_coeff_pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.calc_coeff_pushButton.setObjectName("calc_coeff_pushButton")
        self.verticalLayout_8.addWidget(self.calc_coeff_pushButton)
        spacerItem32 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem32)
        self.label_28 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_28.setObjectName("label_28")
        self.verticalLayout_8.addWidget(self.label_28)
        self.ref_coeff_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.ref_coeff_lineEdit.setObjectName("ref_coeff_lineEdit")
        self.verticalLayout_8.addWidget(self.ref_coeff_lineEdit)
        spacerItem33 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem33)
        self.tabWidget.addTab(self.Page, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem34 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem34)
        self.label_7 = QtWidgets.QLabel(self.tab_3)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.ref_file_lineEdit = QtWidgets.QLineEdit(self.tab_3)
        self.ref_file_lineEdit.setObjectName("ref_file_lineEdit")
        self.horizontalLayout_5.addWidget(self.ref_file_lineEdit)
        self.ref_file_pushButton = QtWidgets.QPushButton(self.tab_3)
        self.ref_file_pushButton.setObjectName("ref_file_pushButton")
        self.horizontalLayout_5.addWidget(self.ref_file_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.skip_checkBox = QtWidgets.QCheckBox(self.tab_3)
        self.skip_checkBox.setObjectName("skip_checkBox")
        self.verticalLayout.addWidget(self.skip_checkBox)
        spacerItem35 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem35)
        self.label = QtWidgets.QLabel(self.tab_3)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.data_file_textEdit = QtWidgets.QTextEdit(self.tab_3)
        self.data_file_textEdit.setObjectName("data_file_textEdit")
        self.horizontalLayout_2.addWidget(self.data_file_textEdit)
        self.data_file_pushButton = QtWidgets.QPushButton(self.tab_3)
        self.data_file_pushButton.setObjectName("data_file_pushButton")
        self.horizontalLayout_2.addWidget(self.data_file_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.nb_samples_averaged_lineEdit = QtWidgets.QLineEdit(self.tab_3)
        self.nb_samples_averaged_lineEdit.setObjectName("nb_samples_averaged_lineEdit")
        self.horizontalLayout_4.addWidget(self.nb_samples_averaged_lineEdit)
        spacerItem36 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem36)
        self.setItransto1_pushButton = QtWidgets.QPushButton(self.tab_3)
        self.setItransto1_pushButton.setObjectName("setItransto1_pushButton")
        self.horizontalLayout_4.addWidget(self.setItransto1_pushButton)
        spacerItem37 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem37)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem38 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem38)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        spacerItem39 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem39)
        self.sasview_checkBox = QtWidgets.QCheckBox(self.tab_3)
        self.sasview_checkBox.setObjectName("sasview_checkBox")
        self.horizontalLayout_17.addWidget(self.sasview_checkBox)
        spacerItem40 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem40)
        self.convert_pushButton = QtWidgets.QPushButton(self.tab_3)
        self.convert_pushButton.setObjectName("convert_pushButton")
        self.horizontalLayout_17.addWidget(self.convert_pushButton)
        spacerItem41 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem41)
        self.verticalLayout.addLayout(self.horizontalLayout_17)
        spacerItem42 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem42)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalLayout.addLayout(self.verticalLayout_11)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.tabWidget.addTab(self.tab_3, "")
        self.verticalLayout_9.addWidget(self.tabWidget)
        self.console_textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.console_textEdit.setObjectName("console_textEdit")
        self.verticalLayout_9.addWidget(self.console_textEdit)
        SAXS_TOOLBOX.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SAXS_TOOLBOX)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1106, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menupyFAI = QtWidgets.QMenu(self.menubar)
        self.menupyFAI.setObjectName("menupyFAI")
        self.menuGenerate_mask = QtWidgets.QMenu(self.menupyFAI)
        self.menuGenerate_mask.setObjectName("menuGenerate_mask")
        self.menuInspect_data = QtWidgets.QMenu(self.menubar)
        self.menuInspect_data.setObjectName("menuInspect_data")
        self.menuplot_1D_data_file_s_2 = QtWidgets.QMenu(self.menuInspect_data)
        self.menuplot_1D_data_file_s_2.setObjectName("menuplot_1D_data_file_s_2")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        self.menuConvert_nxs_h5 = QtWidgets.QMenu(self.menuTools)
        self.menuConvert_nxs_h5.setObjectName("menuConvert_nxs_h5")
        SAXS_TOOLBOX.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SAXS_TOOLBOX)
        self.statusbar.setObjectName("statusbar")
        SAXS_TOOLBOX.setStatusBar(self.statusbar)
        self.actionSet_Working_Directory = QtWidgets.QAction(SAXS_TOOLBOX)
        self.actionSet_Working_Directory.setObjectName("actionSet_Working_Directory")
        self.actionQuit = QtWidgets.QAction(SAXS_TOOLBOX)
        self.actionQuit.setObjectName("actionQuit")
        self.actionInitialize_Form = QtWidgets.QAction(SAXS_TOOLBOX)
        self.actionInitialize_Form.setObjectName("actionInitialize_Form")
        self.actionView_image = QtWidgets.QAction(SAXS_TOOLBOX)
        self.actionView_image.setObjectName("actionView_image")
        self.actionOpen_view_image = QtWidgets.QAction(SAXS_TOOLBOX)
        self.actionOpen_view_image.setObjectName("actionOpen_view_image")
        self.actionDetector_calibration = QtWidgets.QAction(SAXS_TOOLBOX)
        self.actionDetector_calibration.setObjectName("actionDetector_calibration")
        self.actionFrame_integration = QtWidgets.QAction(SAXS_TOOLBOX)
        self.actionFrame_integration.setObjectName("actionFrame_integration")
        self.actionSWING = QtWidgets.QAction(SAXS_TOOLBOX)
        self.actionSWING.setObjectName("actionSWING")
        self.actionfrom_ID15 = QtWidgets.QAction(SAXS_TOOLBOX)
        self.actionfrom_ID15.setObjectName("actionfrom_ID15")
        self.actionfrom_scratch = QtWidgets.QAction(SAXS_TOOLBOX)
        self.actionfrom_scratch.setObjectName("actionfrom_scratch")
        self.actionconvert_foxtrot_mask = QtWidgets.QAction(SAXS_TOOLBOX)
        self.actionconvert_foxtrot_mask.setObjectName("actionconvert_foxtrot_mask")
        self.actionAverage_frames = QtWidgets.QAction(SAXS_TOOLBOX)
        self.actionAverage_frames.setObjectName("actionAverage_frames")
        self.actionloglog = QtWidgets.QAction(SAXS_TOOLBOX)
        self.actionloglog.setObjectName("actionloglog")
        self.actionlinear = QtWidgets.QAction(SAXS_TOOLBOX)
        self.actionlinear.setObjectName("actionlinear")
        self.actionOpen_view_image_2 = QtWidgets.QAction(SAXS_TOOLBOX)
        self.actionOpen_view_image_2.setObjectName("actionOpen_view_image_2")
        self.actionloglog_2 = QtWidgets.QAction(SAXS_TOOLBOX)
        self.actionloglog_2.setObjectName("actionloglog_2")
        self.actionlinear_2 = QtWidgets.QAction(SAXS_TOOLBOX)
        self.actionlinear_2.setObjectName("actionlinear_2")
        self.actionAverage_frames_2 = QtWidgets.QAction(SAXS_TOOLBOX)
        self.actionAverage_frames_2.setObjectName("actionAverage_frames_2")
        self.actionSWING_2 = QtWidgets.QAction(SAXS_TOOLBOX)
        self.actionSWING_2.setObjectName("actionSWING_2")
        self.actionfrom_ID15_2 = QtWidgets.QAction(SAXS_TOOLBOX)
        self.actionfrom_ID15_2.setObjectName("actionfrom_ID15_2")
        self.actionfrom_ID02_SAXS = QtWidgets.QAction(SAXS_TOOLBOX)
        self.actionfrom_ID02_SAXS.setObjectName("actionfrom_ID02_SAXS")
        self.actionfrom_ID02_WAXS = QtWidgets.QAction(SAXS_TOOLBOX)
        self.actionfrom_ID02_WAXS.setObjectName("actionfrom_ID02_WAXS")
        self.menuFile.addAction(self.actionSet_Working_Directory)
        self.menuFile.addAction(self.actionInitialize_Form)
        self.menuGenerate_mask.addAction(self.actionfrom_scratch)
        self.menuGenerate_mask.addAction(self.actionconvert_foxtrot_mask)
        self.menupyFAI.addAction(self.actionDetector_calibration)
        self.menupyFAI.addAction(self.actionFrame_integration)
        self.menupyFAI.addAction(self.menuGenerate_mask.menuAction())
        self.menuplot_1D_data_file_s_2.addAction(self.actionloglog_2)
        self.menuplot_1D_data_file_s_2.addAction(self.actionlinear_2)
        self.menuInspect_data.addAction(self.actionOpen_view_image_2)
        self.menuInspect_data.addAction(self.menuplot_1D_data_file_s_2.menuAction())
        self.menuConvert_nxs_h5.addAction(self.actionSWING_2)
        self.menuConvert_nxs_h5.addAction(self.actionfrom_ID15_2)
        self.menuConvert_nxs_h5.addAction(self.actionfrom_ID02_SAXS)
        self.menuConvert_nxs_h5.addAction(self.actionfrom_ID02_WAXS)
        self.menuTools.addAction(self.actionAverage_frames_2)
        self.menuTools.addAction(self.menuConvert_nxs_h5.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menupyFAI.menuAction())
        self.menubar.addAction(self.menuInspect_data.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())

        self.retranslateUi(SAXS_TOOLBOX)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(SAXS_TOOLBOX)

    def retranslateUi(self, SAXS_TOOLBOX):
        _translate = QtCore.QCoreApplication.translate
        SAXS_TOOLBOX.setWindowTitle(_translate("SAXS_TOOLBOX", "SAXS_TOOLBOX"))
        self.label_4.setText(_translate("SAXS_TOOLBOX", "<html><head/><body><p><span style=\" font-size:12pt; text-decoration: underline;\">1. </span><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">Load Mask file</span><span style=\" font-size:12pt; text-decoration: underline;\"> (use pyFAI/Generate Mask to create a mask file)</span></p></body></html>"))
        self.mask_file_pushButton.setText(_translate("SAXS_TOOLBOX", "..."))
        self.label_2.setText(_translate("SAXS_TOOLBOX", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">2. CALIBRATION: </span><span style=\" font-size:12pt; text-decoration: underline;\">choose between importing a poni file or retrieve calibration information from frame meta data</span></p></body></html>"))
        self.label_15.setText(_translate("SAXS_TOOLBOX", "<html><head/><body><p><span style=\" font-weight:600;\">Specify </span><span style=\" font-weight:600; text-decoration: underline;\">text </span><span style=\" font-weight:600; text-decoration: underline;\">keys</span><span style=\" font-weight:600;\"> provided in the header to collect meta data for the following items (check header using &quot;Inspect data&quot; menu):</span></p></body></html>"))
        self.label_14.setText(_translate("SAXS_TOOLBOX", "        Wavelength  (m)        "))
        self.label_18.setText(_translate("SAXS_TOOLBOX", "Sample to detector distance (m)"))
        self.label_19.setText(_translate("SAXS_TOOLBOX", "    Beam center X (pixels)  "))
        self.label_20.setText(_translate("SAXS_TOOLBOX", "  Beam center Y (pixels)   "))
        self.label_22.setText(_translate("SAXS_TOOLBOX", "Number of pixels along X"))
        self.label_24.setText(_translate("SAXS_TOOLBOX", "Number of pixels along Y"))
        self.label_26.setText(_translate("SAXS_TOOLBOX", "    Pixel size along X (m)    "))
        self.label_30.setText(_translate("SAXS_TOOLBOX", "    Pixel size along Y (m)    "))
        self.label_31.setText(_translate("SAXS_TOOLBOX", "Provide image file from which data should be extracted"))
        self.image_header_pushButton.setText(_translate("SAXS_TOOLBOX", "..."))
        self.calibframe_header_pushButton.setText(_translate("SAXS_TOOLBOX", "Apply calibration and generate corresponding poni file (calibration.poni)"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("SAXS_TOOLBOX", "Retrieve calibration infos from frame header"))
        self.label_3.setText(_translate("SAXS_TOOLBOX", "Load poni file"))
        self.poniFile_pushButton.setText(_translate("SAXS_TOOLBOX", "..."))
        self.label_13.setText(_translate("SAXS_TOOLBOX", "The following information about images must be provided manually:"))
        self.label_6.setText(_translate("SAXS_TOOLBOX", "Number of pixels along X"))
        self.label_8.setText(_translate("SAXS_TOOLBOX", "Number of pixels along Y"))
        self.label_10.setText(_translate("SAXS_TOOLBOX", "    Pixel size along X (m)    "))
        self.label_11.setText(_translate("SAXS_TOOLBOX", "     Pixel size along Y (m)    "))
        self.calibframe_pushButton.setText(_translate("SAXS_TOOLBOX", "Apply calibration"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("SAXS_TOOLBOX", "Import poni file"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("SAXS_TOOLBOX", "Experiment description"))
        self.label_54.setText(_translate("SAXS_TOOLBOX", "          I_0 =    "))
        self.label_51.setText(_translate("SAXS_TOOLBOX", "<html><head/><body><p><span style=\" font-weight:600;\">Transmission files for intensity calibration</span></p></body></html>"))
        self.label_60.setText(_translate("SAXS_TOOLBOX", "Image file for empty cell transmission (I_calib_ref)"))
        self.label_56.setText(_translate("SAXS_TOOLBOX", "         I_sample =  "))
        self.transmission_I_ref_calc_pushButton.setText(_translate("SAXS_TOOLBOX", "Calculate I_ref"))
        self.transmission_I0_calc_pushButton.setText(_translate("SAXS_TOOLBOX", "Calculate I_0"))
        self.transmission_I_calib_ref_Browse_pushButton.setText(_translate("SAXS_TOOLBOX", "..."))
        self.label_61.setText(_translate("SAXS_TOOLBOX", "<html><head/><body><p><span style=\" font-weight:600;\">Transmission files for specimen measurements</span></p></body></html>"))
        self.transmission_I0_Browse_pushButton.setText(_translate("SAXS_TOOLBOX", "..."))
        self.label_49.setText(_translate("SAXS_TOOLBOX", "Image file for empty beam transmission (I_0)"))
        self.transmission_I_sample_calc_pushButton.setText(_translate("SAXS_TOOLBOX", "Calculate I_sample"))
        self.label_57.setText(_translate("SAXS_TOOLBOX", "Image file for reference transmission (I_ref)"))
        self.transmission_I_calib_ref_calc_pushButton.setText(_translate("SAXS_TOOLBOX", "Calculate I_calib_ref"))
        self.label_50.setText(_translate("SAXS_TOOLBOX", "<html><head/><body><p><span style=\" font-weight:600;\">window width</span> (pixels) for transmission calculation</p></body></html>"))
        self.label_52.setText(_translate("SAXS_TOOLBOX", "      I_calib =  "))
        self.label_59.setText(_translate("SAXS_TOOLBOX", "Image file for calibrant transmission (I_calib)"))
        self.transmission_I_calib_Browse_pushButton.setText(_translate("SAXS_TOOLBOX", "..."))
        self.label_58.setText(_translate("SAXS_TOOLBOX", "    I_calib_ref =   "))
        self.transmission_I_ref_Browse_pushButton.setText(_translate("SAXS_TOOLBOX", "..."))
        self.transmission_I_calib_calc_pushButton.setText(_translate("SAXS_TOOLBOX", "Calculate I_calib"))
        self.label_55.setText(_translate("SAXS_TOOLBOX", "Image files for sample transmission (I_sample=[a,b...])"))
        self.label_53.setText(_translate("SAXS_TOOLBOX", "         I_ref =  "))
        self.transmission_I_sample_Browse_pushButton.setText(_translate("SAXS_TOOLBOX", "..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("SAXS_TOOLBOX", "Transmission"))
        self.groupBox.setTitle(_translate("SAXS_TOOLBOX", "Nature of the calibrant"))
        self.water_checkBox.setText(_translate("SAXS_TOOLBOX", "Water"))
        self.hexane_checkBox.setText(_translate("SAXS_TOOLBOX", "Hexane"))
        self.label_12.setText(_translate("SAXS_TOOLBOX", "OR specify calibrant Theoretical SLD (cm-1)"))
        self.groupBox_2.setTitle(_translate("SAXS_TOOLBOX", "Load calibration frame data"))
        self.label_21.setText(_translate("SAXS_TOOLBOX", "Reference data (empty cell)"))
        self.water_ref_calib_file_pushButton.setText(_translate("SAXS_TOOLBOX", "..."))
        self.label_23.setText(_translate("SAXS_TOOLBOX", "Calibrant data (cell+sample)"))
        self.water_calib_file_pushButton.setText(_translate("SAXS_TOOLBOX", "..."))
        self.label_27.setText(_translate("SAXS_TOOLBOX", "Calibration parameters: define square area where the intensity is estimated"))
        self.label_9.setText(_translate("SAXS_TOOLBOX", "x_center"))
        self.label_16.setText(_translate("SAXS_TOOLBOX", "y_center"))
        self.label_17.setText(_translate("SAXS_TOOLBOX", "window width (pixels)"))
        self.calib_pushButton.setText(_translate("SAXS_TOOLBOX", "Calculate the calibration coefficient"))
        self.label_25.setText(_translate("SAXS_TOOLBOX", "Calibration coefficient :"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("SAXS_TOOLBOX", "Intensity calibration"))
        self.label_35.setText(_translate("SAXS_TOOLBOX", "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">OPTIONAL</span></p><p>Provide<span style=\" font-weight:600;\"> uncorrected (raw) 1D data </span></p><p>Transmission is taken into account for the calculation.</p></body></html>"))
        self.browse_ref_1D_pushButton.setText(_translate("SAXS_TOOLBOX", "Browse for Reference file (1D)"))
        self.pushButton.setText(_translate("SAXS_TOOLBOX", "Browse for specimen data"))
        self.label_29.setText(_translate("SAXS_TOOLBOX", "Specimen transmission"))
        self.calc_coeff_pushButton.setText(_translate("SAXS_TOOLBOX", "Estimate coefficient"))
        self.label_28.setText(_translate("SAXS_TOOLBOX", "Estimated coefficient"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Page), _translate("SAXS_TOOLBOX", "Refine correction (optional)"))
        self.label_7.setText(_translate("SAXS_TOOLBOX", "<html><head/><body><p><span style=\" font-weight:600;\">Reference </span>scattering data (select a single file, in case of multiple files, generate an average image using the above button):</p></body></html>"))
        self.ref_file_pushButton.setText(_translate("SAXS_TOOLBOX", "..."))
        self.skip_checkBox.setText(_translate("SAXS_TOOLBOX", "Check this box to skip reference substraction"))
        self.label.setText(_translate("SAXS_TOOLBOX", "<html><head/><body><p><span style=\" font-weight:600;\">Specimen </span>scattering data (multiple selection possible)</p></body></html>"))
        self.data_file_pushButton.setText(_translate("SAXS_TOOLBOX", "..."))
        self.label_5.setText(_translate("SAXS_TOOLBOX", "Average by bunch of:"))
        self.setItransto1_pushButton.setText(_translate("SAXS_TOOLBOX", "Set sample transmissions to 1"))
        self.sasview_checkBox.setText(_translate("SAXS_TOOLBOX", "Convert edf to Qx,Qy I for input in sasview"))
        self.convert_pushButton.setText(_translate("SAXS_TOOLBOX", "Process Files"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("SAXS_TOOLBOX", "Process data"))
        self.menuFile.setTitle(_translate("SAXS_TOOLBOX", "Menu"))
        self.menupyFAI.setTitle(_translate("SAXS_TOOLBOX", "pyFAI"))
        self.menuGenerate_mask.setTitle(_translate("SAXS_TOOLBOX", "Generate mask"))
        self.menuInspect_data.setTitle(_translate("SAXS_TOOLBOX", "Inspect data"))
        self.menuplot_1D_data_file_s_2.setTitle(_translate("SAXS_TOOLBOX", "plot 1D data file(s)"))
        self.menuTools.setTitle(_translate("SAXS_TOOLBOX", "Tools"))
        self.menuConvert_nxs_h5.setTitle(_translate("SAXS_TOOLBOX", "Convert nxs/h5"))
        self.actionSet_Working_Directory.setText(_translate("SAXS_TOOLBOX", "Set Working Directory"))
        self.actionQuit.setText(_translate("SAXS_TOOLBOX", "Initialize Form"))
        self.actionInitialize_Form.setText(_translate("SAXS_TOOLBOX", "Initialize Form"))
        self.actionView_image.setText(_translate("SAXS_TOOLBOX", "View image"))
        self.actionOpen_view_image.setText(_translate("SAXS_TOOLBOX", "Open and view image"))
        self.actionDetector_calibration.setText(_translate("SAXS_TOOLBOX", "Detector calibration"))
        self.actionFrame_integration.setText(_translate("SAXS_TOOLBOX", "Frame integration"))
        self.actionSWING.setText(_translate("SAXS_TOOLBOX", "from SWING"))
        self.actionfrom_ID15.setText(_translate("SAXS_TOOLBOX", "from ID15"))
        self.actionfrom_scratch.setText(_translate("SAXS_TOOLBOX", "using an image file"))
        self.actionconvert_foxtrot_mask.setText(_translate("SAXS_TOOLBOX", "convert foxtrot mask"))
        self.actionAverage_frames.setText(_translate("SAXS_TOOLBOX", "Average frames"))
        self.actionloglog.setText(_translate("SAXS_TOOLBOX", "loglog"))
        self.actionlinear.setText(_translate("SAXS_TOOLBOX", "linear"))
        self.actionOpen_view_image_2.setText(_translate("SAXS_TOOLBOX", "Open and view image"))
        self.actionloglog_2.setText(_translate("SAXS_TOOLBOX", "log-log plot"))
        self.actionlinear_2.setText(_translate("SAXS_TOOLBOX", "linear plot"))
        self.actionAverage_frames_2.setText(_translate("SAXS_TOOLBOX", "Average frames"))
        self.actionSWING_2.setText(_translate("SAXS_TOOLBOX", "from SWING"))
        self.actionfrom_ID15_2.setText(_translate("SAXS_TOOLBOX", "from ID15"))
        self.actionfrom_ID02_SAXS.setText(_translate("SAXS_TOOLBOX", "from ID02_SAXS"))
        self.actionfrom_ID02_WAXS.setText(_translate("SAXS_TOOLBOX", "from ID02_WAXS"))

        
#variable initialization for verification of provided files 
a=0
b=0
class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        
        self.ui = Ui_SAXS_TOOLBOX()
        self.ui.setupUi(self)
        
        self.ui.calib_pushButton.clicked.connect(self.calibration)
        self.ui.water_calib_file_pushButton.clicked.connect(self.openfile_calib_water)
        self.ui.water_ref_calib_file_pushButton.clicked.connect(self.openfile_calib_water_ref)
        self.ui.poniFile_pushButton.clicked.connect(self.setponifile)
        self.ui.mask_file_pushButton.clicked.connect(self.openmaskfile)
        self.ui.ref_file_pushButton.clicked.connect(self.openreffile)
        self.ui.data_file_pushButton.clicked.connect(self.opendatafiles)
        
        self.ui.actionDetector_calibration.triggered.connect(self.pyFAI_calib)
        self.ui.actionFrame_integration.triggered.connect(self.pyFAI_integrate)
        self.ui.convert_pushButton.clicked.connect(self.check)
        self.ui.Itrans_lineEdit.setText('[value1,value2,...]')
        self.ui.I0_lineEdit.setText('1')
        self.ui.Iref_lineEdit.setText('1')
        self.ui.calculated_calibration_coeflineEdit.setText('1')
        self.ui.skip_checkBox.setChecked(False)
        self.ui.nb_samples_averaged_lineEdit.setText('1')
        self.ui.actionSet_Working_Directory.triggered.connect(self.getWD)
        self.ui.actionInitialize_Form.triggered.connect(self.init_form)
        self.path=os.getcwd()
        # Intialisation transmission tab
        self.ui.transmission_I0_Browse_pushButton.clicked.connect(self.openfile_trans_I0)
        self.ui.transmission_I0_calc_pushButton.clicked.connect(self.calc_trans_I0)
        self.ui.I_ref_water_lineEdit.setText("1")
        self.ui.I_water_lineEdit.setText("1")
        self.ui.transmission_I_calib_ref_Browse_pushButton.clicked.connect(self.openfile_trans_I_calib_ref)
        self.ui.transmission_I_calib_ref_calc_pushButton.clicked.connect(self.calc_trans_I_calib_ref)
        
        self.ui.transmission_I_calib_Browse_pushButton.clicked.connect(self.openfile_trans_I_calib)
        self.ui.transmission_I_calib_calc_pushButton.clicked.connect(self.calc_trans_I_calib)
        
        self.ui.transmission_I_ref_Browse_pushButton.clicked.connect(self.openfile_trans_I_ref)
        self.ui.transmission_I_ref_calc_pushButton.clicked.connect(self.calc_trans_I_ref)
        
        self.ui.transmission_I_sample_Browse_pushButton.clicked.connect(self.openfile_trans_I_sample)
        self.ui.transmission_I_sample_calc_pushButton.clicked.connect(self.calc_trans_I_sample)          
        
        self.ui.setItransto1_pushButton.clicked.connect(self.setItransto1)
        
        # Viewer
        #self.ui.viewer_pushButton.clicked.connect(self.viewer)
        self.ui.actionOpen_view_image_2.triggered.connect(self.openfile4viewer) 
        self.ui.actionloglog_2.triggered.connect(self.plotloglog)
        self.ui.actionlinear_2.triggered.connect(self.plotlinear)
        
        self.ui.window_width_trans_lineEdit.setText("10")
        self.ui.x_center_lineEdit.setText("750")
        self.ui.y_center_lineEdit.setText("500")
        self.ui.window_width_calib_lineEdit.setText("70")
        self.ui.ref_coeff_lineEdit.setText("1")
        self.cf=float(self.ui.ref_coeff_lineEdit.text())
        #refine background
        self.ui.browse_ref_1D_pushButton.clicked.connect(self.openref1D)
        self.ui.pushButton.clicked.connect(self.opensample1D)
        self.ui.calc_coeff_pushButton.clicked.connect(self.calc_coeff)
        self.ui.spec_trans_lineEdit.setText("1")
        self.ui.ref_coeff_lineEdit.setText("1")
        
        self.ui.actionfrom_scratch.triggered.connect(self.generatemask)
        self.ui.actionconvert_foxtrot_mask.triggered.connect(self.convertfoxtrotmask)
        self.ui.pixsizeH_lineEdit.setText("0.000172")
        self.ui.pixsizeV_lineEdit.setText("0.000172")
        self.ui.number_X_lineEdit.setText("981")
        self.ui.number_Y_lineEdit.setText("1043")
        self.number_pixel_x=int(self.ui.number_X_lineEdit.text())
        self.number_pixel_y=int(self.ui.number_Y_lineEdit.text())
        self.ui.calibframe_pushButton.clicked.connect(self.calibrate_frames)
        self.setponi=False
        
        self.ui.actionSWING_2.triggered.connect(self.nxs2edf_swing)
        self.ui.actionfrom_ID15_2.triggered.connect(self.nxs2edf_id15)
        self.ui.actionfrom_ID02_SAXS.triggered.connect(self.nxs2edf_id02saxs)
        self.ui.actionfrom_ID02_WAXS.triggered.connect(self.nxs2edf_id02waxs)
        self.ui.actionAverage_frames_2.triggered.connect(self.average)
        
        # intialize keys
        self.ui.key_wl_lineEdit.setText("WaveLength")
        self.ui.key_distance_lineEdit.setText("SampleDistance")
        self.ui.key_X_lineEdit.setText("Center_1")
        self.ui.key_Y_lineEdit.setText("Center_2")
        self.ui.key_sizeX_lineEdit.setText("PSize_1")
        self.ui.key_sizeY_lineEdit.setText("PSize_2")
        self.ui.key_dim1_lineEdit.setText("Dim_1")
        self.ui.key_dim2_lineEdit.setText("Dim_2")
        #self.ui.detectorName_lineEdit.setText("Pilatus 1M")
        #self.ui.pyfai_list_pushButton.clicked.connect(self.openpyfaihelp)
        self.ui.image_header_pushButton.clicked.connect(self.open_image_header)
        self.ui.calibframe_header_pushButton.clicked.connect(self.retrieve_from_header)
        return
    

    def init_form(self):   
        self.ui.ref_coeff_lineEdit.setText("1") 
        self.ui.console_textEdit.setText("")
        self.ui.console_textEdit.insertPlainText("Last value of calibration coefficient was %s"%str(self.cf)+"\n")
        self.ui.console_textEdit.insertPlainText("Last value of coefficient for reference substractions was %s"%self.ui.ref_coeff_lineEdit.text()+"\n")
        self.path=os.getcwd()
        self.n=1
        
        self.file4refpathname=""
        self.view_file=""
        self.setponi=False
        self.ui.pixsizeH_lineEdit.setText("0.000172")
        self.ui.pixsizeV_lineEdit.setText("0.000172")
        self.ui.number_X_lineEdit.setText("981")
        self.ui.number_Y_lineEdit.setText("1043")        
        self.maskpathname=""
        self.refpathname=""
        self.ui.ref_file_lineEdit.setText("")
        self.datafile_list=""
        self.ui.water_calib_file_lineEdit.setText("")
        self.water_calib_file=""
        self.ui.water_ref_calib_file_lineEdit.setText("")
        self.water_ref_calib_file=""
        self.ui.calculated_calibration_coeflineEdit.setText("")
        self.cf=1
        self.ui.transmission_I0_lineEdit.setText("")
        self.trans_I0_file=""
        self.ui.I0_lineEdit.setText("1")
        self.ui.transmission_I_calib_ref_lineEdit.setText("")
        self.trans_I_calib_ref_file =""
        self.ui.I_ref_water_lineEdit.setText("1")
        self.ui.transmission_I_calib_lineEdit.setText("")
        self.trans_I_calib_file=""              
        self.ui.I_water_lineEdit.setText("1")
        self.ui.transmission_I_ref_lineEdit.setText("")
        self.trans_I_ref_file=""              
        self.ui.Iref_lineEdit.setText("1")
        self.ui.transmission_I_sample_lineEdit.setText("")
        self.trans_I_sample_file=""             
        self.ui.Itrans_lineEdit.setText("[value1, value2,...]")
        self.ui.nb_samples_averaged_lineEdit.setText("1")
        self.ui.spec_trans_lineEdit.setText("1")
        self.ui.mask_file_lineEdit.setText("")
        self.ui.data_file_textEdit.clear()
        return
      
    def getWD(self):
        self.path=QtWidgets.QFileDialog.getExistingDirectory()
        self.ui.console_textEdit.insertPlainText("Working directory was set to %s" %self.path + "\n")
        return self.path  
    
    def nxs2edf_swing(self):
        self.nxs_files=QtWidgets.QFileDialog.getOpenFileNames( self,"Open image file(s)","%s"%self.path,"*.nxs")
        file_list=self.nxs_files[0]
        try:
            file=file_list[0]
            directory=os.path.dirname(file)
            #create output directory
            outputedf=directory+'/edf_from_nxs/'
            if not os.path.exists(outputedf):
                os.makedirs(outputedf)          
            for nxs_file in self.nxs_files[0]:
                with h5py.File(nxs_file, "r") as f:
                    filename=str(nxs_file)
                    # get first object key; it corresponds to a group
                    group = list(f.keys())[0]
                    nb_frames=f[group+'/SWING/EIGER-4M/nb_frames'][0]                   
                    
                    ### RETRIEVE IMAGE DATA
                    target=group+'/scan_data/eiger_image'
                    data = np.array(f[target])      # returns as a np array for RGB image data
                    
                    # check for headr infofrom scratch
                    target=group+'/SWING/ans__ca__machinestatus/current'
                    current=f[target][0]
                    #normalize data by source current (equivalent to monitor normalization)
                    #data/=current
                    target=group+'/SWING/EIGER-4M'
                    # get distance and convert from mm to m
                    distance_m=(f[target+'/distance'][0])/1000
                    pixel_size_x=f[target+'/pixel_size_x'][0]*0.000001
                    pixel_size_z=f[target+'/pixel_size_z'][0]*0.000001
                    x_center=f[target+'/dir_beam_x'][0]
                    z_center=f[target+'/dir_beam_z'][0]
                    num_pixel_x=len(data[1])
                    num_pixel_z=len(data[2])
                    bin_x=f[target+'/binning_x'][0]
                    bin_y=f[target+'/binning_y'][0]                    
                                    
                    #retrieve wavelength
                    target=group+'/SWING/i11-c-c03__op__mono'
                    wl=(f[target+'/wavelength'][0])*1e-10
                header={"title":str(group),"WaveLength":float(wl),"Center_1":float(x_center),"Center_2":float(z_center),"PSize_1":float(pixel_size_x),"PSize_2":float(pixel_size_z),"SampleDistance":float(distance_m),"Dim_1":int(num_pixel_x),"Dim_2":int(num_pixel_z),"ExposureTime":1,'MachineCurrent':float(current),'Binning_1':int(bin_x),'Binning_2':int(bin_y)}
                
                for i in range(nb_frames):
                    data_ok=data[i,:,:]
                    #creation ficher edf
                    outputname=outputedf+group+"_"+f'{i:{0}{4}}'+".edf"
                    obj = fabio.edfimage.EdfImage(header=header,data=data_ok)
                    obj.write(outputname)
            self.ui.console_textEdit.insertPlainText("Conversion of .nxs files to .edf files completed.\n")
            self.ui.console_textEdit.insertPlainText("Meta-data are: %s"%header+'\n')
            self.ui.console_textEdit.insertPlainText("Files are stored in %s"%outputedf+"\n")
            redColor = QColor(255, 0, 0)
            blackColor = QColor(0, 0, 0)
            self.ui.console_textEdit.setTextColor(redColor)
            self.ui.console_textEdit.insertPlainText("WARNING: DETECTOR CALIBRATION  REQUIRED\n")
            self.ui.console_textEdit.insertPlainText("Header in the generated edf files contain calibration information (leave default parameters, simply click Apply Calibration).\n")
            self.ui.console_textEdit.setTextColor(blackColor)
        except:
            filename=str(nxs_file)
            self.ui.console_textEdit.insertPlainText("Crashed at file %s"%filename+"\n")
            pass
        return
    
    def nxs2edf_id15(self):
        self.nxs_files=QtWidgets.QFileDialog.getOpenFileNames( self,"Open image file(s)","%s"%self.path)
        file_list=self.nxs_files[0]
        try:
            file=file_list[0]
            directory=os.path.dirname(file)
            #create output directory
            outputedf=directory+'/edf_from_h5/'
            if not os.path.exists(outputedf):
                os.makedirs(outputedf)          
            for nxs_file in self.nxs_files[0]:
                with h5py.File(nxs_file, "r") as f:
                    
                    # get first object key; it corresponds to a group
                    group = list(f.keys())[0]
                    nb_frames=f[group+'/instrument/pilatus/acquisition/nb_frames'][()]                   
                    
                    ### RETRIEVE IMAGE DATA
                    target=group+'/measurement/data'
                    data = np.array(f[target])      # returns as a np array for RGB image data
                    shape=np.shape(data)
                    # check for headr info
                    target=group+'/instrument/pilatus/detector_information/pixel_size/'
                    # get distance and convert from mm to m
                    #distance_m=(f[target+'/distance'][0])/1000
                    pixel_size_x=f[target+'/xsize'][()]
                    pixel_size_z=f[target+'/ysize'][()]
                    #x_center=f[target+'/dir_beam_x'][0]
                    #z_center=f[target+'/dir_beam_z'][0]
                    num_pixel_x=shape[1]
                    num_pixel_z=shape[2]
                                    
                    
                header={"title":str(group),"PSize_1":pixel_size_x,"PSize_2":pixel_size_z,"Dim_1":num_pixel_x,"Dim_2":num_pixel_z,"ExposureTime":1}
                
                for i in range(nb_frames):
                    data_ok=data[i,:,:]
                    #creation ficher edf
                    fname=Path(nxs_file).stem
                    outputname=outputedf+fname+"_"+f'{i:{0}{4}}'+".edf"
                    obj = fabio.edfimage.EdfImage(header=header,data=data_ok)
                    obj.write(outputname)
            self.ui.console_textEdit.insertPlainText("Conversion of .nxs files to .edf files completed.\n")
            self.ui.console_textEdit.insertPlainText("Meta-data are: %s"%header+'\n')
            redColor = QColor(255, 0, 0)
            blackColor = QColor(0, 0, 0)
            self.ui.console_textEdit.setTextColor(redColor)
            self.ui.console_textEdit.insertPlainText("WARNING: DETECTOR CALIBRATION  REQUIRED\n")
            self.ui.console_textEdit.setTextColor(blackColor)
            self.ui.console_textEdit.insertPlainText("Files are stored in %s"%outputedf+"\n")
        except:
            pass
        return 
    
    
    def nxs2edf_id02saxs(self):
        self.nxs_files=QtWidgets.QFileDialog.getOpenFileNames( self,"Open image file(s)","%s"%self.path)
        file_list=self.nxs_files[0]
        try:
            file=file_list[0]
            directory=os.path.dirname(file)
            #create output directory
            outputedf=directory+'/edf_from_h5/'
            if not os.path.exists(outputedf):
                os.makedirs(outputedf)          
            for nxs_file in self.nxs_files[0]:
                with h5py.File(nxs_file, "r") as f:
                    
                    # get first object key; it corresponds to a group
                    group = list(f.keys())[0]
                    nb_frames=f[group+'/instrument/id02-eiger2-saxs/acquisition/nb_frames'][()]
                    acq_time=f[group+'/instrument/id02-eiger2-saxs/acquisition/exposure_time'][()]
                    ### RETRIEVE IMAGE DATA
                    target=group+'/measurement/data'
                    data = np.array(f[target])      
                    shape=np.shape(data)
                    num_pixel_x=shape[1]
                    num_pixel_z=shape[2]                
                    # check for headr info
                    
                    header=group+'/instrument/id02-eiger2-saxs/header'
                    # pixel_size
                    pixel_size_x=f[header+'/PSize_1'][()]
                    pixel_size_z=f[header+'/PSize_2'][()]
                    #Wavelength
                    wl=f[header+'/WaveLength'][()]
                    # beam center
                    x_center=f[header+'/Center_1'][()]
                    z_center=f[header+'/Center_2'][()]
                    # distance
                    distance=f[header+'/SampleDistance'][()]
                    # monitor
                    machine_info=f[header+'/MachineInfo'][()]
                    current=machine_info[3:9]
                    norm_factor=f[header+'/NormalizationFactor'][()]
                    
                    header='/entry_0000/instrument/id02-eiger2-saxs/image_operation/binning'
                    bin_x=f[header+'/x'][()]
                    bin_y=f[header+'/y'][()]
                    
                                    
                    
                header={"title":str(group),"WaveLength":float(wl),"Center_1":float(x_center),"Center_2":float(z_center),"PSize_1":float(pixel_size_x),"PSize_2":float(pixel_size_z),"SampleDistance":float(distance),"Dim_1":int(num_pixel_x),"Dim_2":int(num_pixel_z),"ExposureTime":float(acq_time),"NormalizationFactor":float(norm_factor),'MachineInfo':float(current),'Binning_1':int(bin_x),'Binning_2':int(bin_y)}
                
                for i in range(nb_frames):
                    data_ok=data[i,:,:]
                    #creation ficher edf
                    fname=Path(nxs_file).stem
                    outputname=outputedf+fname+"_"+f'{i:{0}{4}}'+".edf"
                    obj = fabio.edfimage.EdfImage(header=header,data=data_ok)
                    obj.write(outputname)
            self.ui.console_textEdit.insertPlainText("Conversion of .nxs files to .edf files completed.\n")
            self.ui.console_textEdit.insertPlainText("Meta-data are: %s"%header+'\n')
            redColor = QColor(255, 0, 0)
            blackColor = QColor(0, 0, 0)
            self.ui.console_textEdit.setTextColor(redColor)
            self.ui.console_textEdit.insertPlainText("WARNING: DETECTOR CALIBRATION  REQUIRED\n")
            self.ui.console_textEdit.insertPlainText("Header in the generated edf files contain calibration information (leave default parameters, simply click Apply Calibration).\n")
            self.ui.console_textEdit.setTextColor(blackColor)
            self.ui.console_textEdit.insertPlainText("Files are stored in %s"%outputedf+"\n")
        except:
            pass
        return    
    
    def nxs2edf_id02waxs(self):
        self.nxs_files=QtWidgets.QFileDialog.getOpenFileNames( self,"Open image file(s)","%s"%self.path)
        file_list=self.nxs_files[0]
        try:
            file=file_list[0]
            directory=os.path.dirname(file)
            #create output directory
            outputedf=directory+'/edf_from_h5/'
            if not os.path.exists(outputedf):
                os.makedirs(outputedf)          
            for nxs_file in self.nxs_files[0]:
                with h5py.File(nxs_file, "r") as f:
                    
                    # get first object key; it corresponds to a group
                    group = list(f.keys())[0]
                    nb_frames=f[group+'/instrument/id02-rayonixhs-waxs/acquisition/nb_frames'][()]
                    acq_time=f[group+'/instrument/id02-rayonixhs-waxs/acquisition/exposure_time'][()]
                    ### RETRIEVE IMAGE DATA
                    target=group+'/measurement/data'
                    data = np.array(f[target])      
                    shape=np.shape(data)
                    num_pixel_x=shape[1]
                    num_pixel_z=shape[2]                
                    # check for headr info
                    
                    header=group+'/instrument/id02-rayonixhs-waxs/header'
                    # pixel_size
                    pixel_size_x=f[header+'/PSize_1'][()]
                    pixel_size_z=f[header+'/PSize_2'][()]
                    #Wavelength
                    wl=f[header+'/WaveLength'][()]
                    # beam center
                    x_center=f[header+'/Center_1'][()]
                    z_center=f[header+'/Center_2'][()]
                    # distance
                    distance=f[header+'/SampleDistance'][()]
                    # monitor
                    machine_info=f[header+'/MachineInfo'][()]
                    current=machine_info[3:9]
                    norm_factor=f[header+'/NormalizationFactor'][()]
                    header='/entry_0000/instrument/id02-rayonixhs-waxs/image_operation/binning'
                    bin_x=f[header+'/x'][()]
                    bin_y=f[header+'/y'][()]                    
                                    
                    
                header={"title":str(group),"WaveLength":float(wl),"Center_1":float(x_center),"Center_2":float(z_center),"PSize_1":float(pixel_size_x),"PSize_2":float(pixel_size_z),"SampleDistance":float(distance),"Dim_1":int(num_pixel_x),"Dim_2":int(num_pixel_z),"ExposureTime":float(acq_time),"NormalizationFactor":float(norm_factor),'MachineInfo':float(current),'Binning_1':int(bin_x),'Binning_2':int(bin_y)}
                
                for i in range(nb_frames):
                    data_ok=data[i,:,:]
                    #creation ficher edf
                    fname=Path(nxs_file).stem
                    outputname=outputedf+fname+"_"+f'{i:{0}{4}}'+".edf"
                    obj = fabio.edfimage.EdfImage(header=header,data=data_ok)
                    obj.write(outputname)
            self.ui.console_textEdit.insertPlainText("Conversion of .nxs files to .edf files completed.\n")
            self.ui.console_textEdit.insertPlainText("Meta-data are: %s"%header+'\n')
            redColor = QColor(255, 0, 0)
            blackColor = QColor(0, 0, 0)
            self.ui.console_textEdit.setTextColor(redColor)
            self.ui.console_textEdit.insertPlainText("WARNING: DETECTOR CALIBRATION  REQUIRED\n")
            self.ui.console_textEdit.insertPlainText("Header in the generated edf files contain calibration information (leave default parameters, simply click Apply Calibration).\n")
            self.ui.console_textEdit.setTextColor(blackColor)
            self.ui.console_textEdit.insertPlainText("Files are stored in %s"%outputedf+"\n")
        except:
            pass
        return        
    
    ###Viewer   
    
    def openfile4viewer(self):
        
        self.view_file_path=QtWidgets.QFileDialog.getOpenFileName( self,"Open image file","%s"%self.path)
        try:
            self.view_file=self.view_file_path[0]
            ext=self.view_file.split('.')[1]
            if self.view_file!='':
                if ext=="dat":
                    self.ui.console_textEdit.insertPlainText("CAUTION: Plotting of 2D dat files is still under development.\n What you see may not correspond to the real image\n")
                    data=np.array(np.loadtxt(self.view_file))
                    
                    
                    qx=data[:,:,0]
                    qy=data[:,:,1]
                    intensity=data[:,:,2]
        
                    
                    i=0
                    while qy[i]==qy[i+1]:
                        i=i+1
                    nb_ligne=int(i+1)
                    nb_col=int(len(qx)/nb_ligne) 
                    print(nb_col,nb_ligne)
                    
                    tab=np.zeros((nb_ligne,nb_col,3),dtype=np.uint8)
                    data[:,0]=intensity
                    data[:,1]=qx
                    data[:,2]=qy
                    
                    for i in range(nb_ligne):
                        for j in range(nb_col):
                            tab[i,j]=data[j+i*nb_ligne,:]
                       
                    #scale=np.meshgrid(data[:,1],data[:,2],sparse=True)[0]
                    #print(scale)
                    plt.imshow(tab)
                    plt.show()
                else:
                    try:           
                        os.system ("fabio_viewer %s" %self.view_file)
                    except:
                        self.ui.console_textEdit.insertPlainText("Image file format not supported by fabio library.\n")
            else:
                self.ui.console_textEdit.insertPlainText("An error occured, please try again.\n")
        except:
            self.ui.console_textEdit.insertPlainText("An error occured, please try again.\n")            
        return self.view_file
    
    def plotloglog(self):
        
        filelist=QtWidgets.QFileDialog.getOpenFileNames( self,"Open 1D data file","%s"%self.path)
        filenames=filelist[0]
        
        plt.figure(1)
        plt.xlabel(r'Q (1/ $\mathrm{\AA}$ )')
        plt.ylabel(r'I (1/cm)')
        i=0
        for file in filenames:
            #print(file)
            label=Path(file).stem
            q,i=np.loadtxt(str(file),unpack=True,skiprows=2)
        
            plt.loglog(q,i,label=label)
            i+=1
        plt.legend()
        plt.show()
        return
    
    def plotlinear(self):
        
        filelist=QtWidgets.QFileDialog.getOpenFileNames( self,"Open 1D data file","%s"%self.path)
        filenames=filelist[0]
        
        plt.figure(1)
        plt.xlabel(r'Q (1/ $\mathrm{\AA}$ )')
        plt.ylabel(r'I (1/cm)')
        i=0
        for file in filenames:
            #print(file)
            label=Path(file).stem
            q,i=np.loadtxt(str(file),unpack=True,skiprows=2)
        
            plt.plot(q,i,label=label)
            i+=1
        plt.legend()
        plt.show()
        return    
  
   ######Mask 
    def setponifile(self):
        try:
            self.ponipath=QtWidgets.QFileDialog.getOpenFileNames( self,"Open detector calibration file","%s"%self.path,"poni file *.poni" )
            self.poniname=self.ponipath[0]
            res=os.path.basename(self.poniname[0])
            self.ui.poniFile_lineEdit.setText(res)
            if res!='':
                self.ui.console_textEdit.insertPlainText("Poni file successfully provided.\n")
            else:
                self.ui.console_textEdit.insertPlainText("No poni file provided, please try again\n")            
            
        except:
            self.ui.console_textEdit.insertPlainText("An error occured, please try again \n")        
        return self.poniname
    
    def calibrate_frames(self):
        try:
            f=open(self.poniname[0],'r')
            contenu=f.readlines()
            content=dict()
            for line in contenu[2:]:
                x=line.split(":")
                item=str(x[0])
                val=(x[1])
                content.update({item:val})
            
            self.distance=float(content['Distance'])
            poni1=float(content['Poni1'])
            poni2=float(content['Poni2'])
            Rot1=float(content['Rot1'])
            Rot2=float(content['Rot2'])
            Rot3=float(content['Rot3'])
            self.wl=float(content['Wavelength'])
            #print('lambda',self.wl)
            pixel_sizeH=float(self.ui.pixsizeH_lineEdit.text())
            pixel_sizeV=float(self.ui.pixsizeV_lineEdit.text())
            self.pix_size=pixel_sizeH
            self.x_center=(1/pixel_sizeH)*abs(poni2-self.distance*math.tan(Rot1))
            self.y_center=(1/pixel_sizeV)*abs(poni1+self.distance*(math.tan(Rot2)/math.cos(Rot1)))
            self.number_pixel_x=int(self.ui.number_X_lineEdit.text())
            self.number_pixel_y=int(self.ui.number_Y_lineEdit.text())
            self.setponi=True
            self.ui.console_textEdit.insertPlainText("Sample to detector distance is %s"%str(self.distance)+"m.\n")
            self.ui.console_textEdit.insertPlainText("Beam center X coordinate (pixels) is: %s"%str(self.x_center)+"\n")
            self.ui.console_textEdit.insertPlainText("Beam center Y coordinate (pixels) is %s"%str(self.y_center)+"\n")
            self.ui.console_textEdit.insertPlainText("Wavelength is %f"%(1e10*self.wl)+"angströms. \n")
        except:
            self.ui.console_textEdit.insertPlainText("No poni file provided, please try again\n")
        return
    
    def open_image_header(self):
        try:
            self.header=QtWidgets.QFileDialog.getOpenFileNames( self,"Open Reference image file","%s"%self.path)
            self.headername=self.header[0]
            res = ''.join(os.path.basename(i) + '\n' 
                               for i in self.headername)
            self.ui.image_header_lineEdit.setText(res) 
            #print(self.headername[0])
        except:
            self.ui.console_textEdit.insertPlainText("An error occured, please try again \n")
        return self.headername     
    
    def retrieve_from_header(self):
        try:
            image=fabio.open(self.headername[0])
            header=image.header
            self.wl=float(header[self.ui.key_wl_lineEdit.text()])
            print(self.wl)
            self.x_center = float(header[self.ui.key_X_lineEdit.text()])
            self.y_center = float(header[self.ui.key_Y_lineEdit.text()])
            self.pix_size = float(header[self.ui.key_sizeX_lineEdit.text()])
            self.distance = float(header[self.ui.key_distance_lineEdit.text()])
            self.number_pixel_x = int(header[self.ui.key_dim1_lineEdit.text()])
            self.number_pixel_y = int(header[self.ui.key_dim2_lineEdit.text()])        
            self.ui.console_textEdit.insertPlainText("Sample to detector distance is %s"%str(self.distance)+"m.\n")
            self.ui.console_textEdit.insertPlainText("Beam center X coordinate (pixels) is: %s"%str(self.x_center)+"\n")
            self.ui.console_textEdit.insertPlainText("Beam center Y coordinate (pixels) is %s"%str(self.y_center)+"\n")
            self.ui.console_textEdit.insertPlainText("Wavelength is %s"%(str(self.wl))+" angströms. \n") 
            self.ui.console_textEdit.insertPlainText("Frame size is %d"%self.number_pixel_x+"X%d"%self.number_pixel_y +"pixels. \n") 
            self.ui.console_textEdit.insertPlainText("Pixel size is %f"%self.pix_size+"m. \n")
            try:
                bin_x=int(header['Binning_1'])
                bin_y=int(header['Binning_2'])
            except:
                bin_x=1
                bin_y=1
            ## Generate poni file
            poni1=self.pix_size*self.y_center*bin_y
            poni2=self.pix_size*self.x_center*bin_x
            poniname=self.path+"/calibration_detector.poni"
            
            line2write="# Nota: C-Order, 1 refers to the Y axis, 2 to the X axis \n"
            line2write+="poni_version: 2\n"
            line2write+="Detector: Detector \n"
            #line2write+="Detector: %s"%str(self.ui.detectorName_lineEdit.text())+"\n"
            #line2write+="{} \n"
            line2write+='Detector_config: {"pixel1":%f'%(bin_y*self.pix_size)+', "pixel2":%f'%(bin_x*self.pix_size)+', "max_shape": [%d'%self.number_pixel_y+', %d'%self.number_pixel_x+']} \n'
            line2write+="Distance: %f"%self.distance+"\n"
            line2write+="Poni1: %f"%poni1+"\n"
            line2write+="Poni2: %f"%poni2+"\n"
            line2write+="Rot1: 0.0 \n"
            line2write+="Rot2: 0.0 \n"
            line2write+="Rot3: 0.0 \n"
            line2write+="Wavelength: %s"%str(self.wl)+"\n"
            print(line2write)
            with open(poniname, 'w') as f:
                f.write(line2write)
            self.ui.console_textEdit.insertPlainText("The corresponding poni file was generated as %s"%str(poniname)+". \n")
            
        except:
            self.ui.console_textEdit.insertPlainText("Please provide an image file.\n")
        return

#fonctions pour le moyennage des images de réfèrences
        
    def average(self):
        try:
        #n=int(self.ui.nb_ref_averaged_lineEdit.text())
            self.file4refpath=QtWidgets.QFileDialog.getOpenFileNames( self,"Open images to average","%s"%self.path)
            self.file4refpathname=self.file4refpath[0]        
            n=len(self.file4refpathname)
            self.liste_de_n_fichiers=[]
            for j in range(n):
                self.liste_de_n_fichiers.append(str(self.file4refpathname[j]))
                
            liste=' '.join(self.liste_de_n_fichiers)
            directory=os.path.dirname(self.liste_de_n_fichiers[0])
            outputname=directory+'/'+str(os.path.basename(self.liste_de_n_fichiers[0]).split('.')[0])+"_"+str(os.path.basename(self.liste_de_n_fichiers[-1]).split('.')[0])+"_averaged-ref.edf"
                   
            self.ui.console_textEdit.insertPlainText("Averaging of %d" %n+ " provided frames \n")
            self.ui.console_textEdit.insertPlainText("The averaged file is saved in %s \n"%outputname)
            
            #os.system ("pyFAI-average -o %s" %outputname +" %s"%liste)
            os.system ("pyFAI-average -o %s" %self.path+"average.edf %s"%liste)
            image_avg=fabio.open(self.path+"average.edf")
            data_average=image_avg.data
            image_head=fabio.open(self.file4refpathname[0])
            header_calib=image_head.header
            obj = fabio.edfimage.EdfImage(header=header_calib,data=data_average)
            obj.write(outputname)
            os.remove(self.path+"average.edf")
        except:
            self.ui.console_textEdit.insertPlainText("An error occured, please try again \n")        
        return
        
        
    def generatemask(self):
        try:
            self.file4maskpath=QtWidgets.QFileDialog.getOpenFileNames( self,"Open image file to generate a mask","%s"%self.path)
            self.file4maskpathname=self.file4maskpath[0]
            #print('mask_file',self.file4maskpathname[0])
            #self.ui.console_textEdit.insertPlainText("Use pyFAI-drawmask to create a mask file\n")
            os.chdir(self.path)
            os.system ("pyFAI-drawmask %s"%self.file4maskpathname[0]) 
        except:
            self.ui.console_textEdit.insertPlainText("An error occured, please try again \n")        
        return
    
    def convertfoxtrotmask(self):
        try:
            self.foxtrotmask=QtWidgets.QFileDialog.getOpenFileNames( self,"Open Foxtrot mask file","%s"%self.path,"Foxtrot mask *.txt" )
            maskfilearr=self.foxtrotmask[0]
            maskfile=maskfilearr[0]
            print(maskfile)
            maskarray=np.loadtxt(maskfile,delimiter=';')
            mask_ok=1-maskarray
            num_X,num_Y=np.shape(mask_ok)
            outputname=os.path.splitext(maskfile)[0]+".edf"
            obj = fabio.edfimage.EdfImage(data=mask_ok)
            obj.write(outputname)
            os.system("fabio_viewer %s"%str(outputname))
            self.ui.console_textEdit.insertPlainText('Foxtrot mask converted to .edf format in %s'%outputname+'\n')
        except:
            self.ui.console_textEdit.insertPlainText("An error occured, please try again \n")        
        return
        
        
        
    def openmaskfile(self):
        
        try:
            global a
            self.maskpath=QtWidgets.QFileDialog.getOpenFileNames( self,"Open pyFAI Mask File(s)","%s"%self.path,"Mask file from pyFAI *.edf" )
            self.maskpathname=self.maskpath[0]
            res = ''.join(os.path.basename(i) + '\n' 
                               for i in self.maskpathname)
            self.ui.mask_file_lineEdit.setText(res)
            a=1 #variable for check function
            if res!='':
                self.ui.console_textEdit.insertPlainText("Mask file successfully provided.\n")
            else:
                self.ui.console_textEdit.insertPlainText("No mask file provided, please try again\n")
        except:
            self.ui.console_textEdit.insertPlainText("An error occured, please try again \n")        
        return self.maskpathname
    
    def openreffile(self):
        try:
            global b
            self.refpath=QtWidgets.QFileDialog.getOpenFileNames( self,"Open Reference image file","%s"%self.path)
            self.refpathname=self.refpath[0]
            res = ''.join(os.path.basename(i) + '\n' 
                               for i in self.refpathname)
            self.ui.ref_file_lineEdit.setText(res) 
            b=1 #variable for check function
            #self.ui.console_textEdit.insertPlainText("Reference data file provided!\n")
            if res!='':
                self.ui.console_textEdit.insertPlainText("Reference file successfully provided.\n")
            else:
                self.ui.console_textEdit.insertPlainText("No reference file provided, please try again\n")            
        except:
            self.ui.console_textEdit.insertPlainText("An error occured, please try again \n")         
        return self.refpathname    
        
        
    def opendatafiles (self):
        try:
            
            self.datapath= QtWidgets.QFileDialog.getOpenFileNames( self,"Open Data File(s)","%s"%self.path)
            self.datafile_list=self.datapath[0]
            res = ''.join(os.path.basename(i) + '\n' 
                               for i in self.datafile_list)
            self.ui.data_file_textEdit.insertPlainText(res) 
            #self.ui.console_textEdit.insertPlainText("Sample data file provided!\n")
            if res!='':
                self.ui.console_textEdit.insertPlainText("Sampe data file successfully provided.\n")
            else:
                self.ui.console_textEdit.insertPlainText("No data file provided, please try again\n")            
        except:
            self.ui.console_textEdit.insertPlainText("An error occured, please try again \n")         
        #print (str(self.datafile_list))        
        return self.datafile_list
    
            
    
    
#fonctions pour la calibration

    def openfile_calib_water(self):
        try:
            self.file=QtWidgets.QFileDialog.getOpenFileNames( self,"Open data file for calibrant measurement","%s"%self.path)
            self.water_calib_file=self.file[0]
            res=os.path.basename(self.water_calib_file[0])
            self.ui.water_calib_file_lineEdit.setText(res)
            if res!='':
                self.ui.console_textEdit.insertPlainText("Calibration file successfully provided.\n")
            else:
                self.ui.console_textEdit.insertPlainText("No calibration file provided, please try again\n")            
        except:
            self.ui.console_textEdit.insertPlainText("An error occured, please try again \n")         
        return self.water_calib_file 
     
        
    def openfile_calib_water_ref(self):
        try:
            self.file=QtWidgets.QFileDialog.getOpenFileNames( self,"Open data file for empty cell measurement","%s"%self.path)
            self.water_ref_calib_file=self.file[0]
            res=os.path.basename(self.water_ref_calib_file[0])
            self.ui.water_ref_calib_file_lineEdit.setText(res)
            if res!='':
                self.ui.console_textEdit.insertPlainText("Reference file for calibration successfully provided.\n")
            else:
                self.ui.console_textEdit.insertPlainText("No reference file provided, please try again\n")            
        except:
            self.ui.console_textEdit.insertPlainText("An error occured, please try again \n")         
        return self.water_ref_calib_file 

      
    def calibration(self): 
        try:
            I_0=float(self.ui.I0_lineEdit.text())
            I_water_ref=float(self.ui.I_ref_water_lineEdit.text())
            I_water=float(self.ui.I_water_lineEdit.text())
            if self.ui.water_checkBox.isChecked()==True:
                self.ui.console_textEdit.insertPlainText('Water calibrant selected (SLD=0.0162).\n')
                I_th=0.0162
            elif self.ui.hexane_checkBox.isChecked()==True:
                self.ui.console_textEdit.insertPlainText('Hexane calibrant selected (SLD=0.028).\n')
                I_th=0.028
            else:
                I_th=float(self.ui.lineEdit.text())
            water=fabio.open(str(self.water_calib_file[0]))
            header_water=water.header
            #water_acq_time=float(header_water["ExposureTime"])
            intensity_water=water.data
            
            water_ref=fabio.open(str(self.water_ref_calib_file[0]))
            header_water_ref=water_ref.header
            #water_ref_acq_time=float(header_water_ref["ExposureTime"])
            intensity_water_ref=water_ref.data
            x_center=int(self.ui.x_center_lineEdit.text());y_center=int(self.ui.y_center_lineEdit.text())
           
            width_x=int(self.ui.window_width_calib_lineEdit.text())
            width_y=int(self.ui.window_width_calib_lineEdit.text())
            
            x1=y_center-width_y;x2=y_center+width_y
            y1=x_center-width_x;y2=x_center+width_x
            
            i_water=np.mean(intensity_water[x1:x2,y1:y2])
            std_water=np.std(intensity_water[x1:x2,y1:y2])        
            i_water_ref=np.mean(intensity_water_ref[x1:x2,y1:y2])
            std_ref=np.std(intensity_water_ref[x1:x2,y1:y2])        
             
            i_ref_trans=(I_0/I_water_ref)*i_water_ref
            i_cal_trans=(I_0/I_water)*i_water
            self.ui.console_textEdit.insertPlainText('Calculated mean reference intensity is %f'%i_water_ref+' with standard deviation %f'%(std_ref*(I_0/I_water_ref))+'.\n')
            self.ui.console_textEdit.insertPlainText('Calculated mean reference intensity, after transmission correction is %f'%i_ref_trans+'.\n')
            self.ui.console_textEdit.insertPlainText('Calculated mean calibrant intensity is %f'%i_water+' with standard deviation %f'%((I_0/I_water)*std_water)+'.\n')
            self.ui.console_textEdit.insertPlainText('Calculated mean calibrant intensity, after transmission correction is %f'%i_cal_trans+'.\n')        
            
            
            i=(I_0/ I_water)*i_water - (I_0/ I_water_ref)*i_water_ref
            #print('net intensity=',i)
            self.ui.console_textEdit.insertPlainText('Calculated net intensity is %f'%i+'.\n')
            self.cf=I_th/i
            self.ui.console_textEdit.insertPlainText('The calibration coefficient is %4f'%self.cf+'.\n')
            self.ui.calculated_calibration_coeflineEdit.setText(str(self.cf)[:6])
        except:
            self.ui.console_textEdit.insertPlainText("Missing arguments, please check.\n")
        return self.cf



#fonctions integration/calibration

    def pyFAI_calib(self):
        #os.system ("cd %s" %self.path)
        os.chdir(self.path)
        os.system ("pyFAI-calib2")
        
    def pyFAI_integrate(self):
        os.chdir(self.path)
        os.system ("pyFAI-integrate")
        
################################# Fonctions de calcul des transmissions        
    
    def calc_transmission(self,frame):
        """
        cette fonction calcule la transmission à partir d'une image de transmission, en moyennant l'intensité transmise
        La variable frame contient le chemin d'accès au fichier edf.
        La variable window_width correspond à la largeur du carré d'intégration
        """
        filename, file_extension = os.path.splitext(frame)
        image = fabio.open(frame)
        header=image.header
        #acq_time=float(header["ExposureTime"])
        intensity=image.data
        
        if self.setponi==False:
            
            if file_extension=='.edf':
                header = (image.header)
                self.wl = float(header["WaveLength"])*1e10
                self.x_center = math.ceil(float(header["Center_1"]))
                self.y_center = math.ceil(float(header["Center_2"]))
                
        window_with=int(self.ui.window_width_trans_lineEdit.text())
        xmin=int(self.x_center-window_with)
        xmax=int(self.x_center+window_with)
        ymin=int(self.y_center-window_with)
        ymax=int(self.y_center+window_with)
        shape=(ymax-ymin,xmax-xmin)
        i_masked=np.empty(shape)
        i_masked=intensity[ymin:ymax,xmin:xmax]
        transmission=np.average(i_masked)
        return transmission
    
    ## Calcul de I0
    def openfile_trans_I0(self):
        try:
            self.I0file=QtWidgets.QFileDialog.getOpenFileName( self,"Open image file for empty beam transmission","%s"%self.path )
            
            self.trans_I0_file=Path(str(self.I0file[0]))
            res=os.path.basename(self.I0file[0])
            
            self.ui.transmission_I0_lineEdit.setText(res)
            if res!='':
                self.ui.console_textEdit.insertPlainText("Transmission file successfully provided.\n")
            else:
                self.ui.console_textEdit.insertPlainText("No transmission file provided, please try again\n")            
        except:
            self.ui.console_textEdit.insertPlainText("An error occured, please try again \n")         
        return self.trans_I0_file  
    
    def calc_trans_I0(self):
        try:
            I0=self.calc_transmission(self.trans_I0_file)
            self.ui.I0_lineEdit.setText(str(I0))
            self.ui.console_textEdit.insertPlainText("Empty beam transmission calculated as %s"%str(I0)+"\n")
        except:
            self.ui.console_textEdit.insertPlainText("Missing data file or specify widow width.\n")
            
        return
    
    ## Calcul de I_calib_ref
    def openfile_trans_I_calib_ref(self):
        try:
            self.I_calib_reffile=QtWidgets.QFileDialog.getOpenFileName( self,"Open image file for empty cell transmission","%s"%self.path)
            self.trans_I_calib_ref_file=Path(str(self.I_calib_reffile[0]))
            res=os.path.basename(self.I_calib_reffile[0])
            self.ui.transmission_I_calib_ref_lineEdit.setText(res)
            if res!='':
                self.ui.console_textEdit.insertPlainText("Transmission file successfully provided.\n")
            else:
                self.ui.console_textEdit.insertPlainText("No transmission file provided, please try again\n")            
        except:
            self.ui.console_textEdit.insertPlainText("An error occured, please try again \n")         
        return self.trans_I_calib_ref_file  
    
    def calc_trans_I_calib_ref(self):
        try:
            I_calib_ref=self.calc_transmission(self.trans_I_calib_ref_file)
            self.ui.I_ref_water_lineEdit.setText(str(I_calib_ref))
            self.ui.console_textEdit.insertPlainText("Empty cell transmission calculated as %s"%str(I_calib_ref)+"\n")
        except:
            self.ui.console_textEdit.insertPlainText("Missing data file or specify widow width.\n")        
        return
    
    ## Calcul de I_calib
    def openfile_trans_I_calib(self):
        try:
            self.I_calib_file=QtWidgets.QFileDialog.getOpenFileName( self,"Open image file for calibrant transmission","%s"%self.path)
            self.trans_I_calib_file=Path(str(self.I_calib_file[0]))
            res=os.path.basename(self.I_calib_file[0])
            self.ui.transmission_I_calib_lineEdit.setText(res)
            if res!='':
                self.ui.console_textEdit.insertPlainText("Transmission file successfully provided.\n")
            else:
                self.ui.console_textEdit.insertPlainText("No transmission file provided, please try again\n")            
        except:
            self.ui.console_textEdit.insertPlainText("An error occured, please try again \n")         
        return self.trans_I_calib_file  
    
    def calc_trans_I_calib(self):
        try:
            I_calib=self.calc_transmission(self.trans_I_calib_file)
            self.ui.I_water_lineEdit.setText(str(I_calib))
            self.ui.console_textEdit.insertPlainText("Calibrant transmission calculated as %s"%str(I_calib)+"\n")
        except:
            self.ui.console_textEdit.insertPlainText("Missing data file or specify widow width.\n")        
        return  
    
    ## Calcul de I_ref
    def openfile_trans_I_ref(self):
        try:
            self.I_ref_file=QtWidgets.QFileDialog.getOpenFileName( self,"Open image file for reference transmission","%s"%self.path)
            self.trans_I_ref_file=Path(str(self.I_ref_file[0]))
            res=os.path.basename(self.I_ref_file[0])
            self.ui.transmission_I_ref_lineEdit.setText(res)
            if res!='':
                self.ui.console_textEdit.insertPlainText("Transmission file successfully provided.\n")
            else:
                self.ui.console_textEdit.insertPlainText("No transmission file provided, please try again\n")            
        except:
            self.ui.console_textEdit.insertPlainText("An error occured, please try again \n")         
        return self.trans_I_ref_file  
    
    def calc_trans_I_ref(self):
        try:
            I_ref=self.calc_transmission(self.trans_I_ref_file)
            self.ui.Iref_lineEdit.setText(str(I_ref))
            self.ui.console_textEdit.insertPlainText("Reference transmission calculated as %s"%str(I_ref)+"\n")
        except:
            self.ui.console_textEdit.insertPlainText("Missing data file or specify widow width.\n")        
        return     
    
    ## Calcul de I_sample
    def openfile_trans_I_sample(self):
        try:
            self.I_sample_file=QtWidgets.QFileDialog.getOpenFileNames( self,"Open image files for specimen transmission","%s"%self.path)
            
            self.trans_I_sample_file=self.I_sample_file[0]
            res = ''.join(os.path.basename(i) + '\n' 
                               for i in self.trans_I_sample_file)
            self.ui.transmission_I_sample_lineEdit.setText(res)
            if res!='':
                self.ui.console_textEdit.insertPlainText("Transmission file successfully provided.\n")
            else:
                self.ui.console_textEdit.insertPlainText("No transmission file provided, please try again\n")            
        except:
            self.ui.console_textEdit.insertPlainText("An error occured, please try again \n")         
        return self.trans_I_sample_file  
    
    def calc_trans_I_sample(self):
        try:
            n=len(self.trans_I_sample_file)
            I_sample_array=np.zeros(n)
            i=0
            for file in self.trans_I_sample_file:
                file_ok=Path(str(file))
                I_sample=self.calc_transmission(file_ok)
                I_sample_array[i]=I_sample
                i+=1
            array2write=''
            for t in I_sample_array:
                array2write+='%f'%t+' '
            array2write=array2write[:]
            self.ui.Itrans_lineEdit.setText(array2write)
            self.ui.console_textEdit.insertPlainText("Sample transmissions calculated as %s"%array2write+"\n")
        except:
            self.ui.console_textEdit.insertPlainText("Missing data file or specify widow width.\n")        
        return
    
    def setItransto1(self):
        if self.ui.data_file_textEdit.toPlainText()=="":
            self.ui.console_textEdit.insertPlainText("Please provide data files first.\n")
        else:
            self.n=int(self.ui.nb_samples_averaged_lineEdit.text())
            print('list',self.datafile_list)
            length=int(len(self.datafile_list)/self.n)
            line2write=''
            for i in range(length):
                line2write+='1.0 '
            
            self.ui.Itrans_lineEdit.setText(line2write)            
            self.ui.console_textEdit.insertPlainText("Sample transmissions have been set to 1\n")
        return
    
        
    
        
################################### Conversion des fichiers
    def convertfiles(self):
        import ast
        from pathlib import Path
        
        #nombre de fichiers à moyenner
        self.n=int(self.ui.nb_samples_averaged_lineEdit.text())
        
        
        # Récupération du coefficient de calibration
        self.cf=float(self.ui.calculated_calibration_coeflineEdit.text())
        
        # récupération du coefficient refine reference substraction
        refcoeff=float(self.ui.ref_coeff_lineEdit.text())
        
        # Création des répertoires de sortie
        if self.ui.skip_checkBox.isChecked()==True:
            outputedf=self.path+'/uncorrected_edf_files'
        else:
            outputedf=self.path+'/corrected_edf_files'
        if not os.path.exists(outputedf):
            os.makedirs(outputedf)
        
        
        ############# Calcul de Qx Qy
        filename, file_extension = os.path.splitext(self.datafile_list[0])
           
        
        
        qx_array = np.zeros(self.number_pixel_x);qy_array = np.zeros(self.number_pixel_y)
      
        
        for k in range(self.number_pixel_x):
            for l in range(self.number_pixel_y):
                denominateur=(self.distance**2+((k-self.x_center)*self.pix_size)**2+((l-self.y_center)*self.pix_size)**2)**(1/2)
                qx_array[k] = (2*np.pi/self.wl)*((k-self.x_center)*self.pix_size/denominateur)
                qy_array[l] = (2*np.pi/self.wl)*((l-self.y_center)*self.pix_size/denominateur)
                
        
        ##################### Case where no reference file is provided (only mask is applied)
        if self.ui.skip_checkBox.isChecked()==True:
            #créer liste de fichiers
            if (self.ui.I0_lineEdit.text()=='') or (self.ui.Itrans_lineEdit.text()==''):
                self.ui.console_textEdit.insertPlainText('Missing arguments - Please provide transmitted intensity values I0, and specimen')
            else:
                l=0
                # Récupération des transmissions
                I_0=float(self.ui.I0_lineEdit.text())
                try:
                    #Isample_array=ast.literal_eval(self.ui.Itrans_lineEdit.text())
                    Isample_array=np.fromstring(self.ui.Itrans_lineEdit.text(),dtype=float,sep=' ')
                    print(Isample_array)
                except:
                    self.setItransto1()
                    #Isample_array=ast.literal_eval(self.ui.Itrans_lineEdit.text())
                    Isample_array=np.fromstring(self.ui.Itrans_lineEdit.text(),dtype=float,sep=' ')
                    self.ui.console_textEdit.insertPlainText('Sample transmissions were missing - They have been set to 1 by default.')
                
                k=0
                              
            for i in range(int(len(self.datafile_list)/self.n)):



            
        
  
                self.liste_de_n_fichiers=[]
                for j in range(self.n):
                    self.liste_de_n_fichiers.append(str(self.datafile_list[j+i*self.n]))
                # calcul de l'intensité moyenne
                liste=' '.join(self.liste_de_n_fichiers)
                os.system ("pyFAI-average -o %s" %self.path+"average.edf %s"%liste)
                image_avg=fabio.open(self.path+"average.edf")
                i_moyen=image_avg.data
                os.remove(self.path+"average.edf")               
                
                
                #i_moyen=self.averaging()
                Isample=float(Isample_array[i])
                self.ui.console_textEdit.insertPlainText("Processing files %s"%str(self.liste_de_n_fichiers)+"\n")
                # Incrémentation de la barre de progression
                self.ui.console_textEdit.insertPlainText("Converting image %d"%(i+1)+"/%d"%(len(self.datafile_list)/self.n)+"\n")
                # ouverture du fichier masque
                try:
                    mask = fabio.open(self.maskpathname[0])
                    mask_file=mask.data
                    
                    
                    # Création des images edf corrigées
                    i_corr=self.cf*((1-mask_file)*i_moyen)
                    if (len(self.liste_de_n_fichiers)>1):
                        outputname=outputedf+'/'+str(os.path.basename(self.liste_de_n_fichiers[0]).split('.')[0])+"_"+str(os.path.basename(self.liste_de_n_fichiers[-1]).split('.')[0])+'_masked.edf'
                    else:
                        outputname=outputedf+'/'+str(os.path.basename(self.liste_de_n_fichiers[0]).split('.')[0])+'_masked.edf'
                    # Ecriture edf
                    image=fabio.open(self.datafile_list[0]) #récup header
                    header=image.header
                    obj = fabio.edfimage.EdfImage(header=header,data=i_corr)
                    obj.write(outputname)                
                    
                    
                    ###### WRITE file in Qx Qy Intensity format
                    if self.ui.sasview_checkBox.isChecked()==True:
                        if self.ui.skip_checkBox.isChecked()==True:
                            outputdir=self.path+'/2D_uncorr_dat_files'
                        else:
                            outputdir= self.path+'/2D_corr_dat_files'
                        if not os.path.exists(outputdir):
                            os.makedirs(outputdir)                    
                        line2write = "#Data columns Qx - Qy - I(Qx,Qy) \n"
                        line2write+="#ASCII data"+"\n"
                        # Apply mask
                        for k in range (self.number_pixel_y-1):
                            for l in range(self.number_pixel_x-1):
                                i_masked=self.cf*float((1-mask_file[k][l])*i_moyen[k][l])
                                if i_masked==0:
                                    line2write += "%f"%float(qx_array[l])+'\t %f'%float(qy_array[k])+"\t NaN \n"
                                else:
                                    line2write += "%f"%float(qx_array[l])+'\t %f'%float(qy_array[k])+"\t %f"%i_masked +"\n"                        
                                #line2write += "%f"%float(qx_array[l])+'\t %f'%float(qy_array[k])+"\t %f"%i_masked+'\n'
                        filename=Path(str(self.liste_de_n_fichiers[0])).stem
                        outputfile=outputdir+'/'+filename+'.dat'
                        
                        file = open(outputfile,'w',encoding='utf-8')
                        file.write(line2write)
                        file.close()
                                            
                    self.ui.console_textEdit.insertPlainText("Done \n")
                except:
                    self.ui.console_textEdit.insertPlainText("Mask file not provided, please provide a mask file")
                    
                
            
        
        ### Cas où on soustrait du signal de référence
        else:
            if (self.ui.I0_lineEdit.text()=='') or (self.ui.Iref_lineEdit.text()=='') or (self.ui.Itrans_lineEdit.text()==''):
                self.ui.console_textEdit.insertPlainText('Missing arguments - Please provide transmitted intensity values I0, Iref, and specimen')
            else:
                l=0
                # Récupération des transmissions
                I_0=float(self.ui.I0_lineEdit.text())
                I_ref=float(self.ui.Iref_lineEdit.text())
                Isample_array=ast.literal_eval(self.ui.Itrans_lineEdit.text())
                
                k=0
                
                          
                for i in range(int(len(self.datafile_list)/self.n)):
                    self.liste_de_n_fichiers=[]
                    for j in range(self.n):
                        self.liste_de_n_fichiers.append(str(self.datafile_list[j+i*self.n]))
                    liste=' '.join(self.liste_de_n_fichiers)
                    print(liste)
                    self.ui.console_textEdit.insertPlainText("Averagaging files %s"%liste+"\n")
                    os.system ("pyFAI-average -o %s" %self.path+"/average.edf %s"%liste)
                    image_avg=fabio.open(self.path+"/average.edf")
                    #i_moyen=image_avg.data/acq_time
                    i_moyen=image_avg.data
                    os.remove(self.path+"/average.edf")   
                
                    Isample=float(Isample_array[i])
                    print("Converting image %d"%(i+1)+"/%d"%(len(self.datafile_list)/self.n)+"\n")
                    self.ui.console_textEdit.insertPlainText("Processing files %s"%str(self.liste_de_n_fichiers)+"\n")
                    self.ui.console_textEdit.insertPlainText("Converting image %d"%(i+1)+"/%d"%(len(self.datafile_list)/self.n)+"\n")
                    
                    
                                        
                        
                    # ref
                    ref=fabio.open(self.refpathname[0])
                    ref_header=ref.header
                    #acq_time_ref=float(ref_header["ExposureTime"])
                    #i_ref=ref.data/acq_time_ref
                    i_ref=ref.data
                    # mask
                    try:
                        mask = fabio.open(self.maskpathname[0])                
                        mask_file=mask.data
                        i_corr=self.cf*((1-mask.data)*((I_0/Isample)*i_moyen-refcoeff*(I_0/I_ref)*i_ref))
                        
                        if (len(self.liste_de_n_fichiers)>1):
                            outputname=outputedf+'/'+str(os.path.basename(self.liste_de_n_fichiers[0]).split('.')[0])+"_"+str(os.path.basename(self.liste_de_n_fichiers[-1]).split('.')[0])+'_corr.edf'
                        else:
                            outputname=outputedf+'/'+str(os.path.basename(self.liste_de_n_fichiers[0]).split('.')[0])+'_corr.edf'
                        image=fabio.open(self.datafile_list[0])
                        #récup header
                        header=image.header
                        obj = fabio.edfimage.EdfImage(header=header,data=i_corr)
                        obj.write(outputname)       
                        
                        ###### WRITE file in Qx Qy Intensity format
                        if self.ui.sasview_checkBox.isChecked()==True:                    
                            if self.ui.skip_checkBox.isChecked()==True:
                                outputdir=self.path+'/2D_uncorr_dat_files'
                            else:
                                outputdir= self.path+'/2D_corr_dat_files'
                            if not os.path.exists(outputdir):
                                os.makedirs(outputdir)                        
                            line2write = "#Data columns Qx - Qy - I(Qx,Qy) \n"
                            line2write+="#ASCII data"+"\n"                    
                            for k in range(self.number_pixel_y-1):
                                for l in range(self.number_pixel_x-1):                    
                                    i_corr=self.cf*float(1-mask_file[k][l])*((I_0/Isample)*i_moyen[k][l]-refcoeff*(I_0/I_ref)*i_ref[k][l])
                                    if i_corr==0:
                                        line2write += "%f"%float(qx_array[l])+'\t %f'%float(qy_array[k])+"\t NaN\n"
                                    else:
                                        line2write += "%f"%float(qx_array[l])+'\t %f'%float(qy_array[k])+"\t %f"%i_corr+'\n'
                            filename=Path(str(self.liste_de_n_fichiers[0])).stem
                            outputfile=outputdir+'/'+filename+'.dat'                    
                            #outputfile = os.path.splitext(str(self.liste_de_n_fichiers[0]))[0]+'_corr_masked.dat'
                            file = open(outputfile,'w',encoding='utf-8')
                            file.write(line2write)
                            file.close()
                            
                         
                        print("Done.")
                        #self.ui.console_textEdit.insertPlainText("Converting image %d"%(i+1)+"/%d"%(len(self.datafile_list)/self.n)+"\n")
                        self.ui.console_textEdit.insertPlainText("Done \n")                        
                    except:
                        self.ui.console_textEdit.insertPlainText("Mask file not provided, please provide a mask file")
        return
    
    def check (self): #checks whethe an image has been supplied for the reference and the mask
        if a==0 :
            self.ui.console_textEdit.insertPlainText('Mask image is missing! \n')
            self.ui.console_textEdit.insertPlainText('Please provide a mask file. \n')
        if self.ui.skip_checkBox.isChecked()==True:
            if a==1:
                self.convertfiles()
              
        else:
            if b==0:
                self.ui.console_textEdit.insertPlainText('Reference data is missing! \n')
                self.ui.console_textEdit.insertPlainText('Please provide a reference frame. \n')
            if b==1 and a==1:
                self.convertfiles()
    
    def openref1D(self):
        try:
            self.ref1D=QtWidgets.QFileDialog.getOpenFileNames( self,"Open 1D reference data file","%s"%self.path,"*.dat" )
            self.ref1Dname=self.ref1D[0]
            print(self.ref1Dname[0])
            res=os.path.basename(self.ref1Dname[0])
            #self.ui.data_file4mask_lineEdit.setText(res)
            if res!='':
                self.ui.console_textEdit.insertPlainText("1D Data file for reference data is %s"%str(res)+'\n')
            else:
                self.ui.console_textEdit.insertPlainText("No data file provided, please try again\n")            
            
        except:
            self.ui.console_textEdit.insertPlainText("An error occured, please try again \n")         
        return self.ref1Dname
    
    def opensample1D(self):
        try:
            self.sample1D=QtWidgets.QFileDialog.getOpenFileNames( self,"Open 1D sample data file","%s"%self.path,"*.dat" )
            self.sample1Dname=self.sample1D[0]
            res=os.path.basename(self.sample1Dname[0])
            #self.ui.data_file4mask_lineEdit.setText(res)
            if res!='':
                self.ui.console_textEdit.insertPlainText("1D Data file for specimen data is %s"%str(res)+'\n')
            else:
                self.ui.console_textEdit.insertPlainText("No data file provided, please try again\n") 
        except:
            self.ui.console_textEdit.insertPlainText("An error occured, please try again \n")         
        return self.sample1Dname  
    
    def calc_coeff(self):
        from scipy.signal import savgol_filter
        try:
            qref, iref=np.loadtxt(self.ref1Dname[0], skiprows=2, unpack=True)
            qsample, isample=np.loadtxt(self.sample1Dname[0], skiprows=2, unpack=True)
            index=np.searchsorted(qref,0.9)
            iref_max=np.amax(savgol_filter(iref[index:],9,2))
            index=np.searchsorted(qsample,0.9)
            isample_max=np.amax(savgol_filter(isample[index:],9,2))                
            # Récupération des transmissions
            I_0=float(self.ui.I0_lineEdit.text())
            I_ref=float(self.ui.Iref_lineEdit.text())
            Isample=float(self.ui.spec_trans_lineEdit.text())           
            k=(I_0/Isample)*isample_max/((I_0/I_ref)*(iref_max))        
            self.ui.ref_coeff_lineEdit.setText("%s"%str(k))
            self.cf=k
        except:
            self.ui.console_textEdit.insertPlainText("Missing arguments, please check.\n")
        return
        
         
     
def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()




