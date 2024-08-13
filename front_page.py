import pandas as pd
from PySide6.QtWidgets import QMainWindow, QFileDialog, QTableWidgetItem, QComboBox
from PySide6.QtGui import QAction
# from matplotlib.pylab import f
from ui_index import Ui_MainWindow

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)        
        self.settings_page_btn.setChecked(True)

        # Variables    
        self.type_file = None
        self.delimiter_data = None
        self.encoding_data = None
        self.choiced_period = None
        self.choiced_moth = None
        self.year = None
        self.company = None
        self.cnpj = None
        self.data = None
        self.new_data = None
        self.data_columns = None
        self.name_account_column = None
        self.name_descretion_account_column = None
        self.name_value_column = None

        # Constants
        self.ACCOUNT_LIST = [
            '1','1.01','1.01.01', '1.01.02', '1.01.04', '1.02', '1.02.01', '2', '2.01',
            '2.01.04', '2.02', '2.02.01', '2.03', '3.01', '3.02', '3.03', '3.05', '3.08', '6.01.01.02'
        ]
        self.ACCOUNT_BALANCE_SHEET_ASSETS = ['1','1.01','1.01.01', '1.01.02', '1.01.04', '1.02', '1.02.01']
        self.ACCOUNT_BALANCE_SHEET_LIABILITIES = ['2', '2.01', '2.01.04', '2.02', '2.02.01', '2.03']
        self.ACCOUNT_RESULTS = ['3.01', '3.02', '3.03', '3.05', '3.08']        
        self.CASH_FLOW = ['6.01.01.02'] 

        # Switch pages
        self.settings_page_btn.clicked.connect(self.switch_to_setting_page)
        self.load_file_page_btn.clicked.connect(self.switch_to_load_file_page)
        self.update_data_page_btn.clicked.connect(self.switch_to_update_data_page)
        self.exportation_page_btn.clicked.connect(self.switch_to_exportation_page)

        # buttons
        self.choiced_type_file = self.save_btn_load_data_page.clicked.connect(self.save_settings)
        self.upload_file_next_btn.clicked.connect(self.get_selected_columns)
        self.next_btn_update_data_page.clicked.connect(self.load_new_data_into_table)


        # load file
        self.upload_file_btn.clicked.connect(self.load_data_into_table)

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////
# /////////// SETTINGS PAGE/////////////////////////////////////////////////////////////////////////////////

    # Save selected settings
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

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////
# /////////// UPLOAD FILE PAGE  /////////////////////////////////////////////////////////////////////////////

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
        self.data = self.load_file()
        # Read columns name
        self.data_columns = self.data.columns
        # Set coluns name to the table
        self.upload_file_table.setColumnCount(len(self.data_columns))        
        # Set columns name to the combobox
        self.set_columns_to_combobox(self.data_columns)

        # Set columns name into the table
        self.upload_file_table.setHorizontalHeaderLabels(self.data_columns)
        # Insert data into the table
        for row_index, row_data in self.data.iterrows():
            self.upload_file_table.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.upload_file_table.setItem(row_index,col_index, item)
                
    # Set the columns into combobox
    def set_columns_to_combobox(self, columns):
        for column in columns:
            self.comboBox_select_account.addItem(column)
            self.comboBox_select_desc_account.addItem(column)
            self.comboBox_select_value.addItem(column)

    # Get the comboboxes value selected 
    def get_selected_columns(self):
        self.name_account_column = self.comboBox_select_account.currentText()
        self.name_descretion_account_column = self.comboBox_select_desc_account.currentText()
        self.name_value_column = self.comboBox_select_value.currentText()
        self.switch_to_update_data_page()
        self.insert_combobox_into_table()


    # Get the account data
    def get_account_column(self):
        # Get the column`s name
        column = self.name_account_column
        # Get data`s column
        data_account_column = self.data[column]
        # Delete Nan
        data_account_column.dropna(inplace=True)
        return data_account_column


