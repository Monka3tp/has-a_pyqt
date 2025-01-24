import sys

from PyQt6.QtWidgets import QDialog, QApplication

from layout import Ui_Dialog
import random

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.generujButton.clicked.connect(self.generuj_haslo)
        self.show()

    duze_litery = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O","P", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    male_litery = ["a", "b", "c", "d","e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t","u", "v", "w", "x", "y", "z"]
    cyfry = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    znaki_specjalne = ["!", "-", "@", "#"]

    def generuj_haslo(self):
        dlugosc = int(self.ui.znakEdit.text())
        znaki = ""
        if self.ui.literyBox.isChecked():
            znaki += random.choice(self.duze_litery) + random.choice(self.male_litery)
        elif self.ui.cyfryBox.isChecked():
            znaki += random.choice(self.cyfry)
        elif self.ui.znakiSpecjalneBox.isChecked():
            znaki += random.choice(self.znaki_specjalne)

        haslo = "".join(random.choice(znaki))
        print(haslo)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyForm()
    sys.exit(app.exec())