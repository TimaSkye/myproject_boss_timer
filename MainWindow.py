"""Сгенерированно при помощи pyuic. Разработано в QT Designer."""
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModality.NonModal)
        MainWindow.resize(322, 294)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(322, 294))
        MainWindow.setMaximumSize(QtCore.QSize(322, 294))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 321, 271))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_naga = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.btn_naga.setObjectName("btn_naga")
        self.gridLayout.addWidget(self.btn_naga, 8, 1, 1, 1)
        self.btn_pixi = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.btn_pixi.setObjectName("btn_pixi")
        self.gridLayout.addWidget(self.btn_pixi, 6, 1, 1, 1)
        self.btn_lancer = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.btn_lancer.setObjectName("btn_lancer")
        self.gridLayout.addWidget(self.btn_lancer, 8, 8, 1, 1)
        self.btn_gvard = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.btn_gvard.setObjectName("btn_gvard")
        self.gridLayout.addWidget(self.btn_gvard, 8, 0, 1, 1)
        self.btn_scare = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.btn_scare.setObjectName("btn_scare")
        self.gridLayout.addWidget(self.btn_scare, 6, 8, 1, 1)
        self.btn_kurolisk = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.btn_kurolisk.setObjectName("btn_kurolisk")
        self.gridLayout.addWidget(self.btn_kurolisk, 6, 0, 1, 1)
        self.btn_vasilisk = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.btn_vasilisk.setObjectName("btn_vasilisk")
        self.gridLayout.addWidget(self.btn_vasilisk, 0, 0, 1, 1)
        self.btn_sirena = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.btn_sirena.setObjectName("btn_sirena")
        self.gridLayout.addWidget(self.btn_sirena, 0, 8, 1, 1)
        self.btn_kuru = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.btn_kuru.setObjectName("btn_kuru")
        self.gridLayout.addWidget(self.btn_kuru, 0, 1, 1, 1)
        self.btn_triton = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.btn_triton.setObjectName("btn_triton")
        self.gridLayout.addWidget(self.btn_triton, 2, 8, 1, 1)
        self.btn_orc = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.btn_orc.setObjectName("btn_orc")
        self.gridLayout.addWidget(self.btn_orc, 4, 1, 1, 1)
        self.btn_troll = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.btn_troll.setObjectName("btn_troll")
        self.gridLayout.addWidget(self.btn_troll, 3, 8, 1, 1)
        self.btn_ogr = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.btn_ogr.setObjectName("btn_ogr")
        self.gridLayout.addWidget(self.btn_ogr, 3, 1, 1, 1)
        self.btn_kobold = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.btn_kobold.setObjectName("btn_kobold")
        self.gridLayout.addWidget(self.btn_kobold, 5, 0, 1, 1)
        self.btn_kaballo = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.btn_kaballo.setObjectName("btn_kaballo")
        self.gridLayout.addWidget(self.btn_kaballo, 4, 0, 1, 1)
        self.btn_flind = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.btn_flind.setObjectName("btn_flind")
        self.gridLayout.addWidget(self.btn_flind, 4, 8, 1, 1)
        self.btn_garpy = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.btn_garpy.setObjectName("btn_garpy")
        self.gridLayout.addWidget(self.btn_garpy, 1, 0, 1, 1)
        self.btn_gigant = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.btn_gigant.setObjectName("btn_gigant")
        self.gridLayout.addWidget(self.btn_gigant, 2, 0, 1, 1)
        self.btn_minotaur = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.btn_minotaur.setObjectName("btn_minotaur")
        self.gridLayout.addWidget(self.btn_minotaur, 2, 1, 1, 1)
        self.btn_chabon = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.btn_chabon.setObjectName("btn_chabon")
        self.gridLayout.addWidget(self.btn_chabon, 5, 8, 1, 1)
        self.btn_bug = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.btn_bug.setObjectName("btn_bug")
        self.gridLayout.addWidget(self.btn_bug, 3, 0, 1, 1)
        self.btn_leprikon = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.btn_leprikon.setObjectName("btn_leprikon")
        self.gridLayout.addWidget(self.btn_leprikon, 1, 1, 1, 1)
        self.btn_skelet = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.btn_skelet.setObjectName("btn_skelet")
        self.gridLayout.addWidget(self.btn_skelet, 1, 8, 1, 1)
        self.btn_spider = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.btn_spider.setObjectName("btn_spider")
        self.gridLayout.addWidget(self.btn_spider, 5, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_next_info = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_next_info.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_next_info.setObjectName("label_next_info")
        self.verticalLayout_2.addWidget(self.label_next_info)
        self.label_next = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_next.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignTop)
        self.label_next.setObjectName("label_next")
        self.verticalLayout_2.addWidget(self.label_next)
        self.gridLayout.addLayout(self.verticalLayout_2, 9, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_now_info = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_now_info.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_now_info.setObjectName("label_now_info")
        self.verticalLayout.addWidget(self.label_now_info)
        self.label_now = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_now.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignTop)
        self.label_now.setObjectName("label_now")
        self.verticalLayout.addWidget(self.label_now)
        self.gridLayout.addLayout(self.verticalLayout, 9, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label__timer_info = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label__timer_info.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label__timer_info.setObjectName("label__timer_info")
        self.verticalLayout_3.addWidget(self.label__timer_info)
        self.label_timer = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_timer.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignTop)
        self.label_timer.setObjectName("label_timer")
        self.verticalLayout_3.addWidget(self.label_timer)
        self.gridLayout.addLayout(self.verticalLayout_3, 9, 8, 1, 1)
        self.btn_scaner = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_scaner.setGeometry(QtCore.QRect(0, 270, 321, 23))
        self.btn_scaner.setObjectName("btn_scaner")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Таймер боссов R2 Online"))
        self.btn_naga.setText(_translate("MainWindow", "Нага-королева"))
        self.btn_pixi.setText(_translate("MainWindow", "Королева Мав"))
        self.btn_lancer.setText(_translate("MainWindow", "Копейщик Акрионцев"))
        self.btn_gvard.setText(_translate("MainWindow", "Гвардеец-Защитник"))
        self.btn_scare.setText(_translate("MainWindow", "Шрам"))
        self.btn_kurolisk.setText(_translate("MainWindow", "Лесной куролиск"))
        self.btn_vasilisk.setText(_translate("MainWindow", "Гигантский Василиск"))
        self.btn_sirena.setText(_translate("MainWindow", "Сирена"))
        self.btn_kuru.setText(_translate("MainWindow", "Куру"))
        self.btn_triton.setText(_translate("MainWindow", "Гигантский тритон"))
        self.btn_orc.setText(_translate("MainWindow", "Руум"))
        self.btn_troll.setText(_translate("MainWindow", "Большой тролль-воин"))
        self.btn_ogr.setText(_translate("MainWindow", "Огр-воин"))
        self.btn_kobold.setText(_translate("MainWindow", "Командир кобольдов"))
        self.btn_kaballo.setText(_translate("MainWindow", "Кабалло"))
        self.btn_flind.setText(_translate("MainWindow", "Флинд мечник"))
        self.btn_garpy.setText(_translate("MainWindow", "Королева Гарпий"))
        self.btn_gigant.setText(_translate("MainWindow", "Вождь Гигантов"))
        self.btn_minotaur.setText(_translate("MainWindow", "Минотавр-воин"))
        self.btn_chabon.setText(_translate("MainWindow", "Чабон"))
        self.btn_bug.setText(_translate("MainWindow", "Стальной жук"))
        self.btn_leprikon.setText(_translate("MainWindow", "Король Ракум"))
        self.btn_skelet.setText(_translate("MainWindow", "Крепкий скелет"))
        self.btn_spider.setText(_translate("MainWindow", "Паук-птицеед"))
        self.label_next_info.setText(_translate("MainWindow", "Следующий"))
        self.label_next.setText(_translate("MainWindow", "Имя босса"))
        self.label_now_info.setText(_translate("MainWindow", "Убит"))
        self.label_now.setText(_translate("MainWindow", "Имя босса"))
        self.label__timer_info.setText(_translate("MainWindow", "Таймер до следующего"))
        self.label_timer.setText(_translate("MainWindow", "Таймер"))
        self.btn_scaner.setText(_translate("MainWindow", "Сканнер боссов"))
