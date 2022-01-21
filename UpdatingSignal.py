from PyQt5.QtCore import QObject, pyqtSignal
import time

class UpdatingValue(QObject):
    
    def __init__(self):
        QObject.__init__(self)
        
    value_changed = pyqtSignal(int)
    
    def emit_signal(self):
        iteration_time = time.time()
        iteration = 0 
        while(iteration < 10):
            if (time.time() > 1. + iteration_time):
                iteration += 1
                iteration_time = time.time()
                self.value_changed.emit(iteration)
                        
