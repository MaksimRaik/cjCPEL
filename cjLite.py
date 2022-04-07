import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as Navi
from matplotlib.figure import Figure
matplotlib.use('Qt5Agg')
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import seaborn as sns
import sip
from timeit import *
import sys

#################################
import functionSA as fsa
import funforhelp as ffp
from cjLiteSubWinTab import Ui_ConstTab
from cjLiteSubWinParam import Ui_Param
from cjLiteSubWinVinP import Ui_VinP
from cjLiteSubWinPlSt import Ui_PlSt

import platform

# Use NSURL as a workaround to pyside/Qt4 behaviour for dragging and dropping on OSx
#op_sys = platform.system()
#if op_sys == 'Darwin':
 #   from Foundation import NSURL

class MatplotlibCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, dpi=130):
        self.fig = Figure( figsize = ( 8, 12 ), dpi=dpi)

        super(MatplotlibCanvas, self).__init__(self.fig)
        self.fig.tight_layout()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1400, 1000)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout.addWidget(self.lineEdit_3)
        self.spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(self.spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(self.spacerItem1)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1145, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuModel = QtWidgets.QMenu(self.menubar)
        self.menuModel.setObjectName("menuModel")
        self.menuStart = QtWidgets.QMenu( self.menubar )
        self.menuStart.setObjectName('menuStart')
        self.menuPlot = QtWidgets.QMenu( self.menubar )
        self.menuPlot.setObjectName( 'menuPlot' )
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.toolBar = QtWidgets.QToolBar( MainWindow )
        self.toolBar.setObjectName( 'toolBar' )
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)


##################### ACTION FOR MENU BAR ########################################

        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionMax = QtWidgets.QAction(MainWindow)
        self.actionMax.setObjectName("actionMax")
        self.actionNorm = QtWidgets.QAction(MainWindow)
        self.actionNorm.setObjectName("actionNorm")
        self.actionEoS = QtWidgets.QAction(MainWindow)
        self.actionEoS.setObjectName('actionEoS')
        self.actionCom = QtWidgets.QAction( MainWindow )
        self.actionCom.setObjectName('actionCom')
        self.actionVinP = QtWidgets.QAction(MainWindow)
        self.actionVinP.setObjectName('actionVinP')
        self.actionStart = QtWidgets.QAction(MainWindow)
        self.actionStart.setObjectName('actionStart')
        self.actionParam = QtWidgets.QAction(MainWindow)
        self.actionParam.setObjectName('actionParam')
        self.actionPlotSet = QtWidgets.QAction(MainWindow)
        self.actionPlotSet.setObjectName('actionPlotSet')
        self.actionPlot = QtWidgets.QAction( 'actionPlot' )
        self.actionPlot.setObjectName('actionPlot')
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionExit)
        self.menuView.addAction(self.actionMax)
        self.menuView.addAction(self.actionNorm)
        self.menuModel.addAction(self.actionEoS)
        self.menuModel.addAction(self.actionCom)
        self.menuModel.addAction(self.actionVinP)
        self.menuStart.addAction(self.actionStart)
        self.menuStart.addAction(self.actionParam)
        self.menuPlot.addAction(self.actionPlotSet)
        self.menuPlot.addAction(self.actionPlot)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuModel.menuAction())
        self.menubar.addAction(self.menuStart.menuAction())
        self.menubar.addAction(self.menuPlot.menuAction())

#######################################################################################
#################### ACTION FOR TOOLBAR ########################################

        self.actionTBOpen = QtWidgets.QAction(MainWindow)
        self.actionTBOpen.setIcon(QtGui.QIcon( 'Day/folder.ico' ))
        self.actionTBParam = QtWidgets.QAction(MainWindow)
        self.actionTBParam.setIcon( QtGui.QIcon( 'Day/adjustments.ico' ) )
        self.actionTBStart = QtWidgets.QAction(MainWindow)
        self.actionTBStart.setIcon( QtGui.QIcon( 'Day/tabler.ico' ) )
        self.actionTBPlSet = QtWidgets.QAction(MainWindow)
        self.actionTBPlSet.setIcon(QtGui.QIcon('Day/tool.ico'))
        self.actionTBPlot = QtWidgets.QAction(MainWindow)
        self.actionTBPlot.setIcon(QtGui.QIcon('Day/chart.png'))
        self.actionTBVinP = QtWidgets.QAction(MainWindow)
        self.actionTBVinP.setIcon(QtGui.QIcon('Day/notes.ico'))
        self.toolBar.addAction(self.actionTBOpen)
        self.toolBar.addAction(self.actionTBParam)
        self.toolBar.addAction(self.actionTBStart)
        self.toolBar.addAction(self.actionTBPlSet)
        self.toolBar.addAction(self.actionTBPlot)
        self.toolBar.addAction(self.actionTBVinP)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

