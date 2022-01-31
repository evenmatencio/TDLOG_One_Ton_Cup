from PyQt5.QtCore import QObject, pyqtSignal
import time

"""
This file is designed for handling the update of the data displayed to the crewmates.
    ¤ NUMBER_OF_DATA : gives the number of lines of the .csv file used. It must depend on the 
    way the .csv file is built
    ¤ UPDTAING_TIME     
"""



NUMBER_OF_DATA = 72
UPDATING_TIME = 0.5

class UpdatingValue(QObject):
    
    def __init__(self, crewmate):
        QObject.__init__(self)
        self.crewmate = crewmate
        
    value_changed = pyqtSignal(int)
    
    def emit_signal(self):
        iteration_time = time.time()
        iteration = 0 
        while(iteration < NUMBER_OF_DATA):
            if(sum(window.isVisible() for window in self.crewmate.list_of_windows)) :
                if ((time.time() > UPDATING_TIME + iteration_time)):
                    iteration += 1
                    iteration_time = time.time()
                    self.value_changed.emit(iteration)
            else :
                iteration = 10000000
        


                        
