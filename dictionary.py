from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog
from PyQt6.QtCore import Qt
from pathlib import Path


app = QApplication([])
window = QWidget()
window.setWindowTitle("Dictionary")
layout = QVBoxLayout()

description = QLabel('Search for a definition:')
layout.addWidget(description)


message = QLabel("")
layout.addWidget(message, alignment=Qt.AlignmentFlag.AlignCenter)

window.setLayout(layout)
window.show()
app.exec()