import sys

from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton)
from PyQt5.QtGui import QIcon, QFont, QPixmap
#from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI")
        self.setGeometry(100, 150, 500, 500)
        self.setWindowIcon(QIcon("New boltu.jpg"))
        self.button = QPushButton("Click me", self)
        self.label = QLabel("hello", self)
        self.initUI()

# buttons
    def initUI(self):
        self.button.setGeometry(150, 200, 200, 100)
        self.button.setStyleSheet("font-size: 30px;")
        self.button.clicked.connect(self.on_click)

        self.label.setGeometry(150, 300, 200, 100)
        self.label.setStyleSheet("font-size: 50px;")

    def on_click(self):
       # print("button clicked")
       # self.button.setText("Clicked")
       # self.button.setDisabled(True)
        self.label.setText("Goodbye")



# layout managers

   # def initUI(self):
       # central_widget = QWidget()
       # self.setCentralWidget(central_widget)

       # label1 = QLabel("#1", self)
       # label2 = QLabel("#2", self)
       # label3 = QLabel("#3", self)
       # label4 = QLabel("#4", self)
       # label5 = QLabel("#5", self)

       # label1.setStyleSheet("background-color: red")
       # label2.setStyleSheet("background-color: green")
       # label3.setStyleSheet("background-color: blue")
       # label4.setStyleSheet("background-color: yellow")
       # label5.setStyleSheet("background-color: purple")

       # grid = QGridLayout()

       # grid.addWidget(label1, 0, 0)
       # grid.addWidget(label2, 0, 1)
       # grid.addWidget(label3, 1, 0)
       # grid.addWidget(label4, 1, 1)
       # grid.addWidget(label5, 1, 2)

       # central_widget.setLayout(grid)



# images

       # label = QLabel(self)
       # label.setGeometry(0, 0, 250, 250)

       # Pixmap = QPixmap("New boltu.jpg")
       # label.setPixmap(Pixmap)

       # label.setScaledContents(True)

       # label.setGeometry((self.width() - label.width()) // 2,
       #                   (self.height() - label.height()) // 2,
       #                   label.width(),
       #                   label.height())



# labels

       # label = QLabel("Hello", self)
       # label.setFont(QFont("Arial", 30))
       # label.setGeometry(0, 0, 500, 50)
       # label.setStyleSheet("color: green;"
       #                     "background-color: red;"
       #                     "font-weight: bold;"
       #                     "font-style: italic;"
       #                     "text-decoration: underline;")

        #label.setAlignment(Qt.AlignTop)
        #label.setAlignment(Qt.AlignBottom)
        #label.setAlignment(Qt.AlignVCenter)

        #label.setAlignment(Qt.AlignRight)
        #label.setAlignment(Qt.AlignLeft)
        #label.setAlignment(Qt.AlignHCenter)

        #label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()