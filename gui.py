from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QGridLayout, QTextEdit, QPushButton, QMenu, QAction, qApp


class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.InitWin()
        self.InitUI()
        self.show()


    def InitWin(self):
        
        self.setGeometry(700, 100, 500, 700)
        self.setWindowTitle("Simple Text Editor by Chewycide")

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")

        exit_act = QAction("Exit", self)
        exit_act.triggered.connect(qApp.quit)
        file_menu.addAction(exit_act)


    def InitUI(self):
        
        pass
