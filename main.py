import sys
import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.do_paint = False
        uic.loadUi('main.ui', self)
        self.pushButton.clicked.connect(self.read)
        con = sqlite3.connect('coffe.sqlite')
        cur = con.cursor()
        self.res = cur.execute('''SELECT * FROM COFFE''')

    def read(self):
        for i in self.res:
            self.Zap.addItem(('    '.join(list(map(str, list(i))))))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())
