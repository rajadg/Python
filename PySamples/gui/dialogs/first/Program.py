'''
Created on Nov 27, 2013

@author: dgraja
'''

# To use the Gui framework to create a dialog
from PyQt4 import QtGui

# for getting arguments and also application exit
import sys

# for QApplication (the main gui application)
from PySide.QtGui import QApplication

# the dialog created in this sample
from gui.dialogs.first.basicDialog import Ui_Dialog

if __name__ == '__main__':
    # Create a Qt application
    app = QApplication(sys.argv)
    
    # Create a dialog
    Dialog = QtGui.QDialog()
    
    # Create current dialog class instance and show using dialog
    dlg = Ui_Dialog()
    dlg.setupUi(Dialog)
    Dialog.show()

    # Enter Qt application main loop
    app.exec_()
    sys.exit()
    pass