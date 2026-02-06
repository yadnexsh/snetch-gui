import sys
from PySide6.QtWidgets import(
    QMainWindow, QWidget, QApplication, QVBoxLayout,
    QHBoxLayout, QLabel, QPushButton, QDockWidget, QListWidget,
    QProgressBar, QTabWidget, QToolButton, QTreeView, QGroupBox, QLineEdit, QGridLayout, QComboBox
    
)
from PySide6.QtCore import Slot , Qt , QSize
from PySide6.QtGui import QIcon , QStandardItem, QStandardItemModel


import os


class ExpenseWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Track Expense")
        self.initUI()
        
    def initUI(self):
        self.layout = QHBoxLayout()

        self.groupbox = QGroupBox("Expense")
        self.groupbox_layout = QGridLayout()
        self.submit_btn = QPushButton("Submit")
        
        self.amount_lbl = QLabel("Amount")
        self.amount = QLineEdit()
        self.amount.setPlaceholderText("Enter Final Amount")
        
        self.type_lbl = QLabel("Type")
        self.type_box = QComboBox()
        self.type_box.addItems(["Start", "End"])
        
        self.groupbox_layout.addWidget(self.type_box)
        self.groupbox_layout.addWidget(self.type_box)
        
        
        self.groupbox_layout.addWidget(self.amount_lbl, 0,0)
        self.groupbox_layout.addWidget(self.amount, 0,1)
        
        
        
        self.groupbox_layout.addWidget(self.submit_btn)
        self.groupbox.setLayout(self.groupbox_layout)
        
        self.layout.addWidget(self.groupbox)
        self.setLayout(self.layout)
        
        
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExpenseWindow()
    window.show()
    sys.exit(app.exec())