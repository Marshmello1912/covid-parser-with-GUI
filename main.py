import sys

import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from bs4 import BeautifulSoup


def parse():
    urt = 'https://стопкоронавирус.рф'
    headers1 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 OPR/68.0.3618.206'}

    response = requests.get(urt, headers=headers1)

    soup = BeautifulSoup(response.content, 'html.parser')

    items = soup.find_all('div', class_='cv-countdown__item')
    asd = []
    for item in items:
        asd.append(item.find('div', class_='cv-countdown__item-value').getText())

    return asd


def parse_world():
    url = 'https://www.worldometers.info/coronavirus/'
    headers1 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 OPR/68.0.3618.206'}
    response = requests.get(url, headers=headers1)

    soup = BeautifulSoup(response.content, 'html.parser')

    items = soup.find_all('div', id='maincounter-wrap')
    asd = []
    for item in items:
        asd.append(item.find('div', class_='maincounter-number').getText().strip())
    return asd



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(600, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(40)
        sizePolicy.setVerticalStretch(41)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(600, 600))
        MainWindow.setMaximumSize(QtCore.QSize(600, 600))
        MainWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setStyleSheet("")
        MainWindow.setIconSize(QtCore.QSize(24, 24))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setAnimated(False)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 571, 481))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(4, 520, 290, 51))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setMouseTracking(False)
        self.pushButton.setStyleSheet(".QPushButton{\n"
"background-color: rgb(225, 225, 225);\n"
"border-radius: 20px\n"
"}\n"
"\n"
".QPushButton:hover{\n"
"border: solid red 20px;\n"
"background-color: rgb(132, 142, 202);\n"
"border-radius:20px;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(306, 520, 290, 51))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setMouseTracking(True)
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet(".QPushButton{\n"
"background-color: rgb(225, 225, 225);\n"
"border-radius: 20px\n"
"}\n"
"\n"
".QPushButton:hover{\n"
"border: solid red 20px;\n"
"background-color: rgb(132, 142, 202);\n"
"border-radius:20px;\n"
"}")
        self.pushButton_2.setInputMethodHints(QtCore.Qt.ImhNone)
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setDefault(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-10, -10, 611, 611))
        self.frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.483, y1:0.142045, x2:0.534, y2:1, stop:0 rgba(174, 174, 174, 246), stop:1 rgba(255, 255, 255, 255));")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.raise_()
        self.label.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Statistics covid-19"))
        self.pushButton.setText(_translate("MainWindow", "Получить статистику по РФ"))
        self.pushButton_2.setText(_translate("MainWindow", "Получить статистику по миру"))

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()


def pb():
    a = parse()
    ui.label.setText(f'Выявлено заболеваний: {a[1]}\n'
                     f'Выявлено за последние сутки: {a[2]}\n'
                     f'Выздоровело: {a[3]}\n'
                     f'Умерло: {a[4]}')

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(441, 397)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(90, 0, 261, 421))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "TextLabel"))
def pb2():
    a = parse_world()
    ui.label.setText(f'Выявлено заболеваний: {a[0]}\n'
                     f'Выздоровело: {a[2]}\n'
                     f'Умерло: {a[1]}')


ui.pushButton.clicked.connect(pb)
ui.pushButton_2.clicked.connect(pb2)
sys.exit(app.exec_())
