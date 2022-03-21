from re import S
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QPushButton,
    QLineEdit,
    QLabel,
    QMessageBox,
)
from PyQt5.Qt import QUrl, QDesktopServices
import requests
import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Client")
        self.setFixedSize(400, 400)

        self.label1 = QLabel("Enter your Hostname:", self)
        self.label1.move(10, 1)
        self.text = QLineEdit(self)
        self.text.move(10, 20)

        self.label10 = QLabel("Enter your API key:", self)
        self.label10.move(10, 60)
        self.text1 = QLineEdit(self)
        self.text1.move(10, 80)

        self.label100 = QLabel("Enter your IP:", self)
        self.label100.move(10, 120)
        self.text10 = QLineEdit(self)
        self.text10.move(10, 140)




        self.label2 = QLabel("Answer:", self)
        self.label2.move(10, 230)
        self.button = QPushButton("Send", self)
        self.button.move(10, 190)

        self.button.clicked.connect(self.on_click)
        self.button.pressed.connect(self.on_click)

        self.show()

    def on_click(self):
        hostname = self.text.text()
        ip = self.text10.text()
        api_key = self.text1.text()

        if hostname == "":
            QMessageBox.about(self, "Error", "Please fill the field")
        else:
            res = self.__query(hostname,ip,api_key)
            
            if res:
                self.label2.setText("\n \n Longitude: %s \n Latitude: %s \n" % (res["Longitude"], res["Latitude"]))
                self.label2.adjustSize()
                self.show()

    def __query(self, hostname, ip, api_key):
        url = "http://%s/ip/%s?key=%s" % (hostname,ip, api_key) 
        r = requests.get(url)
        if r.status_code == requests.codes.NOT_FOUND:
            QMessageBox.about(self, "Error", "IP not found")
        if r.status_code == requests.codes.OK:
            return r.json()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    app.exec_()