import sys
from PySide6.QtWidgets import(
    QMainWindow, QWidget, QApplication, QVBoxLayout,
    QHBoxLayout, QLabel, QPushButton, QDockWidget, QListWidget,
    QProgressBar, QTabWidget, QToolButton, QTreeView
    
)
from PySide6.QtCore import Slot , Qt , QSize
from PySide6.QtGui import QIcon , QStandardItem, QStandardItemModel


import os


class CardWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        
        layout = QVBoxLayout()
        
        
        
        self.setLayout(layout)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Program")
        self.resize(1800, 800)
        self.initUI()
        
            
    def initUI(self):
        
        main_layout = QHBoxLayout()
        
        
        # ------------ CENTRAL WIDGET - TAB -----------------
        
        self.main_tab = QTabWidget()
        
        self.library_tab = QWidget()
        self.draft_tab = QWidget()
        self.section_tab = QWidget()
        self.onhovered_tab = QWidget()
        self.episodes_tab = QWidget()
        
        self.main_tab.addTab(self.library_tab, "Library")
        self.main_tab.addTab(self.draft_tab, "Draft")
        self.main_tab.addTab(self.section_tab, "Section")
        self.main_tab.addTab(self.onhovered_tab, "OnHovered")
        self.main_tab.addTab(self.episodes_tab, "Episodes")
        
        self.main_tab.setCurrentIndex(1)
        
        self.projects_draft_label = QLabel("Projects Draft")
        self.separator = QLabel(" | ")
        self.add_new_label = QLabel("Add New")
        
        self.draft_tab_layout = QVBoxLayout()
        self.header_layout = QHBoxLayout()

        
        self.draft_tab_layout = QVBoxLayout()
        self.header_layout = QHBoxLayout()
        self.header_layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.draft_tab.setLayout(self.draft_tab_layout)
        self.draft_tab_layout.addLayout(self.header_layout)

        self.header_layout.addWidget(self.projects_draft_label)
        self.header_layout.addWidget(self.separator)
        self.header_layout.addWidget(self.add_new_label)


        # ---------------------------- LEFT PANEL ------------------------------------
        
        self.left_panel = QTreeView()
        self.model = QStandardItemModel()
        self.model.setColumnCount(2)
        self.model.setHorizontalHeaderLabels(["1", "2"])
        self.left_panel.setHeaderHidden(True)
        
        root_node = self.model.invisibleRootItem()
        
        starter = QStandardItem("Get Started")
        styles = QStandardItem("Style")
        grid = QStandardItem("Grid")
        
        colors = QStandardItem("Colors")
        gradients = QStandardItem("Gradients")
        positive = QStandardItem("Positive")
        folder_01 = QStandardItem("Folder 01")
        folder_02 = QStandardItem("Folder 02")
        documents = QStandardItem("Documents.txt")
        projects_draft = QStandardItem("Projects Draft")
        my_docs = QStandardItem("My Documents")
        backgrounds = QStandardItem("Backgrounds")
        stroke = QStandardItem("Stroke")
        shadows = QStandardItem("Shadows")
        icons = QStandardItem("Icons")
        layouts = QStandardItem("Layouts")
        templates = QStandardItem("Templates")
        components = QStandardItem("COMPONENTS")
        components_no = QStandardItem("124")
        # components_no.setTextAlignment(Qt.AlignRight)
        libraries = QStandardItem("LIBRARIES")
        teams = QStandardItem("TEAMS")
        settings_icon = QStandardItem()
        
        
        # -- Tree Structure --
        root_node.appendRows([starter, styles, grid])
        root_node.appendRow(colors)
        colors.appendRow(gradients)
        gradients.appendRow(positive)
        positive.appendRow(folder_01)
        positive.appendRow(folder_02)
        folder_02.appendRow(documents)
        folder_02.appendRow(projects_draft)
        folder_02.appendRow(my_docs)
        colors.appendRow(backgrounds)
        colors.appendRow(stroke)
        colors.appendRow(shadows)
        
        root_node.appendRows([icons, layouts, templates])
        root_node.appendRow([components, components_no])
        root_node.appendRow(libraries)
        root_node.appendRow([teams, settings_icon])
        
        # -- Icons Folder Path --
        current_dir = os.path.dirname(__file__)
        root_dir = os.path.dirname(current_dir)
        icons_path = os.path.join(root_dir , "resources\icons")

        # -- Assigning Icons --
        starter.setIcon(QIcon(os.path.join(icons_path, "book.png")))
        styles.setIcon(QIcon(os.path.join(icons_path, "brush.png")))
        grid.setIcon(QIcon(os.path.join(icons_path, "grid.png")))
        colors.setIcon(QIcon(os.path.join(icons_path, "picker.png")))
        
        colors_childs = [gradients , positive , folder_01 , folder_02, backgrounds, stroke, shadows]
        
        for each in colors_childs:
            each.setIcon(QIcon(os.path.join(icons_path, "folder.png")))
            
        documents.setIcon(QIcon(os.path.join(icons_path, "documents.png")))
        projects_draft.setIcon(QIcon(os.path.join(icons_path, "documents.png")))
        my_docs.setIcon(QIcon(os.path.join(icons_path, "documents.png")))
        icons.setIcon(QIcon(os.path.join(icons_path, "icon.png")))
        layouts.setIcon(QIcon(os.path.join(icons_path, "layout.png")))
        templates.setIcon(QIcon(os.path.join(icons_path, "template.png")))
        settings_icon.setIcon(QIcon(os.path.join(icons_path, "settings.png")))
        
        
        # -- Assigning Fake Child Item to have side down arrow --
        
        fake_childs = [
            starter, styles, grid, backgrounds, stroke, shadows, icons,
            layouts, templates, folder_01, components, libraries, teams
            ]
        
        for each in fake_childs:
            each.appendRow(QStandardItem())

        self.left_panel.setModel(self.model)
        index = self.model.indexFromItem(projects_draft)
        self.left_panel.setCurrentIndex(index)
        self.left_panel.setColumnWidth(0, 220)
        self.left_panel.setFixedWidth(250)
        
        # ---------------------------- RIGHT PANEL ------------------------------------
        
        self.right_panel = QTabWidget()
        
        self.tab_1 = QWidget()
        self.tab_2 = QWidget()
        self.tab_3 = QWidget()
        self.tab_4 = QWidget()
        self.tab_5 = QWidget()
        self.tab_6 = QWidget()
        
        
        self.right_panel.addTab(self.tab_1, QIcon(os.path.join(icons_path, "bell.png")), None)
        self.right_panel.addTab(self.tab_2, QIcon(os.path.join(icons_path, "shapes.png")), None)
        self.right_panel.addTab(self.tab_3, QIcon(os.path.join(icons_path, "file.png")), None)
        self.right_panel.addTab(self.tab_4, QIcon(os.path.join(icons_path, "message.png")), None)
        self.right_panel.addTab(self.tab_5, QIcon(os.path.join(icons_path, "folder.png")), None)
        self.right_panel.addTab(self.tab_6, QIcon(os.path.join(icons_path, "card.png")), None)
        
        self.right_panel.setCurrentIndex(1)
        
        
        # --------- LAYOUT ------------ 
        main_layout.addWidget(self.left_panel)
        main_layout.addWidget(self.main_tab)        
        main_layout.addWidget(self.right_panel)
        
        self.setLayout(main_layout)
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())