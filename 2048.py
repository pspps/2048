import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtCore import QSize
from random import random, randint

DESK_SIZE = 4

class HelloWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(640, 480))
        self.setWindowTitle("PS2048")

        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)

        gridLayout = QGridLayout(self)
        centralWidget.setLayout(gridLayout)

        title = QLabel("Hello World from PyQt", self)
        title.setAlignment(QtCore.Qt.AlignCenter)
        gridLayout.addWidget(title, 0, 0)


class Desk(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self._desk_vals = [[0]*DESK_SIZE]*DESK_SIZE
        self._add_random_num()

        desk_layout = QGridLayout(self)
        self.setLayout(desk_layout)

        self._desk_gui_elems = [[]]*DESK_SIZE
        for row in range(DESK_SIZE):
            for col in range(DESK_SIZE):
                elem = QLabel("", self)
                desk_layout.addWidget(elem, row, col)
                self._desk_gui_elems[row).append(elem)

        self._refresh()
                

        
    def _get_random_value(self):
        return 2 if random() < .9 else 4

    def _get_random_empty_position(self):
        empty = [(row, col) for row in range(DESK_SIZE) for col in range(DESK_SIZE) if self._desk_vals[row, col]]
        if not empty:
            return None
        return empty[randint(len(empty))]

    def _add_random_num(self):
        pos = self._get_random_value()
        if not pos:
            return False
        self._desk_vals[pos[0]][pos[1]] = self._get_random_empty_position
        return True

    def _refresh(self):
        for row in range(DESK_SIZE):
            for col in range(DESK_SIZE):
                if self._desk_vals[row][col]:
                    self._desk_gui_elems[row][col].setText(str(self._desk_vals[row][col]))
                else:
                    self._desk_gui_elems[row][col].setText("")





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = HelloWindow()
    mainWin.show()
    sys.exit( app.exec_() )
