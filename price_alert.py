from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import smtplib
import schedule
import time
import requests
from urllib.request import urlopen as get_url
from bs4 import BeautifulSoup as soup
import sys
import re

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_Dialog(QWidget):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(688, 578)

        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet(
            "QWidget#Dialog {background-image: url('data/logo.png');background-repeat: no-repeat; background-position: bottom right;}")
       
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("data\icon.ico")),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.servername = QtGui.QLineEdit(Dialog)
        self.servername.setGeometry(QtCore.QRect(180, 120, 191, 20))
        self.servername.setObjectName(_fromUtf8("servername"))
        self.port = QtGui.QLineEdit(Dialog)
        self.port.setGeometry(QtCore.QRect(180, 160, 191, 20))
        self.port.setObjectName(_fromUtf8("port"))
        self.mailid = QtGui.QLineEdit(Dialog)
        self.mailid.setGeometry(QtCore.QRect(180, 210, 191, 20))
        self.mailid.setObjectName(_fromUtf8("mailid"))
        self.password = QtGui.QLineEdit(Dialog)
        self.password.setGeometry(QtCore.QRect(180, 250, 191, 20))
        self.password.setObjectName(_fromUtf8("password"))
        self.password.setEchoMode(QtGui.QLineEdit.Password)
        self.tomail = QtGui.QLineEdit(Dialog)
        self.tomail.setGeometry(QtCore.QRect(180, 290, 191, 20))
        self.tomail.setObjectName(_fromUtf8("tomail"))
        self.url = QtGui.QTextEdit(Dialog)
        self.url.setGeometry(QtCore.QRect(180, 340, 371, 71))
        self.url.setObjectName(_fromUtf8("url"))
        self.price = QtGui.QLineEdit(Dialog)
        self.price.setGeometry(QtCore.QRect(190, 440, 113, 20))
        self.price.setObjectName(_fromUtf8("price"))
        self.label2 = QtGui.QLabel(Dialog)
        self.label2.setGeometry(QtCore.QRect(20, 80, 111, 16))
        self.label2.setObjectName(_fromUtf8("label2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 101, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 160, 91, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 210, 81, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 250, 81, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(20, 290, 71, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(20, 370, 101, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(20, 440, 151, 20))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_1 = QtGui.QLabel(Dialog)
        self.label_1.setGeometry(QtCore.QRect(20, 50, 101, 16))
        self.label_1.setObjectName(_fromUtf8("label_1"))
        self.flipkart = QtGui.QRadioButton(Dialog)
        self.flipkart.setGeometry(QtCore.QRect(180, 50, 82, 17))
        self.flipkart.setCheckable(True)
        self.flipkart.setChecked(True)
        self.flipkart.setAutoExclusive(True)
        self.flipkart.setObjectName(_fromUtf8("flipkart"))
        self.buttonGroup = QtGui.QButtonGroup(Dialog)
        self.buttonGroup.setObjectName(_fromUtf8("buttonGroup"))
        self.buttonGroup.addButton(self.flipkart)
        self.Amazon = QtGui.QRadioButton(Dialog)
        self.Amazon.setGeometry(QtCore.QRect(300, 50, 82, 17))
        self.Amazon.setCheckable(True)
        self.Amazon.setChecked(False)
        self.Amazon.setObjectName(_fromUtf8("Amazon"))
        self.buttonGroup.addButton(self.Amazon)
        self.spinBox = QtGui.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(230, 490, 42, 22))
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(24)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.label_10 = QtGui.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(20, 490, 161, 16))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.Gmail = QtGui.QRadioButton(Dialog)
        self.Gmail.setGeometry(QtCore.QRect(180, 80, 82, 17))
        self.Gmail.setChecked(True)
        self.Gmail.setAutoRepeat(False)
        self.Gmail.setObjectName(_fromUtf8("Gmail"))
        self.Gmail.toggled.connect(lambda: self.btnstate(self.Gmail))
        self.buttonGroup_2 = QtGui.QButtonGroup(Dialog)
        self.buttonGroup_2.setObjectName(_fromUtf8("buttonGroup_2"))
        self.buttonGroup_2.addButton(self.Gmail)
        self.other = QtGui.QRadioButton(Dialog)
        self.other.setGeometry(QtCore.QRect(300, 80, 82, 17))
        self.other.setAutoRepeat(False)
        self.other.setObjectName(_fromUtf8("other"))
        self.other.toggled.connect(lambda: self.btnstate(self.other))
        self.buttonGroup_2.addButton(self.other)
        self.submit = QtGui.QPushButton(Dialog)
        self.submit.setGeometry(QtCore.QRect(330, 540, 75, 23))
        self.submit.setObjectName(_fromUtf8("submit"))
        self.submit.clicked.connect(self.submit_)
        self.Exit = QtGui.QPushButton(Dialog)
        self.Exit.setGeometry(QtCore.QRect(470, 540, 75, 23))
        self.Exit.setObjectName(_fromUtf8("Exit"))
        self.Exit.clicked.connect(self.exit_)
        self.label_11 = QtGui.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(330, 420, 351, 111))
        self.label_11.setObjectName(_fromUtf8("label_11"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Price Tracker", None))
        self.servername.setText(_translate("Dialog", "smtp.gmail.com", None))
        self.port.setText(_translate("Dialog", "587", None))
        self.label2.setText(_translate("Dialog", "Select Mail Server", None))
        self.label_3.setText(_translate("Dialog", "SMTP Server Name", None))
        self.label_4.setText(_translate("Dialog", "Port Number", None))
        self.label_5.setText(_translate("Dialog", "Email Address", None))
        self.label_6.setText(_translate("Dialog", "Password", None))
        self.label_7.setText(_translate("Dialog", "To Mail Id", None))
        self.label_8.setText(_translate("Dialog", "Url of the Product", None))
        self.label_9.setText(_translate("Dialog", "Price range", None))
        self.label_1.setText(_translate("Dialog", "Select Website", None))
        self.flipkart.setText(_translate("Dialog", "Flipkart", None))
        self.Amazon.setText(_translate("Dialog", "Amazon", None))
        self.label_10.setText(_translate(
            "Dialog", "Set Hours for checking the price", None))
        self.Gmail.setText(_translate("Dialog", "Gmail", None))
        self.other.setText(_translate("Dialog", "Other", None))
        self.submit.setText(_translate("Dialog", "Submit", None))
        self.Exit.setText(_translate("Dialog", "Exit", None))
        self.label_11.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">Note</span>:1. If using gmail account you need turn off only allow secure apps</p><p>2. Enter SMTP Sever Name correctly of your respective service provider</p><p>3. Set Hours wisely for better results</p><p><span style=\" font-weight:600; text-decoration: underline;\">Contact</span><span style=\" font-weight:600;\">: </span>Akhil</p><p>                 MadeWithPY009@gmail.com</p><p><br/></p></body></html>", None))

    def btnstate(self, b):

        if self.Gmail.isChecked() == True:
            self.servername.setText('smtp.gmail.com')
            self.port.setText('587')

        if self.other.isChecked() == True:
            self.servername.clear()
            self.port.clear()

    def submit_(self):
        global smtp, port, user_email_id, user_email_password, to_email_id, url_, price, hour
        smtp = self.servername.text()
        port = self.port.text()
        user_email_id = self.mailid.text()
        user_email_password = self.password.text()
        to_email_id = self.tomail.text()
        url_ = self.url.toPlainText()
        price = int(self.price.text())
        hour = self.spinBox.value()
        if self.flipkart.isChecked() == True:
            schedule.every(hour).hours.do(self.flipkart_)
            while True:
                schedule.run_pending()
                time.sleep(1)
        else:
            schedule.every(hour).hours.do(self.amazon_)
            while True:
                schedule.run_pending()
                time.sleep(1)

    def flipkart_(self):
        web_page = get_url(url_)
        page_html = web_page.read()
        web_page.close()
        page_data = soup(page_html, "html.parser")
        current_price = page_data.find(
            "div", {"class": "_1vC4OE _3qQ9m1"}).text
        current_price = int(current_price[1:].replace(',', '', 3))
        if current_price <= price:
            s = smtplib.SMTP(smtp, port)
            s.starttls()
            s.login(user_email_id, user_email_password)
            header = 'To:' + to_email_id + '\n' + 'From: ' + user_email_id + \
                '\n' + 'Subject:URGENT PRICE ALERT BUY QUICKLY \n'
            message = header + '\n Lucky! item price as been drop u can have it now! \n\n'
            s.sendmail(user_email_id, to_email_id, message)
            print('Price alert')
            s.quit()
            sys.exit(0)

    def amazon_(self):
        web_page = get_url(url_)
        page_html = web_page.read()
        web_page.close()
        page_data = soup(page_html, "html.parser")
        current_price = page_data.find(
            "span", {"class": "a-size-medium a-color-price priceBlockBuyingPriceString"}).text
        current_price = re.findall("[0-9].+", a)
        current_price = ''.join(map(str, x))
        current_price = int(listToStr.rpartition('.')[0].replace(',', '', 3))

        if current_price <= price:
            s = smtplib.SMTP(smtp, port)
            s.starttls()
            s.login(user_email_id, user_email_password)
            header = 'To:' + to_email_id + '\n' + 'From: ' + user_email_id + \
                '\n' + 'Subject:URGENT PRICE ALERT BUY QUICKLY \n'
            message = header + '\n Lucky! item price as been drop u can have it now! \n\n'
            s.sendmail(user_email_id, to_email_id, message)
            print('Price alert')
            s.quit()
            sys.exit(0)

    def exit_(self):
        sys.exit(0)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
