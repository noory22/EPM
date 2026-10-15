# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_epm.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QLabel,
    QLineEdit, QListView, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 560)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u"../../Users/Software Department/.designer/Users/Software Department/Users/Software Department/.designer/backup/rsc/104ca819-58f3-4fa3-9909-01662f14ec27.jpeg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        MainWindow.setToolButtonStyle(Qt.ToolButtonTextOnly)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.label_A = QLabel(self.centralwidget)
        self.label_A.setObjectName(u"label_A")
        self.label_A.setGeometry(QRect(60, 0, 361, 61))
        font1 = QFont()
        font1.setFamilies([u"SF Pro Display"])
        font1.setPointSize(23)
        font1.setBold(True)
        self.label_A.setFont(font1)
        self.label_A.setStyleSheet(u"b")
        self.label_A.setScaledContents(False)
        self.screen_2 = QFrame(self.centralwidget)
        self.screen_2.setObjectName(u"screen_2")
        self.screen_2.setGeometry(QRect(0, 59, 1024, 541))
        font2 = QFont()
        font2.setFamilies([u"SF Pro Display"])
        font2.setPointSize(14)
        self.screen_2.setFont(font2)
        self.screen_2.setStyleSheet(u"background-color: rgb(233, 238, 241);")
        self.screen_2.setFrameShape(QFrame.StyledPanel)
        self.screen_2.setFrameShadow(QFrame.Raised)
        self.button_2 = QPushButton(self.screen_2)
        self.button_2.setObjectName(u"button_2")
        self.button_2.setGeometry(QRect(99, 100, 300, 60))
        font3 = QFont()
        font3.setFamilies([u"SF Pro Display"])
        font3.setPointSize(16)
        font3.setBold(True)
        self.button_2.setFont(font3)
        self.button_2.setStyleSheet(u"QPushButton#button_2 {\n"
"    color: #FFFFFF; /* White text */\n"
"    background-color: #00509E; /* Dark blue background for sufficient contrast */\n"
"    border-radius: 5px; /* Optional styling */\n"
"    padding: 5px 10px; /* Optional spacing */\n"
"}\n"
"QPushButton#button_2:hover {\n"
"    background-color: #003F7F; /* Slightly darker blue on hover */\n"
"}\n"
"")
        self.label_15 = QLabel(self.screen_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(468, 140, 361, 71))
        font4 = QFont()
        font4.setFamilies([u"SF Pro Display"])
        font4.setPointSize(48)
        font4.setBold(True)
        font4.setKerning(True)
        self.label_15.setFont(font4)
        self.label_15.setStyleSheet(u"background-color: transparent;\n"
"color: rgb(154, 153, 150);\n"
"color: rgb(47, 47, 47);")
        self.label_16 = QLabel(self.screen_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(470, 210, 421, 51))
        font5 = QFont()
        font5.setFamilies([u"SF Pro Display"])
        font5.setPointSize(22)
        font5.setBold(True)
        font5.setKerning(True)
        self.label_16.setFont(font5)
        self.label_16.setStyleSheet(u"background-color: transparent;\n"
"color: #308DC2;")
        self.label_16.setTextFormat(Qt.RichText)
        self.label_17 = QLabel(self.screen_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(470, 260, 501, 141))
        font6 = QFont()
        font6.setFamilies([u"SF Pro Display"])
        font6.setPointSize(16)
        font6.setBold(False)
        font6.setKerning(True)
        self.label_17.setFont(font6)
        self.label_17.setStyleSheet(u"QTextEdit {\n"
"    line-height: 1.5;\n"
"}\n"
"background-color: transparent;\n"
"color: rgb(154, 153, 150);\n"
"color: rgb(47, 47, 47);")
        self.label_17.setTextFormat(Qt.RichText)
        self.label_17.setAlignment(Qt.AlignJustify|Qt.AlignTop)
        self.label_17.setWordWrap(True)
        self.label_17.setIndent(2)
        self.button_3 = QPushButton(self.screen_2)
        self.button_3.setObjectName(u"button_3")
        self.button_3.setGeometry(QRect(100, 260, 300, 60))
        self.button_3.setFont(font3)
        self.button_3.setStyleSheet(u"QPushButton#button_3 {\n"
"    color: #FFFFFF; /* White text */\n"
"    background-color: #00509E; /* Dark blue background for sufficient contrast */\n"
"    border-radius: 5px; /* Optional styling */\n"
"    padding: 5px 10px; /* Optional spacing */\n"
"}\n"
"QPushButton#button_3:hover {\n"
"    background-color: #003F7F; /* Slightly darker blue on hover */\n"
"}")
        self.button_10 = QPushButton(self.screen_2)
        self.button_10.setObjectName(u"button_10")
        self.button_10.setGeometry(QRect(100, 340, 300, 60))
        self.button_10.setFont(font3)
        self.button_10.setLayoutDirection(Qt.RightToLeft)
        self.button_10.setStyleSheet(u"QPushButton {\n"
"    color: #FFFFFF; /* White text for contrast */\n"
"    background-color: #AA0000; /* Dark red background */\n"
"    border-radius: 5px; /* Consistent with the settings button */\n"
"    padding: 5px 10px; /* Same spacing as the settings button */\n"
"    border: none; /* Clean, minimal look */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #8C0000; /* Slightly darker red on hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #700000; /* Even darker red when pressed */\n"
"}")
        self.button_10.setIconSize(QSize(24, 24))
        self.label_55 = QLabel(self.screen_2)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setGeometry(QRect(60, 53, 380, 400))
        font7 = QFont()
        font7.setFamilies([u"SF Pro Display"])
        self.label_55.setFont(font7)
        self.label_55.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 20;")
        self.button_12 = QPushButton(self.screen_2)
        self.button_12.setObjectName(u"button_12")
        self.button_12.setGeometry(QRect(100, 180, 300, 60))
        self.button_12.setFont(font3)
        self.button_12.setStyleSheet(u"QPushButton#button_12{\n"
"    color: #FFFFFF; /* White text */\n"
"    background-color: #00509E; /* Dark blue background for sufficient contrast */\n"
"    border-radius: 5px; /* Optional styling */\n"
"    padding: 5px 10px; /* Optional spacing */\n"
"}\n"
"QPushButton#button_12:hover {\n"
"    background-color: #003F7F; /* Slightly darker blue on hover */\n"
"}")
        self.label_55.raise_()
        self.button_2.raise_()
        self.label_15.raise_()
        self.label_17.raise_()
        self.button_3.raise_()
        self.label_16.raise_()
        self.button_12.raise_()
        self.button_10.raise_()
        self.screen_3 = QFrame(self.centralwidget)
        self.screen_3.setObjectName(u"screen_3")
        self.screen_3.setGeometry(QRect(0, 59, 1024, 541))
        font8 = QFont()
        font8.setFamilies([u"SF Pro Display"])
        font8.setPointSize(10)
        self.screen_3.setFont(font8)
        self.screen_3.setStyleSheet(u"background-color: rgb(233, 238, 241);")
        self.screen_3.setFrameShape(QFrame.StyledPanel)
        self.screen_3.setFrameShadow(QFrame.Raised)
        self.button_4 = QPushButton(self.screen_3)
        self.button_4.setObjectName(u"button_4")
        self.button_4.setGeometry(QRect(800, 370, 170, 60))
        self.button_4.setFont(font3)
        self.button_4.setStyleSheet(u"QPushButton#button_4 {\n"
"    color: #FFFFFF; /* White text */\n"
"    background-color: #00509E; /* Dark blue background for sufficient contrast */\n"
"    border-radius: 5px; /* Optional styling */\n"
"    padding: 5px 10px; /* Optional spacing */\n"
"}\n"
"QPushButton#button_4:hover {\n"
"    background-color: #003F7F; /* Slightly darker blue on hover */\n"
"}")
        self.label_18 = QLabel(self.screen_3)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(16, 30, 211, 41))
        self.label_18.setFont(font3)
        self.label_18.setStyleSheet(u"color: #6d6d6d;")
        self.label_18.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_21 = QLabel(self.screen_3)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(136, 110, 91, 41))
        self.label_21.setFont(font3)
        self.label_21.setStyleSheet(u"color: #6d6d6d;")
        self.label_21.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_22 = QLabel(self.screen_3)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(106, 190, 121, 41))
        self.label_22.setFont(font3)
        self.label_22.setStyleSheet(u"color: #6d6d6d;")
        self.label_22.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.input_3 = QLineEdit(self.screen_3)
        self.input_3.setObjectName(u"input_3")
        self.input_3.setGeometry(QRect(234, 20, 735, 60))
        font9 = QFont()
        font9.setFamilies([u"SF Pro Display"])
        font9.setPointSize(16)
        font9.setBold(False)
        self.input_3.setFont(font9)
        self.input_3.setStyleSheet(u"QLineEdit#input_3 {\n"
"    background-color: white;\n"
"    border: 1px solid gray;\n"
"    border-radius: 4px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"/* When the user hovers over the input field */\n"
"QLineEdit#input_3:hover {\n"
"    background-color: #e0eef9;\n"
"}\n"
"\n"
"/* When the input field is clicked/focused */\n"
"QLineEdit#input_3:focus {\n"
"    background-color: #cce7ff;\n"
"    border: 1px solid #0078d7; /* Optional: Highlight border */\n"
"}")
        self.input_3.setClearButtonEnabled(True)
        self.input_6 = QLineEdit(self.screen_3)
        self.input_6.setObjectName(u"input_6")
        self.input_6.setGeometry(QRect(234, 100, 280, 60))
        self.input_6.setFont(font9)
        self.input_6.setStyleSheet(u"QLineEdit#input_6 {\n"
"    background-color: white;\n"
"    border: 1px solid gray;\n"
"    border-radius: 4px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"/* When the user hovers over the input field */\n"
"QLineEdit#input_6:hover {\n"
"    background-color: #e0eef9;\n"
"}\n"
"\n"
"/* When the input field is clicked/focused */\n"
"QLineEdit#input_6:focus {\n"
"    background-color: #cce7ff;\n"
"    border: 1px solid #0078d7; /* Optional: Highlight border */\n"
"}")
        self.input_6.setClearButtonEnabled(True)
        self.input_7 = QLineEdit(self.screen_3)
        self.input_7.setObjectName(u"input_7")
        self.input_7.setGeometry(QRect(234, 180, 280, 60))
        self.input_7.setFont(font9)
        self.input_7.setStyleSheet(u"QLineEdit#input_7 {\n"
"    background-color: white;\n"
"    border: 1px solid gray;\n"
"    border-radius: 4px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"/* When the user hovers over the input field */\n"
"QLineEdit#input_7:hover {\n"
"    background-color: #e0eef9;\n"
"}\n"
"\n"
"/* When the input field is clicked/focused */\n"
"QLineEdit#input_7:focus {\n"
"    background-color: #cce7ff;\n"
"    border: 1px solid #0078d7; /* Optional: Highlight border */\n"
"}")
        self.input_7.setClearButtonEnabled(True)
        self.label_41 = QLabel(self.screen_3)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(106, 270, 121, 41))
        self.label_41.setFont(font3)
        self.label_41.setStyleSheet(u"color: #6d6d6d;")
        self.label_41.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.input_8 = QLineEdit(self.screen_3)
        self.input_8.setObjectName(u"input_8")
        self.input_8.setGeometry(QRect(234, 260, 280, 60))
        self.input_8.setFont(font9)
        self.input_8.setStyleSheet(u"QLineEdit#input_8 {\n"
"    background-color: white;\n"
"    border: 1px solid gray;\n"
"    border-radius: 4px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"/* When the user hovers over the input field */\n"
"QLineEdit#input_8:hover {\n"
"    background-color: #e0eef9;\n"
"}\n"
"\n"
"/* When the input field is clicked/focused */\n"
"QLineEdit#input_8:focus {\n"
"    background-color: #cce7ff;\n"
"    border: 1px solid #0078d7; /* Optional: Highlight border */\n"
"}")
        self.input_8.setClearButtonEnabled(True)
        self.label_23 = QLabel(self.screen_3)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(170, 370, 551, 51))
        self.label_23.setFont(font2)
        self.label_23.setAlignment(Qt.AlignCenter)
        self.label_54 = QLabel(self.screen_3)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setGeometry(QRect(530, 190, 151, 41))
        self.label_54.setFont(font3)
        self.label_54.setStyleSheet(u"color: #6d6d6d;")
        self.label_54.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_53 = QLabel(self.screen_3)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setGeometry(QRect(530, 270, 151, 41))
        self.label_53.setFont(font3)
        self.label_53.setStyleSheet(u"color: #6d6d6d;")
        self.label_53.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_50 = QLabel(self.screen_3)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setGeometry(QRect(520, 100, 161, 60))
        self.label_50.setFont(font3)
        self.label_50.setStyleSheet(u"color: #6d6d6d;")
        self.label_50.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.input_12 = QLineEdit(self.screen_3)
        self.input_12.setObjectName(u"input_12")
        self.input_12.setGeometry(QRect(690, 100, 280, 60))
        self.input_12.setFont(font9)
        self.input_12.setStyleSheet(u"QLineEdit#input_12{\n"
"    background-color: white;\n"
"    border: 1px solid gray;\n"
"    border-radius: 4px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"/* When the user hovers over the input field */\n"
"QLineEdit#input_12:hover {\n"
"    background-color: #e0eef9;\n"
"}\n"
"\n"
"/* When the input field is clicked/focused */\n"
"QLineEdit#input_12:focus {\n"
"    background-color: #cce7ff;\n"
"    border: 1px solid #0078d7; /* Optional: Highlight border */\n"
"}")
        self.input_12.setClearButtonEnabled(True)
        self.input_13 = QLineEdit(self.screen_3)
        self.input_13.setObjectName(u"input_13")
        self.input_13.setGeometry(QRect(690, 260, 280, 60))
        self.input_13.setFont(font9)
        self.input_13.setStyleSheet(u"QLineEdit#input_13 {\n"
"    background-color: white;\n"
"    border: 1px solid gray;\n"
"    border-radius: 4px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"/* When the user hovers over the input field */\n"
"QLineEdit#input_13:hover {\n"
"    background-color: #e0eef9;\n"
"}\n"
"\n"
"/* When the input field is clicked/focused */\n"
"QLineEdit#input_13:focus {\n"
"    background-color: #cce7ff;\n"
"    border: 1px solid #0078d7; /* Optional: Highlight border */\n"
"}")
        self.input_13.setClearButtonEnabled(True)
        self.input_14 = QLineEdit(self.screen_3)
        self.input_14.setObjectName(u"input_14")
        self.input_14.setGeometry(QRect(690, 180, 280, 60))
        self.input_14.setFont(font9)
        self.input_14.setStyleSheet(u"QLineEdit#input_14 {\n"
"    background-color: white;\n"
"    border: 1px solid gray;\n"
"    border-radius: 4px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"/* When the user hovers over the input field */\n"
"QLineEdit#input_14:hover {\n"
"    background-color: #e0eef9;\n"
"}\n"
"\n"
"/* When the input field is clicked/focused */\n"
"QLineEdit#input_14:focus {\n"
"    background-color: #cce7ff;\n"
"    border: 1px solid #0078d7; /* Optional: Highlight border */\n"
"}")
        self.input_14.setClearButtonEnabled(True)
        self.screen_4 = QFrame(self.centralwidget)
        self.screen_4.setObjectName(u"screen_4")
        self.screen_4.setGeometry(QRect(0, 59, 1024, 530))
        self.screen_4.setFont(font8)
        self.screen_4.setStyleSheet(u"background-color: rgb(233, 238, 241);")
        self.screen_4.setFrameShape(QFrame.NoFrame)
        self.screen_4.setFrameShadow(QFrame.Plain)
        self.button_5 = QPushButton(self.screen_4)
        self.button_5.setObjectName(u"button_5")
        self.button_5.setGeometry(QRect(810, 420, 170, 60))
        self.button_5.setFont(font3)
        self.button_5.setStyleSheet(u"QPushButton#button_5 {\n"
"    color: #FFFFFF; /* White text */\n"
"    background-color: #00509E; /* Dark blue background for sufficient contrast */\n"
"    border-radius: 5px; /* Optional styling */\n"
"    padding: 5px 10px; /* Optional spacing */\n"
"}\n"
"QPushButton#button_5:hover {\n"
"    background-color: #003F7F; /* Slightly darker blue on hover */\n"
"}")
        self.label_24 = QLabel(self.screen_4)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(400, 40, 211, 31))
        font10 = QFont()
        font10.setFamilies([u"SF Pro Display"])
        font10.setPointSize(14)
        font10.setBold(True)
        self.label_24.setFont(font10)
        self.label_24.setStyleSheet(u"color: #6d6d6d;")
        self.label_24.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_27 = QLabel(self.screen_4)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(470, 90, 141, 31))
        self.label_27.setFont(font10)
        self.label_27.setStyleSheet(u"color: rgb(109, 109, 109);")
        self.label_27.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_28 = QLabel(self.screen_4)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(469, 140, 141, 31))
        self.label_28.setFont(font10)
        self.label_28.setStyleSheet(u"color: rgb(109, 109, 109);")
        self.label_28.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_29 = QLabel(self.screen_4)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(640, 40, 340, 35))
        font11 = QFont()
        font11.setFamilies([u"SF Pro Display"])
        font11.setPointSize(12)
        self.label_29.setFont(font11)
        self.label_29.setStyleSheet(u"color: #2f2f2f;\n"
"border:1px solid #bebebe;\n"
"border-radius: 5px;\n"
"padding-left: 5px;\n"
"background: \"white\";")
        self.label_29.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_32 = QLabel(self.screen_4)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(640, 90, 340, 35))
        self.label_32.setFont(font11)
        self.label_32.setStyleSheet(u"color: #2f2f2f;\n"
"border:1px solid #bebebe;\n"
"border-radius: 5px;\n"
"padding-left: 5px;\n"
"background: \"white\";")
        self.label_32.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.button_6 = QPushButton(self.screen_4)
        self.button_6.setObjectName(u"button_6")
        self.button_6.setGeometry(QRect(40, 30, 350, 60))
        self.button_6.setFont(font3)
        self.button_6.setLayoutDirection(Qt.RightToLeft)
        self.button_6.setStyleSheet(u"QPushButton{\n"
"	background-color: qlineargradient(spread:pad, x1:0.47, y1:0, x2:0.5, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(239, 239, 239, 255));\n"
"color:  #308DC2;\n"
"border:1px solid #bebebe;\n"
"text-align: left;\n"
"padding-left: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: #bebebe;\n"
"}\n"
"QPushButton {\n"
"    padding-left: 10px; /* Adds padding on the left of the text */\n"
"    padding-right: 10px; /* Adds padding on the right of the icon */\n"
"    text-align: left; /* Aligns text to the left for better spacing */\n"
"    icon-size: 16px 16px; /* Adjusts icon size if needed */\n"
"}\n"
"\n"
"QPushButton::menu-indicator {\n"
"    subcontrol-origin: padding; /* Ensures proper spacing for dropdown icon */\n"
"    subcontrol-position: right center; /* Aligns dropdown icon to the right */\n"
"    padding-right: 10px; /* Adds space to the right of the dropdown icon */\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"icons/angle-down-solid.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_6.setIcon(icon1)
        self.button_6.setAutoDefault(False)
        self.button_6.setFlat(False)
        self.label_33 = QLabel(self.screen_4)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(640, 140, 340, 35))
        self.label_33.setFont(font11)
        self.label_33.setStyleSheet(u"color: #2f2f2f;\n"
"border:1px solid #bebebe;\n"
"border-radius: 5px;\n"
"padding-left: 5px;\n"
"background: \"white\";")
        self.label_33.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.configlist = QListWidget(self.screen_4)
        font12 = QFont()
        font12.setPointSize(12)
        __qlistwidgetitem = QListWidgetItem(self.configlist)
        __qlistwidgetitem.setFont(font12);
        self.configlist.setObjectName(u"configlist")
        self.configlist.setGeometry(QRect(40, 89, 351, 391))
        self.configlist.setFont(font3)
        self.configlist.setStyleSheet(u"QListWidget {\n"
"    background-color:transparent;\n"
"   border: none;\n"
"   outline: none;\n"
"   \n"
"}\n"
"\n"
"QListWidget::item {\n"
"    height: 60px;\n"
"   background-color: white; \n"
"    border: 1px solid #bebebe;\n"
"    padding-left: 5px;\n"
"   \n"
"}\n"
"QListWidget::item:hover {\n"
"    height: 60px;\n"
"   background-color:#e0eef9; \n"
"    border: 1px solid #bebebe;\n"
"    padding-left: 5px;\n"
"    outline: none; /* Remove focus */\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    background-color: #00509E;\n"
"  /* color: #ffffff;*/\n"
"   /* border: 1px solid rgb(0, 74, 74);\n"
"    outline: none; /* Remove selection focus */\n"
"}\n"
"")
        self.configlist.setFrameShadow(QFrame.Plain)
        self.configlist.setResizeMode(QListView.Adjust)
        self.configlist.setBatchSize(10)
        self.button_11 = QPushButton(self.screen_4)
        self.button_11.setObjectName(u"button_11")
        self.button_11.setGeometry(QRect(810, 420, 170, 60))
        self.button_11.setFont(font3)
        self.button_11.setStyleSheet(u"QPushButton#button_11 {\n"
"    color: #FFFFFF; /* White text for contrast */\n"
"    background-color: #AA0000; /* Dark red background */\n"
"    border-radius: 5px; /* Consistent with the settings button */\n"
"    padding: 5px 10px; /* Same spacing as the settings button */\n"
"    border: none; /* Clean, minimal look */\n"
"}\n"
"\n"
"QPushButton#button_11:hover {\n"
"    background-color: #8C0000; /* Slightly darker red on hover */\n"
"}\n"
"\n"
"QPushButton#button_11:pressed {\n"
"    background-color: #700000; /* Even darker red when pressed */\n"
"}")
        self.label_42 = QLabel(self.screen_4)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(640, 190, 340, 35))
        self.label_42.setFont(font11)
        self.label_42.setStyleSheet(u"color: #2f2f2f;\n"
"border:1px solid #bebebe;\n"
"border-radius: 5px;\n"
"padding-left: 5px;\n"
"background: \"white\";")
        self.label_42.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_43 = QLabel(self.screen_4)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(470, 190, 141, 31))
        self.label_43.setFont(font10)
        self.label_43.setStyleSheet(u"color: rgb(109, 109, 109);")
        self.label_43.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_60 = QLabel(self.screen_4)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setGeometry(QRect(470, 290, 141, 31))
        self.label_60.setFont(font10)
        self.label_60.setStyleSheet(u"color: rgb(109, 109, 109);")
        self.label_60.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_61 = QLabel(self.screen_4)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setGeometry(QRect(640, 240, 340, 35))
        self.label_61.setFont(font11)
        self.label_61.setStyleSheet(u"color: #2f2f2f;\n"
"border:1px solid #bebebe;\n"
"border-radius: 5px;\n"
"padding-left: 5px;\n"
"background: \"white\";")
        self.label_61.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_62 = QLabel(self.screen_4)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setGeometry(QRect(440, 340, 171, 31))
        self.label_62.setFont(font10)
        self.label_62.setStyleSheet(u"color: rgb(109, 109, 109);")
        self.label_62.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_77 = QLabel(self.screen_4)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setGeometry(QRect(640, 290, 340, 35))
        self.label_77.setFont(font11)
        self.label_77.setStyleSheet(u"color: #2f2f2f;\n"
"border:1px solid #bebebe;\n"
"border-radius: 5px;\n"
"padding-left: 5px;\n"
"background: \"white\";")
        self.label_77.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_78 = QLabel(self.screen_4)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setGeometry(QRect(470, 240, 141, 31))
        self.label_78.setFont(font10)
        self.label_78.setStyleSheet(u"color: rgb(109, 109, 109);")
        self.label_78.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_79 = QLabel(self.screen_4)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setGeometry(QRect(640, 340, 340, 35))
        self.label_79.setFont(font11)
        self.label_79.setStyleSheet(u"color: #2f2f2f;\n"
"border:1px solid #bebebe;\n"
"border-radius: 5px;\n"
"padding-left: 5px;\n"
"background: \"white\";")
        self.label_79.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.button_5.raise_()
        self.label_24.raise_()
        self.label_27.raise_()
        self.label_28.raise_()
        self.label_29.raise_()
        self.label_32.raise_()
        self.button_6.raise_()
        self.label_33.raise_()
        self.button_11.raise_()
        self.label_42.raise_()
        self.label_43.raise_()
        self.label_60.raise_()
        self.label_61.raise_()
        self.label_62.raise_()
        self.label_77.raise_()
        self.label_78.raise_()
        self.configlist.raise_()
        self.label_79.raise_()
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setEnabled(True)
        self.comboBox.setGeometry(QRect(510, 10, 180, 40))
        font13 = QFont()
        font13.setFamilies([u"SF Pro Display"])
        font13.setPointSize(13)
        self.comboBox.setFont(font13)
        self.comboBox.setFocusPolicy(Qt.NoFocus)
        self.comboBox.setStyleSheet(u"QPushButton{\n"
"	background-color: qlineargradient(spread:pad, x1:0.47, y1:0, x2:0.5, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(239, 239, 239, 255));\n"
"color: #3BADED;\n"
"border:1px solid #bebebe;\n"
"text-align: left;\n"
"padding-left: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: #bebebe;\n"
"}\n"
"QPushButton {\n"
"    padding-left: 10px; /* Adds padding on the left of the text */\n"
"    padding-right: 10px; /* Adds padding on the right of the icon */\n"
"    text-align: left; /* Aligns text to the left for better spacing */\n"
"    icon-size: 16px 16px; /* Adjusts icon size if needed */\n"
"}\n"
"\n"
"QPushButton::menu-indicator {\n"
"    subcontrol-origin: padding; /* Ensures proper spacing for dropdown icon */\n"
"    subcontrol-position: right center; /* Aligns dropdown icon to the right */\n"
"    padding-right: 10px; /* Adds space to the right of the dropdown icon */\n"
"}")
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(780, 40, 241, 16))
        self.label_9.setFont(font7)
        self.label_9.setStyleSheet(u"color:rgb(255, 0, 0);")
        self.label_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_9.setWordWrap(True)
        self.comboBox_2 = QComboBox(self.centralwidget)
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(780, 10, 180, 40))
        font14 = QFont()
        font14.setFamilies([u"SF Pro Display"])
        font14.setPointSize(13)
        font14.setKerning(True)
        self.comboBox_2.setFont(font14)
        self.comboBox_2.setFocusPolicy(Qt.NoFocus)
        self.comboBox_2.setStyleSheet(u"QPushButton{\n"
"	background-color: qlineargradient(spread:pad, x1:0.47, y1:0, x2:0.5, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(239, 239, 239, 255));\n"
"color: #3BADED;\n"
"border:1px solid #bebebe;\n"
"text-align: left;\n"
"padding-left: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: #bebebe;\n"
"}\n"
"QPushButton {\n"
"    padding-left: 10px; /* Adds padding on the left of the text */\n"
"    padding-right: 10px; /* Adds padding on the right of the icon */\n"
"    text-align: left; /* Aligns text to the left for better spacing */\n"
"    icon-size: 16px 16px; /* Adjusts icon size if needed */\n"
"}\n"
"\n"
"QPushButton::menu-indicator {\n"
"    subcontrol-origin: padding; /* Ensures proper spacing for dropdown icon */\n"
"    subcontrol-position: right center; /* Aligns dropdown icon to the right */\n"
"    padding-right: 10px; /* Adds space to the right of the dropdown icon */\n"
"}")
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(430, 10, 71, 41))
        self.label_10.setFont(font10)
        self.label_10.setAlignment(Qt.AlignCenter)
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(710, 10, 71, 41))
        self.label_11.setFont(font10)
        self.label_11.setAlignment(Qt.AlignCenter)
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(510, 40, 221, 21))
        self.label_12.setFont(font7)
        self.label_12.setStyleSheet(u"color:rgb(255, 0, 0);")
        self.label_12.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.screen_6 = QFrame(self.centralwidget)
        self.screen_6.setObjectName(u"screen_6")
        self.screen_6.setGeometry(QRect(-7, 60, 1051, 531))
        self.screen_6.setFont(font7)
        self.screen_6.setStyleSheet(u"background-color:rgb(255, 255, 255);")
        self.screen_6.setFrameShape(QFrame.NoFrame)
        self.screen_6.setFrameShadow(QFrame.Plain)
        self.label_48 = QLabel(self.screen_6)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setGeometry(QRect(550, 350, 51, 60))
        self.label_48.setFont(font10)
        self.label_48.setStyleSheet(u"background:none;\n"
"color:black;")
        self.label_48.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_52 = QLabel(self.screen_6)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setGeometry(QRect(610, 350, 41, 61))
        font15 = QFont()
        font15.setFamilies([u"SF Pro Display"])
        font15.setPointSize(14)
        font15.setBold(True)
        font15.setKerning(True)
        self.label_52.setFont(font15)
        self.label_52.setStyleSheet(u"background:none; color:#9f9f9f;")
        self.label_52.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_39 = QLabel(self.screen_6)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(410, 350, 241, 61))
        self.label_39.setStyleSheet(u"background-color:white;\n"
"border-radius:20px;\n"
"")
        self.label_56 = QLabel(self.screen_6)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setGeometry(QRect(420, 350, 121, 61))
        self.label_56.setFont(font10)
        self.label_56.setStyleSheet(u"background:none;\n"
"color:#9f9f9f;\n"
"")
        self.label_56.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_58 = QLabel(self.screen_6)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setGeometry(QRect(160, 10, 721, 441))
        self.label_58.setAutoFillBackground(False)
        self.label_58.setStyleSheet(u"background-color: rgb(233, 238, 241);\n"
"border-radius:50;")
        self.label_58.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.button_26 = QPushButton(self.screen_6)
        self.button_26.setObjectName(u"button_26")
        self.button_26.setGeometry(QRect(580, 80, 121, 101))
        font16 = QFont()
        font16.setFamilies([u"SF Pro Display"])
        font16.setPointSize(13)
        font16.setBold(True)
        self.button_26.setFont(font16)
        self.button_26.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(255, 120, 0);\n"
