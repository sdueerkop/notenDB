import sys
from PyQt4 import QtGui, QtCore
import functions

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("PyQT tuts!")
        self.name = "UNDEFINED"
        self.klasse = "UNDEFINED"
        self.leistung = "UNDEFINED"
        self.note = "NONE"
        self.anmerkungen = ""
        self.setupForm()

    def confirm(self):
        entries = "Name: {}\n Klasse: {}\n Leistung: {}\n Note: {}\n Anmerkungen {}\n".format(
                   self.name, self.klasse, self.leistung, self.note, self.anmerkungen)
        message = "Angaben korrekt?\n\n {}".format(entries)
        choice = QtGui.QMessageBox.question(self, "Confirm",
                                            message,
                                            QtGui.QMessageBox.Yes |
                                            QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            return True
        else:
            return False

    def submit(self):
        print("Submit Button was pressed.")
        self.name = str(self.nm.text())
        self.klasse = str(self.kl.text())
        self.leistung = str(self.lst.text())
        self.note = str(self.dropDown.currentText())
        self.anmerkungen = str(self.ank.text())
        name = self.name
        klasse = self.klasse
        leistung = self.leistung
        anmerkungen = self.anmerkungen
        note = self.note
        if self.confirm():
            functions.storeData(name, klasse, leistung, note, anmerkungen)
            sys.exit()
        else:
            pass

    def cancel(self):
        print("Cancel Button was pressed.")
        sys.exit()

    def setupForm(self):

        self.win = QtGui.QWidget()
        # Define the items in the rows

        self.l1 = QtGui.QLabel("Name")
        self.nm = QtGui.QLineEdit()

        self.l2 = QtGui.QLabel("Leistung")
        self.lst = QtGui.QLineEdit()

        self.l3 = QtGui.QLabel("Note")
        self.dropDown = QtGui.QComboBox()
        self.dropDown.addItem("1")
        self.dropDown.addItem("2")
        self.dropDown.addItem("3")
        self.dropDown.addItem("4")
        self.dropDown.addItem("5")
        self.dropDown.addItem("6")

        self.l4 = QtGui.QLabel("Klasse")
        self.kl = QtGui.QLineEdit()

        self.l5 = QtGui.QLabel("Anmerkungen")
        self.ank = QtGui.QLineEdit()

        self.submitBtn = QtGui.QPushButton("Submit")
        self.submitBtn.clicked.connect(self.submit)

        self.cancelBtn = QtGui.QPushButton("Cancel")
        self.cancelBtn.clicked.connect(self.cancel)

        # Set up Layout, add items defined above
        self.fbox = QtGui.QFormLayout()
        self.fbox.addRow(self.l1,self.nm)
        self.fbox.addRow(self.l4, self.kl)
        self.fbox.addRow(self.l2,self.lst)
        self.fbox.addRow(self.l3, self.dropDown)
        self.fbox.addRow(self.l5, self.ank)
        self.fbox.addRow(self.submitBtn,self.cancelBtn)

        self.win.setLayout(self.fbox)
        self.win.show()

def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())



run()
