import os
import sys
import pandas
from PyQt5 import QtCore, QtGui, QtWidgets
import Crewmates as Crew
from ui_test2 import Ui_MainWindow


dataframe = pandas.read_csv(os.getcwd() + '/Random_data.csv', delimiter=',', header=0)

def main():
    helm = Crew.Helmsman.from_pandas("Alvin", dataframe)
    foil = Crew.Foilsman.from_pandas("Brad", dataframe)
    wing = Crew.Wingsman.from_pandas("Cristina", dataframe)
    helm.display()
    foil.display()
    wing.display()

    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    window.setGeometry(100, 200, 600, 600)
    test = Ui_MainWindow()
    test.setupUi(window)
    test.retranslateUi(window)

    window.show()
    sys.exit(app.exec_())

main()