# ///////////////////////////////////////////////////////////////////////////////////////////////////////////
# /////////// UPDATE DATA PAGE  /////////////////////////////////////////////////////////////////////////////

    def insert_combobox_into_table(self):
        data_items = self.get_account_column()

        self.combo_boxes = []  # List to store combo box instances
        for i in range(0,19):
            self.row_comboBox = QComboBox()  # Combobox instance
            self.row_comboBox.addItem("SELECIONE")
            self.row_comboBox.addItems(data_items)  # Add items to combobox
            self.update_account_table.setCellWidget(i, 2, self.row_comboBox)  # Insert combobox into the table
            self.combo_boxes.append(self.row_comboBox)  # Store combo box instance
            
    def read_combobox_values(self):
        combobox_values = [comboBox.currentText() for comboBox in self.combo_boxes]
        print(combobox_values)
        return combobox_values

    def update_account_value(self):
        # Get data
        data = self.data
        # read combobox values
        combobox_values = self.read_combobox_values()

        # Update data
        for old_value, new_value in zip(combobox_values, self.ACCOUNT_LIST):
            data.loc[data["Conta"] == old_value, self.name_account_column] = new_value     
        return data
        
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////
# /////////// EXPORTATION DATA PAGE  /////////////////////////////////////////////////////////////////////////////
    def create_statement_column(self, data):
        data = data.copy()
        # Create column
        data['DEMONSTRATIVO'] = ""

        # Verify account 
        is_balance_sheet_assets = data.loc[:,self.name_account_column].isin(self.ACCOUNT_BALANCE_SHEET_ASSETS)
        is_balance_sheet_liabilities = data.loc[:,self.name_account_column].isin(self.ACCOUNT_BALANCE_SHEET_LIABILITIES)
        is_results = data.loc[:,self.name_account_column].isin(self.ACCOUNT_RESULTS)
        is_cashflow = data.loc[:,self.name_account_column].isin(self.CASH_FLOW)

        # Create the column
        data.loc[is_balance_sheet_assets, 'DEMONSTRATIVO'] = 'Balanço Patrimonial Ativo'
        data.loc[is_balance_sheet_liabilities, 'DEMONSTRATIVO'] = 'Balanço Patrimonial Passivo'
        data.loc[is_results, 'DEMONSTRATIVO'] = 'Demonstração do Resultado'
        data.loc[is_cashflow, 'DEMONSTRATIVO'] = 'Demonstração do Fluxo de Caixa' 
        
        return data

    def create_new_data(self):
        # update account values 
        new_data = self.update_account_value()
        # copy new_data
        new_data = new_data.copy()
        # Filtering only accounts that have been changed
        new_data = new_data.loc[new_data[self.name_account_column].isin(self.ACCOUNT_LIST)]

        # Add data
        new_data.loc[:,'CNPJ'] = self.cnpj    
        new_data.loc[:,'EMPRESA'] = self.company
        new_data.loc[:,'ANO'] = self.year
        new_data.loc[:,'MES'] = self.choiced_moth
        new_data.loc[:,'PERIODO'] = self.choiced_period.upper()
        new_data = self.create_statement_column(new_data)

        # Filtering columns 
        new_data = new_data[['CNPJ', 'EMPRESA', self.name_account_column, 
                             self.name_descretion_account_column, self.name_value_column, 'DEMONSTRATIVO', 'ANO', 'MES', 'PERIODO']]

        # Update name`s column `
        columns_name = ['CNPJ', 'EMPRESA', 'CONTA', 'DESCRIÇÃO', 'VALOR', 'DEMONSTRATIVO', 'ANO', 'MES', 'PERIODO']
        new_data.columns = columns_name

        new_data.reset_index(inplace=True, drop=True)
        return new_data

    def load_new_data_into_table(self):
        new_data = self.create_new_data()

        # Verifique se os dados estão sendo gerados corretamente
        if new_data is None or new_data.empty:
            print("No new data to load into the table.")
            return  # Exit the function if there is no data
        # else:
        #     print(new_data)
        #     print("Dados gerados")
        
        # Read columns name
        new_data_columns = new_data.columns

        # Set coluns name to the table
        self.export_table.setColumnCount(len(new_data_columns))
        self.export_table.setHorizontalHeaderLabels(new_data_columns)

        # Clear the existing rows in the table
        self.export_table.setRowCount(0)    

        # Insert data into the table
        for row_index, row_data in new_data.iterrows():
            self.export_table.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.export_table.setItem(row_index, col_index, item)
            
        # Change page
        self.switch_to_exportation_page()

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