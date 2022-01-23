from PyQt5.QtCore import QObject, pyqtSignal
import time

class UpdatingValue(QObject):
    
    def __init__(self, helm):
        QObject.__init__(self)
        self.helm = helm
        
    value_changed = pyqtSignal(int)
    
    def emit_signal(self):
        iteration_time = time.time()
        iteration = 0 
        while(iteration < 10):
            if(sum(window.isVisible() for window in self.helm.displayed_widget) == 1) :
                if ((time.time() > 2. + iteration_time)):
                    iteration += 1
                    iteration_time = time.time()
                    self.value_changed.emit(iteration)
            else :
                iteration = 10000000
        
        # while(time.time() < iteration_time + 1.):
        #     pass
        # if(sum(window.isVisible() for window in self.helm.displayed_widget) == 1 and (self.iteration<10)) :
        #     self.iteration+=1
        #     self.value_changed.emit(self.iteration)
        # else : 
        #     self.iteration = 0

                        
