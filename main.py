import os
import sys
sys.path.insert(0, os.path.join( os.getcwd(), 'Helmsman') )
sys.path.insert(0, os.path.join( os.getcwd(), 'Helmsman', 'widgets'))

try :
    
    import pandas
    from PyQt5 import QtCore, QtGui, QtWidgets
    import mainwindow1_py as MainWindow
    import Crewmates

except Exception as e:
    
    print(e)



def main():

    #Initialisation des classes d'equipier, initialisation de l'interface et recuperation des donnees
    #-----------------------------------------------------------------------------------------------------

    dataframe = pandas.read_csv(os.getcwd() + '/Random_data.csv', delimiter=',', header=0)
    helm = Crewmates.Helmsman( 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    #helm.from_pandas(dataframe)
    #foil = Crew.Foilsman.from_pandas("Brad", dataframe)
    #wing = Crew.Wingsman.from_pandas("Cristina", dataframe)
    app = QtWidgets.QApplication(sys.argv)

    #Chargement et affichage de la première fenêtre
    #------------------------------------------------------------------------------------------------------

    main_window = QtWidgets.QMainWindow()
    ui = MainWindow.Ui_MainWindow()
    ui.setupUi(main_window)
    main_window.show()
    #helm.main_window_helmsman.show()


    #Chargement des différentes fenêtres des équipiers : à faire dans les classes crewmate init de l'attribut window de chacun
    # MainWindowFoil = QtWidgets.QMainWindow()
    # ui_foil = Ui_MainWindow2()
    # ui_foil.setupUi(MainWindowFoil)
    # helm.window = QtWidgets.QMainWindow()
    # #à faire dans la classe helm
    # self.window.gite_window.value = self.gite
    #
    # helm.ui = Ui_MainWindow2()
    # ui_helm.setupUi(MainWindowFoil)

    #Choix de l'équipier
    # ui.foilsman_button.clicked.connect(MainWindowFoil.show)
    # ui.helmsman_button.clicked.connect(helm.main_window_helmsman.show())
    # ui.wingsman_button.clicked.connect(MainWindowWing.show)
    # for i in range(len(dataframe)):

        # dataframe = pandas.read_csv(os.getcwd() + '/Random_data.csv', delimiter=',', header=0)
        # if(choice_helmsman):
        #     helm.update()
        #     #helm a un attribut Helsman_window qui est mis à jour avec update
        #     ui_helm.button_gite.clicked.connect(show_gite)
        #     ui_helm.button_gite.clicked.connect(show_gite)
        # if(choice_wingsman):
        #
        # time.sleep(20)
    sys.exit(app.exec_())




main()



