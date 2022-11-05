from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog, QLineEdit
from PyQt6.QtCore import Qt
from pathlib import Path
import json

# Show word definition from dictionary
def word_look_up():
    word = input.text()
    if word in dictionary:
        definition.setText("\n\n".join(dictionary[word]))
        definition.setFixedSize(definition.sizeHint())
    else:
        definition.setText("Your word is not in this dictionary")

# Open dictionary 
with Path("data/data.json").open() as source:
    dictionary = json.load(source)

# Set up app, vertical layout
app = QApplication([])
window = QWidget()
window.setWindowTitle("Dictionary")
window.setFixedWidth(500)
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

# Definition
definition = QLabel("")
definition.setWordWrap(True)
layout.addWidget(definition)

window.setLayout(layout)
window.show()
app.exec()