# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_AboutDialog.ui'
#
# Created: Tue Apr 21 15:16:55 2015
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

class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        AboutDialog.setObjectName(_fromUtf8("AboutDialog"))
        AboutDialog.resize(741, 222)
        self.gridLayout = QtGui.QGridLayout(AboutDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.widget = QtGui.QWidget(AboutDialog)
        self.widget.setMinimumSize(QtCore.QSize(0, 0))
        self.widget.setMaximumSize(QtCore.QSize(180, 16777215))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lblVersion = QtGui.QLabel(self.widget)
        self.lblVersion.setMaximumSize(QtCore.QSize(16777215, 14))
        self.lblVersion.setObjectName(_fromUtf8("lblVersion"))
        self.verticalLayout.addWidget(self.lblVersion)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtGui.QDialogButtonBox(self.widget)
        self.buttonBox.setMaximumSize(QtCore.QSize(200, 16777215))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        self.tabWidget = QtGui.QTabWidget(AboutDialog)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.memAbout = QtGui.QTextEdit(self.tab)
        self.memAbout.setUndoRedoEnabled(False)
        self.memAbout.setReadOnly(True)
        self.memAbout.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.memAbout.setObjectName(_fromUtf8("memAbout"))
        self.gridLayout_2.addWidget(self.memAbout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab_3)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.memContrib = QtGui.QTextEdit(self.tab_3)
        self.memContrib.setUndoRedoEnabled(False)
        self.memContrib.setReadOnly(True)
        self.memContrib.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.memContrib.setObjectName(_fromUtf8("memContrib"))
        self.gridLayout_3.addWidget(self.memContrib, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.memAcknowl = QtGui.QTextEdit(self.tab_2)
        self.memAcknowl.setUndoRedoEnabled(False)
        self.memAcknowl.setReadOnly(True)
        self.memAcknowl.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.memAcknowl.setObjectName(_fromUtf8("memAcknowl"))
        self.gridLayout_4.addWidget(self.memAcknowl, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.gridLayout_5 = QtGui.QGridLayout(self.tab_4)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.memChangeLog = QtGui.QTextEdit(self.tab_4)
        self.memChangeLog.setUndoRedoEnabled(False)
        self.memChangeLog.setReadOnly(True)
        self.memChangeLog.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.memChangeLog.setObjectName(_fromUtf8("memChangeLog"))
        self.gridLayout_5.addWidget(self.memChangeLog, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)

        self.retranslateUi(AboutDialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), AboutDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), AboutDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AboutDialog)

    def retranslateUi(self, AboutDialog):
        AboutDialog.setWindowTitle(_translate("AboutDialog", "About", None))
        self.lblVersion.setText(_translate("AboutDialog", "Version:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("AboutDialog", "About ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("AboutDialog", "Contributors", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("AboutDialog", "Contact", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("AboutDialog", "Change Log", None))

