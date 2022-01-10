import os
import sys
import pandas
from PyQt5 import QtCore, QtGui, QtWidgets
import Crewmates as Crew
from ui_test2 import Ui_MainWindow
import TDL_OTC_Data


def main():
    import sys
    dataframe = pandas.read_csv(os.getcwd() + '/Random_data.csv', delimiter=',', header=0)
    helm = Crew.Helmsman.from_pandas("Alvin", dataframe)
    foil = Crew.Foilsman.from_pandas("Brad", dataframe)
    wing = Crew.Wingsman.from_pandas("Cristina", dataframe)

    app = QtWidgets.QApplication(sys.argv)

    #Chargement et affichage de la première fenêtre
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow1()
    ui.setupUi(MainWindow)
    MainWindow.show()
    #Chargement des différentes fenêtres des équipiers : à faire dans les classes crewmate init de l'attribut window de chacun
    MainWindowFoil = QtWidgets.QMainWindow()
    ui_foil = Ui_MainWindow2()
    ui_foil.setupUi(MainWindowFoil)
    helm.window = QtWidgets.QMainWindow()
    #à faire dans la calsse helm
    self.window.gite_window.value = self.gite

    helm.ui = Ui_MainWindow2()
    ui_helm.setupUi(MainWindowFoil)

    #Choix de l'équipier
    ui.foilsman_button.clicked.connect(MainWindowFoil.show)
    ui.helmsman_button.clicked.connect(MainWindowHelm.show)
    ui.wingsman_button.clicked.connect(MainWindowWing.show)
    for i in range(len(dataframe)):

        dataframe = pandas.read_csv(os.getcwd() + '/Random_data.csv', delimiter=',', header=0)
        if(choice_helmsman):
            helm.update()
            #helm a un attribut Helsman_window qui est mis à jour avec update
            ui_helm.button_gite.clicked.connect(show_gite)
            ui_helm.button_gite.clicked.connect(show_gite)
        if(choice_wingsman):

        time.sleep(20)



main()



