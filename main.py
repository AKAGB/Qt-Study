import sys

from PyQt5 import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from gui import *

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    wd = QWidget()
    wd.setWindowFlags(Qt.Qt.CustomizeWindowHint)
    ui = Ui_Form()
    ui.setupUi(wd)
    with open('window.qss', 'r') as f:
        wd.setStyleSheet(f.read()) 
    wd.show()

    sys.exit(app.exec_())