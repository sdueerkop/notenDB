import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import functions # File in same dir

def window():
    app = QApplication(sys.argv)
    win = QWidget()

    # Define the items in the rows

    l1 = QLabel("Name")
    nm = QLineEdit()

    l2 = QLabel("Leistung")
    add1 = QLineEdit()

    l3 = QLabel("Note")
    dropDown = QComboBox()
    dropDown.addItem("1")
    dropDown.addItem("2")
    dropDown.addItem("3")
    dropDown.addItem("4")
    dropDown.addItem("5")
    dropDown.addItem("6")

    submitBtn = QPushButton("Submit")
    text = str(dropDown.currentText())
    submitBtn.clicked.connect(functions.submit)

    cancelBtn = QPushButton("Cancel")
    cancelBtn.clicked.connect(functions.cancel)

    # Set up Layout, add items defined above
    fbox = QFormLayout()
    fbox.addRow(l1,nm)
    fbox.addRow(l2,add1)
    fbox.addRow(l3, dropDown)
    fbox.addRow(submitBtn,cancelBtn)

    # Get ready and display the complete window
    win.setLayout(fbox)
    win.setWindowTitle("Form Experiments")
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    window()
