from PyQt5.QtWidgets import QPushButton

class CustomButton(QPushButton):
    """Class to customize the QPushButton"""

    def __init__(self, text='', parent=None):
        
        super().__init__(text, parent=parent)

        self.setFixedWidth(100)
        self.setFixedHeight(50)