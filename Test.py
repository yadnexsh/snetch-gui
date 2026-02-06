import sys
from PySide6.QtWidgets import(
    QMainWindow, QWidget, QApplication, QVBoxLayout,
    QHBoxLayout, QLabel, QPushButton, QDockWidget, QListWidget,
    QProgressBar, QTabWidget, QToolButton, QTreeView, 
    
)
from PySide6.QtCore import Slot , Qt , QSize
from PySide6.QtGui import QIcon , QStandardItem, QStandardItemModel, QPixmap

class CardWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        
        layout = QVBoxLayout()
        
        label = QLabel("Test")
        para = QLabel("Paragraph , Paragraph, Paragraph, Paragraph, Paragraph, Paragraph")
        

        
        icon = QLabel("test2")
        pixmap = QPixmap("book.png")
        # icon.setScaledContents(True)
        icon.setPixmap(pixmap)
    
        # icon.setWindowIcon("book.png")

        layout.addWidget(label)
        layout.addWidget(para)
        layout.addWidget(icon)
        
        
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CardWidget()
    window.show()
    sys.exit(app.exec())
    
    # -------------------------------------------
import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Signal, Slot

class ClickableWidget(QWidget):
    # Define a custom signal named 'clicked'
    clicked = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setLayout(QVBoxLayout())
        self.label = QLabel("Click me!", self)
        self.layout().addWidget(self.label)
        # Optional: set a style to make it visually distinct
        self.setStyleSheet("background-color: lightgray; border: 1px solid black;")

    def mousePressEvent(self, event):
        """Handle mouse press events."""
        # Emit the custom clicked signal
        self.clicked.emit()
        # Call the base class method (optional, but good practice)
        super().mousePressEvent(event)

# Main application logic
if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create the clickable widget
    window = ClickableWidget()
    window.setFixedSize(200, 100)

    # Connect the custom clicked signal to a Python slot (function)
    @Slot()
    def on_widget_clicked():
        print("ClickableWidget was clicked!")

    window.clicked.connect(on_widget_clicked)

    window.show()
    sys.exit(app.exec())
