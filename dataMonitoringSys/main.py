import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QLabel

class COZADashBoard(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setWindowTitle('COZA BED IoT : MONITORING DASHBOARD')
        self.setGeometry(300, 300, 960, 720)

        # Left pannel
        layout_left = QVBoxLayout()
        layout_left.setAlignment(Qt.AlignTop)

        # Right data pannel
        layout_right = QVBoxLayout()

        # Layout
        layout = QHBoxLayout()
        layout.addLayout(layout_left)
        layout.addLayout(layout_right)

        layout.setStretchFactor(layout_left, 2)
        layout.setStretchFactor(layout_right, 8)

        # Add some widget to the layout
        layout_left.addWidget(QLabel("OVERVIEW"))

        layout_right.addWidget(QLabel("Data view pannel"))

        self.setLayout(layout)

        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    dashBoard = COZADashBoard()
    sys.exit(app.exec_())