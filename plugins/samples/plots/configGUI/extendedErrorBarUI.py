# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'extendedErrorBar.ui'
#
# Created: Wed Jun 08 12:19:32 2011
#      by: PyQt4 UI code generator 4.8.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ExtendedErrorBarDialog(object):
    def setupUi(self, ExtendedErrorBarDialog):
        ExtendedErrorBarDialog.setObjectName(_fromUtf8("ExtendedErrorBarDialog"))
        ExtendedErrorBarDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        ExtendedErrorBarDialog.resize(505, 265)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ExtendedErrorBarDialog.sizePolicy().hasHeightForWidth())
        ExtendedErrorBarDialog.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../icons/programIcon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ExtendedErrorBarDialog.setWindowIcon(icon)
        self.horizontalLayout_5 = QtGui.QHBoxLayout(ExtendedErrorBarDialog)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.groupBox_2 = QtGui.QGroupBox(ExtendedErrorBarDialog)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.cboSortingField = QtGui.QComboBox(self.groupBox_2)
        self.cboSortingField.setObjectName(_fromUtf8("cboSortingField"))
        self.cboSortingField.addItem(_fromUtf8(""))
        self.cboSortingField.addItem(_fromUtf8(""))
        self.cboSortingField.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.cboSortingField)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.verticalLayout_5.addWidget(self.groupBox_2)
        self.groupBox_4 = QtGui.QGroupBox(ExtendedErrorBarDialog)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.chkCorrectedPvalues = QtGui.QCheckBox(self.groupBox_4)
        self.chkCorrectedPvalues.setObjectName(_fromUtf8("chkCorrectedPvalues"))
        self.verticalLayout_3.addWidget(self.chkCorrectedPvalues)
        self.verticalLayout_5.addWidget(self.groupBox_4)
        self.groupBox_3 = QtGui.QGroupBox(ExtendedErrorBarDialog)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.lblFigureWidth = QtGui.QLabel(self.groupBox_3)
        self.lblFigureWidth.setObjectName(_fromUtf8("lblFigureWidth"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.lblFigureWidth)
        self.spinFigWidth = QtGui.QDoubleSpinBox(self.groupBox_3)
        self.spinFigWidth.setDecimals(2)
        self.spinFigWidth.setMinimum(2.0)
        self.spinFigWidth.setMaximum(20.0)
        self.spinFigWidth.setSingleStep(0.5)
        self.spinFigWidth.setProperty(_fromUtf8("value"), 8.5)
        self.spinFigWidth.setObjectName(_fromUtf8("spinFigWidth"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.spinFigWidth)
        self.lblFigureHeight = QtGui.QLabel(self.groupBox_3)
        self.lblFigureHeight.setObjectName(_fromUtf8("lblFigureHeight"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.lblFigureHeight)
        self.spinFigRowHeight = QtGui.QDoubleSpinBox(self.groupBox_3)
        self.spinFigRowHeight.setMinimum(0.1)
        self.spinFigRowHeight.setMaximum(1.0)
        self.spinFigRowHeight.setSingleStep(0.05)
        self.spinFigRowHeight.setProperty(_fromUtf8("value"), 0.25)
        self.spinFigRowHeight.setObjectName(_fromUtf8("spinFigRowHeight"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.spinFigRowHeight)
        self.verticalLayout_2.addLayout(self.formLayout_2)
        spacerItem = QtGui.QSpacerItem(13, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout_5.addWidget(self.groupBox_3)
        self.horizontalLayout_5.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.groupBox = QtGui.QGroupBox(ExtendedErrorBarDialog)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.chkShowBarPlot = QtGui.QCheckBox(self.groupBox)
        self.chkShowBarPlot.setChecked(True)
        self.chkShowBarPlot.setObjectName(_fromUtf8("chkShowBarPlot"))
        self.verticalLayout.addWidget(self.chkShowBarPlot)
        self.cboPercentageOrSeqCount = QtGui.QComboBox(self.groupBox)
        self.cboPercentageOrSeqCount.setObjectName(_fromUtf8("cboPercentageOrSeqCount"))
        self.cboPercentageOrSeqCount.addItem(_fromUtf8(""))
        self.cboPercentageOrSeqCount.addItem(_fromUtf8(""))
        self.verticalLayout.addWidget(self.cboPercentageOrSeqCount)
        self.chkPValueLabels = QtGui.QCheckBox(self.groupBox)
        self.chkPValueLabels.setChecked(True)
        self.chkPValueLabels.setObjectName(_fromUtf8("chkPValueLabels"))
        self.verticalLayout.addWidget(self.chkPValueLabels)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_6.addWidget(self.label_4)
        self.spinMarkerSize = QtGui.QSpinBox(self.groupBox)
        self.spinMarkerSize.setMinimum(1)
        self.spinMarkerSize.setMaximum(100)
        self.spinMarkerSize.setProperty(_fromUtf8("value"), 30)
        self.spinMarkerSize.setObjectName(_fromUtf8("spinMarkerSize"))
        self.horizontalLayout_6.addWidget(self.spinMarkerSize)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.verticalLayout_6.addWidget(self.groupBox)
        self.groupBox_5 = QtGui.QGroupBox(ExtendedErrorBarDialog)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.chkCustomLimits = QtGui.QCheckBox(self.groupBox_5)
        self.chkCustomLimits.setObjectName(_fromUtf8("chkCustomLimits"))
        self.verticalLayout_4.addWidget(self.chkCustomLimits)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_2 = QtGui.QLabel(self.groupBox_5)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_4.addWidget(self.label_2)
        self.spinMinimumX = QtGui.QDoubleSpinBox(self.groupBox_5)
        self.spinMinimumX.setEnabled(False)
        self.spinMinimumX.setMinimum(-1000.0)
        self.spinMinimumX.setMaximum(1000.0)
        self.spinMinimumX.setSingleStep(0.1)
        self.spinMinimumX.setProperty(_fromUtf8("value"), -1.0)
        self.spinMinimumX.setObjectName(_fromUtf8("spinMinimumX"))
        self.horizontalLayout_4.addWidget(self.spinMinimumX)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(self.groupBox_5)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.spinMaximumX = QtGui.QDoubleSpinBox(self.groupBox_5)
        self.spinMaximumX.setEnabled(False)
        self.spinMaximumX.setMinimum(-1000.0)
        self.spinMaximumX.setMaximum(10000.0)
        self.spinMaximumX.setSingleStep(0.1)
        self.spinMaximumX.setProperty(_fromUtf8("value"), 1.0)
        self.spinMaximumX.setObjectName(_fromUtf8("spinMaximumX"))
        self.horizontalLayout_2.addWidget(self.spinMaximumX)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_6.addWidget(self.groupBox_5)
        spacerItem1 = QtGui.QSpacerItem(13, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem1)
        self.horizontalLayout_5.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.groupBox_6 = QtGui.QGroupBox(ExtendedErrorBarDialog)
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.radioLegendPosNone = QtGui.QRadioButton(self.groupBox_6)
        self.radioLegendPosNone.setObjectName(_fromUtf8("radioLegendPosNone"))
        self.verticalLayout_9.addWidget(self.radioLegendPosNone)
        self.radioLegendPosUpperLeft = QtGui.QRadioButton(self.groupBox_6)
        self.radioLegendPosUpperLeft.setChecked(True)
        self.radioLegendPosUpperLeft.setObjectName(_fromUtf8("radioLegendPosUpperLeft"))
        self.verticalLayout_9.addWidget(self.radioLegendPosUpperLeft)
        self.radioLegendPosLowerLeft = QtGui.QRadioButton(self.groupBox_6)
        self.radioLegendPosLowerLeft.setObjectName(_fromUtf8("radioLegendPosLowerLeft"))
        self.verticalLayout_9.addWidget(self.radioLegendPosLowerLeft)
        self.radioLegendPosLowerCentre = QtGui.QRadioButton(self.groupBox_6)
        self.radioLegendPosLowerCentre.setObjectName(_fromUtf8("radioLegendPosLowerCentre"))
        self.verticalLayout_9.addWidget(self.radioLegendPosLowerCentre)
        self.radioLegendPosLowerRight = QtGui.QRadioButton(self.groupBox_6)
        self.radioLegendPosLowerRight.setObjectName(_fromUtf8("radioLegendPosLowerRight"))
        self.verticalLayout_9.addWidget(self.radioLegendPosLowerRight)
        self.verticalLayout_8.addWidget(self.groupBox_6)
        self.verticalLayout_7.addLayout(self.verticalLayout_8)
        spacerItem2 = QtGui.QSpacerItem(13, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem3 = QtGui.QSpacerItem(0, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.buttonBox = QtGui.QDialogButtonBox(ExtendedErrorBarDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout_3.addWidget(self.buttonBox)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5.addLayout(self.verticalLayout_7)

        self.retranslateUi(ExtendedErrorBarDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ExtendedErrorBarDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ExtendedErrorBarDialog.reject)
        QtCore.QObject.connect(self.chkCustomLimits, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.spinMinimumX.setEnabled)
        QtCore.QObject.connect(self.chkCustomLimits, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.spinMaximumX.setEnabled)
        QtCore.QObject.connect(self.chkShowBarPlot, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.cboPercentageOrSeqCount.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(ExtendedErrorBarDialog)

    def retranslateUi(self, ExtendedErrorBarDialog):
        ExtendedErrorBarDialog.setWindowTitle(QtGui.QApplication.translate("ExtendedErrorBarDialog", "Extended error bar plot", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("ExtendedErrorBarDialog", "Sorting", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ExtendedErrorBarDialog", "Field:", None, QtGui.QApplication.UnicodeUTF8))
        self.cboSortingField.setItemText(0, QtGui.QApplication.translate("ExtendedErrorBarDialog", "p-values", None, QtGui.QApplication.UnicodeUTF8))
        self.cboSortingField.setItemText(1, QtGui.QApplication.translate("ExtendedErrorBarDialog", "Effect sizes", None, QtGui.QApplication.UnicodeUTF8))
        self.cboSortingField.setItemText(2, QtGui.QApplication.translate("ExtendedErrorBarDialog", "Feature labels", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("ExtendedErrorBarDialog", "Multiple comparisons", None, QtGui.QApplication.UnicodeUTF8))
        self.chkCorrectedPvalues.setText(QtGui.QApplication.translate("ExtendedErrorBarDialog", "Show corrected p-values", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("ExtendedErrorBarDialog", "Figure size", None, QtGui.QApplication.UnicodeUTF8))
        self.lblFigureWidth.setText(QtGui.QApplication.translate("ExtendedErrorBarDialog", "Width:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblFigureHeight.setText(QtGui.QApplication.translate("ExtendedErrorBarDialog", "Row height:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("ExtendedErrorBarDialog", "Figure elements", None, QtGui.QApplication.UnicodeUTF8))
        self.chkShowBarPlot.setText(QtGui.QApplication.translate("ExtendedErrorBarDialog", "Show bar subplot", None, QtGui.QApplication.UnicodeUTF8))
        self.cboPercentageOrSeqCount.setItemText(0, QtGui.QApplication.translate("ExtendedErrorBarDialog", "Sequences", None, QtGui.QApplication.UnicodeUTF8))
        self.cboPercentageOrSeqCount.setItemText(1, QtGui.QApplication.translate("ExtendedErrorBarDialog", "Proportion (%)", None, QtGui.QApplication.UnicodeUTF8))
        self.chkPValueLabels.setText(QtGui.QApplication.translate("ExtendedErrorBarDialog", "Show p-value labels", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ExtendedErrorBarDialog", "Marker size:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_5.setTitle(QtGui.QApplication.translate("ExtendedErrorBarDialog", "Error bar x-axis limits", None, QtGui.QApplication.UnicodeUTF8))
        self.chkCustomLimits.setText(QtGui.QApplication.translate("ExtendedErrorBarDialog", "Use custom limits", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ExtendedErrorBarDialog", "Minimum:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ExtendedErrorBarDialog", "Maximum:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_6.setTitle(QtGui.QApplication.translate("ExtendedErrorBarDialog", "Legend position", None, QtGui.QApplication.UnicodeUTF8))
        self.radioLegendPosNone.setText(QtGui.QApplication.translate("ExtendedErrorBarDialog", "None", None, QtGui.QApplication.UnicodeUTF8))
        self.radioLegendPosUpperLeft.setText(QtGui.QApplication.translate("ExtendedErrorBarDialog", "Upper left", None, QtGui.QApplication.UnicodeUTF8))
        self.radioLegendPosLowerLeft.setText(QtGui.QApplication.translate("ExtendedErrorBarDialog", "Lower left", None, QtGui.QApplication.UnicodeUTF8))
        self.radioLegendPosLowerCentre.setText(QtGui.QApplication.translate("ExtendedErrorBarDialog", "Lower centre", None, QtGui.QApplication.UnicodeUTF8))
        self.radioLegendPosLowerRight.setText(QtGui.QApplication.translate("ExtendedErrorBarDialog", "Lower right", None, QtGui.QApplication.UnicodeUTF8))

