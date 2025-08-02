import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QRadioButton,
    QButtonGroup, QLabel
)
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt
import time
from rename import renameFile

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FileMAZE")
        self.setWindowIcon(QIcon("assets/filemaze.png"))

        self.VLayout = QtWidgets.QVBoxLayout(self)
        self.VLayout.setContentsMargins(20, 20, 20, 20)
        
        self.HLayoutHeading = QtWidgets.QHBoxLayout(self)
        self.headingLabel = QtWidgets.QLabel("Welcome to FileMAZE!", self)
        self.HLayoutHeading.addWidget(self.headingLabel)
        self.headingLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.headingLabel.setStyleSheet("font-size: 26px; font-weight: bold; color: blue;")
        self.VLayout.addLayout(self.HLayoutHeading)

        self.HLayout = QtWidgets.QHBoxLayout(self)

        self.browseLabel= QtWidgets.QLabel("Browse or Enter a path for a folder you want to be renamed:", self)
        self.browseLabel.setStyleSheet("font-size: 16px; padding-top: 20px;")
        self.VLayout.addWidget(self.browseLabel)

        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setPlaceholderText("Enter folder path here...")
        self.lineEdit.setStyleSheet("""
          QLineEdit {
              background-color: #f0f0f0;  /* light gray background */
              border: 2px solid #ccc;     
              border-radius: 6px;         
              padding: 6px 12px;          
              font-size: 14px;            
              color: #333;                
          }
          QLineEdit:focus {
              border-color: #66afe9;      
              outline: none;              
          }
        """)
        self.HLayout.addWidget(self.lineEdit)

        self.browse = QtWidgets.QPushButton("Browse", self)
        self.browse.setStyleSheet("""
          QPushButton {
              background-color: #ff5c5c;     /* red background */
              color: white;                  
              font-size: 14px;
              font-weight: bold;
              border-radius: 6px;
              padding: 6px 12px;
          }
          QPushButton:hover {
              background-color: #ff1c1c;     
          }
        """)  
        self.HLayout.addWidget(self.browse)
        self.browse.clicked.connect(self.browse_folder)
        self.VLayout.addLayout(self.HLayout)

        self.ThemeHLayout = QtWidgets.QHBoxLayout(self)
        self.ThemeHLayout.setContentsMargins(0, 20, 0, 0)
        self.ThemeHLayout.setSpacing(10)
        self.themeLabel = QtWidgets.QLabel("Select a theme:", self)
        self.themeLabel.setStyleSheet("font-size: 16px;")
        self.ThemeHLayout.addWidget(self.themeLabel)
        self.themeComboBox = QtWidgets.QComboBox(self)
        self.themeComboBox.addItems(["Default", "Shakespeare Mode", "Pirate Mode"])
        self.themeComboBox.setStyleSheet("""
          QComboBox {
              background-color: #f0f0f0;  
              border: 2px solid #ccc;     
              border-radius: 6px;         
              padding: 6px 12px;          
              font-size: 14px;            
              color: #333;                
          }
          QComboBox:hover {
              border-color: #66afe9;      
          }
        """)
        self.ThemeHLayout.addWidget(self.themeComboBox)
        self.VLayout.addLayout(self.ThemeHLayout)

        self.difficultyLabel = QtWidgets.QLabel("Select a difficulty:", self)
        self.difficultyLabel.setStyleSheet("font-size: 16px; padding-top: 10px;")
        self.VLayout.addWidget(self.difficultyLabel)
        self.difficultyHLayout=QtWidgets.QHBoxLayout(self)

      # Radio buttons
        self.easyRadio = QRadioButton("Easy")
        self.mediumRadio = QRadioButton("Medium")
        self.hardRadio = QRadioButton("Hard")
        self.nightmareRadio = QRadioButton("Nightmare")
        self.easyRadio.setStyleSheet("font-size: 14px;")
        self.mediumRadio.setStyleSheet("font-size: 14px;")
        self.hardRadio.setStyleSheet("font-size: 14px;")
        self.nightmareRadio.setStyleSheet("font-size: 14px;")

        # Group them so only one can be selected
        self.difficultyGroup = QButtonGroup(self)
        self.difficultyGroup.addButton(self.easyRadio)
        self.difficultyGroup.addButton(self.mediumRadio)
        self.difficultyGroup.addButton(self.hardRadio)
        self.difficultyGroup.addButton(self.nightmareRadio)

        # set default
        self.easyRadio.setChecked(True)

        # Layout for radio buttons
        radioLayout = QHBoxLayout()
        radioLayout.addWidget(self.easyRadio)
        radioLayout.addWidget(self.mediumRadio)
        radioLayout.addWidget(self.hardRadio)
        radioLayout.addWidget(self.nightmareRadio)

        # Add to main layout
        self.VLayout.addLayout(radioLayout)

        self.submitButton = QtWidgets.QPushButton("Submit", self)
        self.submitButton.clicked.connect(self.onSubmitClick)
        self.submitButton.setStyleSheet("""
          QPushButton {
              background-color: #28a745;     /* green background */
              color: white;                  
              font-size: 16px;
              font-weight: bold;
              border-radius: 6px;
              padding: 8px 16px;
              margin-top: 20px;
          }
          QPushButton:hover {
              background-color: #218838;     
          }
        """)
        self.VLayout.addWidget(self.submitButton)

    def onSubmitClick(self):
        t = renameFile(self.lineEdit.text())
        # if t == -1:

    @QtCore.Slot()
    def browse_folder(self):
        path = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory")
        if path:
          self.lineEdit.setText(path)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    # Load splash image
    pixmap = QtGui.QPixmap("assets/filemaze.png")
    splash = QtWidgets.QSplashScreen(pixmap)
    splash.showMessage("Summoning the maze...", alignment=Qt.AlignBottom | Qt.AlignCenter, color=Qt.white)
    splash.show()
    app.processEvents()
    time.sleep(2)

    widget = MyWidget()
    # widget.resize(800, 600)
    widget.show()
    splash.finish(widget)

    sys.exit(app.exec())