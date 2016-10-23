# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created: Mon Apr  6 17:41:19 2015
#      by: PyQt4 UI code generator 4.11.3
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


class Ui_Dialog(QtGui.QDialog):
    def __init__(self):
        super(Ui_Dialog,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        Dialog.resize(537, 422)
        font = QtGui.QFont()
        font.setPointSize(20)
        Dialog.setFont(font)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.leA = QtGui.QLineEdit(Dialog)
        self.leA.setObjectName(_fromUtf8("leA"))
        self.horizontalLayout.addWidget(self.leA)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.lblB_2 = QtGui.QLabel(Dialog)
        self.lblB_2.setObjectName(_fromUtf8("lblB_2"))
        self.horizontalLayout_5.addWidget(self.lblB_2)
        self.lblB = QtGui.QLabel(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblB.sizePolicy().hasHeightForWidth())
        self.lblB.setSizePolicy(sizePolicy)
        self.lblB.setText(_fromUtf8(""))
        self.lblB.setObjectName(_fromUtf8("lblB"))
        self.horizontalLayout_5.addWidget(self.lblB)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.leC = QtGui.QLineEdit(Dialog)
        self.leC.setText(_fromUtf8(""))
        self.leC.setObjectName(_fromUtf8("leC"))
        self.horizontalLayout_2.addWidget(self.leC)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.lblD_2 = QtGui.QLabel(Dialog)
        self.lblD_2.setObjectName(_fromUtf8("lblD_2"))
        self.horizontalLayout_4.addWidget(self.lblD_2)
        self.lblD = QtGui.QLabel(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblD.sizePolicy().hasHeightForWidth())
        self.lblD.setSizePolicy(sizePolicy)
        self.lblD.setText(_fromUtf8(""))
        self.lblD.setObjectName(_fromUtf8("lblD"))
        self.horizontalLayout_4.addWidget(self.lblD)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.pb_clean = QtGui.QPushButton(Dialog)
        self.pb_clean.setAutoDefault(False)
        self.pb_clean.setObjectName(_fromUtf8("pb_clean"))
        self.horizontalLayout_3.addWidget(self.pb_clean)
        self.pb_calculate = QtGui.QPushButton(Dialog)
        self.pb_calculate.setAutoDefault(False)
        self.pb_calculate.setObjectName(_fromUtf8("pb_calculate"))
        self.horizontalLayout_3.addWidget(self.pb_calculate)
        self.pb_quit = QtGui.QPushButton(Dialog)
        self.pb_quit.setAutoDefault(False)
        self.pb_quit.setDefault(False)
        self.pb_quit.setObjectName(_fromUtf8("pb_quit"))
        self.horizontalLayout_3.addWidget(self.pb_quit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pb_quit, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.leA, self.leC)
        Dialog.setTabOrder(self.leC, self.pb_calculate)
        Dialog.setTabOrder(self.pb_calculate, self.pb_quit)
        Dialog.setTabOrder(self.pb_quit, self.pb_clean)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "A、B、C、D计算", None))
        self.label.setText(_translate("Dialog", "*A=", None))
        self.lblB_2.setText(_translate("Dialog", "*B=", None))
        self.label_2.setText(_translate("Dialog", "*C=", None))
        self.lblD_2.setText(_translate("Dialog", "*D=", None))
        self.pb_clean.setText(_translate("Dialog", "清除", None))
        self.pb_calculate.setText(_translate("Dialog", "计算", None))
        self.pb_quit.setText(_translate("Dialog", "关闭", None))

