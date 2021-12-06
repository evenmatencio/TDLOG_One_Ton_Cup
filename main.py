import os
import TDL_OTC_Data as Data
import Crewmates as Crew
import pandas

dataframe = pandas.read_csv(os.getcwd() + '/Random_data.csv', delimiter=',', header=0)

def main():
    helm = Crew.Crewmate.from_pandas("Alvin", dataframe)
    foil = Crew.Foilsman.from_pandas("Brad", dataframe)
    wing = Crew.Wingsman.from_pandas("Cristina", dataframe)
    helm.diplay()
    foil.display()
    wing.display()

main()



