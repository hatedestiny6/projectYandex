# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/posTab.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Positions_Tab(object):
    def setupUi(self, Positions_Tab):
        Positions_Tab.setObjectName("Positions_Tab")
        Positions_Tab.resize(939, 626)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Positions_Tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.newPosBtn = QtWidgets.QPushButton(Positions_Tab)
        self.newPosBtn.setObjectName("newPosBtn")
        self.horizontalLayout_2.addWidget(self.newPosBtn)
        self.changePosBtn = QtWidgets.QPushButton(Positions_Tab)
        self.changePosBtn.setObjectName("changePosBtn")
        self.horizontalLayout_2.addWidget(self.changePosBtn)
        self.deletePosBtn = QtWidgets.QPushButton(Positions_Tab)
        self.deletePosBtn.setObjectName("deletePosBtn")
        self.horizontalLayout_2.addWidget(self.deletePosBtn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.outputPos = QtWidgets.QTableWidget(Positions_Tab)
        self.outputPos.setObjectName("outputPos")
        self.outputPos.setColumnCount(0)
        self.outputPos.setRowCount(0)
        self.verticalLayout.addWidget(self.outputPos)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Positions_Tab)
        QtCore.QMetaObject.connectSlotsByName(Positions_Tab)

    def retranslateUi(self, Positions_Tab):
        _translate = QtCore.QCoreApplication.translate
        Positions_Tab.setWindowTitle(_translate("Positions_Tab", "Должности"))
        self.newPosBtn.setText(_translate("Positions_Tab", "Добавить новый уровень должности"))
        self.changePosBtn.setText(_translate("Positions_Tab", "Изменить уровень должности"))
        self.deletePosBtn.setText(_translate("Positions_Tab", "Удалить должность"))
