from PyQt4 import QtGui, QtCore
import sys

import functions
from config import *

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Notenausgabe")
        self.fach = "UNDEFINED"
        self.setupForm()


    def submit(self):
        #print("Submit Button was pressed.")
        self.s = str(self.schuelerListe.currentText())
        self.f = str(self.fachMenu.currentText()) 
        avg, name, halbjahr, jahr = functions.notenDurchschnittSchueler(self.s, self.f)
        self.show_output.setText("Notendurchschnitt für {} im Fach {} im\
 {}. Halbjahr ({}): {}".format(name, self.f, halbjahr, jahr, avg))

    def cancel(self):
        print("Action canceled. Exiting...")
        sys.exit()

    def setupForm(self):

        self.win = QtGui.QWidget()
        # Define the items in the rows

        schuelerInnen = functions.getTableNames()

        self.l3 = QtGui.QLabel("SchülerIn")
        self.schuelerListe = QtGui.QComboBox()
        self.schuelerListe.addItems(schuelerInnen)

        self.l4 = QtGui.QLabel("Fach")
        self.fachMenu = QtGui.QComboBox()
        self.fachMenu.addItems(FAECHER)


        self.submitBtn = QtGui.QPushButton("Submit")
        self.submitBtn.clicked.connect(self.submit)

        self.cancelBtn = QtGui.QPushButton("Cancel")
        self.cancelBtn.clicked.connect(self.cancel)

        self.show_output = QtGui.QLineEdit()
        self.show_output.setText("Ausgabe...")

        # Set up Layout, add items defined above
        self.fbox = QtGui.QFormLayout()
        self.fbox.addRow(self.l3, self.schuelerListe)
        self.fbox.addRow(self.l4, self.fachMenu)
        self.fbox.addRow(self.submitBtn,self.cancelBtn)
        self.fbox.addRow(self.show_output)

        self.win.setLayout(self.fbox)
        self.win.show()

def callReadMenu():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

if __name__ == "__main__":
    callReadMenu()
