import pandas as pd
from PySide6.QtWidgets import QMainWindow, QFileDialog, QTableWidgetItem
from PySide6.QtGui import QAction
# from matplotlib.pylab import f
from ui_index import Ui_MainWindow

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)        
        self.load_data_page_btn.setChecked(True)
        # load file
        self.df = self.upload_btn.clicked.connect(self.load_data_into_table)

        # Switch pages
        self.load_data_page_btn.clicked.connect(self.switch_to_load_data_page)
        self.update_column_page_btn.clicked.connect(self.switch_to_update_column_page)
        self.add_period_page_btn.clicked.connect(self.switch_to_add_period_page)
        self.update_accounts_page_btn.clicked.connect(self.switch_to_update_accounts)
        self.exportation_page_btn.clicked.connect(self.switch_to_exportation_page)

        # Next page button
        self.next_btn_load_data_page.clicked.connect(self.switch_to_update_column_page)
        self.next_btn_update_column_page.clicked.connect(self.switch_to_add_period_page)
        self.next_btn_add_data_page.clicked.connect(self.switch_to_update_accounts)
        self.next_btn_update_accounts_page.clicked.connect(self.switch_to_exportation_page)

    def separator_file(self):
        file_delimiter = self.comboBox_file_delimiter.currentText()
        if file_delimiter == "Vírgula":
            sep = ","
        elif file_delimiter == "Ponto e Vírgula":
            sep = ";"
        return sep
            
    def load_file(self):
        # Get the separator
        delimiter_data = self.separator_file()
        
        # Store the fila_path
        file_path, _ = QFileDialog.getOpenFileName(self, "Selecione o arquivo", "", "CSV files (*.csv)")
        
        # Read the file
        if file_path:
            data = pd.read_csv(file_path, sep=str(delimiter_data))             
            return data

    def load_data_into_table(self):
        data = self.load_file()
        # Read columns name
        columns = data.columns
        self.tableWidget_load_data_page.setColumnCount(len(columns))

        # Set columns name into the table
        self.tableWidget_load_data_page.setHorizontalHeaderLabels(columns)
        # Insert data into the table
        for row_index, row_data in data.iterrows():
            self.tableWidget_load_data_page.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.tableWidget_load_data_page.setItem(row_index,col_index, item)

    def switch_to_load_data_page(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_update_column_page(self):
        self.stackedWidget.setCurrentIndex(1)
        self.update_column_page_btn.setChecked(True)
        
    def switch_to_add_period_page(self):
        self.stackedWidget.setCurrentIndex(2)
        self.add_period_page_btn.setChecked(True)

    def switch_to_update_accounts(self):
        self.stackedWidget.setCurrentIndex(3)
        self.update_accounts_page_btn.setChecked(True)

    def switch_to_exportation_page(self):
        self.stackedWidget.setCurrentIndex(4)
        self.exportation_page_btn.setChecked(True)