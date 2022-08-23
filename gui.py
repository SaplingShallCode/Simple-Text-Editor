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
                            QMessageBox,
                            qApp)
from PyQt5.QtCore import Qt
from buttons import CustomButton


class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.fname = None

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
        open_act.setStatusTip("Open a File.")
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
        
        self.save_button = CustomButton("Save", self)
        self.save_button.setStatusTip("Save current file")
        if self.fname == None:
            self.save_button.setEnabled(False)
        self.save_button.clicked.connect(self.savefile)

        self.saveas_button = CustomButton("Save as", self)
        self.saveas_button.setStatusTip("Save to a directory")
        self.saveas_button.clicked.connect(self.savetofile)

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
                self.save_button.setEnabled(True)

        except FileNotFoundError:
            return None


    def savefile(self):
        """method to write to opened file"""

        try:
            popup = QMessageBox()
            popup_choice = popup.question(self, "Save File", "Are you sure?", popup.Yes | popup.No, popup.Yes)
            
            if popup_choice == popup.Yes:

                with open(self.fname[0], "w") as text_file:
                    text = self.text_edit.toPlainText()
                    text_file.write(text)

                    self.setStatusTip("File saved.")
            elif popup_choice == popup.No:
                self.setStatusTip("Nothing Happened.")


        except FileNotFoundError:
            self.setStatusTip("Error: File Not Found.")
        
        except AttributeError:
            self.setStatusTip("Error: No filepath to save to.")


    def savetofile(self):
        """method to save current text to a specified file path"""

        self.fname = QFileDialog.getSaveFileName(self, "Save as", "C:/", "Text files (*.txt)")
        with open(f"{self.fname[0]}", "w") as text_file:
            text = self.text_edit.toPlainText()
            text_file.write(text)

            self.setStatusTip("File saved.")