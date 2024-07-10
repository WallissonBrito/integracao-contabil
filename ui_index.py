# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_index_md.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(997, 753)
        MainWindow.setStyleSheet(u"QLineEdit{\n"
"	border:1px solid gray;\n"
"	border-radius: 6px;\n"
"	padding-left:15px;\n"
"	height: 35px;\n"
"	background-color:white;\n"
"	color:black;\n"
"}\n"
"QDateEdit{\n"
"	border:1px solid gray;\n"
"	border-radius: 6px;\n"
"	padding-left:15px;\n"
"	height: 31px;\n"
"	background-color:white;\n"
"	color:black;\n"
"}\n"
"QComboBox{\n"
"	border:2px solid white;\n"
"	border-radius: 8px;\n"
"	padding:1px 18px 1px 3px;\n"
"	background-color:black;\n"
"	color:white;\n"
"	height: 35px;\n"
"	padding-left: 15px;\n"
"	font-weight:bold;\n"
"	selection-background-color:#2980B9;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.left_frame = QWidget(self.centralwidget)
        self.left_frame.setObjectName(u"left_frame")
        self.left_frame.setGeometry(QRect(0, 0, 181, 751))
        self.left_frame.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: white;\n"
"	border: None;\n"
"}\n"
"\n"
"QPushButton {\n"
"	height: 30px;\n"
"	border:None\n"
"}")
        self.layoutWidget = QWidget(self.left_frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 10, 181, 741))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 20, 0, 25)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setPixmap(QPixmap(u":/newPrefix/icons/financessmall2.png"))

        self.horizontalLayout.addWidget(self.label_5)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.vLayout_btns_page = QVBoxLayout()
        self.vLayout_btns_page.setSpacing(20)
        self.vLayout_btns_page.setObjectName(u"vLayout_btns_page")
        self.vLayout_btns_page.setContentsMargins(-1, 20, -1, -1)
        self.load_data_page_btn = QPushButton(self.layoutWidget)
        self.load_data_page_btn.setObjectName(u"load_data_page_btn")
        self.load_data_page_btn.setMinimumSize(QSize(0, 30))
        self.load_data_page_btn.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.load_data_page_btn.setFont(font)
        self.load_data_page_btn.setStyleSheet(u"QPushButton:hover {\n"
"	color:#12B298;\n"
"}\n"
"QPushButton:checked {\n"
"	color:#12B298;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.load_data_page_btn.setCheckable(True)
        self.load_data_page_btn.setAutoExclusive(True)

        self.vLayout_btns_page.addWidget(self.load_data_page_btn)

        self.upddate_column_page_btn = QPushButton(self.layoutWidget)
        self.upddate_column_page_btn.setObjectName(u"upddate_column_page_btn")
        self.upddate_column_page_btn.setMinimumSize(QSize(0, 30))
        self.upddate_column_page_btn.setMaximumSize(QSize(16777215, 30))
        self.upddate_column_page_btn.setFont(font)
        self.upddate_column_page_btn.setStyleSheet(u"QPushButton:hover {\n"
"	color:#12B298;\n"
"}\n"
"QPushButton:checked {\n"
"	color:#12B298;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.upddate_column_page_btn.setCheckable(True)
        self.upddate_column_page_btn.setAutoExclusive(True)

        self.vLayout_btns_page.addWidget(self.upddate_column_page_btn)

        self.add_data_page_btn = QPushButton(self.layoutWidget)
        self.add_data_page_btn.setObjectName(u"add_data_page_btn")
        self.add_data_page_btn.setMinimumSize(QSize(0, 30))
        self.add_data_page_btn.setMaximumSize(QSize(16777215, 30))
        self.add_data_page_btn.setFont(font)
        self.add_data_page_btn.setStyleSheet(u"QPushButton:hover {\n"
"	color:#12B298;\n"
"}\n"
"QPushButton:checked {\n"
"	color:#12B298;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.add_data_page_btn.setCheckable(True)
        self.add_data_page_btn.setAutoExclusive(True)

        self.vLayout_btns_page.addWidget(self.add_data_page_btn)

        self.upddate_accounts_page_btn = QPushButton(self.layoutWidget)
        self.upddate_accounts_page_btn.setObjectName(u"upddate_accounts_page_btn")
        self.upddate_accounts_page_btn.setMinimumSize(QSize(0, 30))
        self.upddate_accounts_page_btn.setMaximumSize(QSize(16777215, 30))
        self.upddate_accounts_page_btn.setFont(font)
        self.upddate_accounts_page_btn.setStyleSheet(u"QPushButton:hover {\n"
"	color:#12B298;\n"
"}\n"
"QPushButton:checked {\n"
"	color:#12B298;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.upddate_accounts_page_btn.setCheckable(True)
        self.upddate_accounts_page_btn.setAutoExclusive(True)

        self.vLayout_btns_page.addWidget(self.upddate_accounts_page_btn)

        self.exportation_page_btn = QPushButton(self.layoutWidget)
        self.exportation_page_btn.setObjectName(u"exportation_page_btn")
        self.exportation_page_btn.setMinimumSize(QSize(0, 30))
        self.exportation_page_btn.setMaximumSize(QSize(16777215, 30))
        self.exportation_page_btn.setFont(font)
        self.exportation_page_btn.setStyleSheet(u"QPushButton:hover {\n"
"	color:#12B298;\n"
"}\n"
"QPushButton:checked {\n"
"	color:#12B298;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.exportation_page_btn.setCheckable(True)
        self.exportation_page_btn.setAutoExclusive(True)

        self.vLayout_btns_page.addWidget(self.exportation_page_btn)


        self.verticalLayout_3.addLayout(self.vLayout_btns_page)

        self.verticalSpacer = QSpacerItem(20, 278, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.exit_btn = QPushButton(self.layoutWidget)
        self.exit_btn.setObjectName(u"exit_btn")
        self.exit_btn.setMinimumSize(QSize(0, 30))
        self.exit_btn.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.exit_btn.setFont(font1)
        self.exit_btn.setStyleSheet(u"QPushButton:hover {\n"
"	color:#12B298;\n"
"}\n"
"QPushButton:checked {\n"
"	color:#12B298;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.exit_btn.setIconSize(QSize(20, 30))
        self.exit_btn.setCheckable(True)
        self.exit_btn.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.exit_btn)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(190, 10, 801, 731))
        self.stackedWidget.setStyleSheet(u"QLineEdit{\n"
"	border:1px solid gray;\n"
"	border-radius: 6px;\n"
"	padding-left:15px;\n"
"	height: 35px;\n"
"	background-color:white;\n"
"	color:black;\n"
"}\n"
"QDateEdit{\n"
"	border:1px solid gray;\n"
"	border-radius: 6px;\n"
"	padding-left:15px;\n"
"	height: 31px;\n"
"	background-color:white;\n"
"	color:black;\n"
"}\n"
"QComboBox{\n"
"	border:2px solid white;\n"
"	border-radius: 8px;\n"
"	padding:1px 18px 1px 3px;\n"
"	background-color:black;\n"
"	color:white;\n"
"	height: 35px;\n"
"	padding-left: 15px;\n"
"	font-weight:bold;\n"
"	selection-background-color:#2980B9;\n"
"}\n"
"QLabel{\n"
"color: black;\n"
"}\n"
"")
        self.a_load_data_page = QWidget()
        self.a_load_data_page.setObjectName(u"a_load_data_page")
        self.a_load_data_page.setMaximumSize(QSize(801, 731))
        self.a_load_data_page.setStyleSheet(u"")
        self.widget_load_data_page = QWidget(self.a_load_data_page)
        self.widget_load_data_page.setObjectName(u"widget_load_data_page")
        self.widget_load_data_page.setGeometry(QRect(0, 0, 801, 741))
        self.widget_load_data_page.setStyleSheet(u"")
        self.botton_frame_widget_load_data_page = QWidget(self.widget_load_data_page)
        self.botton_frame_widget_load_data_page.setObjectName(u"botton_frame_widget_load_data_page")
        self.botton_frame_widget_load_data_page.setGeometry(QRect(0, 660, 801, 70))
        self.botton_frame_widget_load_data_page.setMinimumSize(QSize(0, 70))
        self.botton_frame_widget_load_data_page.setMaximumSize(QSize(16777215, 0))
        font2 = QFont()
        font2.setPointSize(13)
        self.botton_frame_widget_load_data_page.setFont(font2)
        self.botton_frame_widget_load_data_page.setStyleSheet(u"")
        self.layoutWidget_7 = QWidget(self.botton_frame_widget_load_data_page)
        self.layoutWidget_7.setObjectName(u"layoutWidget_7")
        self.layoutWidget_7.setGeometry(QRect(0, 0, 801, 71))
        self.hLayout_bottom_frame_4 = QHBoxLayout(self.layoutWidget_7)
        self.hLayout_bottom_frame_4.setObjectName(u"hLayout_bottom_frame_4")
        self.hLayout_bottom_frame_4.setContentsMargins(0, 0, 10, 0)
        self.horizontalSpacer_7 = QSpacerItem(598, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hLayout_bottom_frame_4.addItem(self.horizontalSpacer_7)

        self.next_btn_load_data_page = QPushButton(self.layoutWidget_7)
        self.next_btn_load_data_page.setObjectName(u"next_btn_load_data_page")
        self.next_btn_load_data_page.setMinimumSize(QSize(150, 35))
        self.next_btn_load_data_page.setMaximumSize(QSize(150, 35))
        self.next_btn_load_data_page.setStyleSheet(u"QPushButton{\n"
"	background-color: #34D481;\n"
"	color:white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight:bold;\n"
"	font-size: 15px;\n"
"}")

        self.hLayout_bottom_frame_4.addWidget(self.next_btn_load_data_page)

        self.table_frame_widget_load_data_page = QWidget(self.widget_load_data_page)
        self.table_frame_widget_load_data_page.setObjectName(u"table_frame_widget_load_data_page")
        self.table_frame_widget_load_data_page.setGeometry(QRect(0, 220, 801, 431))
        self.tableWidget_load_data_page = QTableWidget(self.table_frame_widget_load_data_page)
        if (self.tableWidget_load_data_page.columnCount() < 7):
            self.tableWidget_load_data_page.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_load_data_page.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_load_data_page.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_load_data_page.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_load_data_page.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_load_data_page.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_load_data_page.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_load_data_page.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tableWidget_load_data_page.setObjectName(u"tableWidget_load_data_page")
        self.tableWidget_load_data_page.setGeometry(QRect(0, 0, 801, 431))
        self.tableWidget_load_data_page.horizontalHeader().setMinimumSectionSize(32)
        self.tableWidget_load_data_page.horizontalHeader().setDefaultSectionSize(110)
        self.buttons_widget_load_data_page = QWidget(self.widget_load_data_page)
        self.buttons_widget_load_data_page.setObjectName(u"buttons_widget_load_data_page")
        self.buttons_widget_load_data_page.setGeometry(QRect(0, 70, 801, 141))
        self.buttons_widget_load_data_page.setStyleSheet(u"")
        self.layoutWidget1 = QWidget(self.buttons_widget_load_data_page)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 0, 801, 141))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 0, 0, 0)
        self.label = QLabel(self.layoutWidget1)
        self.label.setObjectName(u"label")
        font3 = QFont()
        font3.setPointSize(10)
        self.label.setFont(font3)

        self.verticalLayout_2.addWidget(self.label)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 10, 400, 20)
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_10 = QLabel(self.layoutWidget1)
        self.label_10.setObjectName(u"label_10")
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(11)
        self.label_10.setFont(font4)
        self.label_10.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_9.addWidget(self.label_10)

        self.comboBox_file_delimiter = QComboBox(self.layoutWidget1)
        self.comboBox_file_delimiter.addItem("")
        self.comboBox_file_delimiter.addItem("")
        self.comboBox_file_delimiter.setObjectName(u"comboBox_7")
        self.comboBox_file_delimiter.setMinimumSize(QSize(187, 35))
        self.comboBox_file_delimiter.setMaximumSize(QSize(187, 35))
        self.comboBox_file_delimiter.setStyleSheet(u"QComboBox{\n"
"	border:2px solid white;\n"
"	border-radius: 8px;\n"
"	padding:1px 18px 1px 3px;\n"
"	background-color:black;\n"
"	color:white;\n"
"	height: 35px;\n"
"	padding-left: 15px;\n"
"	font-weight:bold;\n"
"	selection-background-color:#2980B9;\n"
"	selection-background-color:#2980B9;\n"
"}")

        self.verticalLayout_9.addWidget(self.comboBox_file_delimiter)


        self.horizontalLayout_7.addLayout(self.verticalLayout_9)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, -1, 0, -1)
        self.label_11 = QLabel(self.layoutWidget1)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font4)
        self.label_11.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_11.addWidget(self.label_11)

        self.upload_btn = QPushButton(self.layoutWidget1)
        self.upload_btn.setObjectName(u"upload_btn_5")
        self.upload_btn.setMinimumSize(QSize(150, 32))
        self.upload_btn.setMaximumSize(QSize(150, 32))
        self.upload_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: #34D481;\n"
