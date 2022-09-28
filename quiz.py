
from PyQt5 import QtCore,QtGui,QtWidgets
import random 
import time

import mysql.connector
from mysql.connector.constants import ClientFlag


config = {
    'user': 'root',
    'password': 'Noor@@1628',
    'host': '35.230.139.221',
    'client_flags': [ClientFlag.SSL],
    'ssl_ca': 'ssl/server-ca.pem',
    'ssl_cert': 'ssl/client-cert.pem',
    'ssl_key': 'ssl/client-key.pem'
}

cnxn = mysql.connector.connect(**config)

cursor = cnxn.cursor()  # initialize connection cursor
cnxn = mysql.connector.connect(**config)
cursor = cnxn.cursor()
cursor.execute('use testdb')  # create a new 'testdb' database
cursor.execute("SELECT * FROM Quiz")
res = cursor.fetchall()
print(res)



def fetch_question():
    questiondetails = []
    questionNumber = random.randint(0,(len(res)-1))
    for j in res[questionNumber]:
        questiondetails.append(j)
        print(questiondetails)
    number,question,answer = questiondetails
    return number,question,answer


def get_colors():
    color = [['e63946','f1faee','a8dadc','457b9d','1d3557'],['264653','2a9d8f','e9c46a','f4a261','e76f51'],['2b2d42','8d99ae','edf2f4','ef233c','d90429'],['f72585','7209b7','3a0ca3','4361ee','4cc9f0'],['132a13','31572c','4f772d','90a955','ecf39e'],['ff6700','ebebeb','c0c0c0','3a6ea5','004e98'],['00a6fb','0582ca','006494','003554','051923'],['faf0e6','eb9e65','ff6700','406680','0e161b'],['064287','f2682b','ffffff','f2682b','064287']]
    labelcolor = []

    colorint = random.randint(0,(len(color)-1))
    for i in color[colorint]:
        labelcolor.append(i)
    return labelcolor


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.number,self.question,self.answer = fetch_question()
        self.labelcolor = get_colors()
        self.MainWindow = MainWindow
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(300, 400)
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 25, 300, 200))
        self.label.setAlignment(QtCore.Qt.AlignCenter)           # X-axis,y-axis, width,height
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(110, 290, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(75, 240, 82, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(75, 260, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 300, 80))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 80, 300, 80))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 160, 300, 80))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 240, 300, 80))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(0, 320, 300, 80))
        self.label_6.setObjectName("label_6")
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label.raise_()
        self.pushButton.raise_()
        self.radioButton.raise_()
        self.radioButton_2.raise_()
        self.label.setFont(QtGui.QFont('MS UI Gothic', 20))

        self.radioButton.setFont(QtGui.QFont('MS UI Gothic', 15))
        self.radioButton_2.setFont(QtGui.QFont('MS UI Gothic', 15))		
        self.label_2.setStyleSheet("background-color: #"+self.labelcolor[0])
        self.label_3.setStyleSheet("background-color: #"+self.labelcolor[1])
        self.label_4.setStyleSheet("background-color: #"+self.labelcolor[2])
        self.label_5.setStyleSheet("background-color: #"+self.labelcolor[3])
        self.label_6.setStyleSheet("background-color: #"+self.labelcolor[4])
        self.MainWindow.setCentralWidget(self.centralwidget)
        self.pushButton.clicked.connect(self.checkbuttonClick)
        self.MainWindow.showNormal()
        self.location_on_the_screen()
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", self.question ))
        self.pushButton.setText(_translate("MainWindow", "Check"))
        self.radioButton.setText(_translate("MainWindow", "True"))
        self.radioButton_2.setText(_translate("MainWindow", "False"))
        self.label_2.setText(_translate("MainWindow", ""))
        self.label_3.setText(_translate("MainWindow", ""))
        self.label_4.setText(_translate("MainWindow", ""))
        self.label_5.setText(_translate("MainWindow", ""))
        self.label_6.setText(_translate("MainWindow", ""))

    def checkbuttonClick(self):
        true_checked = self.radioButton.isChecked()
        false_checked = self.radioButton_2.isChecked() 

        if (true_checked == True and self.answer == '1'):
            title = "You have chosen the right answer" 
            text = "Your Answer: True\nCorrect Answer: True"

        elif (false_checked == True and self.answer == '0'):
            title = "You have chosen the right answer" 
            text = "Your Answer: False\nCorrect Answer: False"

        elif(true_checked == True and self.answer == '0'):
            title = "You have chosen the wrong answer" 
            text = "Correct Answer: False"
        
        elif(false_checked == True and self.answer == '1'):
            title = "You have chosen the wrong answer" 
            text = "Correct Answer: True"

        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(text)

        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setDefaultButton(QtWidgets.QMessageBox.Ok)
        msg.exec_()

        self.MainWindow.showMinimized()
        time.sleep(10)
        
        self.MainWindow.showNormal()
        self.newWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.newWindow)
        self.newWindow.show()
        self.newWindow.setWindowState(QtCore.Qt.WindowNoState)
        self.MainWindow.close()
        
    def location_on_the_screen(self):
        ag = QtWidgets.QDesktopWidget().availableGeometry()
        sg = QtWidgets.QDesktopWidget().screenGeometry()

        screen = self.MainWindow.geometry()
        x = ag.width() - screen.width()
        y = 2 * ag.height() - sg.height() - screen.height()
        self.MainWindow.move(x, y)
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
