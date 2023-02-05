from app.variables import *
from PyQt5.QtWidgets import (
    QMainWindow,
    QVBoxLayout,
    QHBoxLayout,
    QTextEdit,
    QPushButton,
    QAction,
    QWidget,
    QFileDialog,
    QMessageBox,
    qApp
    )


class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.file_name = None

        self.InitStyle()
        self.InitWindow()
        self.InitUI()
        self.show()


    def InitStyle(self):
        with open("app/styles/ui.qss", "r") as stylesheet:
            self.setStyleSheet(stylesheet.read())


    def InitWindow(self):
        """Initialize window properties."""

        self.setMinimumSize(MIN_WIDTH, MIN_HEIGHT)
        self.setWindowTitle("Simple Text Editor")
        self.statusBar().showMessage("Hello User :)")

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")

        open_act = QAction("Open", self)
        open_act.setStatusTip("Open a File.")
        open_act.triggered.connect(self.open_file)
        file_menu.addAction(open_act)

        exit_act = QAction("Exit", self)
        exit_act.setStatusTip("Exit App.")
        exit_act.triggered.connect(qApp.quit)
        file_menu.addAction(exit_act)


    def InitUI(self):
        """Initialize Layouts and Widgets"""

        # --- center widget
        widget = QWidget(self)
        self.setCentralWidget(widget)
        main_layout = QVBoxLayout()

        # --- row 1
        self.text_edit = QTextEdit()
        main_layout.addWidget(self.text_edit)
        
        
        # --- row 2
        row_2 = QHBoxLayout()

        self.save_button = QPushButton("Save", self)
        self.save_button.setStatusTip("Save current file")
        self.save_button.setEnabled(False)
        self.save_button.clicked.connect(self.save_opened_file)
        row_2.addWidget(self.save_button)

        self.save_as_button = QPushButton("Save as", self)
        self.save_as_button.setStatusTip("Save to a directory")
        self.save_as_button.clicked.connect(self.save_to_file)
        
        row_2.addWidget(self.save_as_button)
        main_layout.addLayout(row_2)

        # --- main layout setup
        widget.setLayout(main_layout)


    def open_file(self):
        """
            browse and open txt file to text editor using file explorer.
        """
        
        try:
            self.file_name = QFileDialog.getOpenFileName(self, "Open a text file", "C:/", "Text files (*.txt)")
            with open(self.file_name[0], "r") as text_file:
                self.text_edit.setPlainText(text_file.read())
                self.save_button.setEnabled(True)

        except FileNotFoundError:
            return None
        


    def save_opened_file(self):
        """Save when opened a file"""

        try:
            popup = QMessageBox()
            popup_choice = popup.question(self, "Save File", "Are you sure?", popup.Yes | popup.No, popup.Yes)
            if popup_choice == popup.Yes:
                with open(self.file_name[0], "w") as text_file:
                    text = self.text_edit.toPlainText()
                    text_file.write(text)
                    self.setStatusTip("File saved.")

            elif popup_choice == popup.No:
                self.setStatusTip("Nothing Happened.")


        except FileNotFoundError:
            self.setStatusTip("Error: File Not Found.")
        
        except AttributeError:
            self.setStatusTip("Error: No filepath to save to.")


    def save_to_file(self):
        """save current text to a specified file path"""

        try: 
            self.file_name = QFileDialog.getSaveFileName(self, "Save as", "C:/", "Text files (*.txt)")
            with open(f"{self.file_name[0]}", "w") as text_file:
                text = self.text_edit.toPlainText()
                text_file.write(text)
                self.save_button.setEnabled(True)
                self.setStatusTip("File saved.")

        except FileNotFoundError:
            return None