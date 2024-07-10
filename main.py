from PySide6.QtWidgets import QApplication
from front_page import MyMainWindow

import sys

app = QApplication(sys.argv)
windows = MyMainWindow()
windows.show()
app.exec()