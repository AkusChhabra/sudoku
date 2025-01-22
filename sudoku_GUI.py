"""

Implementing GUI for Sudoku game

@author: Akus C.
"""

#import sudoku_randomizer

import os
import sys
import random

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QMainWindow, QApplication, QLabel, QListWidget, 
                               QLineEdit, QGridLayout, QStatusBar)
from PySide6 import QtCore, QtWidgets, QtGui
        
class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Sudoku Game')

        self.button = QtWidgets.QPushButton("Start")
        self.text = QtWidgets.QLabel("Sudoku Puzzle", 
                                     alignment=QtCore.Qt.AlignCenter)

        ## Define layout and start button
        self.layout = QtWidgets.QGridLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.start)
        
        ## Exit Button
        self.button2 = QtWidgets.QPushButton("Exit")
        self.layout.addWidget(self.button2)
        self.button2.clicked.connect(self.exit_app)

    # Click on Exit button
    def exit_app(self):
        self.close()

    # Clicked on Start button
    def start(self):
        
        # Remove Layout
        for i in reversed(range(self.layout.count())): 
            self.layout.itemAt(i).widget().setParent(None)
        
        ## Breaks Code (Careful Here)
        # self.layout.setParent(None)
        
        ## Create sudoku input grid
        self.inputs = []
        for row in range(9):
            self.row_inputs = []
            for col in range(9):
                # Create a QLineEdit for each cell
                self.input_box = QLineEdit(self)
                self.input_box.setFixedSize(40, 40)  # Set a fixed size for each cell
                self.input_box.setMaxLength(1)
                self.input_box.setAlignment(Qt.AlignCenter)  # Center-align the text
                self.layout.addWidget(self.input_box, row, col)
                self.row_inputs.append(self.input_box)
            self.inputs.append(self.row_inputs)
            
        ## Set the layout for the main window
        #self.setLayout(self.layout)
        #self.input_box.move(400,300)
        #self.show()
        #print(self.input_box.text())

def main():
    app = QtWidgets.QApplication(sys.argv)
    
    widget = MyWidget()
    widget.resize(360, 360)
    widget.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main() 

#     if not QtWidgets.QApplication.instance():
#         app = QtWidgets.QApplication(sys.argv)
#     else:
#         app = QtWidgets.QApplication.instance()    
# QApplication.shutdown()