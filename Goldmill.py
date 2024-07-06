import sys
# from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog 
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QCursor
from PyQt5 import QtGui, QtCore

#create a dict of global widgets
widgets = {
    "logo": [],
    "button": [], 
    "score": [],
    "question": []
}

def main():
    app = QApplication(sys.argv)
    grid = QGridLayout()

    window = QWidget()
    window.setWindowTitle("Goldmill-tester")
    window.setGeometry(750,100,500, 500)
    #you can simply use css commands
    window.setStyleSheet("background-color: #2F4F4F;")
    def main_menu():
        logo_image = QPixmap("rocky_logo.png")
        logo  = QLabel()
        logo.setPixmap(logo_image)
        #the alignment flag makes the logo fixed always in the middle of the window (horisontally, because of the H, AlignCenter makes it fixet exactly in the middle)
        logo.setStyleSheet("margin-top: 100px;")
        widgets["logo"].append(logo)

        #creating button widget
        button = QPushButton("PLAY")
        button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        button.setStyleSheet(
            "*{border: 4px solid '#8B0000';" +
            "border-radius: 15px;" +
            "font-size: 35px;" +
            "color: 'white';" + 
            "padding: 25px 0;}"  + 
            #hover event
            "*:hover{background: '#8B0000';}"
                            )
        # button.setStyleSheet("margin-bottom: 100px;")
        widgets["button"].append(button)

        #I add global wigdets, [-1] for the last version
        grid.addWidget(widgets["logo"][-1], 0, 0, alignment=QtCore.Qt.AlignHCenter)
        grid.addWidget(widgets["button"][-1], 1, 0)
    def frame():
        score = QLabel("80")
        score.setAlignment(QtCore.Qt.AlignRight)
        score.setStyleSheet(
             "*{border: 4px solid '#8B0000';" +
            "border-radius: 15px;" +
            "font-size: 35px;" +
            "color: 'white';" + 
            "padding: 25px 0;}"  + 
            #hover event
            "*:hover{background: '#8B0000';}"
        )
        widgets["score"].append(score)
        question = QLabel("Pytanie za 100000 pkt")
        question.setAlignment(QtCore.Qt.AlignCenter)
        #some questions will be shoreter, some longer, the text should wrap
        question.setWordWrap(True)
        question.setStyleSheet(
             "*{border: 4px solid '#8B0000';" +
            "border-radius: 15px;" +
            "font-size: 35px;" +
            "color: 'white';" + 
            "padding: 25px 0;}")
        widgets["question"].append(question)
        grid.addWidget(widgets["score"][-1], 0, 1)
        grid.addWidget(widgets["question"][-1], 1, 0, 1, 2 )

    # main_menu()
    frame()
    window.setLayout(grid)
    #statement at the end to show and exit 
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
