from PyQt5.QtCore import QObject, pyqtSignal
import time

class UpdatingValue(QObject):
    
    def __init__(self, crewmate):
        QObject.__init__(self)
        self.crewmate = crewmate
        
    value_changed = pyqtSignal(int)
    
    def emit_signal(self):
        iteration_time = time.time()
        iteration = 0 
        while(iteration < 72):
            if(sum(window.isVisible() for window in self.crewmate.list_of_windows)) :
                if ((time.time() > 0.5 + iteration_time)):
                    iteration += 1
                    iteration_time = time.time()
                    self.value_changed.emit(iteration)
            else :
                iteration = 10000000
        


                        
