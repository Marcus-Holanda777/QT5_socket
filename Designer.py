# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Designer.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(760, 534)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.btnExec = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnExec.setFont(font)
        self.btnExec.setObjectName("btnExec")
        self.gridLayout.addWidget(self.btnExec, 0, 2, 1, 1)
        self.lbServidor = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbServidor.setFont(font)
        self.lbServidor.setObjectName("lbServidor")
        self.gridLayout.addWidget(self.lbServidor, 5, 1, 1, 1)
        self.comboTarefas = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboTarefas.setFont(font)
        self.comboTarefas.setObjectName("comboTarefas")
        self.gridLayout.addWidget(self.comboTarefas, 0, 1, 1, 1)
        self.lbCliente = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbCliente.setFont(font)
        self.lbCliente.setObjectName("lbCliente")
        self.gridLayout.addWidget(self.lbCliente, 2, 1, 1, 1)
        self.listCliente = QtWidgets.QListWidget(self.centralwidget)
        self.listCliente.setObjectName("listCliente")
        self.gridLayout.addWidget(self.listCliente, 4, 1, 1, 1)
        self.listServidor = QtWidgets.QListWidget(self.centralwidget)
        self.listServidor.setObjectName("listServidor")
        self.gridLayout.addWidget(self.listServidor, 7, 1, 3, 1)
        self.lbStatus = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbStatus.setFont(font)
        self.lbStatus.setObjectName("lbStatus")
        self.gridLayout.addWidget(self.lbStatus, 10, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cliente 0.1"))
        self.btnExec.setText(_translate("MainWindow", "Executar"))
        self.lbServidor.setText(_translate("MainWindow", "Servidor"))
        self.lbCliente.setText(_translate("MainWindow", "Cliente"))
        self.lbStatus.setText(_translate("MainWindow", "Status"))
