import sys
# from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog 
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QCursor
from PyQt5 import QtGui, QtCore

def main():
    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle("Goldmill-tester")
    window.setGeometry(750,100,500, 500)
    #you can simply use css commands
    window.setStyleSheet("background-color: #2F4F4F;")
    #creating layout, with grid there were some issues, it centers vertically when I only want to center hirozontally
    # grid = QGridLayout() 
    main_layout = QVBoxLayout()
    main_layout.setContentsMargins(0, 0, 0, 0)
    main_layout.setSpacing(0)
    # Create a top spacer with fixed height
    top_spacer = QWidget()
    top_spacer.setFixedHeight(100)
    main_layout.addWidget(top_spacer)

    logo_image = QPixmap("rocky_logo.png")
    logo  = QLabel()
    logo.setPixmap(logo_image)
    logo.setAlignment(QtCore.Qt.AlignHCenter)  # Ensure the logo is horizontally centered

    # Add the logo to the main layout
    main_layout.addWidget(logo)

    # Add a stretch at the bottom to push everything up
    bottom_stretch = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
    main_layout.addItem(bottom_stretch)

    # Set the main layout for the window
    window.setLayout(main_layout)

    #the alignment flag makes the logo fixed always in the middle of the window (horisontally, because of the H, AlignCenter makes it fixet exactly in the middle)
    # grid.addWidget(logo, 0, 0, alignment=QtCore.Qt.AlignHCenter)
    logo.setStyleSheet("margin-top: 100px;")

    #layout settings
    window.setLayout(main_layout)
    # window.setLayout(grid)
    #statement at the end to show and exit 
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