"	color:white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight:bold;\n"
"	font-size: 15px;\n"
"}")

        self.verticalLayout_11.addWidget(self.upload_btn)


        self.horizontalLayout_7.addLayout(self.verticalLayout_11)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.top_frame_widget_load_data_page = QWidget(self.widget_load_data_page)
        self.top_frame_widget_load_data_page.setObjectName(u"top_frame_widget_load_data_page")
        self.top_frame_widget_load_data_page.setGeometry(QRect(0, 0, 801, 61))
        self.top_frame_widget_load_data_page.setMinimumSize(QSize(0, 61))
        self.top_frame_widget_load_data_page.setMaximumSize(QSize(16777215, 61))
        self.top_frame_widget_load_data_page.setFont(font2)
        self.top_frame_widget_load_data_page.setStyleSheet(u"")
        self.layoutWidget_9 = QWidget(self.top_frame_widget_load_data_page)
        self.layoutWidget_9.setObjectName(u"layoutWidget_9")
        self.layoutWidget_9.setGeometry(QRect(0, 0, 801, 62))
        self.horizontalLayout_8 = QHBoxLayout(self.layoutWidget_9)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.title_page_load_data_page = QLabel(self.layoutWidget_9)
        self.title_page_load_data_page.setObjectName(u"title_page_load_data_page")
        font5 = QFont()
        font5.setFamilies([u"Arial Black"])
        font5.setPointSize(20)
        font5.setBold(True)
        self.title_page_load_data_page.setFont(font5)
        self.title_page_load_data_page.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.title_page_load_data_page.setMargin(10)

        self.horizontalLayout_8.addWidget(self.title_page_load_data_page)

        self.horizontalSpacer_8 = QSpacerItem(348, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_8)

        self.label_load_data_page = QLabel(self.layoutWidget_9)
        self.label_load_data_page.setObjectName(u"label_load_data_page")
        font6 = QFont()
        font6.setPointSize(11)
        self.label_load_data_page.setFont(font6)
        self.label_load_data_page.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_load_data_page.setMargin(20)

        self.horizontalLayout_8.addWidget(self.label_load_data_page)

        self.stackedWidget.addWidget(self.a_load_data_page)
        self.b_update_column_page = QWidget()
        self.b_update_column_page.setObjectName(u"b_update_column_page")
        self.b_update_column_page.setMaximumSize(QSize(801, 731))
        self.central_widget_update_column_page = QWidget(self.b_update_column_page)
        self.central_widget_update_column_page.setObjectName(u"central_widget_update_column_page")
        self.central_widget_update_column_page.setGeometry(QRect(0, 0, 801, 741))
        self.central_widget_update_column_page.setStyleSheet(u"")
        self.botton_frame_widget_update_column_page = QWidget(self.central_widget_update_column_page)
        self.botton_frame_widget_update_column_page.setObjectName(u"botton_frame_widget_update_column_page")
        self.botton_frame_widget_update_column_page.setGeometry(QRect(0, 660, 801, 70))
        self.botton_frame_widget_update_column_page.setMinimumSize(QSize(0, 70))
        self.botton_frame_widget_update_column_page.setMaximumSize(QSize(16777215, 0))
        self.botton_frame_widget_update_column_page.setFont(font2)
        self.botton_frame_widget_update_column_page.setStyleSheet(u"")
        self.layoutWidget_4 = QWidget(self.botton_frame_widget_update_column_page)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(0, 0, 801, 71))
        self.hLayout_bottom_frame_3 = QHBoxLayout(self.layoutWidget_4)
        self.hLayout_bottom_frame_3.setObjectName(u"hLayout_bottom_frame_3")
        self.hLayout_bottom_frame_3.setContentsMargins(0, 0, 10, 0)
        self.horizontalSpacer_5 = QSpacerItem(598, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hLayout_bottom_frame_3.addItem(self.horizontalSpacer_5)

        self.next_btn_update_column_page = QPushButton(self.layoutWidget_4)
        self.next_btn_update_column_page.setObjectName(u"next_btn_update_column_page")
        self.next_btn_update_column_page.setMinimumSize(QSize(150, 35))
        self.next_btn_update_column_page.setMaximumSize(QSize(150, 35))
        self.next_btn_update_column_page.setStyleSheet(u"QPushButton{\n"
"	background-color: #34D481;\n"
"	color:white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight:bold;\n"
"	font-size: 15px;\n"
"}")

        self.hLayout_bottom_frame_3.addWidget(self.next_btn_update_column_page)

        self.table_frame_widget_update_column_page = QWidget(self.central_widget_update_column_page)
        self.table_frame_widget_update_column_page.setObjectName(u"table_frame_widget_update_column_page")
        self.table_frame_widget_update_column_page.setGeometry(QRect(0, 220, 801, 431))
        self.tableWidget_update_column_page = QTableWidget(self.table_frame_widget_update_column_page)
        if (self.tableWidget_update_column_page.columnCount() < 7):
            self.tableWidget_update_column_page.setColumnCount(7)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_update_column_page.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_update_column_page.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_update_column_page.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_update_column_page.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_update_column_page.setHorizontalHeaderItem(4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_update_column_page.setHorizontalHeaderItem(5, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_update_column_page.setHorizontalHeaderItem(6, __qtablewidgetitem13)
        self.tableWidget_update_column_page.setObjectName(u"tableWidget_update_column_page")
        self.tableWidget_update_column_page.setGeometry(QRect(0, 0, 801, 431))
        self.tableWidget_update_column_page.horizontalHeader().setMinimumSectionSize(32)
        self.tableWidget_update_column_page.horizontalHeader().setDefaultSectionSize(110)
        self.buttons_widget_update_column_page = QWidget(self.central_widget_update_column_page)
        self.buttons_widget_update_column_page.setObjectName(u"buttons_widget_update_column_page")
        self.buttons_widget_update_column_page.setGeometry(QRect(0, 70, 801, 141))
        self.buttons_widget_update_column_page.setStyleSheet(u"")
        self.layoutWidget2 = QWidget(self.buttons_widget_update_column_page)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(0, 0, 801, 141))
        self.verticalLayout = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font3)

        self.verticalLayout.addWidget(self.label_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 10, 200, 20)
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_select_account = QLabel(self.layoutWidget2)
        self.label_select_account.setObjectName(u"label_select_account")
        self.label_select_account.setMinimumSize(QSize(187, 17))
        self.label_select_account.setMaximumSize(QSize(187, 17))
        self.label_select_account.setFont(font4)
        self.label_select_account.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_6.addWidget(self.label_select_account)

        self.comboBox_select_account = QComboBox(self.layoutWidget2)
        self.comboBox_select_account.addItem("")
        self.comboBox_select_account.setObjectName(u"comboBox_select_account")
        self.comboBox_select_account.setMinimumSize(QSize(187, 35))
        self.comboBox_select_account.setMaximumSize(QSize(187, 35))
        self.comboBox_select_account.setStyleSheet(u"QComboBox{\n"
"	border:2px solid white;\n"
"	border-radius: 8px;\n"
"	padding:1px 18px 1px 3px;\n"
"	background-color:black;\n"
"	color:white;\n"
"	height: 35px;\n"
"	padding-left: 15px;\n"
"	font-weight:bold;\n"
"	selection-background-color:#2980B9;\n"
"}")

        self.verticalLayout_6.addWidget(self.comboBox_select_account)


        self.horizontalLayout_5.addLayout(self.verticalLayout_6)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_select_desc_account = QLabel(self.layoutWidget2)
        self.label_select_desc_account.setObjectName(u"label_select_desc_account")
        self.label_select_desc_account.setMinimumSize(QSize(0, 17))
        self.label_select_desc_account.setMaximumSize(QSize(16777215, 17))
        self.label_select_desc_account.setFont(font4)
        self.label_select_desc_account.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_10.addWidget(self.label_select_desc_account)

        self.comboBox_select_desc_account = QComboBox(self.layoutWidget2)
        self.comboBox_select_desc_account.addItem("")
        self.comboBox_select_desc_account.setObjectName(u"comboBox_select_desc_account")
        self.comboBox_select_desc_account.setMinimumSize(QSize(187, 35))
        self.comboBox_select_desc_account.setMaximumSize(QSize(187, 35))
        self.comboBox_select_desc_account.setStyleSheet(u"QComboBox{\n"
"	border:2px solid white;\n"
"	border-radius: 8px;\n"
"	padding:1px 18px 1px 3px;\n"
"	background-color:black;\n"
"	color:white;\n"
"	height: 35px;\n"
"	padding-left: 15px;\n"
"	font-weight:bold;\n"
"	selection-background-color:#2980B9;\n"
"}")

        self.verticalLayout_10.addWidget(self.comboBox_select_desc_account)


        self.horizontalLayout_5.addLayout(self.verticalLayout_10)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_select_value = QLabel(self.layoutWidget2)
        self.label_select_value.setObjectName(u"label_select_value")
        self.label_select_value.setMinimumSize(QSize(0, 17))
        self.label_select_value.setMaximumSize(QSize(16777215, 17))
        self.label_select_value.setFont(font4)
        self.label_select_value.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_7.addWidget(self.label_select_value)

        self.comboBox_select_value = QComboBox(self.layoutWidget2)
        self.comboBox_select_value.addItem("")
        self.comboBox_select_value.setObjectName(u"comboBox_select_value")
        self.comboBox_select_value.setMinimumSize(QSize(0, 35))
        self.comboBox_select_value.setMaximumSize(QSize(16777215, 35))
        self.comboBox_select_value.setStyleSheet(u"QComboBox{\n"
"	border:2px solid white;\n"
"	border-radius: 8px;\n"
"	padding:1px 18px 1px 3px;\n"
"	background-color:black;\n"
"	color:white;\n"
"	height: 35px;\n"
"	padding-left: 15px;\n"
"	font-weight:bold;\n"
"	selection-background-color:#2980B9;\n"
"}")

        self.verticalLayout_7.addWidget(self.comboBox_select_value)


        self.horizontalLayout_5.addLayout(self.verticalLayout_7)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.top_frame_widget_update_column_page = QWidget(self.central_widget_update_column_page)
        self.top_frame_widget_update_column_page.setObjectName(u"top_frame_widget_update_column_page")
        self.top_frame_widget_update_column_page.setGeometry(QRect(0, 0, 801, 61))
        self.top_frame_widget_update_column_page.setMinimumSize(QSize(0, 61))
        self.top_frame_widget_update_column_page.setMaximumSize(QSize(16777215, 61))
        self.top_frame_widget_update_column_page.setFont(font2)
        self.top_frame_widget_update_column_page.setStyleSheet(u"")
        self.layoutWidget_6 = QWidget(self.top_frame_widget_update_column_page)
        self.layoutWidget_6.setObjectName(u"layoutWidget_6")
        self.layoutWidget_6.setGeometry(QRect(0, 0, 801, 62))
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.title_page_update_column_page = QLabel(self.layoutWidget_6)
        self.title_page_update_column_page.setObjectName(u"title_page_update_column_page")
        self.title_page_update_column_page.setFont(font5)
        self.title_page_update_column_page.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.title_page_update_column_page.setMargin(10)

        self.horizontalLayout_6.addWidget(self.title_page_update_column_page)

        self.horizontalSpacer_update_column_page = QSpacerItem(348, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_update_column_page)

        self.file_name_label_update_column_page = QLabel(self.layoutWidget_6)
        self.file_name_label_update_column_page.setObjectName(u"file_name_label_update_column_page")
        self.file_name_label_update_column_page.setFont(font6)
        self.file_name_label_update_column_page.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.file_name_label_update_column_page.setMargin(20)

        self.horizontalLayout_6.addWidget(self.file_name_label_update_column_page)

        self.stackedWidget.addWidget(self.b_update_column_page)
        self.c_add_data_page = QWidget()
        self.c_add_data_page.setObjectName(u"c_add_data_page")
        self.c_add_data_page.setMaximumSize(QSize(801, 731))
        self.central_widget_add_data_page = QWidget(self.c_add_data_page)
        self.central_widget_add_data_page.setObjectName(u"central_widget_add_data_page")
        self.central_widget_add_data_page.setGeometry(QRect(0, 0, 801, 741))
        self.central_widget_add_data_page.setStyleSheet(u"")
        self.botton_frame_widget_add_data_page = QWidget(self.central_widget_add_data_page)
        self.botton_frame_widget_add_data_page.setObjectName(u"botton_frame_widget_add_data_page")
        self.botton_frame_widget_add_data_page.setGeometry(QRect(0, 660, 801, 70))
        self.botton_frame_widget_add_data_page.setMinimumSize(QSize(0, 70))
        self.botton_frame_widget_add_data_page.setMaximumSize(QSize(16777215, 0))
        self.botton_frame_widget_add_data_page.setFont(font2)
        self.botton_frame_widget_add_data_page.setStyleSheet(u"")
        self.layoutWidget_11 = QWidget(self.botton_frame_widget_add_data_page)
        self.layoutWidget_11.setObjectName(u"layoutWidget_11")
        self.layoutWidget_11.setGeometry(QRect(0, 0, 801, 71))
        self.hLayout_bottom_frame_add_data_page = QHBoxLayout(self.layoutWidget_11)
        self.hLayout_bottom_frame_add_data_page.setObjectName(u"hLayout_bottom_frame_add_data_page")
        self.hLayout_bottom_frame_add_data_page.setContentsMargins(0, 0, 10, 0)
        self.horizontalSpacer_6 = QSpacerItem(598, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hLayout_bottom_frame_add_data_page.addItem(self.horizontalSpacer_6)

        self.next_btn_add_data_page = QPushButton(self.layoutWidget_11)
        self.next_btn_add_data_page.setObjectName(u"next_btn_add_data_page")
        self.next_btn_add_data_page.setMinimumSize(QSize(150, 35))
        self.next_btn_add_data_page.setMaximumSize(QSize(150, 35))
        self.next_btn_add_data_page.setStyleSheet(u"QPushButton{\n"
"	background-color: #34D481;\n"
"	color:white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight:bold;\n"
"	font-size: 15px;\n"
"}")

        self.hLayout_bottom_frame_add_data_page.addWidget(self.next_btn_add_data_page)

        self.table_frame_widget_add_data_page = QWidget(self.central_widget_add_data_page)
        self.table_frame_widget_add_data_page.setObjectName(u"table_frame_widget_add_data_page")
        self.table_frame_widget_add_data_page.setGeometry(QRect(0, 220, 801, 431))
        self.table_frame_widget_add_data_page.setStyleSheet(u"")
        self.tableWidget_add_data_page = QTableWidget(self.table_frame_widget_add_data_page)
        if (self.tableWidget_add_data_page.columnCount() < 7):
            self.tableWidget_add_data_page.setColumnCount(7)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_add_data_page.setHorizontalHeaderItem(0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_add_data_page.setHorizontalHeaderItem(1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_add_data_page.setHorizontalHeaderItem(2, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_add_data_page.setHorizontalHeaderItem(3, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_add_data_page.setHorizontalHeaderItem(4, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_add_data_page.setHorizontalHeaderItem(5, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_add_data_page.setHorizontalHeaderItem(6, __qtablewidgetitem20)
        self.tableWidget_add_data_page.setObjectName(u"tableWidget_add_data_page")
        self.tableWidget_add_data_page.setGeometry(QRect(0, 0, 801, 431))
        self.tableWidget_add_data_page.horizontalHeader().setMinimumSectionSize(32)
        self.tableWidget_add_data_page.horizontalHeader().setDefaultSectionSize(110)
        self.buttons_widget_add_data_page = QWidget(self.central_widget_add_data_page)
        self.buttons_widget_add_data_page.setObjectName(u"buttons_widget_add_data_page")
        self.buttons_widget_add_data_page.setGeometry(QRect(0, 70, 801, 141))
        self.buttons_widget_add_data_page.setStyleSheet(u"")
        self.layoutWidget_3 = QWidget(self.buttons_widget_add_data_page)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(0, 0, 801, 143))
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(10, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 43))
        self.label_3.setMaximumSize(QSize(16777215, 43))
        self.label_3.setFont(font3)

        self.verticalLayout_5.addWidget(self.label_3)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(6)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 10, 10, 20)
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_select_period = QLabel(self.layoutWidget_3)
        self.label_select_period.setObjectName(u"label_select_period")
        self.label_select_period.setMinimumSize(QSize(187, 0))
        self.label_select_period.setMaximumSize(QSize(187, 17))
        self.label_select_period.setFont(font4)
        self.label_select_period.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_8.addWidget(self.label_select_period)

        self.comboBox_select_period = QComboBox(self.layoutWidget_3)
        self.comboBox_select_period.addItem("")
        self.comboBox_select_period.addItem("")
        self.comboBox_select_period.addItem("")
        self.comboBox_select_period.setObjectName(u"comboBox_select_period")
        self.comboBox_select_period.setMinimumSize(QSize(187, 35))
        self.comboBox_select_period.setMaximumSize(QSize(187, 35))
        self.comboBox_select_period.setStyleSheet(u"QComboBox{\n"
"	border:2px solid white;\n"
"	border-radius: 8px;\n"
"	padding:1px 18px 1px 3px;\n"
"	background-color:black;\n"
"	color:white;\n"
"	height: 35px;\n"
"	padding-left: 15px;\n"
"	font-weight:bold;\n"
"	selection-background-color:#2980B9;\n"
"}")

        self.verticalLayout_8.addWidget(self.comboBox_select_period)


        self.horizontalLayout_9.addLayout(self.verticalLayout_8)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_select_month = QLabel(self.layoutWidget_3)
        self.label_select_month.setObjectName(u"label_select_month")
        self.label_select_month.setMaximumSize(QSize(16777215, 17))
        self.label_select_month.setFont(font4)
        self.label_select_month.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_13.addWidget(self.label_select_month)

        self.comboBox_select_month = QComboBox(self.layoutWidget_3)
        self.comboBox_select_month.addItem("")
        self.comboBox_select_month.addItem("")
        self.comboBox_select_month.addItem("")
        self.comboBox_select_month.addItem("")
        self.comboBox_select_month.addItem("")
        self.comboBox_select_month.setObjectName(u"comboBox_select_month")
        self.comboBox_select_month.setMinimumSize(QSize(0, 35))
        self.comboBox_select_month.setMaximumSize(QSize(187, 35))
        self.comboBox_select_month.setStyleSheet(u"QComboBox{\n"
"	border:2px solid white;\n"
"	border-radius: 8px;\n"
"	padding:1px 18px 1px 3px;\n"
"	background-color:black;\n"
"	color:white;\n"
"	height: 35px;\n"
"	padding-left: 15px;\n"
"	font-weight:bold;\n"
"	selection-background-color:#2980B9;\n"
"}")

        self.verticalLayout_13.addWidget(self.comboBox_select_month)


        self.horizontalLayout_9.addLayout(self.verticalLayout_13)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_year = QLabel(self.layoutWidget_3)
        self.label_year.setObjectName(u"label_year")
        self.label_year.setMinimumSize(QSize(0, 17))
        self.label_year.setMaximumSize(QSize(16777215, 17))
        self.label_year.setFont(font4)
        self.label_year.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_15.addWidget(self.label_year)

        self.lineEdit_year = QLineEdit(self.layoutWidget_3)
        self.lineEdit_year.setObjectName(u"lineEdit_year")
        self.lineEdit_year.setMinimumSize(QSize(150, 35))
        self.lineEdit_year.setMaximumSize(QSize(150, 35))

        self.verticalLayout_15.addWidget(self.lineEdit_year)


        self.horizontalLayout_9.addLayout(self.verticalLayout_15)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_3)

        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(-1, -1, -1, 2)
        self.label_add_period = QLabel(self.layoutWidget_3)
        self.label_add_period.setObjectName(u"label_add_period")
        self.label_add_period.setMinimumSize(QSize(0, 17))
        self.label_add_period.setMaximumSize(QSize(16777215, 17))
        self.label_add_period.setFont(font4)

        self.verticalLayout_21.addWidget(self.label_add_period)

        self.add_period_btn = QPushButton(self.layoutWidget_3)
        self.add_period_btn.setObjectName(u"add_period_btn")
        self.add_period_btn.setMinimumSize(QSize(150, 36))
        self.add_period_btn.setMaximumSize(QSize(150, 36))
        self.add_period_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: #34D481;\n"
"	color:white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight:bold;\n"
"	font-size: 15px;\n"
"}")

        self.verticalLayout_21.addWidget(self.add_period_btn)


        self.horizontalLayout_9.addLayout(self.verticalLayout_21)


        self.verticalLayout_5.addLayout(self.horizontalLayout_9)

        self.top_frame_widget_add_data_page = QWidget(self.central_widget_add_data_page)
        self.top_frame_widget_add_data_page.setObjectName(u"top_frame_widget_add_data_page")
        self.top_frame_widget_add_data_page.setGeometry(QRect(0, 0, 801, 61))
        self.top_frame_widget_add_data_page.setMinimumSize(QSize(0, 61))
        self.top_frame_widget_add_data_page.setMaximumSize(QSize(16777215, 61))
        self.top_frame_widget_add_data_page.setFont(font2)
        self.top_frame_widget_add_data_page.setStyleSheet(u"")
        self.layoutWidget_13 = QWidget(self.top_frame_widget_add_data_page)
        self.layoutWidget_13.setObjectName(u"layoutWidget_13")
        self.layoutWidget_13.setGeometry(QRect(0, 0, 801, 62))
        self.horizontalLayout_10 = QHBoxLayout(self.layoutWidget_13)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.title_page_add_data_page = QLabel(self.layoutWidget_13)
        self.title_page_add_data_page.setObjectName(u"title_page_add_data_page")
        self.title_page_add_data_page.setFont(font5)
        self.title_page_add_data_page.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.title_page_add_data_page.setMargin(10)

        self.horizontalLayout_10.addWidget(self.title_page_add_data_page)

        self.horizontalSpacer_add_data_page = QSpacerItem(348, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_add_data_page)

        self.file_name_label_add_data_page = QLabel(self.layoutWidget_13)
        self.file_name_label_add_data_page.setObjectName(u"file_name_label_add_data_page")
        self.file_name_label_add_data_page.setFont(font6)
        self.file_name_label_add_data_page.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.file_name_label_add_data_page.setMargin(20)

        self.horizontalLayout_10.addWidget(self.file_name_label_add_data_page)

        self.stackedWidget.addWidget(self.c_add_data_page)
        self.d_apdate_accounts = QWidget()
        self.d_apdate_accounts.setObjectName(u"d_apdate_accounts")
        self.d_apdate_accounts.setMaximumSize(QSize(801, 731))
        self.central_widget_update_accounts_page = QWidget(self.d_apdate_accounts)
        self.central_widget_update_accounts_page.setObjectName(u"central_widget_update_accounts_page")
        self.central_widget_update_accounts_page.setGeometry(QRect(0, 0, 801, 741))
        self.central_widget_update_accounts_page.setStyleSheet(u"")
        self.botton_frame_widget_update_accounts_page = QWidget(self.central_widget_update_accounts_page)
        self.botton_frame_widget_update_accounts_page.setObjectName(u"botton_frame_widget_update_accounts_page")
        self.botton_frame_widget_update_accounts_page.setGeometry(QRect(0, 660, 801, 70))
        self.botton_frame_widget_update_accounts_page.setMinimumSize(QSize(0, 70))
        self.botton_frame_widget_update_accounts_page.setMaximumSize(QSize(16777215, 0))
        self.botton_frame_widget_update_accounts_page.setFont(font2)
        self.botton_frame_widget_update_accounts_page.setStyleSheet(u"")
        self.layoutWidget_17 = QWidget(self.botton_frame_widget_update_accounts_page)
        self.layoutWidget_17.setObjectName(u"layoutWidget_17")
        self.layoutWidget_17.setGeometry(QRect(0, 0, 801, 71))
        self.hLayout_bottom_frame_update_accounts_page = QHBoxLayout(self.layoutWidget_17)
        self.hLayout_bottom_frame_update_accounts_page.setObjectName(u"hLayout_bottom_frame_update_accounts_page")
        self.hLayout_bottom_frame_update_accounts_page.setContentsMargins(0, 0, 10, 0)
        self.horizontalSpacer_10 = QSpacerItem(598, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hLayout_bottom_frame_update_accounts_page.addItem(self.horizontalSpacer_10)

        self.next_btn_update_accounts_page = QPushButton(self.layoutWidget_17)
        self.next_btn_update_accounts_page.setObjectName(u"next_btn_update_accounts_page")
        self.next_btn_update_accounts_page.setMinimumSize(QSize(150, 35))
        self.next_btn_update_accounts_page.setMaximumSize(QSize(150, 35))
        self.next_btn_update_accounts_page.setStyleSheet(u"QPushButton{\n"
"	background-color: #34D481;\n"
"	color:white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight:bold;\n"
"	font-size: 15px;\n"
"}")

        self.hLayout_bottom_frame_update_accounts_page.addWidget(self.next_btn_update_accounts_page)

        self.table_frame_widget_update_accounts_page = QWidget(self.central_widget_update_accounts_page)
        self.table_frame_widget_update_accounts_page.setObjectName(u"table_frame_widget_update_accounts_page")
        self.table_frame_widget_update_accounts_page.setGeometry(QRect(0, 220, 801, 431))
        self.table_frame_widget_update_accounts_page.setStyleSheet(u"")
        self.tableWidget_update_accounts_page = QTableWidget(self.table_frame_widget_update_accounts_page)
        if (self.tableWidget_update_accounts_page.columnCount() < 7):
            self.tableWidget_update_accounts_page.setColumnCount(7)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_update_accounts_page.setHorizontalHeaderItem(0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_update_accounts_page.setHorizontalHeaderItem(1, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget_update_accounts_page.setHorizontalHeaderItem(2, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget_update_accounts_page.setHorizontalHeaderItem(3, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget_update_accounts_page.setHorizontalHeaderItem(4, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget_update_accounts_page.setHorizontalHeaderItem(5, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget_update_accounts_page.setHorizontalHeaderItem(6, __qtablewidgetitem27)
        self.tableWidget_update_accounts_page.setObjectName(u"tableWidget_update_accounts_page")
        self.tableWidget_update_accounts_page.setGeometry(QRect(0, 0, 801, 431))
        self.tableWidget_update_accounts_page.horizontalHeader().setMinimumSectionSize(32)
        self.tableWidget_update_accounts_page.horizontalHeader().setDefaultSectionSize(110)
        self.buttons_widget_update_accounts_page = QWidget(self.central_widget_update_accounts_page)
        self.buttons_widget_update_accounts_page.setObjectName(u"buttons_widget_update_accounts_page")
        self.buttons_widget_update_accounts_page.setGeometry(QRect(0, 70, 801, 141))
        self.buttons_widget_update_accounts_page.setStyleSheet(u"")
        self.layoutWidget_18 = QWidget(self.buttons_widget_update_accounts_page)
        self.layoutWidget_18.setObjectName(u"layoutWidget_18")
        self.layoutWidget_18.setGeometry(QRect(0, 1, 801, 141))
        self.verticalLayout_17 = QVBoxLayout(self.layoutWidget_18)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(10, 0, 0, 0)
        self.label_update_accounts_page = QLabel(self.layoutWidget_18)
        self.label_update_accounts_page.setObjectName(u"label_update_accounts_page")
        self.label_update_accounts_page.setFont(font3)

        self.verticalLayout_17.addWidget(self.label_update_accounts_page)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(10)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 10, 10, 20)
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_names_company = QLabel(self.layoutWidget_18)
        self.label_names_company.setObjectName(u"label_names_company")
        self.label_names_company.setFont(font4)
        self.label_names_company.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_18.addWidget(self.label_names_company)

        self.lineEdit_names_company = QLineEdit(self.layoutWidget_18)
        self.lineEdit_names_company.setObjectName(u"lineEdit_names_company")
        self.lineEdit_names_company.setMinimumSize(QSize(250, 0))
        self.lineEdit_names_company.setMaximumSize(QSize(250, 16777215))

        self.verticalLayout_18.addWidget(self.lineEdit_names_company)


        self.horizontalLayout_13.addLayout(self.verticalLayout_18)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_cnpj = QLabel(self.layoutWidget_18)
        self.label_cnpj.setObjectName(u"label_cnpj")
        self.label_cnpj.setFont(font4)
        self.label_cnpj.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_19.addWidget(self.label_cnpj)

        self.lineEdit_cnpj = QLineEdit(self.layoutWidget_18)
        self.lineEdit_cnpj.setObjectName(u"lineEdit_cnpj")
        self.lineEdit_cnpj.setMinimumSize(QSize(250, 0))
        self.lineEdit_cnpj.setMaximumSize(QSize(250, 16777215))

        self.verticalLayout_19.addWidget(self.lineEdit_cnpj)


        self.horizontalLayout_13.addLayout(self.verticalLayout_19)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_4)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_add_name_cnpj = QLabel(self.layoutWidget_18)
        self.label_add_name_cnpj.setObjectName(u"label_add_name_cnpj")
        self.label_add_name_cnpj.setMinimumSize(QSize(150, 17))
        self.label_add_name_cnpj.setMaximumSize(QSize(150, 17))
        self.label_add_name_cnpj.setFont(font4)
        self.label_add_name_cnpj.setIndent(-1)

        self.verticalLayout_20.addWidget(self.label_add_name_cnpj)

        self.add_name_cnpj_btn = QPushButton(self.layoutWidget_18)
        self.add_name_cnpj_btn.setObjectName(u"add_name_cnpj_btn")
        self.add_name_cnpj_btn.setMinimumSize(QSize(150, 36))
        self.add_name_cnpj_btn.setMaximumSize(QSize(16777215, 36))
        self.add_name_cnpj_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: #34D481;\n"
"	color:white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight:bold;\n"
"	font-size: 15px;\n"
"}")

        self.verticalLayout_20.addWidget(self.add_name_cnpj_btn)


        self.horizontalLayout_13.addLayout(self.verticalLayout_20)


        self.verticalLayout_17.addLayout(self.horizontalLayout_13)

        self.top_frame_widget_update_accounts_page = QWidget(self.central_widget_update_accounts_page)
        self.top_frame_widget_update_accounts_page.setObjectName(u"top_frame_widget_update_accounts_page")
        self.top_frame_widget_update_accounts_page.setGeometry(QRect(0, 0, 801, 61))
        self.top_frame_widget_update_accounts_page.setMinimumSize(QSize(0, 61))
        self.top_frame_widget_update_accounts_page.setMaximumSize(QSize(16777215, 61))
        self.top_frame_widget_update_accounts_page.setFont(font2)
        self.top_frame_widget_update_accounts_page.setStyleSheet(u"")
        self.layoutWidget_19 = QWidget(self.top_frame_widget_update_accounts_page)
        self.layoutWidget_19.setObjectName(u"layoutWidget_19")
        self.layoutWidget_19.setGeometry(QRect(0, 0, 801, 62))
        self.horizontalLayout_14 = QHBoxLayout(self.layoutWidget_19)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.title_page_update_accounts_page = QLabel(self.layoutWidget_19)
        self.title_page_update_accounts_page.setObjectName(u"title_page_update_accounts_page")
        self.title_page_update_accounts_page.setFont(font5)
        self.title_page_update_accounts_page.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.title_page_update_accounts_page.setMargin(10)

        self.horizontalLayout_14.addWidget(self.title_page_update_accounts_page)

        self.horizontalSpacer_update_accounts_page = QSpacerItem(348, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_update_accounts_page)

        self.file_name_label_update_accounts_page = QLabel(self.layoutWidget_19)
        self.file_name_label_update_accounts_page.setObjectName(u"file_name_label_update_accounts_page")
        self.file_name_label_update_accounts_page.setFont(font6)
        self.file_name_label_update_accounts_page.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.file_name_label_update_accounts_page.setMargin(20)

        self.horizontalLayout_14.addWidget(self.file_name_label_update_accounts_page)

        self.stackedWidget.addWidget(self.d_apdate_accounts)
        self.e_exportation_page = QWidget()
        self.e_exportation_page.setObjectName(u"e_exportation_page")
        self.stackedWidget.addWidget(self.e_exportation_page)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.exit_btn.toggled.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Integra\u00e7\u00e3o de Dados Cont\u00e1beis", None))
        self.label_5.setText("")
        self.load_data_page_btn.setText(QCoreApplication.translate("MainWindow", u"Carregar Dados", None))
        self.upddate_column_page_btn.setText(QCoreApplication.translate("MainWindow", u"Alterar Colunas", None))
        self.add_data_page_btn.setText(QCoreApplication.translate("MainWindow", u"Inserir Per\u00edodo", None))
        self.upddate_accounts_page_btn.setText(QCoreApplication.translate("MainWindow", u"Alterar Contas Cont\u00e1beis", None))
        self.exportation_page_btn.setText(QCoreApplication.translate("MainWindow", u"Exportar Dados", None))
        self.exit_btn.setText(QCoreApplication.translate("MainWindow", u"Sair", None))
        self.next_btn_load_data_page.setText(QCoreApplication.translate("MainWindow", u"Avan\u00e7ar", None))
        ___qtablewidgetitem = self.tableWidget_load_data_page.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Column_1", None));
        ___qtablewidgetitem1 = self.tableWidget_load_data_page.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Column_2", None));
        ___qtablewidgetitem2 = self.tableWidget_load_data_page.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Column_3", None));
        ___qtablewidgetitem3 = self.tableWidget_load_data_page.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Column_4", None));
        ___qtablewidgetitem4 = self.tableWidget_load_data_page.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Column_5", None));
        ___qtablewidgetitem5 = self.tableWidget_load_data_page.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Column_6", None));
        ___qtablewidgetitem6 = self.tableWidget_load_data_page.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Column_7", None));
        self.label.setText(QCoreApplication.translate("MainWindow", u"Selecione o delimitador dos dados e clique em carregar", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Delimitador", None))
        self.comboBox_file_delimiter.setItemText(0, QCoreApplication.translate("MainWindow", u"V\u00edrgula", None))
        self.comboBox_file_delimiter.setItemText(1, QCoreApplication.translate("MainWindow", u"Ponto e V\u00edrgula", None))

        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Arquivo", None))
        self.upload_btn.setText(QCoreApplication.translate("MainWindow", u"Carregar", None))
        self.title_page_load_data_page.setText(QCoreApplication.translate("MainWindow", u"Carregar Dados", None))
        self.label_load_data_page.setText(QCoreApplication.translate("MainWindow", u"arquivo.csv", None))
        self.next_btn_update_column_page.setText(QCoreApplication.translate("MainWindow", u"Avan\u00e7ar", None))
        ___qtablewidgetitem7 = self.tableWidget_update_column_page.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Column_1", None));
        ___qtablewidgetitem8 = self.tableWidget_update_column_page.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Column_2", None));
        ___qtablewidgetitem9 = self.tableWidget_update_column_page.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Column_3", None));
        ___qtablewidgetitem10 = self.tableWidget_update_column_page.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Column_4", None));
        ___qtablewidgetitem11 = self.tableWidget_update_column_page.horizontalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Column_5", None));
        ___qtablewidgetitem12 = self.tableWidget_update_column_page.horizontalHeaderItem(5)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Column_6", None));
        ___qtablewidgetitem13 = self.tableWidget_update_column_page.horizontalHeaderItem(6)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Column_7", None));
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Associe as colunas abaixo com as colunas dos seus dados", None))
        self.label_select_account.setText(QCoreApplication.translate("MainWindow", u"Conta", None))
        self.comboBox_select_account.setItemText(0, QCoreApplication.translate("MainWindow", u"SELECIONE  A COLUNA", None))

        self.label_select_desc_account.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o da Conta", None))
        self.comboBox_select_desc_account.setItemText(0, QCoreApplication.translate("MainWindow", u"SELECIONE A COLUNA", None))

        self.label_select_value.setText(QCoreApplication.translate("MainWindow", u" Valor", None))
        self.comboBox_select_value.setItemText(0, QCoreApplication.translate("MainWindow", u"SELECIONE A COLUNA", None))

        self.title_page_update_column_page.setText(QCoreApplication.translate("MainWindow", u"Alterar Colunas", None))
        self.file_name_label_update_column_page.setText(QCoreApplication.translate("MainWindow", u"arquivo.csv", None))
        self.next_btn_add_data_page.setText(QCoreApplication.translate("MainWindow", u"Avan\u00e7ar", None))
        ___qtablewidgetitem14 = self.tableWidget_add_data_page.horizontalHeaderItem(0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Column_1", None));
        ___qtablewidgetitem15 = self.tableWidget_add_data_page.horizontalHeaderItem(1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Column_2", None));
        ___qtablewidgetitem16 = self.tableWidget_add_data_page.horizontalHeaderItem(2)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Column_3", None));
        ___qtablewidgetitem17 = self.tableWidget_add_data_page.horizontalHeaderItem(3)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Column_4", None));
        ___qtablewidgetitem18 = self.tableWidget_add_data_page.horizontalHeaderItem(4)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Column_5", None));
        ___qtablewidgetitem19 = self.tableWidget_add_data_page.horizontalHeaderItem(5)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Column_6", None));
        ___qtablewidgetitem20 = self.tableWidget_add_data_page.horizontalHeaderItem(6)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Column_7", None));
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Entre com o per\u00edodo dos dados, m\u00eas e ano de refer\u00eancia", None))
        self.label_select_period.setText(QCoreApplication.translate("MainWindow", u"Per\u00edodo dos dados", None))
        self.comboBox_select_period.setItemText(0, QCoreApplication.translate("MainWindow", u"SELECIONE  O PERIODO", None))
        self.comboBox_select_period.setItemText(1, QCoreApplication.translate("MainWindow", u"Anual", None))
        self.comboBox_select_period.setItemText(2, QCoreApplication.translate("MainWindow", u"Trimestral", None))

        self.label_select_month.setText(QCoreApplication.translate("MainWindow", u"M\u00eas de Refer\u00eancia", None))
        self.comboBox_select_month.setItemText(0, QCoreApplication.translate("MainWindow", u"SELECIONE O M\u00caS", None))
        self.comboBox_select_month.setItemText(1, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox_select_month.setItemText(2, QCoreApplication.translate("MainWindow", u"6", None))
        self.comboBox_select_month.setItemText(3, QCoreApplication.translate("MainWindow", u"9", None))
        self.comboBox_select_month.setItemText(4, QCoreApplication.translate("MainWindow", u"12", None))

        self.label_year.setText(QCoreApplication.translate("MainWindow", u"Ano", None))
        self.lineEdit_year.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite o ano", None))
        self.label_add_period.setText("")
        self.add_period_btn.setText(QCoreApplication.translate("MainWindow", u"Inserir ", None))
        self.title_page_add_data_page.setText(QCoreApplication.translate("MainWindow", u"Inserir Per\u00edodo", None))
        self.file_name_label_add_data_page.setText(QCoreApplication.translate("MainWindow", u"arquivo.csv", None))
        self.next_btn_update_accounts_page.setText(QCoreApplication.translate("MainWindow", u"Avan\u00e7ar", None))
        ___qtablewidgetitem21 = self.tableWidget_update_accounts_page.horizontalHeaderItem(0)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Column_1", None));
        ___qtablewidgetitem22 = self.tableWidget_update_accounts_page.horizontalHeaderItem(1)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Column_2", None));
        ___qtablewidgetitem23 = self.tableWidget_update_accounts_page.horizontalHeaderItem(2)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Column_3", None));
        ___qtablewidgetitem24 = self.tableWidget_update_accounts_page.horizontalHeaderItem(3)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Column_4", None));
        ___qtablewidgetitem25 = self.tableWidget_update_accounts_page.horizontalHeaderItem(4)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Column_5", None));
        ___qtablewidgetitem26 = self.tableWidget_update_accounts_page.horizontalHeaderItem(5)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Column_6", None));
        ___qtablewidgetitem27 = self.tableWidget_update_accounts_page.horizontalHeaderItem(6)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Column_7", None));
        self.label_update_accounts_page.setText(QCoreApplication.translate("MainWindow", u"Digite o nome e o cnpj da empresa. Para editar as contas, clique no \u00edcone em azul.", None))
        self.label_names_company.setText(QCoreApplication.translate("MainWindow", u"Nome da Empresa", None))
        self.label_cnpj.setText(QCoreApplication.translate("MainWindow", u"CNPJ", None))
        self.label_add_name_cnpj.setText("")
        self.add_name_cnpj_btn.setText(QCoreApplication.translate("MainWindow", u"Inserir ", None))
        self.title_page_update_accounts_page.setText(QCoreApplication.translate("MainWindow", u"Alterar Contas Cont\u00e1beis", None))
        self.file_name_label_update_accounts_page.setText(QCoreApplication.translate("MainWindow", u"arquivo.csv", None))
    # retranslateUi

