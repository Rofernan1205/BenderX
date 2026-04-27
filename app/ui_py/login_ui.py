# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
from . import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1131, 882)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.frame)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setMinimumSize(QSize(0, 40))
        self.header_frame.setMaximumSize(QSize(16777215, 40))
        self.header_frame.setStyleSheet(u"")
        self.header_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.header_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.control = QFrame(self.header_frame)
        self.control.setObjectName(u"control")
        self.control.setStyleSheet(u"")
        self.control.setFrameShape(QFrame.Shape.StyledPanel)
        self.control.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.control)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.min = QPushButton(self.control)
        self.min.setObjectName(u"min")
        self.min.setMinimumSize(QSize(38, 38))
        self.min.setMaximumSize(QSize(38, 38))
        self.min.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.min.setAutoFillBackground(False)
        self.min.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/minimize.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.min.setIcon(icon)
        self.min.setIconSize(QSize(38, 38))

        self.horizontalLayout_2.addWidget(self.min)

        self.mid = QPushButton(self.control)
        self.mid.setObjectName(u"mid")
        self.mid.setMinimumSize(QSize(38, 38))
        self.mid.setMaximumSize(QSize(38, 38))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/windows.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.mid.setIcon(icon1)
        self.mid.setIconSize(QSize(38, 38))

        self.horizontalLayout_2.addWidget(self.mid)

        self.max = QPushButton(self.control)
        self.max.setObjectName(u"max")
        self.max.setMinimumSize(QSize(38, 38))
        self.max.setMaximumSize(QSize(38, 38))
        self.max.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/maximize.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.max.setIcon(icon2)
        self.max.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.max)

        self.close = QPushButton(self.control)
        self.close.setObjectName(u"close")
        self.close.setMinimumSize(QSize(38, 38))
        self.close.setMaximumSize(QSize(38, 38))
        self.close.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/close.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.close.setIcon(icon3)
        self.close.setIconSize(QSize(38, 38))

        self.horizontalLayout_2.addWidget(self.close)


        self.horizontalLayout.addWidget(self.control, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout_2.addWidget(self.header_frame)

        self.body_frame = QFrame(self.frame)
        self.body_frame.setObjectName(u"body_frame")
        self.body_frame.setMaximumSize(QSize(16777215, 16777215))
        self.body_frame.setStyleSheet(u"")
        self.body_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.body_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.body_frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.box_login = QFrame(self.body_frame)
        self.box_login.setObjectName(u"box_login")
        self.box_login.setMinimumSize(QSize(350, 400))
        self.box_login.setMaximumSize(QSize(450, 550))
        self.box_login.setStyleSheet(u"")
        self.box_login.setFrameShape(QFrame.Shape.StyledPanel)
        self.box_login.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.box_login)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.box_login)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_6 = QVBoxLayout(self.widget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.labelError = QLabel(self.widget)
        self.labelError.setObjectName(u"labelError")

        self.verticalLayout_6.addWidget(self.labelError, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout.addWidget(self.widget)

        self.widget_user = QWidget(self.box_login)
        self.widget_user.setObjectName(u"widget_user")
        self.widget_user.setMinimumSize(QSize(0, 80))
        self.widget_user.setMaximumSize(QSize(16777215, 100))
        self.gridLayout = QGridLayout(self.widget_user)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit_username = QLineEdit(self.widget_user)
        self.lineEdit_username.setObjectName(u"lineEdit_username")

        self.gridLayout.addWidget(self.lineEdit_username, 1, 0, 1, 1)

        self.labelUsername = QLabel(self.widget_user)
        self.labelUsername.setObjectName(u"labelUsername")

        self.gridLayout.addWidget(self.labelUsername, 0, 0, 1, 1, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout.addWidget(self.widget_user)

        self.widget_password = QWidget(self.box_login)
        self.widget_password.setObjectName(u"widget_password")
        self.widget_password.setMinimumSize(QSize(0, 100))
        self.widget_password.setMaximumSize(QSize(16777215, 120))
        self.verticalLayout_4 = QVBoxLayout(self.widget_password)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.labelPassword = QLabel(self.widget_password)
        self.labelPassword.setObjectName(u"labelPassword")

        self.verticalLayout_4.addWidget(self.labelPassword, 0, Qt.AlignmentFlag.AlignLeft)

        self.lineEdit_password = QLineEdit(self.widget_password)
        self.lineEdit_password.setObjectName(u"lineEdit_password")
        self.lineEdit_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout_4.addWidget(self.lineEdit_password)

        self.labelForgotPass = QLabel(self.widget_password)
        self.labelForgotPass.setObjectName(u"labelForgotPass")
        self.labelForgotPass.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.labelForgotPass, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout.addWidget(self.widget_password)

        self.widget_button = QWidget(self.box_login)
        self.widget_button.setObjectName(u"widget_button")
        self.verticalLayout_5 = QVBoxLayout(self.widget_button)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.buttonSession = QPushButton(self.widget_button)
        self.buttonSession.setObjectName(u"buttonSession")
        self.buttonSession.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.buttonSession)


        self.verticalLayout.addWidget(self.widget_button)


        self.horizontalLayout_4.addWidget(self.box_login)


        self.verticalLayout_2.addWidget(self.body_frame)

        self.footer_frame = QFrame(self.frame)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setMinimumSize(QSize(0, 40))
        self.footer_frame.setMaximumSize(QSize(16777215, 40))
        self.footer_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.footer_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.company = QLabel(self.footer_frame)
        self.company.setObjectName(u"company")

        self.horizontalLayout_5.addWidget(self.company, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout_2.addWidget(self.footer_frame)


        self.horizontalLayout_3.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.min.setText("")
        self.min.setProperty(u"class", QCoreApplication.translate("MainWindow", u"button-control", None))
        self.mid.setText("")
        self.mid.setProperty(u"class", QCoreApplication.translate("MainWindow", u"button-control", None))
        self.max.setText("")
        self.max.setProperty(u"class", QCoreApplication.translate("MainWindow", u"button-control", None))
        self.close.setText("")
        self.close.setProperty(u"class", QCoreApplication.translate("MainWindow", u"button-control", None))
        self.box_login.setProperty(u"class", QCoreApplication.translate("MainWindow", u"borde-general", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Inicie sesi\u00f3n en BenderX", None))
        self.label.setProperty(u"class", QCoreApplication.translate("MainWindow", u"label-h1", None))
        self.labelError.setText(QCoreApplication.translate("MainWindow", u"Mensaje error", None))
        self.labelError.setProperty(u"class", QCoreApplication.translate("MainWindow", u"label-error", None))
        self.lineEdit_username.setProperty(u"class", QCoreApplication.translate("MainWindow", u"main-field", None))
        self.labelUsername.setText(QCoreApplication.translate("MainWindow", u"Usuario", None))
        self.labelUsername.setProperty(u"class", QCoreApplication.translate("MainWindow", u"label-hint-bold", None))
        self.labelPassword.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.labelPassword.setProperty(u"class", QCoreApplication.translate("MainWindow", u"label-hint-bold", None))
        self.lineEdit_password.setProperty(u"class", QCoreApplication.translate("MainWindow", u"main-field", None))
        self.labelForgotPass.setText(QCoreApplication.translate("MainWindow", u"\u00bfOlvidastes tu contrase\u00f1a?", None))
        self.labelForgotPass.setProperty(u"class", QCoreApplication.translate("MainWindow", u"label-link", None))
        self.buttonSession.setText(QCoreApplication.translate("MainWindow", u"Iniciar Sesi\u00f3n", None))
        self.buttonSession.setProperty(u"class", QCoreApplication.translate("MainWindow", u"main-button", None))
        self.footer_frame.setProperty(u"class", QCoreApplication.translate("MainWindow", u"border-top", None))
        self.company.setText(QCoreApplication.translate("MainWindow", u"ApuByte @ 2026 ", None))
        self.company.setProperty(u"class", QCoreApplication.translate("MainWindow", u"text-company", None))
    # retranslateUi

