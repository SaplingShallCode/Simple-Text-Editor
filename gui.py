from distutils import text_file
from PyQt5.QtWidgets import (QMainWindow,
                            QVBoxLayout,
                            QGridLayout,
                            QHBoxLayout,
                            QPlainTextEdit,
                            QPushButton,
                            QMenu,
                            QAction,
                            QWidget,
                            QFileDialog,
                            qApp)
from PyQt5.QtCore import Qt
from buttons import CustomButton


class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.InitWindow()
        self.InitWidgets()
        self.show()


    def InitWindow(self):
        """method to initialize the window"""
        
        self.setGeometry(700, 100, 500, 700)
        self.setMinimumSize(500, 700)
        self.setMaximumSize(1000, 900)
        self.setWindowTitle("Simple Text Editor")
        self.statusBar().showMessage("Hello User :)")

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")

        open_act = QAction("Open", self)
        open_act.setStatusTip("Open a File. (WIP)")
        open_act.triggered.connect(self.browsefiles)
        file_menu.addAction(open_act)

        exit_act = QAction("Exit", self)
        exit_act.setStatusTip("Exit App.")
        exit_act.triggered.connect(qApp.quit)
        file_menu.addAction(exit_act)


    def InitWidgets(self):
        """method to initialize widgets and layouts"""

# ----- Widgets

        widget = QWidget(self)
        self.setCentralWidget(widget)

        self.text_edit = QPlainTextEdit()
        
        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.savefile)
        self.save_button.setFixedWidth(100)
        self.save_button.setFixedHeight(50)

        self.saveas_button = QPushButton("Save as")
        self.saveas_button.setFixedWidth(100)
        self.saveas_button.setFixedHeight(50)

# ----- Stylesheet import

        with open("styles/ui.qss", "r") as stylesheet:
            self.setStyleSheet(stylesheet.read())

# ----- Layouts

        hbox = QHBoxLayout()
        hbox.addWidget(self.save_button)
        hbox.addWidget(self.saveas_button)

        main_grid = QGridLayout()
        main_grid.setSpacing(10)
        main_grid.addWidget(self.text_edit, 0, 0, 1, 3)
        main_grid.addLayout(hbox, 1, 1)

        widget.setLayout(main_grid)


    def browsefiles(self):
        """method to browse and open a text file to text editor using file explorer"""
        
        self.fname = QFileDialog.getOpenFileName(self, "Open a text file", "C:/", "Text files (*.txt)")

        try:
            with open(self.fname[0], "r") as text_file:
                self.text_edit.setPlainText(text_file.read())

        except FileNotFoundError:
            return None


    def savefile(self):
        pass
        # TODO: prompt user if they want to continue save or not

        try:
            with open(self.fname[0], "w") as text_file:
                text = self.text_edit.toPlainText()
                text_file.write(text)

        except FileNotFoundError:
            self.setStatusTip("Error: File Not Found.")