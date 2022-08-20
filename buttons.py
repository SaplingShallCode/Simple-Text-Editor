from PyQt5.QtWidgets import QPushButton

class CustomButton(QPushButton):
    """Class to customize the QPushButton"""
    def __init__(self, *args):
        
        super().__init__()

        self.setFixedWidth(100)
        self.setFixedHeight(50)