from PyQt6.QtWidgets import QWidget, QTextBrowser, QGridLayout, QLabel, QLineEdit
from PyQt6.QtCore import pyqtSlot, Qt, QSize


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        self.bin_label=QLabel("Binärzahl")
        self.hex_label=QLabel("Hexadezimalzahl")

        self.bin_edit =QLineEdit()
        self.bin_edit.setInputMask("Bbbbbbbb")
        self.hex_edit =QLineEdit()
        self.hex_edit.setInputMask("Hhhhhhhh")

        self.browser = QTextBrowser()

        layout = QGridLayout(self)
        layout.addWidget(self.bin_label, 1, 1)
        layout.addWidget(self.bin_edit, 1, 2)
        layout.addWidget(self.hex_label, 2, 1)
        layout.addWidget(self.hex_edit, 2, 2)
        layout.addWidget(self.browser, 3, 2)

        self.bin_edit.setText("0")
        self.hex_edit.setText("0")

        self.bin_edit.editingFinished.connect(self.calc)
        self.hex_edit.editingFinished.connect(self.calc)

    @pyqtSlot()
    def calc(self):
        if self.bin_edit !="0" and self.hex_edit !="0":
            self.browser.append(self.bin_edit.text()+"+"+self.hex_edit.text())
        else:
            print("fehler")


        