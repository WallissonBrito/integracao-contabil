import pandas as pd
from PySide6.QtWidgets import QMainWindow, QFileDialog, QTableWidgetItem
from PySide6.QtGui import QAction
# from matplotlib.pylab import f
from ui_index import Ui_MainWindow

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # load file
        self.df = self.upload_btn.clicked.connect(self.load_data_into_table)

    def separator_file(self):
        file_delimiter = self.comboBox_file_delimiter.currentText()
        if file_delimiter == "Vírgula":
            sep = ","
        elif file_delimiter == "Ponto e Vírgula":
            sep = ";"
        return sep
            
    def load_file(self):
        # Get the separator
        delimiter_data = str(self.separator_file())
        
        # Store the fila_path
        file_path, _ = QFileDialog.getOpenFileName(self, "Selecione o arquivo", "", "CSV files (*.csv)")
        
        # Read the file
        if file_path:
            data = pd.read_csv(file_path, sep=delimiter_data)             
            return data

    def load_data_into_table(self):
        data = self.load_file()
        # Read columns name
        columns = data.columns
        # Set columns name into the table
        self.tableWidget_load_data_page.setHorizontalHeaderLabels(columns)
        # Insert data into the table
        for row_index, row_data in data.iterrows():
            self.tableWidget_load_data_page.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.tableWidget_load_data_page.setItem(row_index,col_index, item)