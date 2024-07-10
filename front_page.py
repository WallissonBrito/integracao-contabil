from PySide6.QtWidgets import QMainWindow, QMenu
from PySide6.QtGui import QAction
# from matplotlib.pylab import f
from ui_index import Ui_MainWindow

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)