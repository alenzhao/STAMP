# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HeatmapPlot.ui'
#
# Created: Mon Aug 04 15:26:28 2014
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_HeatmapPlotDialog(object):
    def setupUi(self, HeatmapPlotDialog):
        HeatmapPlotDialog.setObjectName(_fromUtf8("HeatmapPlotDialog"))
        HeatmapPlotDialog.resize(260, 455)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(HeatmapPlotDialog.sizePolicy().hasHeightForWidth())
        HeatmapPlotDialog.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../../icons/programIcon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        HeatmapPlotDialog.setWindowIcon(icon)
        self.verticalLayout_3 = QtGui.QVBoxLayout(HeatmapPlotDialog)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label = QtGui.QLabel(HeatmapPlotDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_6.addWidget(self.label)
        self.cboFieldToPlot = QtGui.QComboBox(HeatmapPlotDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboFieldToPlot.sizePolicy().hasHeightForWidth())
        self.cboFieldToPlot.setSizePolicy(sizePolicy)
        self.cboFieldToPlot.setObjectName(_fromUtf8("cboFieldToPlot"))
        self.cboFieldToPlot.addItem(_fromUtf8(""))
        self.cboFieldToPlot.addItem(_fromUtf8(""))
        self.horizontalLayout_6.addWidget(self.cboFieldToPlot)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.chkPlotOnlyActiveFeatures = QtGui.QCheckBox(HeatmapPlotDialog)
        self.chkPlotOnlyActiveFeatures.setObjectName(_fromUtf8("chkPlotOnlyActiveFeatures"))
        self.verticalLayout_3.addWidget(self.chkPlotOnlyActiveFeatures)
        self.groupBox_3 = QtGui.QGroupBox(HeatmapPlotDialog)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lblFigureWidth = QtGui.QLabel(self.groupBox_3)
        self.lblFigureWidth.setObjectName(_fromUtf8("lblFigureWidth"))
        self.horizontalLayout.addWidget(self.lblFigureWidth)
        self.spinFigWidth = QtGui.QDoubleSpinBox(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinFigWidth.sizePolicy().hasHeightForWidth())
        self.spinFigWidth.setSizePolicy(sizePolicy)
        self.spinFigWidth.setDecimals(2)
        self.spinFigWidth.setMinimum(0.5)
        self.spinFigWidth.setMaximum(100.0)
        self.spinFigWidth.setSingleStep(0.1)
        self.spinFigWidth.setProperty("value", 7.0)
        self.spinFigWidth.setObjectName(_fromUtf8("spinFigWidth"))
        self.horizontalLayout.addWidget(self.spinFigWidth)
        self.lblFigureHeight = QtGui.QLabel(self.groupBox_3)
        self.lblFigureHeight.setObjectName(_fromUtf8("lblFigureHeight"))
        self.horizontalLayout.addWidget(self.lblFigureHeight)
        self.spinFigHeight = QtGui.QDoubleSpinBox(self.groupBox_3)
        self.spinFigHeight.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinFigHeight.sizePolicy().hasHeightForWidth())
        self.spinFigHeight.setSizePolicy(sizePolicy)
        self.spinFigHeight.setDecimals(2)
        self.spinFigHeight.setMinimum(0.5)
        self.spinFigHeight.setMaximum(100.0)
        self.spinFigHeight.setSingleStep(0.1)
        self.spinFigHeight.setProperty("value", 7.0)
        self.spinFigHeight.setObjectName(_fromUtf8("spinFigHeight"))
        self.horizontalLayout.addWidget(self.spinFigHeight)
        spacerItem = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.groupBox = QtGui.QGroupBox(HeatmapPlotDialog)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.lblDendrogramMethod = QtGui.QLabel(self.groupBox)
        self.lblDendrogramMethod.setObjectName(_fromUtf8("lblDendrogramMethod"))
        self.horizontalLayout_5.addWidget(self.lblDendrogramMethod)
        self.cboDendrogramMethod = QtGui.QComboBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboDendrogramMethod.sizePolicy().hasHeightForWidth())
        self.cboDendrogramMethod.setSizePolicy(sizePolicy)
        self.cboDendrogramMethod.setObjectName(_fromUtf8("cboDendrogramMethod"))
        self.cboDendrogramMethod.addItem(_fromUtf8(""))
        self.cboDendrogramMethod.addItem(_fromUtf8(""))
        self.cboDendrogramMethod.addItem(_fromUtf8(""))
        self.cboDendrogramMethod.addItem(_fromUtf8(""))
        self.cboDendrogramMethod.addItem(_fromUtf8(""))
        self.horizontalLayout_5.addWidget(self.cboDendrogramMethod)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lblClusteringThreshold = QtGui.QLabel(self.groupBox)
        self.lblClusteringThreshold.setObjectName(_fromUtf8("lblClusteringThreshold"))
        self.horizontalLayout_2.addWidget(self.lblClusteringThreshold)
        self.spinClusteringThreshold = QtGui.QDoubleSpinBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinClusteringThreshold.sizePolicy().hasHeightForWidth())
        self.spinClusteringThreshold.setSizePolicy(sizePolicy)
        self.spinClusteringThreshold.setDecimals(2)
        self.spinClusteringThreshold.setMinimum(0.0)
        self.spinClusteringThreshold.setMaximum(1.0)
        self.spinClusteringThreshold.setSingleStep(0.05)
        self.spinClusteringThreshold.setProperty("value", 0.75)
        self.spinClusteringThreshold.setObjectName(_fromUtf8("spinClusteringThreshold"))
        self.horizontalLayout_2.addWidget(self.spinClusteringThreshold)
        spacerItem1 = QtGui.QSpacerItem(5, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.chkShowTopDendrogram = QtGui.QCheckBox(self.groupBox)
        self.chkShowTopDendrogram.setEnabled(True)
        self.chkShowTopDendrogram.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.chkShowTopDendrogram.setChecked(True)
        self.chkShowTopDendrogram.setObjectName(_fromUtf8("chkShowTopDendrogram"))
        self.verticalLayout_2.addWidget(self.chkShowTopDendrogram)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.lblTopDendrogramHeight = QtGui.QLabel(self.groupBox)
        self.lblTopDendrogramHeight.setObjectName(_fromUtf8("lblTopDendrogramHeight"))
        self.horizontalLayout_8.addWidget(self.lblTopDendrogramHeight)
        self.spinDendrogramHeight = QtGui.QDoubleSpinBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinDendrogramHeight.sizePolicy().hasHeightForWidth())
        self.spinDendrogramHeight.setSizePolicy(sizePolicy)
        self.spinDendrogramHeight.setDecimals(2)
        self.spinDendrogramHeight.setMinimum(0.0)
        self.spinDendrogramHeight.setMaximum(50.0)
        self.spinDendrogramHeight.setSingleStep(0.05)
        self.spinDendrogramHeight.setProperty("value", 1.5)
        self.spinDendrogramHeight.setObjectName(_fromUtf8("spinDendrogramHeight"))
        self.horizontalLayout_8.addWidget(self.spinDendrogramHeight)
        spacerItem2 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.chkShowLeftDendrogram = QtGui.QCheckBox(self.groupBox)
        self.chkShowLeftDendrogram.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.chkShowLeftDendrogram.setChecked(True)
        self.chkShowLeftDendrogram.setObjectName(_fromUtf8("chkShowLeftDendrogram"))
        self.verticalLayout_2.addWidget(self.chkShowLeftDendrogram)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.lblDendrogramWidth = QtGui.QLabel(self.groupBox)
        self.lblDendrogramWidth.setObjectName(_fromUtf8("lblDendrogramWidth"))
        self.horizontalLayout_9.addWidget(self.lblDendrogramWidth)
        self.spinDendrogramWidth = QtGui.QDoubleSpinBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinDendrogramWidth.sizePolicy().hasHeightForWidth())
        self.spinDendrogramWidth.setSizePolicy(sizePolicy)
        self.spinDendrogramWidth.setDecimals(2)
        self.spinDendrogramWidth.setMinimum(0.0)
        self.spinDendrogramWidth.setMaximum(50.0)
        self.spinDendrogramWidth.setSingleStep(0.05)
        self.spinDendrogramWidth.setProperty("value", 1.5)
        self.spinDendrogramWidth.setObjectName(_fromUtf8("spinDendrogramWidth"))
        self.horizontalLayout_9.addWidget(self.spinDendrogramWidth)
        spacerItem3 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_2 = QtGui.QLabel(HeatmapPlotDialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_7.addWidget(self.label_2)
        self.cboColourMap = QtGui.QComboBox(HeatmapPlotDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboColourMap.sizePolicy().hasHeightForWidth())
        self.cboColourMap.setSizePolicy(sizePolicy)
        self.cboColourMap.setObjectName(_fromUtf8("cboColourMap"))
        self.cboColourMap.addItem(_fromUtf8(""))
        self.cboColourMap.addItem(_fromUtf8(""))
        self.cboColourMap.addItem(_fromUtf8(""))
        self.cboColourMap.addItem(_fromUtf8(""))
        self.cboColourMap.addItem(_fromUtf8(""))
        self.cboColourMap.addItem(_fromUtf8(""))
        self.cboColourMap.addItem(_fromUtf8(""))
        self.cboColourMap.addItem(_fromUtf8(""))
        self.cboColourMap.addItem(_fromUtf8(""))
        self.cboColourMap.addItem(_fromUtf8(""))
        self.cboColourMap.addItem(_fromUtf8(""))
        self.cboColourMap.addItem(_fromUtf8(""))
        self.cboColourMap.addItem(_fromUtf8(""))
        self.horizontalLayout_7.addWidget(self.cboColourMap)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.groupBox_6 = QtGui.QGroupBox(HeatmapPlotDialog)
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_6)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.radioLegendPosNone = QtGui.QRadioButton(self.groupBox_6)
        self.radioLegendPosNone.setObjectName(_fromUtf8("radioLegendPosNone"))
        self.gridLayout.addWidget(self.radioLegendPosNone, 0, 0, 1, 1)
        self.radioLegendPosLowerLeft = QtGui.QRadioButton(self.groupBox_6)
        self.radioLegendPosLowerLeft.setObjectName(_fromUtf8("radioLegendPosLowerLeft"))
        self.gridLayout.addWidget(self.radioLegendPosLowerLeft, 0, 2, 1, 1)
        self.radioLegendPosLowerRight = QtGui.QRadioButton(self.groupBox_6)
        self.radioLegendPosLowerRight.setObjectName(_fromUtf8("radioLegendPosLowerRight"))
        self.gridLayout.addWidget(self.radioLegendPosLowerRight, 1, 2, 1, 1)
        self.radioLegendPosUpperRight = QtGui.QRadioButton(self.groupBox_6)
        self.radioLegendPosUpperRight.setObjectName(_fromUtf8("radioLegendPosUpperRight"))
        self.gridLayout.addWidget(self.radioLegendPosUpperRight, 0, 1, 1, 1)
        self.radioLegendPosUpperLeft = QtGui.QRadioButton(self.groupBox_6)
        self.radioLegendPosUpperLeft.setChecked(True)
        self.radioLegendPosUpperLeft.setObjectName(_fromUtf8("radioLegendPosUpperLeft"))
        self.gridLayout.addWidget(self.radioLegendPosUpperLeft, 1, 1, 1, 1)
        self.horizontalLayout_4.addWidget(self.groupBox_6)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.buttonBox = QtGui.QDialogButtonBox(HeatmapPlotDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout_3.addWidget(self.buttonBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.retranslateUi(HeatmapPlotDialog)
        self.cboFieldToPlot.setCurrentIndex(1)
        self.cboColourMap.setCurrentIndex(2)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), HeatmapPlotDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), HeatmapPlotDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(HeatmapPlotDialog)

    def retranslateUi(self, HeatmapPlotDialog):
        HeatmapPlotDialog.setWindowTitle(_translate("HeatmapPlotDialog", "Heatmap plot", None))
        self.label.setText(_translate("HeatmapPlotDialog", "Field to plot:", None))
        self.cboFieldToPlot.setItemText(0, _translate("HeatmapPlotDialog", "Number of sequences", None))
        self.cboFieldToPlot.setItemText(1, _translate("HeatmapPlotDialog", "Proportion of sequences (%)", None))
        self.chkPlotOnlyActiveFeatures.setText(_translate("HeatmapPlotDialog", "Plot only active features", None))
        self.groupBox_3.setTitle(_translate("HeatmapPlotDialog", "Figure size", None))
        self.lblFigureWidth.setText(_translate("HeatmapPlotDialog", "Width:", None))
        self.lblFigureHeight.setText(_translate("HeatmapPlotDialog", "Height:", None))
        self.groupBox.setTitle(_translate("HeatmapPlotDialog", "Dendrograms", None))
        self.lblDendrogramMethod.setText(_translate("HeatmapPlotDialog", "Methods:", None))
        self.cboDendrogramMethod.setItemText(0, _translate("HeatmapPlotDialog", "Average neighbour (UPGMA)", None))
        self.cboDendrogramMethod.setItemText(1, _translate("HeatmapPlotDialog", "Centroid", None))
        self.cboDendrogramMethod.setItemText(2, _translate("HeatmapPlotDialog", "Furthest neighbour", None))
        self.cboDendrogramMethod.setItemText(3, _translate("HeatmapPlotDialog", "Nearest neighbour", None))
        self.cboDendrogramMethod.setItemText(4, _translate("HeatmapPlotDialog", "Ward", None))
        self.lblClusteringThreshold.setText(_translate("HeatmapPlotDialog", "Dendrogram clustering threshold:", None))
        self.chkShowTopDendrogram.setText(_translate("HeatmapPlotDialog", "Show top dendrogram", None))
        self.lblTopDendrogramHeight.setText(_translate("HeatmapPlotDialog", "Height (inches):", None))
        self.chkShowLeftDendrogram.setText(_translate("HeatmapPlotDialog", "Show left dendrogram", None))
        self.lblDendrogramWidth.setText(_translate("HeatmapPlotDialog", "Width (inches):", None))
        self.label_2.setText(_translate("HeatmapPlotDialog", "Colour map:", None))
        self.cboColourMap.setItemText(0, _translate("HeatmapPlotDialog", "Blues", None))
        self.cboColourMap.setItemText(1, _translate("HeatmapPlotDialog", "Blue to red to green", None))
        self.cboColourMap.setItemText(2, _translate("HeatmapPlotDialog", "Blue to white to red", None))
        self.cboColourMap.setItemText(3, _translate("HeatmapPlotDialog", "Cool to warm", None))
        self.cboColourMap.setItemText(4, _translate("HeatmapPlotDialog", "Grayscale", None))
        self.cboColourMap.setItemText(5, _translate("HeatmapPlotDialog", "Jet", None))
        self.cboColourMap.setItemText(6, _translate("HeatmapPlotDialog", "Orange to red", None))
        self.cboColourMap.setItemText(7, _translate("HeatmapPlotDialog", "Paired", None))
        self.cboColourMap.setItemText(8, _translate("HeatmapPlotDialog", "Purple to green", None))
        self.cboColourMap.setItemText(9, _translate("HeatmapPlotDialog", "Reds", None))
        self.cboColourMap.setItemText(10, _translate("HeatmapPlotDialog", "Red to blue", None))
        self.cboColourMap.setItemText(11, _translate("HeatmapPlotDialog", "Spectral", None))
        self.cboColourMap.setItemText(12, _translate("HeatmapPlotDialog", "Yellow to orange to red", None))
        self.groupBox_6.setTitle(_translate("HeatmapPlotDialog", "Legend position", None))
        self.radioLegendPosNone.setText(_translate("HeatmapPlotDialog", "None", None))
        self.radioLegendPosLowerLeft.setText(_translate("HeatmapPlotDialog", "Lower left", None))
        self.radioLegendPosLowerRight.setText(_translate("HeatmapPlotDialog", "Lower right", None))
        self.radioLegendPosUpperRight.setText(_translate("HeatmapPlotDialog", "Upper right", None))
        self.radioLegendPosUpperLeft.setText(_translate("HeatmapPlotDialog", "Upper left", None))

