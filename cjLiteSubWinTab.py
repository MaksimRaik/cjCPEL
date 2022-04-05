import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ConstTab(object):

    def __init__(self, data):

        self.datatb = data

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(950, 600)
        self.centralwidget = QtWidgets.QWidget(Form)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        Form.setCentralWidget(self.centralwidget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.header = self.datatb.columns.values.tolist()
        self.tableWidget.setColumnCount( len( self.header ) )
        self.tableWidget.setHorizontalHeaderLabels( self.header )

        for i, row in self.datatb.iterrows():

            self.tableWidget.setRowCount( self.tableWidget.rowCount() + 1 )

            for j in np.arange( 0, self.tableWidget.columnCount(), 1 ):

                self.tableWidget.setItem( i, j, QtWidgets.QTableWidgetItem( str( row[ j ] ) ) )

        self.tableWidget.resize( 950, 600 )

        self.pushButton.clicked.connect( Form.close )

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Mixture component"))
        self.pushButton.setText(_translate( 'Form', 'Ok' ))