import sys
# from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog 
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QCursor
from PyQt5 import QtGui, QtCore

def main():
    app = QApplication(sys.argv)
    grid = QGridLayout()

    window = QWidget()
    window.setWindowTitle("Goldmill-tester")
    window.setGeometry(750,100,500, 500)
    #you can simply use css commands
    window.setStyleSheet("background-color: #2F4F4F;")

    logo_image = QPixmap("rocky_logo.png")
    logo  = QLabel()
    logo.setPixmap(logo_image)
    #the alignment flag makes the logo fixed always in the middle of the window (horisontally, because of the H, AlignCenter makes it fixet exactly in the middle)
    logo.setStyleSheet("margin-top: 100px;")

    #cerating button widget
    button = QPushButton("PLAY")
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setStyleSheet(
        "border: 4px solid 'BC006C';" +
        "border-radius: 15px;" +
        "font-size: 35px;" +
        "color: 'white';"
                         )
    # button.setStyleSheet("margin-bottom: 100px;")

    grid.addWidget(logo, 0, 0, alignment=QtCore.Qt.AlignHCenter)
    grid.addWidget(button, 1, 0)

    window.setLayout(grid)
    #statement at the end to show and exit 
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
