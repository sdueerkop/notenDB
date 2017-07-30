import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("PyQT tuts!")
        self.setupForm()
#        self.show()

    def setupForm(self):

        self.win = QtGui.QWidget()
        # Define the items in the rows

        self.l1 = QtGui.QLabel("Name")
        self.nm = QtGui.QLineEdit()

        self.l2 = QtGui.QLabel("Leistung")
        self.add1 = QtGui.QLineEdit()

        self.l3 = QtGui.QLabel("Note")
        self.dropDown = QtGui.QComboBox()
        self.dropDown.addItem("1")
        self.dropDown.addItem("2")
        self.dropDown.addItem("3")
        self.dropDown.addItem("4")
        self.dropDown.addItem("5")
        self.dropDown.addItem("6")

        self.submitBtn = QtGui.QPushButton("Submit")
       # self.submitBtn.clicked.connect(functions.submit)

        self.cancelBtn = QtGui.QPushButton("Cancel")
       # self.cancelBtn.clicked.connect(functions.cancel)

        # Set up Layout, add items defined above
        self.fbox = QtGui.QFormLayout()
        self.fbox.addRow(self.l1,self.nm)
        self.fbox.addRow(self.l2,self.add1)
        self.fbox.addRow(self.l3, self.dropDown)
        self.fbox.addRow(self.submitBtn,self.cancelBtn)

        self.win.setLayout(self.fbox)
        self.win.show()

def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())



run()
