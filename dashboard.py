import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QPushButton, QTableWidget, QTableWidgetItem, QGridLayout, QTextEdit, QSizePolicy,QLineEdit
)

from PySide6.QtGui import QFont
from PySide6.QtCore import Qt


class Dashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CineScope – Dashboard")
        self.setMinimumSize(1200, 800)
        self.setStyleSheet("background-color: #121212; color: white; padding: 20px;")
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(10)

        header = QLabel("🎬 CineScope Dashboard")
        header.setFont(QFont("Arial", 24, QFont.Bold))
        header.setAlignment(Qt.AlignCenter)
        header.setFixedHeight(80)
        main_layout.addWidget(header)

        split_layout = QHBoxLayout()

        left_container = QVBoxLayout()
        left_container.setSpacing(10)
        left_container.setAlignment(Qt.AlignTop)  # Move components to the top

        # Existing buttons
        existing_buttons = [
            ("Search by Genre", self.query_genre),
            ("Search by Year", self.query_year),
            ("Search by IMDB Rating", self.query_rating),
            ("Search by Director", self.query_director),
            ("Search by Actor", self.query_actor),
        ]

        existing_grid = QGridLayout()

        for index, (label, callback) in enumerate(existing_buttons):
            btn = QPushButton(label)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #1f1f1f;
                    border: 1px solid #333;
                    border-radius: 3px;
                    padding: 6px;
                }
                QPushButton:hover {
                    background-color: #333;
                }
            """)
            btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            btn.clicked.connect(callback)
            row, col = divmod(index, 2)  
            existing_grid.addWidget(btn, row, col)

        left_container.addLayout(existing_grid)

        category_heading = QLabel("Select Columns")
        category_heading.setFont(QFont("Arial", 18, QFont.Bold))
        category_heading.setAlignment(Qt.AlignLeft)
        left_container.addWidget(category_heading)

        category_buttons = [
            ("Title", self.query_title),
            ("Year", self.query_year),
            ("Genre", self.query_genre),
            ("Rating", self.query_rating),
            ("Director", self.query_directors),
            ("Stars", self.query_actors),
        ]

        category_grid = QGridLayout()

        for index, (label, callback) in enumerate(category_buttons):
            btn = QPushButton(label)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #1f1f1f;
                    border: 1px solid #333;
                    border-radius: 3px;
                    padding: 6px;
                }
                QPushButton:hover {
                    background-color: #333;
                }
            """)
            btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            btn.clicked.connect(callback)
            row, col = divmod(index, 2)
            category_grid.addWidget(btn, row, col)

        left_container.addLayout(category_grid)

        self.query_input = QLineEdit()
        self.query_input.setPlaceholderText("Enter filter value (e.g. 1999 for Year)")
        self.query_input.setStyleSheet("background-color: #1e1e1e; color: white; padding: 5px; border: 1px solid #444;")
        self.query_input.setFixedHeight(30)
        left_container.addWidget(self.query_input)

        send_btn = QPushButton("Send")
        send_btn.setStyleSheet("background-color: #e50914; color: white; padding: 6px; border-radius: 5px;")
        send_btn.setFixedWidth(100)
        left_container.addWidget(send_btn, alignment=Qt.AlignLeft)

        right_side_layout = QVBoxLayout()
        right_side_layout.setSpacing(10)

        # Right Content
        right_content = QWidget()
        right_content.setStyleSheet("background-color: black; border-radius: 8px;")
        right_content.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Table widget
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setRowCount(1)
        self.table.setItem(0, 0, QTableWidgetItem("Movie"))
        self.table.setItem(0, 1, QTableWidgetItem("Genre"))
        self.table.setItem(0, 2, QTableWidgetItem("Year"))
        self.table.setItem(0, 3, QTableWidgetItem("Rating"))
        self.table.setItem(0, 4, QTableWidgetItem("Director"))

        self.table.setStyleSheet("""
            QTableWidget {
                color: white;
                font-family: Arial, sans-serif;
                font-size: 14px;
            }
            QHeaderView::section {
                background-color: white;
                color: black;
                padding: 4px;
            }
        """)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        right_content_layout = QVBoxLayout()
        right_content_layout.addWidget(self.table)
        right_content.setLayout(right_content_layout)
        right_content.setFixedHeight(1200)

        right_side_layout.addWidget(right_content)

        split_layout.addLayout(left_container, 2)
        split_layout.addLayout(right_side_layout, 8)

        main_layout.addLayout(split_layout)

        self.setLayout(main_layout)


    def query_title(self):
        print("title")
        #add your logic

    def query_year(self):
        print("year")
        #add your logic

    def query_genre(self):
        print("genre")
        #add your logic

    def query_directors(self):
        print("directors")
        #add your logic

    def query_actors(self):
        print("actors")
        #add your logic
    
    def query_rating(self):
        print("rating")
        #add your logic
    
    def query_year(self):
        print("year")
        #add your logic
    
    def query_director(self):
        print("director")
        #add your logic
    
    def query_actor(self):
        print("actor")
        #add your logic
    
    def export_csv(self):
        print("Exporting to CSV...")
        # Implement CSV export logic here

    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dashboard = Dashboard()
    dashboard.show()
    sys.exit(app.exec())
