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

        self.fname = None

        self.InitStyle()
        self.InitWindow()
        self.InitUI()
        self.show()


    def InitStyle(self):
        with open("app/styles/ui.qss", "r") as stylesheet:
            self.setStyleSheet(stylesheet.read())


    def InitWindow(self):
        """Initialize window properties."""
        self.setGeometry(700, 100, 500, 700)
        self.setMinimumSize(500, 700)
        self.setMaximumSize(1000, 900)
        self.setWindowTitle("Simple Text Editor")
        self.statusBar().showMessage("Hello User :)")

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")

        open_act = QAction("Open", self)
        open_act.setStatusTip("Open a File.")
        open_act.triggered.connect(self.browse_files)
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
        if self.fname == None:
            self.save_button.setEnabled(False)
        self.save_button.clicked.connect(self.save_file)

        self.saveas_button = QPushButton("Save as", self)
        self.saveas_button.setStatusTip("Save to a directory")
        self.saveas_button.clicked.connect(self.save_to_file)
        
        row_2.addWidget(self.save_button)
        row_2.addWidget(self.saveas_button)
        main_layout.addLayout(row_2)

        # --- main layout setup
        widget.setLayout(main_layout)


    def browse_files(self):
        """method to browse and open a text file to text editor using file explorer"""
        
        self.fname = QFileDialog.getOpenFileName(self, "Open a text file", "C:/", "Text files (*.txt)")

        try:
            with open(self.fname[0], "r") as text_file:
                self.text_edit.setPlainText(text_file.read())
                self.save_button.setEnabled(True)

        except FileNotFoundError:
            return None


    def save_file(self):
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


    def save_to_file(self):
        """method to save current text to a specified file path"""

        self.fname = QFileDialog.getSave_FileName(self, "Save as", "C:/", "Text files (*.txt)")
        with open(f"{self.fname[0]}", "w") as text_file:
            text = self.text_edit.toPlainText()
            text_file.write(text)

            self.setStatusTip("File saved.")