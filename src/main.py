import sys
from PySide6.QtWidgets import(
    QMainWindow, QWidget, QApplication, QVBoxLayout,
    QHBoxLayout, QLabel, QPushButton, QDockWidget, QListWidget,
    QProgressBar, QTabWidget, QToolButton, QTreeView
    
)
from PySide6.QtCore import Slot , Qt , QSize
from PySide6.QtGui import QIcon , QStandardItem, QStandardItemModel




class SnetchMain(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Snetch GUI")
        self.resize(800 , 800)
        self.initUI()
        
    def initUI(self):
        central_widget = QTabWidget()
        self.setCentralWidget(central_widget)
        
        self.main_layout = QHBoxLayout()
        # tab_names = ["Library", "Draft", "Section", "OnHovered", "Episodes"]
        
        self.tab_1 = QWidget()
        self.tab_2 = QWidget()
        self.tab_3 = QWidget()
        self.tab_4 = QWidget()
        self.tab_5 = QWidget()
        
        central_widget.addTab(self.tab_1, "Library")
        central_widget.addTab(self.tab_2, "Draft")
        central_widget.addTab(self.tab_3, "Section")
        central_widget.addTab(self.tab_4, "OnHovered")
        central_widget.addTab(self.tab_5, "Episodes")
        
        self.tab_2_layout = QHBoxLayout(self.tab_2)
        
        self.separator = QLabel(" | ")
        self.projects_draft_lbl = QLabel("Projects Draft")
        self.add_new_lbl = QLabel("Add New")
        # self.projects_draft_btn.setAlignment(Qt.AlignCenter)
        # self.tab_2_layout.addWidget(self.projects_draft_btn)
        
        self.tab_2_layout.addWidget(self.projects_draft_lbl,alignment=Qt.AlignLeft)
        self.tab_2_layout.addWidget(self.separator,alignment=Qt.AlignLeft)
        self.tab_2_layout.addWidget(self.add_new_lbl,alignment=Qt.AlignLeft)
        
        self.setLayout(self.main_layout)
        # ----------- DOCK WIDGET -------------
        
        self.left_panel = QVBoxLayout()
        self.tree = QTreeView()
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels("Header")
        self.tree.setModel(self.model)
        
        root_node = self.model.invisibleRootItem()
        item1 = QStandardItem("1")
        item2 = QStandardItem("2")
        item1.appendRow(QStandardItem("New"))
        
        self.left_panel.addWidget(self.tree)
        self.main_layout.addLayout(self.left_panel)
        

        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SnetchMain()
    window.show()
    sys.exit(app.exec())