# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 23:30:28 2021

@author: Inès
This widget shows the direction the wind is coming from, its speed, and its angle to the axis of the boat.
"""


########################################################################
## IMPORTS
########################################################################

import os
import sys
import math

try:
    from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication

    from PyQt5.QtGui import QPolygon, QPolygonF, QColor, QPen, QFont, QPainter, QFontMetrics, QConicalGradient, QRadialGradient, QFontDatabase

    from PyQt5.QtCore import Qt ,QTime, QTimer, QPoint, QPointF, QRect, QSize, QObject, pyqtSignal

except:
    print("Error while importing PyQt5")
    exit()

################################################################################################
# VOCABULARY
################################################################################################

# Scale= Echelle
# Font = Police
# Offset= Décalage
# Radius= Rayon
#
#
#


################################################################################################
# WIND ANGLE WIDGET CLASS
################################################################################################

class WindAngleWidget(QWidget):
    def __init__(self, parent=None):
        
        super(WindAngleWidget, self).__init__(parent)
        
        # INITIALIZING THE NEEDLE
        