###############################################################################################
###############################################################################################

        self.filename = ''
        self.Window = QtWidgets.QMainWindow()
        self.currentPT = 'Gas diagram'
        self.startprt = fsa.StartParam()

        self.canv = MatplotlibCanvas(self)

        self.toolbar = Navi(self.canv, self.centralwidget)
        self.horizontalLayout.addWidget(self.toolbar)

        self.PlotType = ['Gas diagram', 'Liquid diagram', 'Gas+Liquid', '3D plot', 'Dew line']
        self.comboBox.addItems(self.PlotType)
        self.comboBox.currentIndexChanged['QString'].connect( self.Update )

        self.lineEdit.textChanged[str].connect( self.changeP )
        self.lineEdit_2.textChanged[str].connect(self.changeT)

        self.actionExit.triggered.connect(MainWindow.close)  # type: ignore
        self.actionMax.triggered.connect(MainWindow.showMaximized)  # type: ignore
        self.actionNorm.triggered.connect(MainWindow.showNormal)
        self.actionOpen.triggered.connect(self.getFile)
        self.actionTBOpen.triggered.connect( self.getFile)
        self.actionStart.triggered.connect(self.getData)
        self.actionTBStart.triggered.connect(self.getData)
        self.actionCom.triggered.connect(self.openMComWin)
        self.actionVinP.triggered.connect( self.openMVinPWin )
        self.actionTBVinP.triggered.connect(self.openMVinPWin)
        self.actionParam.triggered.connect( self.openCParamWin )
        self.actionTBParam.triggered.connect( self.openCParamWin )
        self.actionPlot.triggered.connect( self.getPlot )
        self.actionTBPlot.triggered.connect(self.getPlot)
        self.actionPlotSet.triggered.connect(self.openPPlStWin)
        self.actionTBPlSet.triggered.connect(self.openPPlStWin)




    def getFile(self):

        self.filename = QFileDialog.getOpenFileName(filter = 'PVI (*.PVI)')[0]

        self.startprt = None

        self.startprt = fsa.StartParam()
        self.lineEdit_2.clear()
        self.lineEdit.clear()

        print( ' File ' + self.filename + ' was opened' )

        self.statusbar.showMessage( ' File ' + self.filename + ' was opened' )

    def getData(self):

        if self.filename == '':

            print( 'File not found' )
            self.lineEdit_3.setText('File not found')

        else:

            print('Start calculation data')
            self.lineEdit_3.setText('Start calculation data')
            start = default_timer()

            Const = fsa.Constant(self.filename)

            if self.startprt.Pend == 0.0:

                Pdew = fsa.DewPoint( Const.N, Const.z, np.asarray([self.startprt.T,]), Const.Pcr, Const.Tcr, Const.omega, Const.omegaA,
                                Const.omegaB, Const.Kjk)[0] * 1.0e-5

                self.startprt.Pend = Pdew * 1.03

                print( 'Pressure of dew point is', Pdew)

            else:

                print('Pressure of end is', self.startprt.Pend )

            self.Pg, self.Pl, self.Sl, self.Sg = fsa.PhaseDiogramSecondVersion(Const.N, self.startprt.M, self.startprt.Pbeg * 1.0e5, self.startprt.Pend * 1.0e5,
                                                                                   self.startprt.T, Const.z,
                                                                                   Const.Pcr, Const.Tcr, Const.omega,
                                                                                   Const.omegaA,
                                                                                   Const.omegaB, Const.Kjk)

            stop = default_timer()
            total_time = stop - start

            mins, secs = divmod(total_time, 60)
            hours, mins = divmod(mins, 60)

            print( 'Finish calculation data' )
            self.lineEdit_3.setText('Finish calculation data')
            print( 'Calculation time is' + str(hours) + 'h ' + str(mins) + 'min ' + str(round(secs, 1)) + 'sec'  )

    def getPlot(self):

        axes = self.canv.fig.add_subplot(212)
        axes2 = self.canv.fig.add_subplot(211)
        axes3d = self.canv.fig.add_subplot( projection='3d')

        print( 'Plotting...' )
        self.lineEdit_3.setText('Plotting...')

        plt.clf()
        try:
            self.horizontalLayout.removeWidget(self.toolbar)
            self.verticalLayout.removeWidget(self.canv)

            sip.delete(self.toolbar)
            sip.delete(self.canv)
            self.toolbar = None
            self.canv = None
            self.verticalLayout.removeItem(self.spacerItem1)
        except Exception as e:
            print(e)
            pass
        self.canv = MatplotlibCanvas(self)
        self.toolbar = Navi(self.canv, self.centralwidget)

        self.horizontalLayout.addWidget(self.toolbar)
        self.verticalLayout.addWidget(self.canv)

        axes.cla()
        axes2.cla()
        axes3d.cla()

        if self.currentPT == self.PlotType[ 0 ]:

            axes = self.canv.fig.add_subplot( 111 )

            scc = None

            scc = axes.contourf( self.Pg / 1.0e5, self.Pl / 1.0e5, self.Sg, np.linspace( 1.0 - np.max( self.Sl ), np.max( self.Sg ), 15 ), cmap = 'BuPu' )

            self.canv.fig.colorbar(scc, ax=axes, label = r'$ S_{gas} $')

            axes.plot( [ self.startprt.Pbeg, self.startprt.Pend ], [ self.startprt.Pbeg, self.startprt.Pend ], 'b-' )

            axes.set_xlabel(r'$ P_{gas} $')
            axes.set_ylabel(r'$ P_{liq} $')

            axes.grid()

        elif self.currentPT == self.PlotType[ 1 ]:

            axes = self.canv.fig.add_subplot( 111 )

            scc = None

            scc = axes.contourf(self.Pg / 1.0e5, self.Pl / 1.0e5, self.Sl, np.linspace( np.min( self.Sl ), np.max( self.Sl ), 15 ), cmap = 'BuPu' )

            self.canv.fig.colorbar(scc, ax=axes, label = r'$ S_{liq} $')

            axes.plot([self.startprt.Pbeg, self.startprt.Pend], [self.startprt.Pbeg, self.startprt.Pend], 'b-')

            axes.set_xlabel(r'$ P_{gas} $')
            axes.set_ylabel(r'$ P_{liq} $')

            axes.grid()

        elif self.currentPT == self.PlotType[ 2 ]:

            axes = self.canv.fig.add_subplot(211)
            axes2 = self.canv.fig.add_subplot(212)

            scc = None

            scc = axes.contourf(self.Pg / 1.0e5, self.Pl / 1.0e5, self.Sg,
                                          np.linspace(1.0 - np.max(self.Sl), np.max(self.Sg), 15), cmap='BuPu')

            self.canv.fig.colorbar(scc, ax=axes, label=r'$ S_{gas} $')

            axes.plot([self.startprt.Pbeg, self.startprt.Pend], [self.startprt.Pbeg, self.startprt.Pend], 'b-')

            axes.set_xlabel(r'$ P_{gas} $')
            axes.set_ylabel(r'$ P_{liq} $')

            axes.grid()

            scc = None

            scc = axes2.contourf(self.Pg / 1.0e5, self.Pl / 1.0e5, self.Sl,
                                          np.linspace(np.min(self.Sl), np.max(self.Sl), 15), cmap='BuPu')

            self.canv.fig.colorbar(scc, ax=axes2, label=r'$ S_{liq} $')

            axes.plot([self.startprt.Pbeg, self.startprt.Pend], [self.startprt.Pbeg, self.startprt.Pend], 'b-')

            axes2.set_xlabel(r'$ P_{gas} $')
            axes2.set_ylabel(r'$ P_{liq} $')

            axes2.grid()

        elif self.currentPT == self.PlotType[ 3 ]:

            print('YES')

            axes3d = self.canv.fig.add_subplot( 111, projection='3d' )

            scc = None

            PG, PL = np.meshgrid( self.Pg / 1.0e5, self.Pl / 1.0e5 )

            scc = axes3d.plot_surface(PG, PL, self.Sl, np.linspace(np.min(self.Sl), np.max(self.Sl), 15), cmap='BuPu' )

            axes3d.set_xlabel(r'$ P_{gas} $')
            axes3d.set_ylabel(r'$ P_{liq} $')
            axes3d.set_zlabel( r'$ S_{liq} $' )

            self.canv.fig.colorbar(scc, ax=axes3d)

        elif self.currentPT == self.PlotType[ 4 ]:

            axes = self.canv.fig.add_subplot(111)

            scc = None

            Const = fsa.Constant(self.filename)

            Tdew = np.arange( 230, 550, 10 )

            Pdew = fsa.DewPoint( Const.N, Const.z, Tdew, Const.Pcr, Const.Tcr, Const.omega, Const.omegaA,
                                Const.omegaB, Const.Kjk) * 1.0e-5

            axes.plot( Tdew, Pdew, 'b-' )

            axes.legend( [ 'Dew line' ] )
            axes.set_xlabel(r'$ T $')
            axes.set_ylabel(r'$ P $')

            axes.grid()

        self.canv.draw()

        ffp.PrintData(self.startprt.Pbeg, self.startprt.Pend, self.startprt.T, self.currentPT)
        print('Finish plot')
        self.lineEdit_3.setText('Finish plot')

    def getCastPlot(self):

        pass

    def Update(self, value):

        self.currentPT = value

    def changeP(self, Pnew):

        self.startprt = None
        self.startprt = fsa.StartParam()

        if Pnew == '':

            self.startprt.Pbeg = 0.0

        else:

            self.startprt.Pbeg = np.float( Pnew )

        print( 'New value of Pbeg =', self.startprt.Pbeg )

    def changeP2(self, Pnew):

        if Pnew == '':

            self.startprt.Pend = 0.0

        else:

            self.startprt.Pend = np.float( Pnew )

        print( 'New value of Pend =', self.startprt.Pend )

    def changeT(self, Tnew):

        if Tnew == '':

            self.startprt.T = 0.0

        else:

            self.startprt.T = np.float( Tnew )

        print('New value of T =', self.startprt.T)

    def changeM(self, Mnew):

        if Mnew == '':

            self.startprt.M = 1

        else:

            self.startprt.M = np.int(Mnew)

        print('New value of M =', self.startprt.M)

