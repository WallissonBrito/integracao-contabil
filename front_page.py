import pandas as pd
from PySide6.QtWidgets import QMainWindow, QFileDialog, QTableWidgetItem
from PySide6.QtGui import QAction
# from matplotlib.pylab import f
from ui_index import Ui_MainWindow

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)        
        self.settings_page_btn.setChecked(True)

        # Switch pages
        self.settings_page_btn.clicked.connect(self.switch_to_setting_page)
        self.load_file_page_btn.clicked.connect(self.switch_to_load_file_page)
        self.update_data_page_btn.clicked.connect(self.switch_to_update_data_page)
        self.exportation_page_btn.clicked.connect(self.switch_to_exportation_page)

        # Variable to store the settings value    
        self.type_file = None
        self.delimiter_data = None
        self.encoding_data = None
        self.choiced_period = None
        self.choiced_moth = None
        self.year = None
        self.company = None
        self.cnpj = None

        # Settings
        self.choiced_type_file = self.save_btn_load_data_page.clicked.connect(self.save_settings)

        # load file
        self.upload_file_btn.clicked.connect(self.load_data_into_table)


    def save_settings(self):
        self.type_file = self.type_file_comboBox.currentText()
        self.delimiter_data = self.delimiter_comboBox_file.currentText()
        self.encoding_data = self.encoding_comboBox_file.currentText()
        self.choiced_period = self.period_comboBox.currentText()
        self.choiced_moth = self.month_comboBox_select.currentText()
        self.year = self.year_lineEdit.text()
        self.company = self.names_company_lineEdit.text()
        self.cnpj = self.cnpj_lineEdit.text()      
        self.switch_to_load_file_page() 

    def separator_file(self):
        # Get choiced delimiter
        file_delimiter = self.delimiter_data
        if file_delimiter == "Vírgula":
            sep = ","
        elif file_delimiter == "Ponto e Vírgula":
            sep = ";"
        return sep
            
    def load_file(self ):
        # Get the separator
        delimiter_data = self.separator_file()
        type_file = self.type_file
        selected_encoding = self.encoding_data

        # text_type_file = None
        if type_file == ".csv":
            text_type_file = "CSV files (*.csv)"

        # Store the fila_path
        file_path, _ = QFileDialog.getOpenFileName(self, "Selecione o arquivo", "", text_type_file)
        
        # Read the file
        if file_path:
            data = pd.read_csv(file_path, sep=str(delimiter_data), encoding=selected_encoding )             
            return data

    def load_data_into_table(self):

        data = self.load_file()
        # Read columns name
        columns = data.columns
        self.upload_file_table.setColumnCount(len(columns))

        # Set columns name into the table
        self.upload_file_table.setHorizontalHeaderLabels(columns)
        # Insert data into the table
        for row_index, row_data in data.iterrows():
            self.upload_file_table.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.upload_file_table.setItem(row_index,col_index, item)

    def set_account_name(self):
        data = self.load_file()
        columns = data.columns
        print(columns)

    def add_data_update_colums_page(self):
        # self.switch_to_update_column_page()
        self.set_account_name()

    def switch_to_setting_page(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_load_file_page(self):
        self.stackedWidget.setCurrentIndex(1)
        self.load_file_page_btn.setChecked(True)
        
    def switch_to_update_data_page(self):
        self.stackedWidget.setCurrentIndex(2)
        self.update_data_page_btn.setChecked(True)

    def switch_to_exportation_page(self):
        self.stackedWidget.setCurrentIndex(3)
        self.exportation_page_btn.setChecked(True)