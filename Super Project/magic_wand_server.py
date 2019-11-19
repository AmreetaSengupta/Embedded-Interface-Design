from PyQt5 import QtWidgets, uic
import sys

class MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__() 
        uic.loadUi('magic_wand.ui', self) #ui file loaded
        self.refresh_button = self.findChild(QtWidgets.QPushButton, 'refresh_button') 
        self.refresh_button.clicked.connect(self.refresh)
        self.image_label = self.findChild(QtWidgets.QLabel, 'image_label')
        self.correct_image = self.findChild(QtWidgets.QLabel, 'correct_image')
        self.incorrect_image = self.findChild(QtWidgets.QLabel, 'incorrect_image')
        self.total_image = self.findChild(QtWidgets.QLabel, 'total_image')
        self.correct_cmd = self.findChild(QtWidgets.QLabel, 'correct_cmd')
        self.incorrect_cmd = self.findChild(QtWidgets.QLabel, 'incorrect_cmd')
        self.total_cmd = self.findChild(QtWidgets.QLabel, 'total_cmd')
        self.per_image = self.findChild(QtWidgets.QLabel, 'per_image')
        self.per_cmd = self.findChild(QtWidgets.QLabel, 'per_cmd')
        self.show()
    
    def refresh(self):
        self.image_label.setText("{}".format("IMAGE LABEL NOT FOUND"))
        self.correct_image.setText("{}".format("0"))
        self.incorrect_image.setText("{}".format("0"))
        self.total_image.setText("{}".format("0"))
        self.correct_cmd.setText("{}".format("0"))
        self.incorrect_cmd.setText("{}".format("0"))
        self.total_cmd.setText("{}".format("0"))
        self.per_image.setText("{}".format("0"))
        self.per_cmd.setText("{}".format("0"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow();
    sys.exit(app.exec_())