#################### FUNCTION OPEN WINDOW ############################################

    def openMComWin(self):

        sip.delete(self.Window)

        self.Window = None

        if self.filename == '':

            print( 'File not found' )
            self.lineEdit_3.setText('File not found')

        else:

            DataTable = ffp.DataForTable( fsa.Constant(self.filename) )

            self.Window = QtWidgets.QMainWindow(self.centralwidget)
            ui = Ui_ConstTab( DataTable )
            ui.setupUi(self.Window)
            self.Window.show()

    def openMVinPWin(self):

        sip.delete(self.Window)

        self.Window = None
        self.Window = QtWidgets.QMainWindow(self.centralwidget)
        self.ui = Ui_VinP(self.filename)
        self.ui.setupUi(self.Window)

        self.Window.show()

    def openCParamWin(self):

        sip.delete(self.Window)

        self.Window = None

        self.Window = QtWidgets.QMainWindow(self.centralwidget)
        ui = Ui_Param()
        ui.setupUi(self.Window)
        ui.lineEdit.textChanged[str].connect( self.changeP )
        ui.lineEdit_2.textChanged[str].connect( self.changeT )
        ui.lineEdit_3.textChanged[str].connect(self.changeM )
        ui.lineEdit_4.textChanged[str].connect( self.changeP2 )
        self.Window.show()

    def openPPlStWin(self):

        sip.delete(self.Window)

        self.Window = None
        self.Window = QtWidgets.QMainWindow(self.centralwidget)
        self.ui = Ui_PlSt()
        self.ui.setupUi(self.Window)
        self.Window.show()

