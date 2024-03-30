# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainuihFQoBn.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(393, 383)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label1 = QLabel(self.centralwidget)
        self.label1.setObjectName(u"label1")

        self.horizontalLayout.addWidget(self.label1)

        self.nameip = QLineEdit(self.centralwidget)
        self.nameip.setObjectName(u"nameip")

        self.horizontalLayout.addWidget(self.nameip)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label2 = QLabel(self.centralwidget)
        self.label2.setObjectName(u"label2")

        self.horizontalLayout_2.addWidget(self.label2)

        self.urlip = QLineEdit(self.centralwidget)
        self.urlip.setObjectName(u"urlip")

        self.horizontalLayout_2.addWidget(self.urlip)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label3 = QLabel(self.centralwidget)
        self.label3.setObjectName(u"label3")

        self.horizontalLayout_3.addWidget(self.label3)

        self.browsernameip = QComboBox(self.centralwidget)
        self.browsernameip.setObjectName(u"browsernameip")

        self.horizontalLayout_3.addWidget(self.browsernameip)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label4 = QLabel(self.centralwidget)
        self.label4.setObjectName(u"label4")

        self.horizontalLayout_4.addWidget(self.label4)

        self.browsermodeip = QComboBox(self.centralwidget)
        self.browsermodeip.setObjectName(u"browsermodeip")

        self.horizontalLayout_4.addWidget(self.browsermodeip)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label5 = QLabel(self.centralwidget)
        self.label5.setObjectName(u"label5")

        self.horizontalLayout_5.addWidget(self.label5)

        self.iconpathip = QLineEdit(self.centralwidget)
        self.iconpathip.setObjectName(u"iconpathip")

        self.horizontalLayout_5.addWidget(self.iconpathip)

        self.chooseiconbtn = QPushButton(self.centralwidget)
        self.chooseiconbtn.setObjectName(u"chooseiconbtn")

        self.horizontalLayout_5.addWidget(self.chooseiconbtn)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label6 = QLabel(self.centralwidget)
        self.label6.setObjectName(u"label6")

        self.horizontalLayout_6.addWidget(self.label6)

        self.appmode = QCheckBox(self.centralwidget)
        self.appmode.setObjectName(u"appmode")

        self.horizontalLayout_6.addWidget(self.appmode)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)

        self.createwa = QPushButton(self.centralwidget)
        self.createwa.setObjectName(u"createwa")

        self.horizontalLayout_7.addWidget(self.createwa)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Web App Manager", None))
        self.label1.setText(QCoreApplication.translate("MainWindow", u"Website name:", None))
        self.label2.setText(QCoreApplication.translate("MainWindow", u"URL of the website:", None))
        self.label3.setText(QCoreApplication.translate("MainWindow", u"Select browser:", None))
        self.label4.setText(QCoreApplication.translate("MainWindow", u"Select browser mode:", None))
        self.label5.setText(QCoreApplication.translate("MainWindow", u"Select icon:", None))
        self.chooseiconbtn.setText(QCoreApplication.translate("MainWindow", u"Select an icon", None))
        self.label6.setText(QCoreApplication.translate("MainWindow", u"App mode:", None))
        self.appmode.setText("")
        self.createwa.setText(QCoreApplication.translate("MainWindow", u"Create Web App", None))
    # retranslateUi

