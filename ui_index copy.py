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
        MainWindow.resize(999, 769)
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
        self.left_frame_verticalLayout = QVBoxLayout(self.layoutWidget)
        self.left_frame_verticalLayout.setObjectName(u"left_frame_verticalLayout")
        self.left_frame_verticalLayout.setContentsMargins(0, 20, 0, 25)
        self.horizontalLayout_icon = QHBoxLayout()
        self.horizontalLayout_icon.setObjectName(u"horizontalLayout_icon")
        self.horizontalSpacer_left_icon_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_icon.addItem(self.horizontalSpacer_left_icon_2)

        self.icon_left_frame = QLabel(self.layoutWidget)
        self.icon_left_frame.setObjectName(u"icon_left_frame")
        self.icon_left_frame.setMaximumSize(QSize(50, 50))
        self.icon_left_frame.setPixmap(QPixmap(u":/newPrefix/icons/financessmall2.png"))

        self.horizontalLayout_icon.addWidget(self.icon_left_frame)

        self.horizontalSpacer_left_icon = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_icon.addItem(self.horizontalSpacer_left_icon)


        self.left_frame_verticalLayout.addLayout(self.horizontalLayout_icon)

        self.vLayout_btns_page = QVBoxLayout()
        self.vLayout_btns_page.setSpacing(20)
        self.vLayout_btns_page.setObjectName(u"vLayout_btns_page")
        self.vLayout_btns_page.setContentsMargins(-1, 20, -1, -1)
        self.settings_page_btn = QPushButton(self.layoutWidget)
        self.settings_page_btn.setObjectName(u"settings_page_btn")
        self.settings_page_btn.setMinimumSize(QSize(0, 30))
        self.settings_page_btn.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.settings_page_btn.setFont(font)
        self.settings_page_btn.setStyleSheet(u"QPushButton:hover {\n"
"	color:#12B298;\n"
"}\n"
"QPushButton:checked {\n"
"	color:#12B298;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.settings_page_btn.setCheckable(True)
        self.settings_page_btn.setAutoExclusive(True)

        self.vLayout_btns_page.addWidget(self.settings_page_btn)

        self.load_file_page_btn = QPushButton(self.layoutWidget)
        self.load_file_page_btn.setObjectName(u"load_file_page_btn")
        self.load_file_page_btn.setMinimumSize(QSize(0, 30))
        self.load_file_page_btn.setMaximumSize(QSize(16777215, 30))
        self.load_file_page_btn.setFont(font)
        self.load_file_page_btn.setStyleSheet(u"QPushButton:hover {\n"
"	color:#12B298;\n"
"}\n"
"QPushButton:checked {\n"
"	color:#12B298;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.load_file_page_btn.setCheckable(True)
        self.load_file_page_btn.setAutoExclusive(True)

        self.vLayout_btns_page.addWidget(self.load_file_page_btn)

        self.update_data_page_btn = QPushButton(self.layoutWidget)
        self.update_data_page_btn.setObjectName(u"update_data_page_btn")
        self.update_data_page_btn.setMinimumSize(QSize(0, 30))
        self.update_data_page_btn.setMaximumSize(QSize(16777215, 30))
        self.update_data_page_btn.setFont(font)
        self.update_data_page_btn.setStyleSheet(u"QPushButton:hover {\n"
"	color:#12B298;\n"
"}\n"
"QPushButton:checked {\n"
"	color:#12B298;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.update_data_page_btn.setCheckable(True)
        self.update_data_page_btn.setAutoExclusive(True)

        self.vLayout_btns_page.addWidget(self.update_data_page_btn)

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


        self.left_frame_verticalLayout.addLayout(self.vLayout_btns_page)

        self.verticalSpacer_left_frame = QSpacerItem(20, 278, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.left_frame_verticalLayout.addItem(self.verticalSpacer_left_frame)

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

        self.left_frame_verticalLayout.addWidget(self.exit_btn)

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
        self.a_settings_page = QWidget()
        self.a_settings_page.setObjectName(u"a_settings_page")
        self.a_settings_page.setMaximumSize(QSize(801, 731))
        self.a_settings_page.setStyleSheet(u"")
        self.settings_page_widget = QWidget(self.a_settings_page)
        self.settings_page_widget.setObjectName(u"settings_page_widget")
        self.settings_page_widget.setGeometry(QRect(0, 0, 801, 741))
        self.settings_page_widget.setStyleSheet(u"")
        self.settings_page_botton_frame = QWidget(self.settings_page_widget)
        self.settings_page_botton_frame.setObjectName(u"settings_page_botton_frame")
        self.settings_page_botton_frame.setGeometry(QRect(0, 670, 801, 70))
        self.settings_page_botton_frame.setMinimumSize(QSize(0, 70))
        self.settings_page_botton_frame.setMaximumSize(QSize(16777215, 0))
        font2 = QFont()
        font2.setPointSize(13)
        self.settings_page_botton_frame.setFont(font2)
        self.settings_page_botton_frame.setStyleSheet(u"")
        self.layoutWidget_7 = QWidget(self.settings_page_botton_frame)
        self.layoutWidget_7.setObjectName(u"layoutWidget_7")
        self.layoutWidget_7.setGeometry(QRect(0, 0, 801, 71))
        self.settings_botton_frame_hLayout = QHBoxLayout(self.layoutWidget_7)
        self.settings_botton_frame_hLayout.setObjectName(u"settings_botton_frame_hLayout")
        self.settings_botton_frame_hLayout.setContentsMargins(0, 0, 10, 0)
        self.settings_horizontal_Spacer = QSpacerItem(598, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.settings_botton_frame_hLayout.addItem(self.settings_horizontal_Spacer)

        self.save_btn_load_data_page = QPushButton(self.layoutWidget_7)
        self.save_btn_load_data_page.setObjectName(u"save_btn_load_data_page")
        self.save_btn_load_data_page.setMinimumSize(QSize(150, 35))
        self.save_btn_load_data_page.setMaximumSize(QSize(150, 35))
        self.save_btn_load_data_page.setStyleSheet(u"QPushButton{\n"
"	background-color: #34D481;\n"
"	color:white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight:bold;\n"
"	font-size: 15px;\n"
"}")

        self.settings_botton_frame_hLayout.addWidget(self.save_btn_load_data_page)

        self.settings_page_file_widget = QWidget(self.settings_page_widget)
        self.settings_page_file_widget.setObjectName(u"settings_page_file_widget")
        self.settings_page_file_widget.setGeometry(QRect(0, 70, 801, 131))
        self.settings_page_file_widget.setStyleSheet(u"")
        self.widget = QWidget(self.settings_page_file_widget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 1, 801, 131))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 0, 0, 0)
        self.label_info_settings = QLabel(self.widget)
        self.label_info_settings.setObjectName(u"label_info_settings")
        font3 = QFont()
        font3.setPointSize(10)
        self.label_info_settings.setFont(font3)

        self.verticalLayout.addWidget(self.label_info_settings)

        self.file_info_label = QLabel(self.widget)
        self.file_info_label.setObjectName(u"file_info_label")
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(11)
        self.file_info_label.setFont(font4)

        self.verticalLayout.addWidget(self.file_info_label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, -1, -1, -1)
        self.type_file_verticalLayout = QVBoxLayout()
        self.type_file_verticalLayout.setObjectName(u"type_file_verticalLayout")
        self.type_file_label = QLabel(self.widget)
        self.type_file_label.setObjectName(u"type_file_label")
        self.type_file_label.setMinimumSize(QSize(187, 17))
        self.type_file_label.setMaximumSize(QSize(187, 17))
        self.type_file_label.setFont(font4)
        self.type_file_label.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.type_file_verticalLayout.addWidget(self.type_file_label)

        self.type_file_comboBox = QComboBox(self.widget)
        self.type_file_comboBox.addItem("")
        self.type_file_comboBox.setObjectName(u"type_file_comboBox")
        self.type_file_comboBox.setMinimumSize(QSize(187, 35))
        self.type_file_comboBox.setMaximumSize(QSize(187, 35))
        self.type_file_comboBox.setStyleSheet(u"QComboBox{\n"
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

        self.type_file_verticalLayout.addWidget(self.type_file_comboBox)


        self.horizontalLayout.addLayout(self.type_file_verticalLayout)

        self.demiliter_verticalLayout = QVBoxLayout()
        self.demiliter_verticalLayout.setObjectName(u"demiliter_verticalLayout")
        self.delimiter_info_label = QLabel(self.widget)
        self.delimiter_info_label.setObjectName(u"delimiter_info_label")
        self.delimiter_info_label.setMinimumSize(QSize(187, 17))
        self.delimiter_info_label.setMaximumSize(QSize(187, 17))
        self.delimiter_info_label.setFont(font4)
        self.delimiter_info_label.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.demiliter_verticalLayout.addWidget(self.delimiter_info_label)

        self.delimiter_comboBox_file = QComboBox(self.widget)
        self.delimiter_comboBox_file.addItem("")
        self.delimiter_comboBox_file.addItem("")
        self.delimiter_comboBox_file.setObjectName(u"delimiter_comboBox_file")
        self.delimiter_comboBox_file.setMinimumSize(QSize(187, 35))
        self.delimiter_comboBox_file.setMaximumSize(QSize(187, 35))
        self.delimiter_comboBox_file.setStyleSheet(u"QComboBox{\n"
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

        self.demiliter_verticalLayout.addWidget(self.delimiter_comboBox_file)


        self.horizontalLayout.addLayout(self.demiliter_verticalLayout)

        self.encoding_verticalLayout = QVBoxLayout()
        self.encoding_verticalLayout.setObjectName(u"encoding_verticalLayout")
        self.encoding_label = QLabel(self.widget)
        self.encoding_label.setObjectName(u"encoding_label")
        self.encoding_label.setMinimumSize(QSize(187, 17))
        self.encoding_label.setMaximumSize(QSize(187, 17))
        self.encoding_label.setFont(font4)
        self.encoding_label.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.encoding_verticalLayout.addWidget(self.encoding_label)

        self.encoding_comboBox_file = QComboBox(self.widget)
        self.encoding_comboBox_file.addItem("")
        self.encoding_comboBox_file.addItem("")
        self.encoding_comboBox_file.setObjectName(u"encoding_comboBox_file")
        self.encoding_comboBox_file.setMinimumSize(QSize(187, 35))
        self.encoding_comboBox_file.setMaximumSize(QSize(187, 35))
        self.encoding_comboBox_file.setStyleSheet(u"QComboBox{\n"
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

        self.encoding_verticalLayout.addWidget(self.encoding_comboBox_file)


        self.horizontalLayout.addLayout(self.encoding_verticalLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.top_frame_widget_load_data_page = QWidget(self.settings_page_widget)
        self.top_frame_widget_load_data_page.setObjectName(u"top_frame_widget_load_data_page")
        self.top_frame_widget_load_data_page.setGeometry(QRect(0, 0, 801, 61))
        self.top_frame_widget_load_data_page.setMinimumSize(QSize(0, 61))
        self.top_frame_widget_load_data_page.setMaximumSize(QSize(16777215, 61))
        self.top_frame_widget_load_data_page.setFont(font2)
        self.top_frame_widget_load_data_page.setStyleSheet(u"")
        self.layoutWidget_9 = QWidget(self.top_frame_widget_load_data_page)
        self.layoutWidget_9.setObjectName(u"layoutWidget_9")
        self.layoutWidget_9.setGeometry(QRect(0, 0, 801, 62))
        self.settings_horizontalLayout = QHBoxLayout(self.layoutWidget_9)
        self.settings_horizontalLayout.setObjectName(u"settings_horizontalLayout")
        self.settings_horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.settings_page_title = QLabel(self.layoutWidget_9)
        self.settings_page_title.setObjectName(u"settings_page_title")
        font5 = QFont()
        font5.setFamilies([u"Arial Black"])
        font5.setPointSize(20)
        font5.setBold(True)
        self.settings_page_title.setFont(font5)
        self.settings_page_title.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.settings_page_title.setMargin(10)

        self.settings_horizontalLayout.addWidget(self.settings_page_title)

        self.settings_horizontalSpacer = QSpacerItem(348, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.settings_horizontalLayout.addItem(self.settings_horizontalSpacer)

        self.settings_page_period_widget = QWidget(self.settings_page_widget)
        self.settings_page_period_widget.setObjectName(u"settings_page_period_widget")
        self.settings_page_period_widget.setGeometry(QRect(0, 210, 801, 111))
        self.settings_page_period_widget.setStyleSheet(u"")
        self.widget1 = QWidget(self.settings_page_period_widget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(0, 0, 801, 111))
        self.info_periodo_verticalLayout = QVBoxLayout(self.widget1)
        self.info_periodo_verticalLayout.setObjectName(u"info_periodo_verticalLayout")
        self.info_periodo_verticalLayout.setContentsMargins(5, 0, 0, 0)
        self.period_info_label = QLabel(self.widget1)
        self.period_info_label.setObjectName(u"period_info_label")
        self.period_info_label.setFont(font4)

        self.info_periodo_verticalLayout.addWidget(self.period_info_label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, -1, -1, -1)
        self.period_verticalLayout = QVBoxLayout()
        self.period_verticalLayout.setObjectName(u"period_verticalLayout")
        self.period_label = QLabel(self.widget1)
        self.period_label.setObjectName(u"period_label")
        self.period_label.setMinimumSize(QSize(187, 17))
        self.period_label.setMaximumSize(QSize(187, 17))
        self.period_label.setFont(font4)
        self.period_label.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.period_verticalLayout.addWidget(self.period_label)

        self.period_comboBox = QComboBox(self.widget1)
        self.period_comboBox.addItem("")
        self.period_comboBox.addItem("")
        self.period_comboBox.addItem("")
        self.period_comboBox.addItem("")
        self.period_comboBox.setObjectName(u"period_comboBox")
        self.period_comboBox.setMinimumSize(QSize(187, 35))
        self.period_comboBox.setMaximumSize(QSize(187, 35))
        self.period_comboBox.setStyleSheet(u"QComboBox{\n"
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

        self.period_verticalLayout.addWidget(self.period_comboBox)


        self.horizontalLayout_2.addLayout(self.period_verticalLayout)

        self.month_verticalLayout = QVBoxLayout()
        self.month_verticalLayout.setObjectName(u"month_verticalLayout")
        self.month_label_select = QLabel(self.widget1)
        self.month_label_select.setObjectName(u"month_label_select")
        self.month_label_select.setMinimumSize(QSize(187, 17))
        self.month_label_select.setMaximumSize(QSize(187, 17))
        self.month_label_select.setFont(font4)
        self.month_label_select.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.month_verticalLayout.addWidget(self.month_label_select)

        self.month_comboBox_select = QComboBox(self.widget1)
        self.month_comboBox_select.addItem("")
        self.month_comboBox_select.addItem("")
        self.month_comboBox_select.addItem("")
        self.month_comboBox_select.addItem("")
        self.month_comboBox_select.addItem("")
        self.month_comboBox_select.addItem("")
        self.month_comboBox_select.addItem("")
        self.month_comboBox_select.addItem("")
        self.month_comboBox_select.addItem("")
        self.month_comboBox_select.addItem("")
        self.month_comboBox_select.addItem("")
        self.month_comboBox_select.addItem("")
        self.month_comboBox_select.addItem("")
        self.month_comboBox_select.setObjectName(u"month_comboBox_select")
        self.month_comboBox_select.setMinimumSize(QSize(187, 35))
        self.month_comboBox_select.setMaximumSize(QSize(187, 35))
        self.month_comboBox_select.setStyleSheet(u"QComboBox{\n"
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

        self.month_verticalLayout.addWidget(self.month_comboBox_select)


        self.horizontalLayout_2.addLayout(self.month_verticalLayout)

        self.year_verticalLayout = QVBoxLayout()
        self.year_verticalLayout.setObjectName(u"year_verticalLayout")
        self.year_label = QLabel(self.widget1)
        self.year_label.setObjectName(u"year_label")
        self.year_label.setMinimumSize(QSize(187, 17))
        self.year_label.setMaximumSize(QSize(187, 17))
        self.year_label.setFont(font4)
        self.year_label.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.year_verticalLayout.addWidget(self.year_label)

        self.year_lineEdit = QLineEdit(self.widget1)
        self.year_lineEdit.setObjectName(u"year_lineEdit")
        self.year_lineEdit.setMinimumSize(QSize(150, 35))
        self.year_lineEdit.setMaximumSize(QSize(187, 35))

        self.year_verticalLayout.addWidget(self.year_lineEdit)


        self.horizontalLayout_2.addLayout(self.year_verticalLayout)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.info_periodo_verticalLayout.addLayout(self.horizontalLayout_2)

        self.settings_page_info_company_widget = QWidget(self.settings_page_widget)
        self.settings_page_info_company_widget.setObjectName(u"settings_page_info_company_widget")
        self.settings_page_info_company_widget.setGeometry(QRect(0, 330, 801, 111))
        self.settings_page_info_company_widget.setStyleSheet(u"")
        self.widget2 = QWidget(self.settings_page_info_company_widget)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(0, 0, 801, 111))
        self.verticalLayout_2 = QVBoxLayout(self.widget2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 0, 0, 0)
        self.company_label = QLabel(self.widget2)
        self.company_label.setObjectName(u"company_label")
        self.company_label.setFont(font4)

        self.verticalLayout_2.addWidget(self.company_label)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, -1, -1, -1)
        self.name_company_verticalLayout = QVBoxLayout()
        self.name_company_verticalLayout.setObjectName(u"name_company_verticalLayout")
        self.names_company_label = QLabel(self.widget2)
        self.names_company_label.setObjectName(u"names_company_label")
        self.names_company_label.setMaximumSize(QSize(250, 17))
        self.names_company_label.setFont(font4)
        self.names_company_label.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.name_company_verticalLayout.addWidget(self.names_company_label)

        self.names_company_lineEdit = QLineEdit(self.widget2)
        self.names_company_lineEdit.setObjectName(u"names_company_lineEdit")
        self.names_company_lineEdit.setMinimumSize(QSize(250, 33))
        self.names_company_lineEdit.setMaximumSize(QSize(250, 33))

        self.name_company_verticalLayout.addWidget(self.names_company_lineEdit)


        self.horizontalLayout_3.addLayout(self.name_company_verticalLayout)

        self.cnpj_verticalLayout = QVBoxLayout()
        self.cnpj_verticalLayout.setObjectName(u"cnpj_verticalLayout")
        self.cnpj_label = QLabel(self.widget2)
        self.cnpj_label.setObjectName(u"cnpj_label")
        self.cnpj_label.setMinimumSize(QSize(0, 17))
        self.cnpj_label.setMaximumSize(QSize(250, 17))
        self.cnpj_label.setFont(font4)
        self.cnpj_label.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.cnpj_verticalLayout.addWidget(self.cnpj_label)

        self.cnpj_lineEdit = QLineEdit(self.widget2)
        self.cnpj_lineEdit.setObjectName(u"cnpj_lineEdit")
        self.cnpj_lineEdit.setMinimumSize(QSize(250, 33))
        self.cnpj_lineEdit.setMaximumSize(QSize(250, 33))

        self.cnpj_verticalLayout.addWidget(self.cnpj_lineEdit)


        self.horizontalLayout_3.addLayout(self.cnpj_verticalLayout)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.stackedWidget.addWidget(self.a_settings_page)
        self.b_upload_file_page = QWidget()
        self.b_upload_file_page.setObjectName(u"b_upload_file_page")
        self.b_upload_file_page.setMaximumSize(QSize(801, 731))
        self.upload_file_central_widget = QWidget(self.b_upload_file_page)
        self.upload_file_central_widget.setObjectName(u"upload_file_central_widget")
        self.upload_file_central_widget.setGeometry(QRect(0, 0, 801, 741))
        self.upload_file_central_widget.setStyleSheet(u"")
        self.upload_file_botton_frame = QWidget(self.upload_file_central_widget)
        self.upload_file_botton_frame.setObjectName(u"upload_file_botton_frame")
        self.upload_file_botton_frame.setGeometry(QRect(0, 660, 801, 70))
        self.upload_file_botton_frame.setMinimumSize(QSize(0, 70))
        self.upload_file_botton_frame.setMaximumSize(QSize(16777215, 0))
        self.upload_file_botton_frame.setFont(font2)
        self.upload_file_botton_frame.setStyleSheet(u"")
        self.layoutWidget_17 = QWidget(self.upload_file_botton_frame)
        self.layoutWidget_17.setObjectName(u"layoutWidget_17")
        self.layoutWidget_17.setGeometry(QRect(0, 10, 801, 71))
        self.upload_file_botton_frame_hLayout = QHBoxLayout(self.layoutWidget_17)
        self.upload_file_botton_frame_hLayout.setObjectName(u"upload_file_botton_frame_hLayout")
        self.upload_file_botton_frame_hLayout.setContentsMargins(0, 0, 10, 0)
        self.upload_file_horizontalSpacer = QSpacerItem(598, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.upload_file_botton_frame_hLayout.addItem(self.upload_file_horizontalSpacer)

        self.upload_file_next_btn = QPushButton(self.layoutWidget_17)
        self.upload_file_next_btn.setObjectName(u"upload_file_next_btn")
        self.upload_file_next_btn.setMinimumSize(QSize(150, 35))
        self.upload_file_next_btn.setMaximumSize(QSize(150, 35))
        self.upload_file_next_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: #34D481;\n"
"	color:white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight:bold;\n"
"	font-size: 15px;\n"
"}")

        self.upload_file_botton_frame_hLayout.addWidget(self.upload_file_next_btn)

        self.upload_file_page_table = QWidget(self.upload_file_central_widget)
        self.upload_file_page_table.setObjectName(u"upload_file_page_table")
        self.upload_file_page_table.setGeometry(QRect(0, 270, 801, 391))
        self.upload_file_page_table.setStyleSheet(u"")
        self.upload_file_table = QTableWidget(self.upload_file_page_table)
        if (self.upload_file_table.columnCount() < 7):
            self.upload_file_table.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.upload_file_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.upload_file_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.upload_file_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.upload_file_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.upload_file_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.upload_file_table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.upload_file_table.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.upload_file_table.setObjectName(u"upload_file_table")
        self.upload_file_table.setGeometry(QRect(0, 0, 801, 431))
        self.upload_file_table.horizontalHeader().setMinimumSectionSize(32)
        self.upload_file_table.horizontalHeader().setDefaultSectionSize(110)
        self.upload_file_page_buttons = QWidget(self.upload_file_central_widget)
        self.upload_file_page_buttons.setObjectName(u"upload_file_page_buttons")
        self.upload_file_page_buttons.setGeometry(QRect(0, 70, 801, 221))
        self.upload_file_page_buttons.setStyleSheet(u"")
        self.layoutWidget_8 = QWidget(self.upload_file_page_buttons)
        self.layoutWidget_8.setObjectName(u"layoutWidget_8")
        self.layoutWidget_8.setGeometry(QRect(0, 80, 801, 111))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget_8)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget_8)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font3)

        self.verticalLayout_4.addWidget(self.label_3)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(5, 10, 0, 10)
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_select_account = QLabel(self.layoutWidget_8)
        self.label_select_account.setObjectName(u"label_select_account")
        self.label_select_account.setMinimumSize(QSize(187, 17))
        self.label_select_account.setMaximumSize(QSize(187, 17))
        self.label_select_account.setFont(font4)
        self.label_select_account.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_8.addWidget(self.label_select_account)

        self.comboBox_select_account = QComboBox(self.layoutWidget_8)
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

        self.verticalLayout_8.addWidget(self.comboBox_select_account)


        self.horizontalLayout_7.addLayout(self.verticalLayout_8)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_select_desc_account = QLabel(self.layoutWidget_8)
        self.label_select_desc_account.setObjectName(u"label_select_desc_account")
        self.label_select_desc_account.setMinimumSize(QSize(0, 17))
        self.label_select_desc_account.setMaximumSize(QSize(16777215, 17))
        self.label_select_desc_account.setFont(font4)
        self.label_select_desc_account.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_11.addWidget(self.label_select_desc_account)

        self.comboBox_select_desc_account = QComboBox(self.layoutWidget_8)
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

        self.verticalLayout_11.addWidget(self.comboBox_select_desc_account)


        self.horizontalLayout_7.addLayout(self.verticalLayout_11)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_select_value = QLabel(self.layoutWidget_8)
        self.label_select_value.setObjectName(u"label_select_value")
        self.label_select_value.setMinimumSize(QSize(0, 17))
        self.label_select_value.setMaximumSize(QSize(16777215, 17))
        self.label_select_value.setFont(font4)
        self.label_select_value.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_9.addWidget(self.label_select_value)

        self.comboBox_select_value = QComboBox(self.layoutWidget_8)
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

        self.verticalLayout_9.addWidget(self.comboBox_select_value)


        self.horizontalLayout_7.addLayout(self.verticalLayout_9)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_6)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.widget3 = QWidget(self.upload_file_page_buttons)
        self.widget3.setObjectName(u"widget3")
        self.widget3.setGeometry(QRect(0, 0, 344, 76))
        self.verticalLayout_3 = QVBoxLayout(self.widget3)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 7, 0, 10)
        self.upload_file_page_label = QLabel(self.widget3)
        self.upload_file_page_label.setObjectName(u"upload_file_page_label")
        self.upload_file_page_label.setFont(font3)

        self.verticalLayout_3.addWidget(self.upload_file_page_label)

        self.upload_file_btn = QPushButton(self.widget3)
        self.upload_file_btn.setObjectName(u"upload_file_btn")
        self.upload_file_btn.setMinimumSize(QSize(150, 35))
        self.upload_file_btn.setMaximumSize(QSize(150, 35))
        self.upload_file_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: #34D481;\n"
"	color:white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight:bold;\n"
"	font-size: 15px;\n"
"}")

        self.verticalLayout_3.addWidget(self.upload_file_btn)

        self.upload_file_page_top_frame = QWidget(self.upload_file_central_widget)
        self.upload_file_page_top_frame.setObjectName(u"upload_file_page_top_frame")
        self.upload_file_page_top_frame.setGeometry(QRect(0, 0, 801, 61))
        self.upload_file_page_top_frame.setMinimumSize(QSize(0, 61))
        self.upload_file_page_top_frame.setMaximumSize(QSize(16777215, 61))
        self.upload_file_page_top_frame.setFont(font2)
        self.upload_file_page_top_frame.setStyleSheet(u"")
        self.layoutWidget_19 = QWidget(self.upload_file_page_top_frame)
        self.layoutWidget_19.setObjectName(u"layoutWidget_19")
        self.layoutWidget_19.setGeometry(QRect(0, 0, 801, 62))
        self.upload_file_page_horizontalLayout = QHBoxLayout(self.layoutWidget_19)
        self.upload_file_page_horizontalLayout.setObjectName(u"upload_file_page_horizontalLayout")
        self.upload_file_page_horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.upload_file_page_title = QLabel(self.layoutWidget_19)
        self.upload_file_page_title.setObjectName(u"upload_file_page_title")
        self.upload_file_page_title.setFont(font5)
        self.upload_file_page_title.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.upload_file_page_title.setMargin(10)

        self.upload_file_page_horizontalLayout.addWidget(self.upload_file_page_title)

        self.upload_file_page_horizontalSpacer = QSpacerItem(348, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.upload_file_page_horizontalLayout.addItem(self.upload_file_page_horizontalSpacer)

        self.stackedWidget.addWidget(self.b_upload_file_page)
        self.c_update_data_page = QWidget()
        self.c_update_data_page.setObjectName(u"c_update_data_page")
        self.c_update_data_page.setMaximumSize(QSize(801, 731))
        self.central_widget_update_column_page = QWidget(self.c_update_data_page)
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
        self.layoutWidget_4.setGeometry(QRect(0, 10, 801, 71))
        self.hLayout_bottom_frame_3 = QHBoxLayout(self.layoutWidget_4)
        self.hLayout_bottom_frame_3.setObjectName(u"hLayout_bottom_frame_3")
        self.hLayout_bottom_frame_3.setContentsMargins(0, 0, 10, 0)
        self.horizontalSpacer_5 = QSpacerItem(598, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hLayout_bottom_frame_3.addItem(self.horizontalSpacer_5)

        self.next_btn_update_data_page = QPushButton(self.layoutWidget_4)
        self.next_btn_update_data_page.setObjectName(u"next_btn_update_data_page")
        self.next_btn_update_data_page.setMinimumSize(QSize(150, 35))
        self.next_btn_update_data_page.setMaximumSize(QSize(150, 35))
        self.next_btn_update_data_page.setStyleSheet(u"QPushButton{\n"
"	background-color: #34D481;\n"
"	color:white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight:bold;\n"
"	font-size: 15px;\n"
"}")

        self.hLayout_bottom_frame_3.addWidget(self.next_btn_update_data_page)

        self.table_frame_widget_update_column_page = QWidget(self.central_widget_update_column_page)
        self.table_frame_widget_update_column_page.setObjectName(u"table_frame_widget_update_column_page")
        self.table_frame_widget_update_column_page.setGeometry(QRect(0, 70, 801, 591))
        self.widget4 = QWidget(self.table_frame_widget_update_column_page)
        self.widget4.setObjectName(u"widget4")
        self.widget4.setGeometry(QRect(0, 0, 801, 591))
        self.verticalLayout_6 = QVBoxLayout(self.widget4)
        self.verticalLayout_6.setSpacing(20)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 0, 0, 0)
        self.label_2 = QLabel(self.widget4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font3)

        self.verticalLayout_6.addWidget(self.label_2)

        self.update_account_table = QTableWidget(self.widget4)
        if (self.update_account_table.columnCount() < 3):
            self.update_account_table.setColumnCount(3)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.update_account_table.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.update_account_table.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.update_account_table.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        if (self.update_account_table.rowCount() < 19):
            self.update_account_table.setRowCount(19)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.update_account_table.setVerticalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.update_account_table.setVerticalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.update_account_table.setVerticalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.update_account_table.setVerticalHeaderItem(3, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.update_account_table.setVerticalHeaderItem(4, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.update_account_table.setVerticalHeaderItem(5, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.update_account_table.setVerticalHeaderItem(6, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.update_account_table.setVerticalHeaderItem(7, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.update_account_table.setVerticalHeaderItem(8, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.update_account_table.setVerticalHeaderItem(9, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.update_account_table.setVerticalHeaderItem(10, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.update_account_table.setVerticalHeaderItem(11, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.update_account_table.setVerticalHeaderItem(12, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.update_account_table.setVerticalHeaderItem(13, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.update_account_table.setVerticalHeaderItem(14, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.update_account_table.setVerticalHeaderItem(15, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.update_account_table.setVerticalHeaderItem(16, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.update_account_table.setVerticalHeaderItem(17, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.update_account_table.setVerticalHeaderItem(18, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.update_account_table.setItem(0, 0, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.update_account_table.setItem(0, 1, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.update_account_table.setItem(0, 2, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.update_account_table.setItem(1, 0, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.update_account_table.setItem(1, 1, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.update_account_table.setItem(1, 2, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.update_account_table.setItem(2, 0, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.update_account_table.setItem(2, 1, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.update_account_table.setItem(3, 0, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.update_account_table.setItem(3, 1, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.update_account_table.setItem(4, 0, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.update_account_table.setItem(4, 1, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.update_account_table.setItem(5, 0, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.update_account_table.setItem(5, 1, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.update_account_table.setItem(6, 0, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.update_account_table.setItem(6, 1, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.update_account_table.setItem(7, 0, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.update_account_table.setItem(7, 1, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.update_account_table.setItem(7, 2, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.update_account_table.setItem(8, 0, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.update_account_table.setItem(8, 1, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.update_account_table.setItem(9, 0, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.update_account_table.setItem(9, 1, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.update_account_table.setItem(10, 0, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.update_account_table.setItem(10, 1, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.update_account_table.setItem(11, 0, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.update_account_table.setItem(11, 1, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.update_account_table.setItem(12, 0, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.update_account_table.setItem(12, 1, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.update_account_table.setItem(13, 0, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.update_account_table.setItem(13, 1, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.update_account_table.setItem(14, 0, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        self.update_account_table.setItem(14, 1, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        self.update_account_table.setItem(15, 0, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        self.update_account_table.setItem(15, 1, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        self.update_account_table.setItem(16, 0, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        self.update_account_table.setItem(16, 1, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        self.update_account_table.setItem(17, 0, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        self.update_account_table.setItem(17, 1, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        self.update_account_table.setItem(18, 0, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        self.update_account_table.setItem(18, 1, __qtablewidgetitem69)
        self.update_account_table.setObjectName(u"update_account_table")
        self.update_account_table.setMaximumSize(QSize(801, 541))
        font6 = QFont()
        font6.setBold(False)
        self.update_account_table.setFont(font6)
        self.update_account_table.horizontalHeader().setVisible(True)
        self.update_account_table.horizontalHeader().setCascadingSectionResizes(False)
        self.update_account_table.horizontalHeader().setMinimumSectionSize(205)
        self.update_account_table.horizontalHeader().setDefaultSectionSize(205)

        self.verticalLayout_6.addWidget(self.update_account_table)

        self.top_frame_widget_update_data_page = QWidget(self.central_widget_update_column_page)
        self.top_frame_widget_update_data_page.setObjectName(u"top_frame_widget_update_data_page")
        self.top_frame_widget_update_data_page.setGeometry(QRect(0, 0, 801, 61))
        self.top_frame_widget_update_data_page.setMinimumSize(QSize(0, 61))
        self.top_frame_widget_update_data_page.setMaximumSize(QSize(16777215, 61))
        self.top_frame_widget_update_data_page.setFont(font2)
        self.top_frame_widget_update_data_page.setStyleSheet(u"")
        self.layoutWidget_6 = QWidget(self.top_frame_widget_update_data_page)
        self.layoutWidget_6.setObjectName(u"layoutWidget_6")
        self.layoutWidget_6.setGeometry(QRect(0, 0, 801, 62))
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.title_page_update_data_page = QLabel(self.layoutWidget_6)
        self.title_page_update_data_page.setObjectName(u"title_page_update_data_page")
        self.title_page_update_data_page.setFont(font5)
        self.title_page_update_data_page.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.title_page_update_data_page.setMargin(10)

        self.horizontalLayout_6.addWidget(self.title_page_update_data_page)

        self.horizontalSpacer_update_data_page = QSpacerItem(348, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_update_data_page)

        self.file_name_label_update_datat_page = QLabel(self.layoutWidget_6)
        self.file_name_label_update_datat_page.setObjectName(u"file_name_label_update_datat_page")
        font7 = QFont()
        font7.setPointSize(11)
        self.file_name_label_update_datat_page.setFont(font7)
        self.file_name_label_update_datat_page.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.file_name_label_update_datat_page.setMargin(20)

        self.horizontalLayout_6.addWidget(self.file_name_label_update_datat_page)

        self.stackedWidget.addWidget(self.c_update_data_page)
        self.e_exportation_page = QWidget()
        self.e_exportation_page.setObjectName(u"e_exportation_page")
        self.upload_file_central_widget_2 = QWidget(self.e_exportation_page)
        self.upload_file_central_widget_2.setObjectName(u"upload_file_central_widget_2")
        self.upload_file_central_widget_2.setGeometry(QRect(0, 0, 801, 741))
        self.upload_file_central_widget_2.setStyleSheet(u"")
        self.export_page_botton_frame = QWidget(self.upload_file_central_widget_2)
        self.export_page_botton_frame.setObjectName(u"export_page_botton_frame")
        self.export_page_botton_frame.setGeometry(QRect(0, 660, 801, 70))
        self.export_page_botton_frame.setMinimumSize(QSize(0, 70))
        self.export_page_botton_frame.setMaximumSize(QSize(16777215, 0))
        self.export_page_botton_frame.setFont(font2)
        self.export_page_botton_frame.setStyleSheet(u"")
        self.layoutWidget_18 = QWidget(self.export_page_botton_frame)
        self.layoutWidget_18.setObjectName(u"layoutWidget_18")
        self.layoutWidget_18.setGeometry(QRect(0, 10, 801, 71))
        self.export_page_botton_frame_hLayout = QHBoxLayout(self.layoutWidget_18)
        self.export_page_botton_frame_hLayout.setObjectName(u"export_page_botton_frame_hLayout")
        self.export_page_botton_frame_hLayout.setContentsMargins(0, 0, 10, 0)
        self.export_page_horizontalSpacer = QSpacerItem(598, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.export_page_botton_frame_hLayout.addItem(self.export_page_horizontalSpacer)

        self.export_page_close_btn = QPushButton(self.layoutWidget_18)
        self.export_page_close_btn.setObjectName(u"export_page_close_btn")
        self.export_page_close_btn.setMinimumSize(QSize(150, 35))
        self.export_page_close_btn.setMaximumSize(QSize(150, 35))
        self.export_page_close_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: #34D481;\n"
"	color:white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight:bold;\n"
"	font-size: 15px;\n"
"}")
        self.export_page_close_btn.setCheckable(True)

        self.export_page_botton_frame_hLayout.addWidget(self.export_page_close_btn)

        self.export_page_table = QWidget(self.upload_file_central_widget_2)
        self.export_page_table.setObjectName(u"export_page_table")
        self.export_page_table.setGeometry(QRect(0, 190, 801, 471))
        self.export_page_table.setStyleSheet(u"")
        self.export_table = QTableWidget(self.export_page_table)
        if (self.export_table.columnCount() < 7):
            self.export_table.setColumnCount(7)
        __qtablewidgetitem70 = QTableWidgetItem()
        self.export_table.setHorizontalHeaderItem(0, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        self.export_table.setHorizontalHeaderItem(1, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        self.export_table.setHorizontalHeaderItem(2, __qtablewidgetitem72)
        __qtablewidgetitem73 = QTableWidgetItem()
        self.export_table.setHorizontalHeaderItem(3, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        self.export_table.setHorizontalHeaderItem(4, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        self.export_table.setHorizontalHeaderItem(5, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        self.export_table.setHorizontalHeaderItem(6, __qtablewidgetitem76)
        self.export_table.setObjectName(u"export_table")
        self.export_table.setGeometry(QRect(0, 0, 801, 471))
        self.export_table.horizontalHeader().setMinimumSectionSize(32)
        self.export_table.horizontalHeader().setDefaultSectionSize(110)
        self.upload_file_page_buttons_2 = QWidget(self.upload_file_central_widget_2)
        self.upload_file_page_buttons_2.setObjectName(u"upload_file_page_buttons_2")
        self.upload_file_page_buttons_2.setGeometry(QRect(0, 70, 801, 121))
        self.upload_file_page_buttons_2.setStyleSheet(u"")
        self.layoutWidget_12 = QWidget(self.upload_file_page_buttons_2)
        self.layoutWidget_12.setObjectName(u"layoutWidget_12")
        self.layoutWidget_12.setGeometry(QRect(0, 0, 801, 111))
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget_12)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, 5, 0, 0)
        self.label_5 = QLabel(self.layoutWidget_12)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font3)

        self.verticalLayout_5.addWidget(self.label_5)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(6)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(5, 10, 0, 10)
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_select_account_3 = QLabel(self.layoutWidget_12)
        self.label_select_account_3.setObjectName(u"label_select_account_3")
        self.label_select_account_3.setMinimumSize(QSize(187, 17))
        self.label_select_account_3.setMaximumSize(QSize(187, 17))
        self.label_select_account_3.setFont(font4)
        self.label_select_account_3.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_10.addWidget(self.label_select_account_3)

        self.upload_file_next_btn_2 = QPushButton(self.layoutWidget_12)
        self.upload_file_next_btn_2.setObjectName(u"upload_file_next_btn_2")
        self.upload_file_next_btn_2.setMinimumSize(QSize(150, 35))
        self.upload_file_next_btn_2.setMaximumSize(QSize(150, 35))
        self.upload_file_next_btn_2.setStyleSheet(u"QPushButton{\n"
"	background-color: #34D481;\n"
"	color:white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight:bold;\n"
"	font-size: 15px;\n"
"}")

        self.verticalLayout_10.addWidget(self.upload_file_next_btn_2)


        self.horizontalLayout_9.addLayout(self.verticalLayout_10)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_8)


        self.verticalLayout_5.addLayout(self.horizontalLayout_9)

        self.upload_file_page_top_frame_2 = QWidget(self.upload_file_central_widget_2)
        self.upload_file_page_top_frame_2.setObjectName(u"upload_file_page_top_frame_2")
        self.upload_file_page_top_frame_2.setGeometry(QRect(0, 0, 801, 61))
        self.upload_file_page_top_frame_2.setMinimumSize(QSize(0, 61))
        self.upload_file_page_top_frame_2.setMaximumSize(QSize(16777215, 61))
        self.upload_file_page_top_frame_2.setFont(font2)
        self.upload_file_page_top_frame_2.setStyleSheet(u"")
        self.layoutWidget_20 = QWidget(self.upload_file_page_top_frame_2)
        self.layoutWidget_20.setObjectName(u"layoutWidget_20")
        self.layoutWidget_20.setGeometry(QRect(0, 0, 801, 62))
        self.upload_file_page_horizontalLayout_2 = QHBoxLayout(self.layoutWidget_20)
        self.upload_file_page_horizontalLayout_2.setObjectName(u"upload_file_page_horizontalLayout_2")
        self.upload_file_page_horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.upload_file_page_title_2 = QLabel(self.layoutWidget_20)
        self.upload_file_page_title_2.setObjectName(u"upload_file_page_title_2")
        self.upload_file_page_title_2.setFont(font5)
        self.upload_file_page_title_2.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.upload_file_page_title_2.setMargin(10)

        self.upload_file_page_horizontalLayout_2.addWidget(self.upload_file_page_title_2)

        self.upload_file_page_horizontalSpacer_2 = QSpacerItem(348, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.upload_file_page_horizontalLayout_2.addItem(self.upload_file_page_horizontalSpacer_2)

        self.stackedWidget.addWidget(self.e_exportation_page)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.exit_btn.toggled.connect(MainWindow.close)
        self.export_page_close_btn.toggled.connect(MainWindow.close)
        

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Integra\u00e7\u00e3o de Dados Cont\u00e1beis", None))
        self.icon_left_frame.setText("")
        self.settings_page_btn.setText(QCoreApplication.translate("MainWindow", u"Configura\u00e7\u00e3o", None))
        self.load_file_page_btn.setText(QCoreApplication.translate("MainWindow", u"Carregar Arquivo", None))
        self.update_data_page_btn.setText(QCoreApplication.translate("MainWindow", u"ALterar Dados", None))
        self.exportation_page_btn.setText(QCoreApplication.translate("MainWindow", u"Exportar Dados", None))
        self.exit_btn.setText(QCoreApplication.translate("MainWindow", u"Sair", None))
        self.save_btn_load_data_page.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.label_info_settings.setText(QCoreApplication.translate("MainWindow", u"Entre com as informa\u00e7\u00f5es dos dados que voc\u00ea esta inserindo.", None))
        self.file_info_label.setText(QCoreApplication.translate("MainWindow", u"Informa\u00e7\u00f5es do arquivo", None))
        self.type_file_label.setText(QCoreApplication.translate("MainWindow", u"Tipo de arquivo", None))
        self.type_file_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u".csv", None))

        self.delimiter_info_label.setText(QCoreApplication.translate("MainWindow", u"Delimitador", None))
        self.delimiter_comboBox_file.setItemText(0, QCoreApplication.translate("MainWindow", u"V\u00edrgula", None))
        self.delimiter_comboBox_file.setItemText(1, QCoreApplication.translate("MainWindow", u"Ponto e V\u00edrgula", None))

        self.encoding_label.setText(QCoreApplication.translate("MainWindow", u"Encoding", None))
        self.encoding_comboBox_file.setItemText(0, QCoreApplication.translate("MainWindow", u"UTF-8", None))
        self.encoding_comboBox_file.setItemText(1, QCoreApplication.translate("MainWindow", u" ISO-8859-1", None))

        self.settings_page_title.setText(QCoreApplication.translate("MainWindow", u"Configura\u00e7\u00e3o", None))
        self.period_info_label.setText(QCoreApplication.translate("MainWindow", u"Informa\u00e7\u00f5es do P\u00e9riodo", None))
        self.period_label.setText(QCoreApplication.translate("MainWindow", u"Per\u00edodo dos dados", None))
        self.period_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"SELECIONE  O PERIODO", None))
        self.period_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Mensal", None))
        self.period_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Anual", None))
        self.period_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Trimestral", None))

        self.month_label_select.setText(QCoreApplication.translate("MainWindow", u"M\u00eas de Exerc\u00edcio", None))
        self.month_comboBox_select.setItemText(0, QCoreApplication.translate("MainWindow", u"SELECIONE O M\u00caS", None))
        self.month_comboBox_select.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.month_comboBox_select.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))
        self.month_comboBox_select.setItemText(3, QCoreApplication.translate("MainWindow", u"3", None))
        self.month_comboBox_select.setItemText(4, QCoreApplication.translate("MainWindow", u"4", None))
        self.month_comboBox_select.setItemText(5, QCoreApplication.translate("MainWindow", u"5", None))
        self.month_comboBox_select.setItemText(6, QCoreApplication.translate("MainWindow", u"6", None))
        self.month_comboBox_select.setItemText(7, QCoreApplication.translate("MainWindow", u"7", None))
        self.month_comboBox_select.setItemText(8, QCoreApplication.translate("MainWindow", u"8", None))
        self.month_comboBox_select.setItemText(9, QCoreApplication.translate("MainWindow", u"9", None))
        self.month_comboBox_select.setItemText(10, QCoreApplication.translate("MainWindow", u"10", None))
        self.month_comboBox_select.setItemText(11, QCoreApplication.translate("MainWindow", u"11", None))
        self.month_comboBox_select.setItemText(12, QCoreApplication.translate("MainWindow", u"12", None))

        self.year_label.setText(QCoreApplication.translate("MainWindow", u"Ano", None))
        self.year_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite o ano", None))
        self.company_label.setText(QCoreApplication.translate("MainWindow", u"Informa\u00e7\u00f5es da Empresa", None))
        self.names_company_label.setText(QCoreApplication.translate("MainWindow", u"Nome da Empresa", None))
        self.cnpj_label.setText(QCoreApplication.translate("MainWindow", u"CNPJ", None))
        self.upload_file_next_btn.setText(QCoreApplication.translate("MainWindow", u"Avan\u00e7ar", None))
        ___qtablewidgetitem = self.upload_file_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Column_1", None));
        ___qtablewidgetitem1 = self.upload_file_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Column_2", None));
        ___qtablewidgetitem2 = self.upload_file_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Column_3", None));
        ___qtablewidgetitem3 = self.upload_file_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Column_4", None));
        ___qtablewidgetitem4 = self.upload_file_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Column_5", None));
        ___qtablewidgetitem5 = self.upload_file_table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Column_6", None));
        ___qtablewidgetitem6 = self.upload_file_table.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Column_7", None));
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Associe as colunas abaixo com as colunas dos seus dados", None))
        self.label_select_account.setText(QCoreApplication.translate("MainWindow", u"Conta", None))
        self.comboBox_select_account.setItemText(0, QCoreApplication.translate("MainWindow", u"SELECIONE  A COLUNA", None))

        self.label_select_desc_account.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o da Conta", None))
        self.comboBox_select_desc_account.setItemText(0, QCoreApplication.translate("MainWindow", u"SELECIONE A COLUNA", None))

        self.label_select_value.setText(QCoreApplication.translate("MainWindow", u" Valor", None))
        self.comboBox_select_value.setItemText(0, QCoreApplication.translate("MainWindow", u"SELECIONE A COLUNA", None))

        self.upload_file_page_label.setText(QCoreApplication.translate("MainWindow", u"Click em inserir para carregar o arquivo e visualize a tabela.", None))
        self.upload_file_btn.setText(QCoreApplication.translate("MainWindow", u"Inserir ", None))
        self.upload_file_page_title.setText(QCoreApplication.translate("MainWindow", u"Carregar Arquivo", None))
        self.next_btn_update_data_page.setText(QCoreApplication.translate("MainWindow", u"Avan\u00e7ar", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Associe as colunas abaixo com as colunas dos seus dados", None))
        ___qtablewidgetitem7 = self.update_account_table.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo da Conta", None));
        ___qtablewidgetitem8 = self.update_account_table.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o da Conta", None));
        ___qtablewidgetitem9 = self.update_account_table.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Alterar C\u00f3digo", None));
        ___qtablewidgetitem10 = self.update_account_table.verticalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Balan\u00e7o Patrimonial", None));
        ___qtablewidgetitem11 = self.update_account_table.verticalHeaderItem(13)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Demonstra\u00e7\u00e3o do Resultado", None));
        ___qtablewidgetitem12 = self.update_account_table.verticalHeaderItem(18)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Fluxo de Caixa", None));

        __sortingEnabled = self.update_account_table.isSortingEnabled()
        self.update_account_table.setSortingEnabled(False)
        ___qtablewidgetitem13 = self.update_account_table.item(0, 0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem14 = self.update_account_table.item(0, 1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Ativo", None));
        ___qtablewidgetitem15 = self.update_account_table.item(1, 0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"1.01", None));
        ___qtablewidgetitem16 = self.update_account_table.item(1, 1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Ativo Circulante", None));
        ___qtablewidgetitem17 = self.update_account_table.item(2, 0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"1.01.01", None));
        ___qtablewidgetitem18 = self.update_account_table.item(2, 1)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Caixa e Equivalente de Caixa", None));
        ___qtablewidgetitem19 = self.update_account_table.item(3, 0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"1.01.02", None));
        ___qtablewidgetitem20 = self.update_account_table.item(3, 1)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Aplica\u00e7\u00e3o Financeira", None));
        ___qtablewidgetitem21 = self.update_account_table.item(4, 0)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"1.01.04", None));
        ___qtablewidgetitem22 = self.update_account_table.item(4, 1)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Estoque", None));
        ___qtablewidgetitem23 = self.update_account_table.item(5, 0)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"1.02", None));
        ___qtablewidgetitem24 = self.update_account_table.item(5, 1)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Ativo N\u00e3o Circulante", None));
        ___qtablewidgetitem25 = self.update_account_table.item(6, 0)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"1.02.01", None));
        ___qtablewidgetitem26 = self.update_account_table.item(6, 1)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Ativo Realiz\u00e1vel a Long Prazo", None));
        ___qtablewidgetitem27 = self.update_account_table.item(7, 0)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem28 = self.update_account_table.item(7, 1)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Passivo", None));
        ___qtablewidgetitem29 = self.update_account_table.item(8, 0)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"2.01", None));
        ___qtablewidgetitem30 = self.update_account_table.item(8, 1)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Passivo Circulante", None));
        ___qtablewidgetitem31 = self.update_account_table.item(9, 0)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"2.01.04", None));
        ___qtablewidgetitem32 = self.update_account_table.item(9, 1)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Empr\u00e9stimo a Curto Prazo", None));
        ___qtablewidgetitem33 = self.update_account_table.item(10, 0)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"2.02", None));
        ___qtablewidgetitem34 = self.update_account_table.item(10, 1)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Passivo N\u00e3o Circulante", None));
        ___qtablewidgetitem35 = self.update_account_table.item(11, 0)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"2.02.01", None));
        ___qtablewidgetitem36 = self.update_account_table.item(11, 1)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Empr\u00e9stimo a longo Prazo", None));
        ___qtablewidgetitem37 = self.update_account_table.item(12, 0)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"2.03", None));
        ___qtablewidgetitem38 = self.update_account_table.item(12, 1)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"Patrim\u00f4nio L\u00edquido", None));
        ___qtablewidgetitem39 = self.update_account_table.item(13, 0)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"3.01", None));
        ___qtablewidgetitem40 = self.update_account_table.item(13, 1)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"Receita L\u00edquida", None));
        ___qtablewidgetitem41 = self.update_account_table.item(14, 0)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"3.02", None));
        ___qtablewidgetitem42 = self.update_account_table.item(14, 1)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"Custos", None));
        ___qtablewidgetitem43 = self.update_account_table.item(15, 0)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"3.03", None));
        ___qtablewidgetitem44 = self.update_account_table.item(15, 1)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"Lucro Bruto", None));
        ___qtablewidgetitem45 = self.update_account_table.item(16, 0)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"3.05", None));
        ___qtablewidgetitem46 = self.update_account_table.item(16, 1)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"Resultado Antes dos Tributos", None));
        ___qtablewidgetitem47 = self.update_account_table.item(17, 0)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"3.08", None));
        ___qtablewidgetitem48 = self.update_account_table.item(17, 1)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"Imposto de Renda e Contribui\u00e7\u00e3o Social Sobre o Lucro", None));
        ___qtablewidgetitem49 = self.update_account_table.item(18, 0)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"6.01.01.02", None));
        ___qtablewidgetitem50 = self.update_account_table.item(18, 1)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"Deprecia\u00e7\u00e3o e Amortiza\u00e7\u00e3o", None));
        self.update_account_table.setSortingEnabled(__sortingEnabled)

        self.title_page_update_data_page.setText(QCoreApplication.translate("MainWindow", u"Alterar Dados", None))
        self.file_name_label_update_datat_page.setText(QCoreApplication.translate("MainWindow", u"arquivo.csv", None))
        self.export_page_close_btn.setText(QCoreApplication.translate("MainWindow", u"Fechar", None))
        ___qtablewidgetitem51 = self.export_table.horizontalHeaderItem(0)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"Column_1", None));
        ___qtablewidgetitem52 = self.export_table.horizontalHeaderItem(1)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"Column_2", None));
        ___qtablewidgetitem53 = self.export_table.horizontalHeaderItem(2)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"Column_3", None));
        ___qtablewidgetitem54 = self.export_table.horizontalHeaderItem(3)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"Column_4", None));
        ___qtablewidgetitem55 = self.export_table.horizontalHeaderItem(4)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainWindow", u"Column_5", None));
        ___qtablewidgetitem56 = self.export_table.horizontalHeaderItem(5)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MainWindow", u"Column_6", None));
        ___qtablewidgetitem57 = self.export_table.horizontalHeaderItem(6)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("MainWindow", u"Column_7", None));
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Clique em exportar, para baixar o arquivo com os dados gerados.", None))
        self.label_select_account_3.setText(QCoreApplication.translate("MainWindow", u".csv", None))
        self.upload_file_next_btn_2.setText(QCoreApplication.translate("MainWindow", u"Exportar", None))
        self.upload_file_page_title_2.setText(QCoreApplication.translate("MainWindow", u"Exportar Dados", None))
    # retranslateUi

