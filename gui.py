from PyQt5.QtWidgets import (QMainWindow,
                            QVBoxLayout,
                            QGridLayout,
                            QPlainTextEdit,
                            QPushButton,
                            QMenu,
                            QAction,
                            QWidget,
                            qApp)


class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.InitWindow()
        self.InitWidgets()
        self.show()


    def InitWindow(self):
        """method to initialize the window"""
        
        self.setGeometry(700, 100, 500, 700)
        self.setWindowTitle("Simple Text Editor")
        self.statusBar().showMessage("Hello User :)")

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")

        open_act = QAction("Open", self)
        open_act.setStatusTip("Open a File. (WIP)")
        file_menu.addAction(open_act)

        exit_act = QAction("Exit", self)
        exit_act.setStatusTip("Exit App.")
        exit_act.triggered.connect(qApp.quit)
        file_menu.addAction(exit_act)


    def InitWidgets(self):
        """method to initialize widgets and layouts"""
        
        widget = QWidget(self)
        self.setCentralWidget(widget)

        text_edit = QPlainTextEdit()

        grid = QGridLayout()
        grid.addWidget(text_edit, 0, 1)

        widget.setLayout(grid)