###############################################################################################
###############################################################################################

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "cjCPE Lite"))
        self.label.setText(_translate("MainWindow", "Plot Type"))
        self.label_2.setText(_translate("MainWindow", "PBEG ="))
        self.label_3.setText(_translate("MainWindow", "T ="))
        self.label_4.setText(_translate('MainWindow', 'Log Line'))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuModel.setTitle(_translate("MainWindow", "Model"))
        self.menuStart.setTitle(_translate('MainWindow', 'Calculation'))
        self.menuPlot.setTitle(_translate('MainWindow', 'Plot'))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionTBOpen.setText(_translate('MainWindow', 'Open'))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionMax.setText(_translate("MainWindow", "Max"))
        self.actionNorm.setText(_translate("MainWindow", "Norm"))
        self.actionEoS.setText(_translate('MainWindow', 'Equation os State'))
        self.actionCom.setText(_translate('MainWindow', 'Mixture component'))
        self.actionVinP.setText(_translate( 'MainWindow', 'Condition in point' ))
        self.actionTBVinP.setText(_translate('MainWindow','Condition in point'))
        self.actionStart.setText(_translate('MainWindow', 'Start'))
        self.actionParam.setText(_translate('MainWindow', 'Calculation settings'))
        self.actionTBParam.setText(_translate('MainWindow', 'Calculation settings'))
        self.actionPlotSet.setText(_translate('MainWindow', 'Plot settings'))
        self.actionTBPlSet.setText(_translate('MainWindow', 'Plot setting'))
        self.actionPlot.setText(_translate('MainWindow', 'Plot'))
        self.actionTBPlot.setText(_translate('MainWindow', 'Plot'))

