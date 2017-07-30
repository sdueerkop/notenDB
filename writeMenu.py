import sys
from PyQt4 import QtGui, QtCore
import functions

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Noteneingabe")
        self.name = "UNDEFINED"
        self.fach = "UNDEFINED"
        self.klasse = "UNDEFINED"
        self.leistung = "UNDEFINED"
        self.note = "NONE"
        self.anmerkungen = ""
        self.setupForm()

    def confirm(self):
        entries = "Name: {}\n Klasse: {}\n Fach: {}\n Leistung: {}\n Note: {}\n Anmerkungen {}\n".format(
                   self.name, self.klasse, self.fach, self.leistung, self.note, self.anmerkungen)
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
        self.fach = str(self.fachMenu.currentText())
        self.leistung = str(self.lst.text())
        self.note = str(self.notenMenu.currentText())
        self.anmerkungen = str(self.ank.text())
        name = self.name
        klasse = self.klasse
        fach = self.fach
        leistung = self.leistung
        anmerkungen = self.anmerkungen
        note = self.note
        if self.confirm():
            functions.storeData(name, klasse, fach, leistung, note, anmerkungen)
            print("Data written. Exiting...")
            sys.exit()
        else:
            pass

    def cancel(self):
        print("Action canceled. Exiting...")
        sys.exit()

    def setupForm(self):

        self.win = QtGui.QWidget()
        # Define the items in the rows

        self.l1 = QtGui.QLabel("Name")
        self.nm = QtGui.QLineEdit()

        self.l2 = QtGui.QLabel("Leistung")
        self.lst = QtGui.QLineEdit()

        self.l3 = QtGui.QLabel("Note")
        self.notenMenu = QtGui.QComboBox()
        self.notenMenu.addItem("unbenotet")
        self.notenMenu.addItem("1")
        self.notenMenu.addItem("2")
        self.notenMenu.addItem("3")
        self.notenMenu.addItem("4")
        self.notenMenu.addItem("5")
        self.notenMenu.addItem("6")

        self.l4 = QtGui.QLabel("Fach")
        self.fachMenu = QtGui.QComboBox()
        self.fachMenu.addItem("Deutsch")
        self.fachMenu.addItem("Musik")

        self.l5 = QtGui.QLabel("Anmerkungen")
        self.ank = QtGui.QLineEdit()

        self.l6 = QtGui.QLabel("Klasse")
        self.kl = QtGui.QLineEdit()

        self.submitBtn = QtGui.QPushButton("Submit")
        self.submitBtn.clicked.connect(self.submit)

        self.cancelBtn = QtGui.QPushButton("Cancel")
        self.cancelBtn.clicked.connect(self.cancel)

        # Set up Layout, add items defined above
        self.fbox = QtGui.QFormLayout()
        self.fbox.addRow(self.l1,self.nm)
        self.fbox.addRow(self.l6,self.kl)
        self.fbox.addRow(self.l4, self.fachMenu)
        self.fbox.addRow(self.l2,self.lst)
        self.fbox.addRow(self.l3, self.notenMenu)
        self.fbox.addRow(self.l5, self.ank)
        self.fbox.addRow(self.submitBtn,self.cancelBtn)

        self.win.setLayout(self.fbox)
        self.win.show()

def callWriteMenu():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

if __name__ == "__main__":
    callWriteMenu()
