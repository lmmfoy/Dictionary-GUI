from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog, QLineEdit
from PyQt6.QtCore import Qt
from pathlib import Path

def word_look_up():
    pass
    

app = QApplication([])
window = QWidget()
window.setWindowTitle("Dictionary")
layout = QVBoxLayout()

# Top label
description = QLabel('Search for a definition:')
layout.addWidget(description)

# Input for word 
input = QLineEdit()
layout.addWidget(input)

# Search button
button = QPushButton("Look up word")
layout.addWidget(button)
button.clicked.connect(word_look_up)

definition = QLabel("")
layout.addWidget(definition, alignment=Qt.AlignmentFlag.AlignCenter)

window.setLayout(layout)
window.show()
app.exec()