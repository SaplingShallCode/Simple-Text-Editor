from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QTextEdit, QPushButton


class MainWindow(QWidget):

    def __init__(self):

        super().__init__()

        self.InitWin()
        self.InitUI()
        self.show()


    def InitWin(self):
        
        self.setGeometry(700, 100, 500, 700)


    def InitUI(self):
        pass