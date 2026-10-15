# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Virtual_Keyboard.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QMainWindow,
    QSizePolicy, QToolButton, QVBoxLayout, QWidget)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(500, 400)
        icon = QIcon()
        icon.addFile(u"icons/keyboard.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        mainWindow.setWindowIcon(icon)
        mainWindow.setStyleSheet(u"\n"
"background-color: rgb(233, 238, 241);")
        mainWindow.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 0, 10, 0)
        self.toolButton_2 = QToolButton(self.frame)
        self.toolButton_2.setObjectName(u"toolButton_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_2.sizePolicy().hasHeightForWidth())
        self.toolButton_2.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"SF Pro Display"])
        font.setPointSize(16)
        self.toolButton_2.setFont(font)
        self.toolButton_2.setStyleSheet(u"QToolButton {\n"
"                    background-color: white;\n"
"                    color: black;\n"
"                    \n"
"                    border-radius: 5px;\n"
"                }\n"
"                QToolButton:hover {\n"
"                    background-color: #e6e6e6;\n"
"                }\n"
"                QToolButton:pressed {\n"
"                    background-color: #d3d3d3;\n"
"                }")

        self.horizontalLayout.addWidget(self.toolButton_2)

        self.toolButton_3 = QToolButton(self.frame)
        self.toolButton_3.setObjectName(u"toolButton_3")
        sizePolicy.setHeightForWidth(self.toolButton_3.sizePolicy().hasHeightForWidth())
        self.toolButton_3.setSizePolicy(sizePolicy)
        self.toolButton_3.setFont(font)
        self.toolButton_3.setStyleSheet(u"QToolButton {\n"
"                    background-color: white;\n"
"                    color: black;\n"
"                    \n"
"                    border-radius: 5px;\n"
"                }\n"
"                QToolButton:hover {\n"
"                    background-color: #e6e6e6;\n"
"                }\n"
"                QToolButton:pressed {\n"
"                    background-color: #d3d3d3;\n"
"                }")

        self.horizontalLayout.addWidget(self.toolButton_3)

        self.toolButton_4 = QToolButton(self.frame)
        self.toolButton_4.setObjectName(u"toolButton_4")
        sizePolicy.setHeightForWidth(self.toolButton_4.sizePolicy().hasHeightForWidth())
        self.toolButton_4.setSizePolicy(sizePolicy)
        self.toolButton_4.setFont(font)
        self.toolButton_4.setStyleSheet(u"QToolButton {\n"
"                    background-color: white;\n"
"                    color: black;\n"
"                    \n"
"                    border-radius: 5px;\n"
"                }\n"
"                QToolButton:hover {\n"
"                    background-color: #e6e6e6;\n"
"                }\n"
"                QToolButton:pressed {\n"
"                    background-color: #d3d3d3;\n"
"                }")

        self.horizontalLayout.addWidget(self.toolButton_4)

        self.toolButton_5 = QToolButton(self.frame)
        self.toolButton_5.setObjectName(u"toolButton_5")
        sizePolicy.setHeightForWidth(self.toolButton_5.sizePolicy().hasHeightForWidth())
        self.toolButton_5.setSizePolicy(sizePolicy)
        self.toolButton_5.setFont(font)
        self.toolButton_5.setStyleSheet(u"QToolButton {\n"
"                    background-color: white;\n"
"                    color: black;\n"
"                    \n"
"                    border-radius: 5px;\n"
"                }\n"
"                QToolButton:hover {\n"
"                    background-color: #e6e6e6;\n"
"                }\n"
"                QToolButton:pressed {\n"
"                    background-color: #d3d3d3;\n"
"                }")

        self.horizontalLayout.addWidget(self.toolButton_5)

        self.toolButton_6 = QToolButton(self.frame)
        self.toolButton_6.setObjectName(u"toolButton_6")
        sizePolicy.setHeightForWidth(self.toolButton_6.sizePolicy().hasHeightForWidth())
        self.toolButton_6.setSizePolicy(sizePolicy)
        self.toolButton_6.setFont(font)
        self.toolButton_6.setStyleSheet(u"QToolButton {\n"
"                    background-color: white;\n"
"                    color: black;\n"
"                    \n"
"                    border-radius: 5px;\n"
"                }\n"
"                QToolButton:hover {\n"
"                    background-color: #e6e6e6;\n"
"                }\n"
"                QToolButton:pressed {\n"
"                    background-color: #d3d3d3;\n"
"                }")

        self.horizontalLayout.addWidget(self.toolButton_6)

        self.toolButton_7 = QToolButton(self.frame)
        self.toolButton_7.setObjectName(u"toolButton_7")
        sizePolicy.setHeightForWidth(self.toolButton_7.sizePolicy().hasHeightForWidth())
        self.toolButton_7.setSizePolicy(sizePolicy)
        self.toolButton_7.setFont(font)
        self.toolButton_7.setStyleSheet(u"QToolButton {\n"
"                    background-color: white;\n"
"                    color: black;\n"
"                    \n"
"                    border-radius: 5px;\n"
"                }\n"
"                QToolButton:hover {\n"
"                    background-color: #e6e6e6;\n"
"                }\n"
"                QToolButton:pressed {\n"
"                    background-color: #d3d3d3;\n"
"                }")

        self.horizontalLayout.addWidget(self.toolButton_7)

        self.toolButton_8 = QToolButton(self.frame)
        self.toolButton_8.setObjectName(u"toolButton_8")
        sizePolicy.setHeightForWidth(self.toolButton_8.sizePolicy().hasHeightForWidth())
        self.toolButton_8.setSizePolicy(sizePolicy)
        self.toolButton_8.setFont(font)
        self.toolButton_8.setStyleSheet(u"QToolButton {\n"
"                    background-color: white;\n"
"                    color: black;\n"
"                    \n"
"                    border-radius: 5px;\n"
"                }\n"
"                QToolButton:hover {\n"
"                    background-color: #e6e6e6;\n"
"                }\n"
"                QToolButton:pressed {\n"
"                    background-color: #d3d3d3;\n"
"                }")

        self.horizontalLayout.addWidget(self.toolButton_8)

        self.toolButton_9 = QToolButton(self.frame)
        self.toolButton_9.setObjectName(u"toolButton_9")
        sizePolicy.setHeightForWidth(self.toolButton_9.sizePolicy().hasHeightForWidth())
        self.toolButton_9.setSizePolicy(sizePolicy)
        self.toolButton_9.setFont(font)
        self.toolButton_9.setStyleSheet(u"QToolButton {\n"
"                    background-color: white;\n"
"                    color: black;\n"
"                    \n"
"                    border-radius: 5px;\n"
"                }\n"
"                QToolButton:hover {\n"
"                    background-color: #e6e6e6;\n"
"                }\n"
"                QToolButton:pressed {\n"
"                    background-color: #d3d3d3;\n"
"                }")

        self.horizontalLayout.addWidget(self.toolButton_9)

        self.toolButton_10 = QToolButton(self.frame)
        self.toolButton_10.setObjectName(u"toolButton_10")
        sizePolicy.setHeightForWidth(self.toolButton_10.sizePolicy().hasHeightForWidth())
        self.toolButton_10.setSizePolicy(sizePolicy)
        self.toolButton_10.setFont(font)
        self.toolButton_10.setStyleSheet(u"QToolButton {\n"
"                    background-color: white;\n"
"                    color: black;\n"
"                    \n"
"                    border-radius: 5px;\n"
"                }\n"
"                QToolButton:hover {\n"
"                    background-color: #e6e6e6;\n"
"                }\n"
"                QToolButton:pressed {\n"
"                    background-color: #d3d3d3;\n"
"                }")

        self.horizontalLayout.addWidget(self.toolButton_10)

        self.toolButton_11 = QToolButton(self.frame)
        self.toolButton_11.setObjectName(u"toolButton_11")
        sizePolicy.setHeightForWidth(self.toolButton_11.sizePolicy().hasHeightForWidth())
        self.toolButton_11.setSizePolicy(sizePolicy)
        self.toolButton_11.setFont(font)
        self.toolButton_11.setStyleSheet(u"QToolButton {\n"
"                    background-color: white;\n"
"                    color: black;\n"
"                    \n"
"                    border-radius: 5px;\n"
"                }\n"
"                QToolButton:hover {\n"
"                    background-color: #e6e6e6;\n"
"                }\n"
"                QToolButton:pressed {\n"
"                    background-color: #d3d3d3;\n"
"                }")

        self.horizontalLayout.addWidget(self.toolButton_11)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 0, 10, 0)
        self.toolButton_12 = QToolButton(self.frame_2)
        self.toolButton_12.setObjectName(u"toolButton_12")
        sizePolicy.setHeightForWidth(self.toolButton_12.sizePolicy().hasHeightForWidth())
        self.toolButton_12.setSizePolicy(sizePolicy)
        self.toolButton_12.setFont(font)
        self.toolButton_12.setStyleSheet(u"QToolButton {\n"
"                    background-color: white;\n"
"                    color: black;\n"
"                    \n"
"                    border-radius: 5px;\n"
"                }\n"
"                QToolButton:hover {\n"
"                    background-color: #e6e6e6;\n"
"                }\n"
"                QToolButton:pressed {\n"
"                    background-color: #d3d3d3;\n"
"                }")

        self.horizontalLayout_2.addWidget(self.toolButton_12)

        self.toolButton_13 = QToolButton(self.frame_2)
        self.toolButton_13.setObjectName(u"toolButton_13")
        sizePolicy.setHeightForWidth(self.toolButton_13.sizePolicy().hasHeightForWidth())
        self.toolButton_13.setSizePolicy(sizePolicy)
        self.toolButton_13.setFont(font)
        self.toolButton_13.setStyleSheet(u"QToolButton {\n"
"                    background-color: white;\n"
"                    color: black;\n"
"                    \n"
"                    border-radius: 5px;\n"
"                }\n"
"                QToolButton:hover {\n"
"                    background-color: #e6e6e6;\n"
"                }\n"
"                QToolButton:pressed {\n"
"                    background-color: #d3d3d3;\n"
"                }")

        self.horizontalLayout_2.addWidget(self.toolButton_13)

        self.toolButton_14 = QToolButton(self.frame_2)
        self.toolButton_14.setObjectName(u"toolButton_14")
        sizePolicy.setHeightForWidth(self.toolButton_14.sizePolicy().hasHeightForWidth())
        self.toolButton_14.setSizePolicy(sizePolicy)
        self.toolButton_14.setFont(font)
        self.toolButton_14.setStyleSheet(u"QToolButton {\n"
"                    background-color: white;\n"
"                    color: black;\n"
"                    \n"
"                    border-radius: 5px;\n"
"                }\n"
"                QToolButton:hover {\n"
"                    background-color: #e6e6e6;\n"
"                }\n"
"                QToolButton:pressed {\n"
"                    background-color: #d3d3d3;\n"
"                }")

        self.horizontalLayout_2.addWidget(self.toolButton_14)

        self.toolButton_15 = QToolButton(self.frame_2)
        self.toolButton_15.setObjectName(u"toolButton_15")
        sizePolicy.setHeightForWidth(self.toolButton_15.sizePolicy().hasHeightForWidth())
        self.toolButton_15.setSizePolicy(sizePolicy)
        self.toolButton_15.setFont(font)
        self.toolButton_15.setStyleSheet(u"QToolButton {\n"
"                    background-color: white;\n"
"                    color: black;\n"
"                    \n"
"                    border-radius: 5px;\n"
"                }\n"
"                QToolButton:hover {\n"
"                    background-color: #e6e6e6;\n"
"                }\n"
"                QToolButton:pressed {\n"
"                    background-color: #d3d3d3;\n"
"                }")

        self.horizontalLayout_2.addWidget(self.toolButton_15)

        self.toolButton_16 = QToolButton(self.frame_2)
        self.toolButton_16.setObjectName(u"toolButton_16")
        sizePolicy.setHeightForWidth(self.toolButton_16.sizePolicy().hasHeightForWidth())
        self.toolButton_16.setSizePolicy(sizePolicy)
        self.toolButton_16.setFont(font)
        self.toolButton_16.setStyleSheet(u"QToolButton {\n"
"                    background-color: white;\n"
"                    color: black;\n"
"                    \n"
"                    border-radius: 5px;\n"
"                }\n"
"                QToolButton:hover {\n"
"                    background-color: #e6e6e6;\n"
"                }\n"
"                QToolButton:pressed {\n"
"                    background-color: #d3d3d3;\n"
"                }")

        self.horizontalLayout_2.addWidget(self.toolButton_16)

        self.toolButton_17 = QToolButton(self.frame_2)
        self.toolButton_17.setObjectName(u"toolButton_17")
        sizePolicy.setHeightForWidth(self.toolButton_17.sizePolicy().hasHeightForWidth())
        self.toolButton_17.setSizePolicy(sizePolicy)
        self.toolButton_17.setFont(font)
        self.toolButton_17.setStyleSheet(u"QToolButton {\n"
"                    background-color: white;\n"
"                    color: black;\n"
"                    \n"
"                    border-radius: 5px;\n"
"                }\n"
"                QToolButton:hover {\n"
"                    background-color: #e6e6e6;\n"
"                }\n"
"                QToolButton:pressed {\n"
"                    background-color: #d3d3d3;\n"
"                }")

        self.horizontalLayout_2.addWidget(self.toolButton_17)

        self.toolButton_18 = QToolButton(self.frame_2)
        self.toolButton_18.setObjectName(u"toolButton_18")
        sizePolicy.setHeightForWidth(self.toolButton_18.sizePolicy().hasHeightForWidth())
        self.toolButton_18.setSizePolicy(sizePolicy)
        self.toolButton_18.setFont(font)
        self.toolButton_18.setStyleSheet(u"QToolButton {\n"
"                    background-color: white;\n"
"                    color: black;\n"
"                    \n"
"                    border-radius: 5px;\n"
"                }\n"
"                QToolButton:hover {\n"
"                    background-color: #e6e6e6;\n"
"                }\n"
"                QToolButton:pressed {\n"
"                    background-color: #d3d3d3;\n"
"                }")

        self.horizontalLayout_2.addWidget(self.toolButton_18)

        self.toolButton_19 = QToolButton(self.frame_2)
        self.toolButton_19.setObjectName(u"toolButton_19")
        sizePolicy.setHeightForWidth(self.toolButton_19.sizePolicy().hasHeightForWidth())
        self.toolButton_19.setSizePolicy(sizePolicy)
        self.toolButton_19.setFont(font)
        self.toolButton_19.setStyleSheet(u"QToolButton {\n"
"                    background-color: white;\n"
"                    color: black;\n"
"                    \n"
"                    border-radius: 5px;\n"
"                }\n"
"                QToolButton:hover {\n"
"                    background-color: #e6e6e6;\n"
"                }\n"
"                QToolButton:pressed {\n"
"                    background-color: #d3d3d3;\n"
"                }")

        self.horizontalLayout_2.addWidget(self.toolButton_19)

        self.toolButton_20 = QToolButton(self.frame_2)
        self.toolButton_20.setObjectName(u"toolButton_20")
        sizePolicy.setHeightForWidth(self.toolButton_20.sizePolicy().hasHeightForWidth())
        self.toolButton_20.setSizePolicy(sizePolicy)
        self.toolButton_20.setFont(font)
        self.toolButton_20.setStyleSheet(u"QToolButton {\n"
"                    background-color: white;\n"
"                    color: black;\n"
"                    \n"
"                    border-radius: 5px;\n"
"                }\n"
"                QToolButton:hover {\n"
"                    background-color: #e6e6e6;\n"
"                }\n"
"                QToolButton:pressed {\n"
"                    background-color: #d3d3d3;\n"
"                }")

        self.horizontalLayout_2.addWidget(self.toolButton_20)

        self.toolButton_21 = QToolButton(self.frame_2)
        self.toolButton_21.setObjectName(u"toolButton_21")
        sizePolicy.setHeightForWidth(self.toolButton_21.sizePolicy().hasHeightForWidth())
        self.toolButton_21.setSizePolicy(sizePolicy)
        self.toolButton_21.setFont(font)
        self.toolButton_21.setStyleSheet(u"QToolButton {\n"
"                    background-color: white;\n"
"                    color: black;\n"
"                    \n"
"                    border-radius: 5px;\n"
"                }\n"
"                QToolButton:hover {\n"
"                    background-color: #e6e6e6;\n"
"                }\n"
"                QToolButton:pressed {\n"
"                    background-color: #d3d3d3;\n"
"                }")

        self.horizontalLayout_2.addWidget(self.toolButton_21)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 0, 10, 0)
        self.toolButton_24 = QToolButton(self.frame_3)
        self.toolButton_24.setObjectName(u"toolButton_24")
        sizePolicy.setHeightForWidth(self.toolButton_24.sizePolicy().hasHeightForWidth())
        self.toolButton_24.setSizePolicy(sizePolicy)
        self.toolButton_24.setFont(font)
        self.toolButton_24.setStyleSheet(u"QToolButton {\n"
"                    background-color: white;\n"
"                    color: black;\n"
"                    \n"
"                    border-radius: 5px;\n"
"                }\n"
"                QToolButton:hover {\n"
"                    background-color: #e6e6e6;\n"
"                }\n"
"                QToolButton:pressed {\n"
"                    background-color: #d3d3d3;\n"
"                }")

        self.horizontalLayout_3.addWidget(self.toolButton_24)

        self.toolButton_25 = QToolButton(self.frame_3)
        self.toolButton_25.setObjectName(u"toolButton_25")
        sizePolicy.setHeightForWidth(self.toolButton_25.sizePolicy().hasHeightForWidth())
        self.toolButton_25.setSizePolicy(sizePolicy)
        self.toolButton_25.setFont(font)
        self.toolButton_25.setStyleSheet(u"QToolButton {\n"
"                    background-color: white;\n"
"                    color: black;\n"
"                    \n"
"                    border-radius: 5px;\n"
"                }\n"
"                QToolButton:hover {\n"
"                    background-color: #e6e6e6;\n"
"                }\n"
"                QToolButton:pressed {\n"
"                    background-color: #d3d3d3;\n"
"                }")

        self.horizontalLayout_3.addWidget(self.toolButton_25)

        self.toolButton_26 = QToolButton(self.frame_3)
        self.toolButton_26.setObjectName(u"toolButton_26")
        sizePolicy.setHeightForWidth(self.toolButton_26.sizePolicy().hasHeightForWidth())
        self.toolButton_26.setSizePolicy(sizePolicy)
        self.toolButton_26.setFont(font)
        self.toolButton_26.setStyleSheet(u"QToolButton {\n"
"                    background-color: white;\n"
"                    color: black;\n"
"                    \n"
"                    border-radius: 5px;\n"
"                }\n"
"                QToolButton:hover {\n"
"                    background-color: #e6e6e6;\n"
"                }\n"
"                QToolButton:pressed {\n"
"                    background-color: #d3d3d3;\n"
"                }")

        self.horizontalLayout_3.addWidget(self.toolButton_26)

        self.toolButton_27 = QToolButton(self.frame_3)
        self.toolButton_27.setObjectName(u"toolButton_27")
        sizePolicy.setHeightForWidth(self.toolButton_27.sizePolicy().hasHeightForWidth())
        self.toolButton_27.setSizePolicy(sizePolicy)
        self.toolButton_27.setFont(font)
        self.toolButton_27.setStyleSheet(u"QToolButton {\n"
"                    background-color: white;\n"
"                    color: black;\n"
"                    \n"
"                    border-radius: 5px;\n"
"                }\n"
"                QToolButton:hover {\n"
"                    background-color: #e6e6e6;\n"
"                }\n"
"                QToolButton:pressed {\n"
"                    background-color: #d3d3d3;\n"
"                }")

        self.horizontalLayout_3.addWidget(self.toolButton_27)

        self.toolButton_28 = QToolButton(self.frame_3)
        self.toolButton_28.setObjectName(u"toolButton_28")
        sizePolicy.setHeightForWidth(self.toolButton_28.sizePolicy().hasHeightForWidth())
        self.toolButton_28.setSizePolicy(sizePolicy)
        self.toolButton_28.setFont(font)
        self.toolButton_28.setStyleSheet(u"QToolButton {\n"
"                    background-color: white;\n"
"                    color: black;\n"
"                    \n"
"                    border-radius: 5px;\n"
"                }\n"
"                QToolButton:hover {\n"
"                    background-color: #e6e6e6;\n"
"                }\n"
"                QToolButton:pressed {\n"
"                    background-color: #d3d3d3;\n"
"                }")

        self.horizontalLayout_3.addWidget(self.toolButton_28)

        self.toolButton_29 = QToolButton(self.frame_3)
        self.toolButton_29.setObjectName(u"toolButton_29")
        sizePolicy.setHeightForWidth(self.toolButton_29.sizePolicy().hasHeightForWidth())
        self.toolButton_29.setSizePolicy(sizePolicy)
        self.toolButton_29.setFont(font)
        self.toolButton_29.setStyleSheet(u"QToolButton {\n"
"                    background-color: white;\n"
"                    color: black;\n"
"                    \n"
"                    border-radius: 5px;\n"
"                }\n"
"                QToolButton:hover {\n"
"                    background-color: #e6e6e6;\n"
"                }\n"
"                QToolButton:pressed {\n"
"                    background-color: #d3d3d3;\n"
"                }")

        self.horizontalLayout_3.addWidget(self.toolButton_29)

        self.toolButton_30 = QToolButton(self.frame_3)
        self.toolButton_30.setObjectName(u"toolButton_30")
        sizePolicy.setHeightForWidth(self.toolButton_30.sizePolicy().hasHeightForWidth())
        self.toolButton_30.setSizePolicy(sizePolicy)
        self.toolButton_30.setFont(font)
        self.toolButton_30.setStyleSheet(u"QToolButton {\n"
"                    background-color: white;\n"
"                    color: black;\n"
"                    \n"
"                    border-radius: 5px;\n"
"                }\n"
"                QToolButton:hover {\n"
"                    background-color: #e6e6e6;\n"
"                }\n"
"                QToolButton:pressed {\n"
"                    background-color: #d3d3d3;\n"
"                }")

        self.horizontalLayout_3.addWidget(self.toolButton_30)

        self.toolButton_31 = QToolButton(self.frame_3)
        self.toolButton_31.setObjectName(u"toolButton_31")
        sizePolicy.setHeightForWidth(self.toolButton_31.sizePolicy().hasHeightForWidth())
        self.toolButton_31.setSizePolicy(sizePolicy)
        self.toolButton_31.setFont(font)
        self.toolButton_31.setStyleSheet(u"QToolButton {\n"
"                    background-color: white;\n"
"                    color: black;\n"
"                    \n"
"                    border-radius: 5px;\n"
"                }\n"
"                QToolButton:hover {\n"
"                    background-color: #e6e6e6;\n"
"                }\n"
"                QToolButton:pressed {\n"
"                    background-color: #d3d3d3;\n"
"                }")

        self.horizontalLayout_3.addWidget(self.toolButton_31)

        self.toolButton_32 = QToolButton(self.frame_3)
        self.toolButton_32.setObjectName(u"toolButton_32")
        sizePolicy.setHeightForWidth(self.toolButton_32.sizePolicy().hasHeightForWidth())
        self.toolButton_32.setSizePolicy(sizePolicy)
        self.toolButton_32.setFont(font)
        self.toolButton_32.setStyleSheet(u"QToolButton {\n"
"                    background-color: white;\n"
"                    color: black;\n"
"                    \n"
"                    border-radius: 5px;\n"
"                }\n"
"                QToolButton:hover {\n"
"                    background-color: #e6e6e6;\n"
"                }\n"
"                QToolButton:pressed {\n"
"                    background-color: #d3d3d3;\n"
"                }")

        self.horizontalLayout_3.addWidget(self.toolButton_32)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(10, 0, 10, 0)
        self.toolButton_23 = QToolButton(self.frame_4)
        self.toolButton_23.setObjectName(u"toolButton_23")
        sizePolicy.setHeightForWidth(self.toolButton_23.sizePolicy().hasHeightForWidth())
        self.toolButton_23.setSizePolicy(sizePolicy)
        self.toolButton_23.setFont(font)
        self.toolButton_23.setAutoFillBackground(False)
        self.toolButton_23.setStyleSheet(u"QToolButton {\n"
"                    background-color: white;\n"
"                    color: black;\n"
"                    \n"
"                    border-radius: 5px;\n"
"                }\n"
"                QToolButton:hover {\n"
"                    background-color: #e6e6e6;\n"
"                }\n"
"                QToolButton:pressed {\n"
"                    background-color: #d3d3d3;\n"
"                }")

        self.horizontalLayout_4.addWidget(self.toolButton_23)

        self.toolButton_34 = QToolButton(self.frame_4)
        self.toolButton_34.setObjectName(u"toolButton_34")
        sizePolicy.setHeightForWidth(self.toolButton_34.sizePolicy().hasHeightForWidth())
        self.toolButton_34.setSizePolicy(sizePolicy)
        self.toolButton_34.setFont(font)
        self.toolButton_34.setStyleSheet(u"QToolButton {\n"
"                    background-color: white;\n"
"                    color: black;\n"
"                    \n"
"                    border-radius: 5px;\n"
"                }\n"
"                QToolButton:hover {\n"
"                    background-color: #e6e6e6;\n"
"                }\n"
"                QToolButton:pressed {\n"
"                    background-color: #d3d3d3;\n"
"                }")

        self.horizontalLayout_4.addWidget(self.toolButton_34)

        self.toolButton_36 = QToolButton(self.frame_4)
        self.toolButton_36.setObjectName(u"toolButton_36")
        sizePolicy.setHeightForWidth(self.toolButton_36.sizePolicy().hasHeightForWidth())
        self.toolButton_36.setSizePolicy(sizePolicy)
        self.toolButton_36.setFont(font)
        self.toolButton_36.setStyleSheet(u"QToolButton {\n"
"                    background-color: white;\n"
"                    color: black;\n"
"                    \n"
"                    border-radius: 5px;\n"
"                }\n"
"                QToolButton:hover {\n"
"                    background-color: #e6e6e6;\n"
"                }\n"
"                QToolButton:pressed {\n"
"                    background-color: #d3d3d3;\n"
"                }")

        self.horizontalLayout_4.addWidget(self.toolButton_36)

        self.toolButton_35 = QToolButton(self.frame_4)
        self.toolButton_35.setObjectName(u"toolButton_35")
        sizePolicy.setHeightForWidth(self.toolButton_35.sizePolicy().hasHeightForWidth())
        self.toolButton_35.setSizePolicy(sizePolicy)
        self.toolButton_35.setFont(font)
        self.toolButton_35.setStyleSheet(u"QToolButton {\n"
"                    background-color: white;\n"
"                    color: black;\n"
"                    \n"
"                    border-radius: 5px;\n"
"                }\n"
"                QToolButton:hover {\n"
"                    background-color: #e6e6e6;\n"
"                }\n"
"                QToolButton:pressed {\n"
"                    background-color: #d3d3d3;\n"
"                }")

        self.horizontalLayout_4.addWidget(self.toolButton_35)

        self.toolButton_38 = QToolButton(self.frame_4)
        self.toolButton_38.setObjectName(u"toolButton_38")
        sizePolicy.setHeightForWidth(self.toolButton_38.sizePolicy().hasHeightForWidth())
        self.toolButton_38.setSizePolicy(sizePolicy)
        self.toolButton_38.setFont(font)
        self.toolButton_38.setStyleSheet(u"QToolButton {\n"
"                    background-color: white;\n"
"                    color: black;\n"
"                    \n"
"                    border-radius: 5px;\n"
"                }\n"
"                QToolButton:hover {\n"
"                    background-color: #e6e6e6;\n"
"                }\n"
"                QToolButton:pressed {\n"
"                    background-color: #d3d3d3;\n"
"                }")

        self.horizontalLayout_4.addWidget(self.toolButton_38)

        self.toolButton_37 = QToolButton(self.frame_4)
        self.toolButton_37.setObjectName(u"toolButton_37")
        sizePolicy.setHeightForWidth(self.toolButton_37.sizePolicy().hasHeightForWidth())
        self.toolButton_37.setSizePolicy(sizePolicy)
        self.toolButton_37.setFont(font)
        self.toolButton_37.setStyleSheet(u"QToolButton {\n"
"                    background-color: white;\n"
"                    color: black;\n"
"                    \n"
"                    border-radius: 5px;\n"
"                }\n"
"                QToolButton:hover {\n"
"                    background-color: #e6e6e6;\n"
"                }\n"
"                QToolButton:pressed {\n"
"                    background-color: #d3d3d3;\n"
"                }")

        self.horizontalLayout_4.addWidget(self.toolButton_37)

        self.toolButton_40 = QToolButton(self.frame_4)
        self.toolButton_40.setObjectName(u"toolButton_40")
        sizePolicy.setHeightForWidth(self.toolButton_40.sizePolicy().hasHeightForWidth())
        self.toolButton_40.setSizePolicy(sizePolicy)
        self.toolButton_40.setFont(font)
        self.toolButton_40.setStyleSheet(u"QToolButton {\n"
"                    background-color: white;\n"
"                    color: black;\n"
"                    \n"
"                    border-radius: 5px;\n"
"                }\n"
"                QToolButton:hover {\n"
"                    background-color: #e6e6e6;\n"
"                }\n"
"                QToolButton:pressed {\n"
"                    background-color: #d3d3d3;\n"
"                }")

        self.horizontalLayout_4.addWidget(self.toolButton_40)

        self.toolButton_39 = QToolButton(self.frame_4)
        self.toolButton_39.setObjectName(u"toolButton_39")
        sizePolicy.setHeightForWidth(self.toolButton_39.sizePolicy().hasHeightForWidth())
        self.toolButton_39.setSizePolicy(sizePolicy)
        self.toolButton_39.setFont(font)
        self.toolButton_39.setStyleSheet(u"QToolButton {\n"
"                    background-color: white;\n"
"                    color: black;\n"
"                    \n"
"                    border-radius: 5px;\n"
"                }\n"
"                QToolButton:hover {\n"
"                    background-color: #e6e6e6;\n"
"                }\n"
"                QToolButton:pressed {\n"
"                    background-color: #d3d3d3;\n"
"                }")

        self.horizontalLayout_4.addWidget(self.toolButton_39)

        self.toolButton_44 = QToolButton(self.frame_4)
        self.toolButton_44.setObjectName(u"toolButton_44")
        sizePolicy.setHeightForWidth(self.toolButton_44.sizePolicy().hasHeightForWidth())
        self.toolButton_44.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"SF Pro Display"])
        font1.setPointSize(12)
        self.toolButton_44.setFont(font1)
        self.toolButton_44.setStyleSheet(u"QToolButton {\n"
"                    background-color: white;\n"
"                    color: black;\n"
"                    \n"
"                    border-radius: 5px;\n"
"                }\n"
"                QToolButton:hover {\n"
"                    background-color: #e6e6e6;\n"
"                }\n"
"                QToolButton:pressed {\n"
"                    background-color: #d3d3d3;\n"
"                }")
        icon1 = QIcon()
        icon1.addFile(u"icons/png-clipart-computer-icons-arrow-back-angle-text-thumbnail-removebg-preview.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButton_44.setIcon(icon1)
        self.toolButton_44.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.toolButton_44)


        self.verticalLayout.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(10, 0, 10, 0)
        self.toolButton_45 = QToolButton(self.frame_5)
        self.toolButton_45.setObjectName(u"toolButton_45")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(42)
        sizePolicy1.setVerticalStretch(21)
        sizePolicy1.setHeightForWidth(self.toolButton_45.sizePolicy().hasHeightForWidth())
        self.toolButton_45.setSizePolicy(sizePolicy1)
        self.toolButton_45.setFont(font)
        self.toolButton_45.setStyleSheet(u"QToolButton {\n"
"                    background-color: white;\n"
"                    color: black;\n"
"                    \n"
"                    border-radius: 5px;\n"
"                }\n"
"                QToolButton:hover {\n"
"                    background-color: #e6e6e6;\n"
"                }\n"
"                QToolButton:pressed {\n"
"                    background-color: #d3d3d3;\n"
"                }")

        self.horizontalLayout_5.addWidget(self.toolButton_45)


        self.verticalLayout.addWidget(self.frame_5)

        mainWindow.setCentralWidget(self.centralwidget)
        self.frame.raise_()
        self.frame_3.raise_()
        self.frame_4.raise_()
        self.frame_2.raise_()
        self.frame_5.raise_()

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"Virtual Keyboard", None))
        self.toolButton_2.setText(QCoreApplication.translate("mainWindow", u"1", None))
        self.toolButton_3.setText(QCoreApplication.translate("mainWindow", u"2", None))
        self.toolButton_4.setText(QCoreApplication.translate("mainWindow", u"3", None))
        self.toolButton_5.setText(QCoreApplication.translate("mainWindow", u"4", None))
        self.toolButton_6.setText(QCoreApplication.translate("mainWindow", u"5", None))
        self.toolButton_7.setText(QCoreApplication.translate("mainWindow", u"6", None))
        self.toolButton_8.setText(QCoreApplication.translate("mainWindow", u"7", None))
        self.toolButton_9.setText(QCoreApplication.translate("mainWindow", u"8", None))
        self.toolButton_10.setText(QCoreApplication.translate("mainWindow", u"9", None))
        self.toolButton_11.setText(QCoreApplication.translate("mainWindow", u"0", None))
        self.toolButton_12.setText(QCoreApplication.translate("mainWindow", u"q", None))
        self.toolButton_13.setText(QCoreApplication.translate("mainWindow", u"w", None))
        self.toolButton_14.setText(QCoreApplication.translate("mainWindow", u"e", None))
        self.toolButton_15.setText(QCoreApplication.translate("mainWindow", u"r", None))
        self.toolButton_16.setText(QCoreApplication.translate("mainWindow", u"t", None))
        self.toolButton_17.setText(QCoreApplication.translate("mainWindow", u"y", None))
        self.toolButton_18.setText(QCoreApplication.translate("mainWindow", u"u", None))
        self.toolButton_19.setText(QCoreApplication.translate("mainWindow", u"i", None))
        self.toolButton_20.setText(QCoreApplication.translate("mainWindow", u"o", None))
        self.toolButton_21.setText(QCoreApplication.translate("mainWindow", u"p", None))
        self.toolButton_24.setText(QCoreApplication.translate("mainWindow", u"a", None))
        self.toolButton_25.setText(QCoreApplication.translate("mainWindow", u"s", None))
        self.toolButton_26.setText(QCoreApplication.translate("mainWindow", u"d", None))
        self.toolButton_27.setText(QCoreApplication.translate("mainWindow", u"f", None))
        self.toolButton_28.setText(QCoreApplication.translate("mainWindow", u"g", None))
        self.toolButton_29.setText(QCoreApplication.translate("mainWindow", u"h", None))
        self.toolButton_30.setText(QCoreApplication.translate("mainWindow", u"j", None))
        self.toolButton_31.setText(QCoreApplication.translate("mainWindow", u"k", None))
        self.toolButton_32.setText(QCoreApplication.translate("mainWindow", u"l", None))
        self.toolButton_23.setText(QCoreApplication.translate("mainWindow", u"CapsLock ", None))
        self.toolButton_34.setText(QCoreApplication.translate("mainWindow", u"z", None))
        self.toolButton_36.setText(QCoreApplication.translate("mainWindow", u"x", None))
        self.toolButton_35.setText(QCoreApplication.translate("mainWindow", u"c", None))
        self.toolButton_38.setText(QCoreApplication.translate("mainWindow", u"v", None))
        self.toolButton_37.setText(QCoreApplication.translate("mainWindow", u"b", None))
        self.toolButton_40.setText(QCoreApplication.translate("mainWindow", u"n", None))
        self.toolButton_39.setText(QCoreApplication.translate("mainWindow", u"m", None))
        self.toolButton_44.setText(QCoreApplication.translate("mainWindow", u"<--", None))
        self.toolButton_45.setText(QCoreApplication.translate("mainWindow", u"Space", None))
    # retranslateUi