"color: rgb(255, 255, 255);\n"
"border:none;\n"
"border-radius:10;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgb(198, 70, 0);\n"
"}\n"
"")
        self.button_27 = QPushButton(self.screen_6)
        self.button_27.setObjectName(u"button_27")
        self.button_27.setGeometry(QRect(480, 220, 111, 91))
        self.button_27.setFont(font16)
        self.button_27.setStyleSheet(u"QPushButton{\n"
"color: rgb(255, 255, 255);\n"
" border:none;\n"
" border-radius:50;\n"
"background-color:rgb(200, 200, 200);\n"
"}\n"
"\n"
"")
        self.button_28 = QPushButton(self.screen_6)
        self.button_28.setObjectName(u"button_28")
        self.button_28.setGeometry(QRect(370, 80, 121, 101))
        self.button_28.setFont(font16)
        self.button_28.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(0, 183, 1);\n"
"color: rgb(255, 255, 255);\n"
"border:none;\n"
"border-radius:10;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgb(0, 116, 1)\n"
"}\n"
"")
        self.label_69 = QLabel(self.screen_6)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setGeometry(QRect(320, 40, 101, 21))
        self.label_69.setFont(font10)
        self.label_69.setAutoFillBackground(False)
        self.label_69.setStyleSheet(u"background-color:transparent;")
        self.label_69.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_71 = QLabel(self.screen_6)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setGeometry(QRect(330, 200, 91, 20))
        self.label_71.setFont(font10)
        self.label_71.setStyleSheet(u"background-color:transparent;")
        self.label_71.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_58.raise_()
        self.label_39.raise_()
        self.label_52.raise_()
        self.button_26.raise_()
        self.button_27.raise_()
        self.button_28.raise_()
        self.label_69.raise_()
        self.label_71.raise_()
        self.label_56.raise_()
        self.label_48.raise_()
        self.button_A = QPushButton(self.centralwidget)
        self.button_A.setObjectName(u"button_A")
        self.button_A.setGeometry(QRect(9, 10, 41, 40))
        font17 = QFont()
        font17.setFamilies([u"SF Pro Display"])
        font17.setBold(True)
        self.button_A.setFont(font17)
        self.button_A.setStyleSheet(u"background-color: transparent;\n"
"border:none;")
        self.screen_1 = QFrame(self.centralwidget)
        self.screen_1.setObjectName(u"screen_1")
        self.screen_1.setGeometry(QRect(-4, 59, 1031, 560))
        self.screen_1.setFont(font8)
        self.screen_1.setStyleSheet(u"background-color: rgb(233, 238, 241);")
        self.screen_1.setFrameShape(QFrame.StyledPanel)
        self.screen_1.setFrameShadow(QFrame.Raised)
        self.label_47 = QLabel(self.screen_1)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setGeometry(QRect(468, 118, 361, 71))
        self.label_47.setFont(font4)
        self.label_47.setStyleSheet(u"background-color: transparent;\n"
"color: rgb(154, 153, 150);\n"
"color: rgb(47, 47, 47);")
        self.label_49 = QLabel(self.screen_1)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setGeometry(QRect(470, 195, 421, 41))
        self.label_49.setFont(font5)
        self.label_49.setStyleSheet(u"background-color: transparent;\n"
"color: #308DC2;")
        self.label_49.setTextFormat(Qt.RichText)
        self.label_51 = QLabel(self.screen_1)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setGeometry(QRect(470, 245, 511, 141))
        self.label_51.setFont(font6)
        self.label_51.setLayoutDirection(Qt.RightToLeft)
        self.label_51.setStyleSheet(u"QTextEdit {\n"
"    line-height: 1.5;\n"
"    text-align: justify;\n"
"}\n"
"background-color: transparent;\n"
"color: rgb(154, 153, 150);\n"
"color: rgb(47, 47, 47);")
        self.label_51.setTextFormat(Qt.AutoText)
        self.label_51.setAlignment(Qt.AlignJustify|Qt.AlignTop)
        self.label_51.setWordWrap(True)
        self.label_51.setIndent(2)
        self.label_57 = QLabel(self.screen_1)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setGeometry(QRect(53, 49, 380, 400))
        self.label_57.setFont(font7)
        self.label_57.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 20;")
        self.button_1 = QPushButton(self.screen_1)
        self.button_1.setObjectName(u"button_1")
        self.button_1.setGeometry(QRect(160, 330, 150, 60))
        self.button_1.setFont(font3)
        self.button_1.setLayoutDirection(Qt.RightToLeft)
        self.button_1.setStyleSheet(u"QPushButton#button_1 {\n"
"    color: #FFFFFF; /* White text */\n"
"    background-color: #00509E; /* Dark blue background for sufficient contrast */\n"
"    border-radius: 5px; /* Optional styling */\n"
"    padding: 5px 10px; /* Optional spacing */\n"
"}\n"
"QPushButton#button_1:hover {\n"
"    background-color: #003F7F; /* Slightly darker blue on hover */\n"
"}")
        self.button_1.setIconSize(QSize(24, 24))
        self.button_1.setAutoRepeat(False)
        self.button_1.setAutoDefault(False)
        self.button_1.setFlat(False)
        self.label_1 = QLabel(self.screen_1)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setGeometry(QRect(94, 95, 141, 30))
        self.label_1.setFont(font3)
        self.label_1.setStyleSheet(u"background-color: white;")
        self.label_2 = QLabel(self.screen_1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(94, 209, 131, 30))
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u"background-color:white;")
        self.input_1 = QLineEdit(self.screen_1)
        self.input_1.setObjectName(u"input_1")
        self.input_1.setGeometry(QRect(94, 130, 300, 60))
        font18 = QFont()
        font18.setFamilies([u"SF Pro Display"])
        font18.setPointSize(16)
        self.input_1.setFont(font18)
        self.input_1.setStyleSheet(u"QLineEdit#input_1 {\n"
"    background-color: white;\n"
"    border: 1px solid gray;\n"
"    border-radius: 4px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"/* When the user hovers over the input field */\n"
"QLineEdit#input_1:hover {\n"
"    background-color: #e0eef9;\n"
"}\n"
"\n"
"/* Ensure the field highlights when clicked */\n"
"QLineEdit#input_1:focus {\n"
"    background-color: #cce7ff;\n"
"    border: 1px solid #0078d7;\n"
"}\n"
"")
        self.input_1.setClearButtonEnabled(True)
        self.input_2 = QLineEdit(self.screen_1)
        self.input_2.setObjectName(u"input_2")
        self.input_2.setGeometry(QRect(94, 243, 300, 60))
        self.input_2.setFont(font18)
        self.input_2.setStyleSheet(u"QLineEdit#input_2 {\n"
"    background-color: white;\n"
"    border: 1px solid gray;\n"
"    border-radius: 4px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"/* When the user hovers over the input field */\n"
"QLineEdit#input_2:hover {\n"
"    background-color: #e0eef9;\n"
"}\n"
"\n"
"/* When the input field is clicked/focused */\n"
"QLineEdit#input_2:focus {\n"
"    background-color: #cce7ff;\n"
"    border: 1px solid #0078d7; /* Optional: Highlight border */\n"
"}")
        self.input_2.setEchoMode(QLineEdit.Password)
        self.input_2.setClearButtonEnabled(False)
        self.label_6 = QLabel(self.screen_1)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(110, 410, 250, 20))
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"background-color: white;\n"
"color: rgb(255, 255, 255);")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_6.setTextInteractionFlags(Qt.LinksAccessibleByMouse)
        self.label_3 = QLabel(self.screen_1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(680, 430, 341, 20))
        font19 = QFont()
        font19.setFamilies([u"SF Pro Display"])
        font19.setPointSize(12)
        font19.setBold(False)
        self.label_3.setFont(font19)
        self.label_3.setStyleSheet(u"color:#505050;")
        self.button_HS = QPushButton(self.screen_1)
        self.button_HS.setObjectName(u"button_HS")
        self.button_HS.setGeometry(QRect(330, 248, 61, 51))
        self.button_HS.setFont(font11)
        self.button_HS.setStyleSheet(u"background-color: transparent;")
        icon2 = QIcon()
        icon2.addFile(u"icons/eye-slash-regular.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_HS.setIcon(icon2)
        self.button_HS.setIconSize(QSize(32, 32))
        self.button_HS.setCheckable(False)
        self.label_47.raise_()
        self.label_49.raise_()
        self.label_57.raise_()
        self.button_1.raise_()
        self.label_1.raise_()
        self.label_2.raise_()
        self.input_2.raise_()
        self.label_6.raise_()
        self.label_3.raise_()
        self.button_HS.raise_()
        self.label_51.raise_()
        self.input_1.raise_()
        self.screen_5 = QFrame(self.centralwidget)
        self.screen_5.setObjectName(u"screen_5")
        self.screen_5.setGeometry(QRect(0, 60, 1031, 530))
        self.screen_5.setFont(font2)
        self.screen_5.setToolTipDuration(8)
        self.screen_5.setStyleSheet(u"background-color: rgb(233, 238, 241);")
        self.screen_5.setFrameShape(QFrame.NoFrame)
        self.screen_5.setFrameShadow(QFrame.Plain)
        self.button_7 = QPushButton(self.screen_5)
        self.button_7.setObjectName(u"button_7")
        self.button_7.setGeometry(QRect(230, 400, 175, 70))
        font20 = QFont()
        self.button_7.setFont(font20)
        self.button_7.setToolTipDuration(8)
        self.button_7.setStyleSheet(u"QPushButton {\n"
"    background-color: #28a745; /* Standard Green */\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"    padding: 10px;\n"
"    font-size: 20px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #218838; /* Darker green for hover */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #218838; /* Even darker green for pressed */\n"
"    border-color:black\n"
"\n"
"}\n"
"QPushButton:checked {\n"
"    background-color: #218838; /* Darker Green for checked (pressed) */\n"
"    border-color: black; /* Optional border for visual feedback */\n"
"}\n"
"QPushButton:disabled {\n"
"                background-color: #A5D6A7;  /* Lighter green for disabled state */\n"
"                color: #FFFFFF;\n"
"            }")
        self.button_8 = QPushButton(self.screen_5)
        self.button_8.setObjectName(u"button_8")
        self.button_8.setGeometry(QRect(423, 400, 175, 70))
        self.button_8.setFont(font20)
        self.button_8.setToolTipDuration(8)
        self.button_8.setStyleSheet(u"QPushButton{\n"
"	\n"
"    background-color:  #ffc107; /* Standard Orange */\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"    padding: 10px;\n"
"    font-size: 20px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #e0a800; /* Darker orange for hover */\n"
"}\n"
"QPushButton:checked {\n"
"                background-color: #e0a800;\n"
"            }\n"
"\n"
"\n"
"")
        self.button_9 = QPushButton(self.screen_5)
        self.button_9.setObjectName(u"button_9")
        self.button_9.setGeometry(QRect(615, 400, 175, 70))
        self.button_9.setFont(font20)
        self.button_9.setToolTipDuration(8)
        self.button_9.setStyleSheet(u"QPushButton {\n"
"    background-color: #dc3545; /* Standard Red */\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"    padding: 10px;\n"
"    font-size: 20px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #c82333; /* Darker red for hover */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #c82333; /* Even darker red for pressed */\n"
"}\n"
" QPushButton:checked {\n"
"                background-color: #c82333;\n"
"            }")
        self.feed_graph = QFrame(self.screen_5)
        self.feed_graph.setObjectName(u"feed_graph")
        self.feed_graph.setGeometry(QRect(229, 10, 561, 361))
        self.feed_graph.setFont(font7)
        self.feed_graph.setStyleSheet(u"background-color: rgb(246, 245, 244);\n"
"border-radius:10px;\n"
"color: rgb(192, 28, 40);")
        self.feed_graph.setFrameShape(QFrame.StyledPanel)
        self.feed_graph.setFrameShadow(QFrame.Raised)
        self.label_35 = QLabel(self.screen_5)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(810, 80, 61, 21))
        self.label_35.setFont(font10)
        self.label_35.setStyleSheet(u"background:none;\n"
"color: #9f9f9f;")
        self.label_35.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_37 = QLabel(self.screen_5)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(890, 70, 71, 41))
        self.label_37.setFont(font3)
        self.label_37.setStyleSheet(u"background:none;\n"
"color:black;\n"
"")
        self.label_37.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_13 = QLabel(self.screen_5)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(800, 70, 200, 41))
        self.label_13.setFont(font7)
        self.label_13.setStyleSheet(u"background-color:rgb(250, 250, 250);\n"
"border-radius:10px;")
        self.label_19 = QLabel(self.screen_5)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(800, 220, 200, 41))
        self.label_19.setFont(font7)
        self.label_19.setStyleSheet(u"background-color:rgb(250, 250, 250);\n"
"border-radius:10px;")
        self.label_7 = QLabel(self.screen_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(800, 220, 81, 41))
        self.label_7.setFont(font10)
        self.label_7.setStyleSheet(u"background:none;\n"
"color: #9f9f9f;")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_20 = QLabel(self.screen_5)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(890, 220, 101, 41))
        self.label_20.setFont(font9)
        self.label_20.setStyleSheet(u"background-color: transparent;\n"
"color:black;\n"
"")
        self.label_20.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_25 = QLabel(self.screen_5)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(890, 120, 81, 41))
        self.label_25.setFont(font3)
        self.label_25.setStyleSheet(u"background:none;\n"
"color:black;")
        self.label_25.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_30 = QLabel(self.screen_5)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(800, 120, 91, 41))
        self.label_30.setFont(font10)
        self.label_30.setStyleSheet(u"background:none;\n"
"color: #9f9f9f;")
        self.label_30.setAlignment(Qt.AlignCenter)
        self.label_31 = QLabel(self.screen_5)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(810, 170, 71, 41))
        self.label_31.setFont(font10)
        self.label_31.setStyleSheet(u"background:none;\n"
"color: #9f9f9f;")
        self.label_31.setAlignment(Qt.AlignCenter)
        self.label_36 = QLabel(self.screen_5)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(800, 170, 200, 41))
        self.label_36.setFont(font7)
        self.label_36.setStyleSheet(u"background-color:rgb(250, 250, 250);\n"
"border-radius:10px;")
        self.label_40 = QLabel(self.screen_5)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(972, 80, 20, 21))
        font21 = QFont()
        font21.setFamilies([u"SF Pro Display"])
        font21.setPointSize(14)
        font21.setBold(False)
        self.label_40.setFont(font21)
        self.label_40.setStyleSheet(u"background:none;\n"
"color: #9f9f9f;")
        self.label_40.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_44 = QLabel(self.screen_5)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(972, 120, 20, 41))
        self.label_44.setFont(font21)
        self.label_44.setStyleSheet(u"background:none;\n"
"color: #9f9f9f;")
        self.label_44.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_46 = QLabel(self.screen_5)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(971, 170, 20, 41))
        self.label_46.setFont(font21)
        self.label_46.setStyleSheet(u"background:none;\n"
"color: #9f9f9f;")
        self.label_46.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_26 = QLabel(self.screen_5)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(890, 170, 81, 41))
        self.label_26.setFont(font3)
        self.label_26.setStyleSheet(u"background:none;\n"
"color:black;")
        self.label_26.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_14 = QLabel(self.screen_5)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(800, 120, 200, 41))
        self.label_14.setFont(font7)
        self.label_14.setStyleSheet(u"background-color:rgb(250, 250, 250);\n"
"border-radius:10px;")
        self.label_34 = QLabel(self.screen_5)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(800, 271, 200, 101))
        self.label_34.setFont(font7)
        self.label_34.setStyleSheet(u"background-color:rgb(250, 250, 250);\n"
"border-radius:10px;")
        self.label_8 = QLabel(self.screen_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(800, 271, 201, 41))
        self.label_8.setFont(font10)
        self.label_8.setStyleSheet(u"background:none;\n"
"color: rgb(91, 91, 91);")
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_45 = QLabel(self.screen_5)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(820, 310, 161, 31))
        font22 = QFont()
        font22.setFamilies([u"SF Pro Display"])
        font22.setPointSize(18)
        font22.setBold(True)
        self.label_45.setFont(font22)
        self.label_45.setStyleSheet(u"background:none;\n"
"color:black;")
        self.label_45.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label = QLabel(self.screen_5)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(799, 30, 211, 31))
        self.label.setFont(font10)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setStyleSheet(u"color: #2f2f2f;")
        self.label.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_63 = QLabel(self.screen_5)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setGeometry(QRect(10, 30, 201, 31))
        self.label_63.setFont(font10)
        self.label_63.setStyleSheet(u"color: rgb(47, 47, 47);")
        self.label_63.setAlignment(Qt.AlignCenter)
        self.label_64 = QLabel(self.screen_5)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setGeometry(QRect(30, 70, 61, 41))
        self.label_64.setFont(font10)
        self.label_64.setStyleSheet(u"background:none;\n"
"color: #9f9f9f;")
        self.label_65 = QLabel(self.screen_5)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setGeometry(QRect(110, 70, 121, 41))
        self.label_65.setFont(font10)
        self.label_66 = QLabel(self.screen_5)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setGeometry(QRect(40, 120, 51, 21))
        self.label_66.setFont(font10)
        self.label_66.setStyleSheet(u"background:none;\n"
"color: #9f9f9f;")
        self.label_67 = QLabel(self.screen_5)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setGeometry(QRect(110, 120, 71, 21))
        self.label_67.setFont(font10)
        self.label_67.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_68 = QLabel(self.screen_5)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setGeometry(QRect(20, 150, 91, 41))
        self.label_68.setFont(font10)
        self.label_68.setStyleSheet(u"background:none;\n"
"color: #9f9f9f;")
        self.label_70 = QLabel(self.screen_5)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setGeometry(QRect(110, 150, 60, 41))
        self.label_70.setFont(font10)
        self.label_70.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_72 = QLabel(self.screen_5)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setGeometry(QRect(110, 190, 60, 41))
        self.label_72.setFont(font10)
        self.label_72.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_73 = QLabel(self.screen_5)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setGeometry(QRect(20, 200, 91, 21))
        self.label_73.setFont(font10)
        self.label_73.setStyleSheet(u"background:none;\n"
"color: #9f9f9f;")
        self.label_74 = QLabel(self.screen_5)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setGeometry(QRect(155, 200, 61, 21))
        self.label_74.setFont(font10)
        self.label_74.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_75 = QLabel(self.screen_5)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setGeometry(QRect(155, 160, 61, 21))
        self.label_75.setFont(font10)
        self.label_75.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_76 = QLabel(self.screen_5)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setGeometry(QRect(165, 120, 51, 21))
        self.label_76.setFont(font10)
        self.label_76.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_59 = QLabel(self.screen_5)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setGeometry(QRect(844, 345, 101, 31))
        self.label_59.setFont(font11)
        self.label_59.setStyleSheet(u"background:none;\n"
"color: #9f9f9f;")
        self.label_59.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_80 = QLabel(self.screen_5)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setGeometry(QRect(160, 280, 61, 21))
        self.label_80.setFont(font10)
        self.label_80.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_81 = QLabel(self.screen_5)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setGeometry(QRect(110, 230, 60, 41))
        self.label_81.setFont(font10)
        self.label_81.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_82 = QLabel(self.screen_5)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setGeometry(QRect(30, 280, 71, 21))
        self.label_82.setFont(font10)
        self.label_82.setStyleSheet(u"background:none;\n"
"color: #9f9f9f;")
        self.label_83 = QLabel(self.screen_5)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setGeometry(QRect(170, 320, 51, 21))
        self.label_83.setFont(font10)
        self.label_83.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_84 = QLabel(self.screen_5)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setGeometry(QRect(110, 270, 60, 41))
        self.label_84.setFont(font10)
        self.label_84.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_85 = QLabel(self.screen_5)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setGeometry(QRect(40, 320, 61, 21))
        self.label_85.setFont(font10)
        self.label_85.setStyleSheet(u"background:none;\n"
"color: #9f9f9f;")
        self.label_86 = QLabel(self.screen_5)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setGeometry(QRect(160, 240, 61, 21))
        self.label_86.setFont(font10)
        self.label_86.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_87 = QLabel(self.screen_5)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setGeometry(QRect(110, 310, 60, 41))
        self.label_87.setFont(font10)
        self.label_87.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_88 = QLabel(self.screen_5)
        self.label_88.setObjectName(u"label_88")
        self.label_88.setGeometry(QRect(10, 240, 91, 21))
        self.label_88.setFont(font10)
        self.label_88.setStyleSheet(u"background:none;\n"
"color: #9f9f9f;")
        self.label_14.raise_()
        self.label_36.raise_()
        self.label_13.raise_()
        self.button_7.raise_()
        self.button_8.raise_()
        self.button_9.raise_()
        self.label_35.raise_()
        self.label_37.raise_()
        self.label_19.raise_()
        self.label_7.raise_()
        self.label_20.raise_()
        self.label_30.raise_()
        self.label_31.raise_()
        self.feed_graph.raise_()
        self.label_40.raise_()
        self.label_44.raise_()
        self.label_46.raise_()
        self.label_26.raise_()
        self.label_25.raise_()
        self.label_34.raise_()
        self.label_8.raise_()
        self.label_45.raise_()
        self.label.raise_()
        self.label_63.raise_()
        self.label_64.raise_()
        self.label_65.raise_()
        self.label_66.raise_()
        self.label_67.raise_()
        self.label_68.raise_()
        self.label_70.raise_()
        self.label_72.raise_()
        self.label_73.raise_()
        self.label_74.raise_()
        self.label_75.raise_()
        self.label_76.raise_()
        self.label_59.raise_()
        self.label_80.raise_()
        self.label_81.raise_()
        self.label_82.raise_()
        self.label_83.raise_()
        self.label_84.raise_()
        self.label_85.raise_()
        self.label_86.raise_()
        self.label_87.raise_()
        self.label_88.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.comboBox.raise_()
        self.comboBox_2.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.button_A.raise_()
        self.label_9.raise_()
        self.label_A.raise_()
        self.screen_6.raise_()
        self.screen_2.raise_()
        self.screen_3.raise_()
        self.screen_5.raise_()
        self.screen_4.raise_()
        self.screen_1.raise_()

        self.retranslateUi(MainWindow)

        self.button_6.setDefault(False)
        self.configlist.setCurrentRow(-1)
        self.comboBox.setCurrentIndex(0)
        self.comboBox_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Electro Polishing Machine ", None))
        self.label_A.setText("")
        self.button_2.setText(QCoreApplication.translate("MainWindow", u"Load Configuration", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"EPM-01", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Electro Polishing Machine", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Electro Polishing Machine is designed to enhance the surface finish of stents using electrochemical techniques. This process ensures superior smoothness and precision, essential for medical-grade applications.", None))
        self.button_3.setText(QCoreApplication.translate("MainWindow", u"Create Configuration", None))
        self.button_10.setText(QCoreApplication.translate("MainWindow", u"Delete Configuration", None))
        self.label_55.setText("")
        self.button_12.setText(QCoreApplication.translate("MainWindow", u"Service Mode", None))
        self.button_4.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Configuration Name", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Time (s)", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Voltage (V)", None))
        self.input_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Enter Configuration Name", None))
        self.input_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Enter Time (1 - 2000) ", None))
        self.input_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter voltage (1 - 32)", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Current (A)", None))
        self.input_8.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Enter current (1 - 10) ", None))
        self.label_23.setText("")
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Temp (\u00b0C)", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Speed (mm/s) ", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"    Distance (mm)", None))
        self.input_12.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Enter Distance (1 - 20) ", None))
        self.input_13.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Enter Speed (1 - 15)", None))
        self.input_14.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Enter Temp (60 -80) ", None))
        self.button_5.setText(QCoreApplication.translate("MainWindow", u"Process", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Configuration Name ", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Time (s)", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Voltage (V)", None))
        self.label_29.setText("")
        self.label_32.setText("")
        self.button_6.setText(QCoreApplication.translate("MainWindow", u"Select Configuration", None))
        self.label_33.setText("")

        __sortingEnabled = self.configlist.isSortingEnabled()
        self.configlist.setSortingEnabled(False)
        ___qlistwidgetitem = self.configlist.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"item 1", None));
        self.configlist.setSortingEnabled(__sortingEnabled)

        self.button_11.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.label_42.setText("")
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Current (A)", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Speed (mm/s)", None))
        self.label_61.setText("")
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Temperature (\u00b0C)", None))
        self.label_77.setText("")
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"Distance (mm)", None))
        self.label_79.setText("")
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Select COM Port", None))

        self.label_9.setText("")
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Select COM Port", None))

        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Supply:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"MCU:", None))
        self.label_12.setText("")
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_39.setText("")
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Temperature", None))
        self.label_58.setText("")
        self.button_26.setText("")
        self.button_27.setText("")
        self.button_28.setText("")
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"Actuator", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"Heater", None))
        self.button_A.setText("")
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"EPM-01", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Electro Polishing Machine", None))
#if QT_CONFIG(whatsthis)
        self.label_51.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:16pt;\"><br/></span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Electro Polishing Machine is designed to enhance the surface finish of stents using electrochemical techniques. This process ensures superior smoothness and precision, essential for medical-grade applications.", None))
        self.label_57.setText("")
        self.button_1.setText(QCoreApplication.translate("MainWindow", u"LOGIN", None))
        self.label_1.setText(QCoreApplication.translate("MainWindow", u"Username:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.input_1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Username", None))
        self.input_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Password", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Invalid Credentials", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Copyright \u00a9 Revive Medical Technologies Inc.", None))
        self.button_HS.setText("")
        self.button_7.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.button_8.setText(QCoreApplication.translate("MainWindow", u"PAUSE", None))
        self.button_9.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Temp", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_13.setText("")
        self.label_19.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Complete", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Voltage", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Current", None))
        self.label_36.setText("")
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_14.setText("")
        self.label_34.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Remaining Time", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"00 : 00 ", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Real-Time Values", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"User-Defined Values", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.label_65.setStyleSheet(QCoreApplication.translate("MainWindow", u"background:none;\n"
"color: #9f9f9f;", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Config Name", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"Time:", None))
        self.label_67.setStyleSheet(QCoreApplication.translate("MainWindow", u"background:none;\n"
"color: #9f9f9f;", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"00 : 00", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Voltage:", None))
        self.label_70.setStyleSheet(QCoreApplication.translate("MainWindow", u"background:none;\n"
"color: #9f9f9f;", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"12", None))
        self.label_72.setStyleSheet(QCoreApplication.translate("MainWindow", u"background:none;\n"
"color: #9f9f9f;", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"Current:", None))
        self.label_74.setStyleSheet(QCoreApplication.translate("MainWindow", u"background:none;\n"
"color: #9f9f9f;", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.label_75.setStyleSheet(QCoreApplication.translate("MainWindow", u"background:none;\n"
"color: #9f9f9f;", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.label_76.setStyleSheet(QCoreApplication.translate("MainWindow", u"background:none;\n"
"color: #9f9f9f;", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"MM : SS", None))
        self.label_80.setStyleSheet(QCoreApplication.translate("MainWindow", u"background:none;\n"
"color: #9f9f9f;", None))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"mm/s", None))
        self.label_81.setStyleSheet(QCoreApplication.translate("MainWindow", u"background:none;\n"
"color: #9f9f9f;", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"Speed:", None))
        self.label_83.setStyleSheet(QCoreApplication.translate("MainWindow", u"background:none;\n"
"color: #9f9f9f;", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_84.setStyleSheet(QCoreApplication.translate("MainWindow", u"background:none;\n"
"color: #9f9f9f;", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"Temp:", None))
        self.label_86.setStyleSheet(QCoreApplication.translate("MainWindow", u"background:none;\n"
"color: #9f9f9f;", None))
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"mm", None))
        self.label_87.setStyleSheet(QCoreApplication.translate("MainWindow", u"background:none;\n"
"color: #9f9f9f;", None))
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.label_88.setText(QCoreApplication.translate("MainWindow", u"Distance:", None))
    # retranslateUi

