from machine import Pin, Timer, idle
from L76xxx import xxx
from pytrack import Pytrack
import gc

GPS_TIMEOUT = const(30)
TIME_BETWEEN_FIX = const(90)
REPETITION = const(10)

class GPSFIX:

    def __init__(self):
        self.pytrack = Pytrack()
        self.gps=GNSS(self.pytrack, timeout = 1)
        #self.start(GT, TBF, repetition)

    def start(self, GT = GPS_TIMEOUT, TBF = TIME_BETWEEN_FIX, repetition = REPETITION):
        self.gps.timeout = GT
        self.repetition = repetition
        self.pauseEntreFix = TBF
        self.timer = Timer.Alarm(self.timerCallback, self.pauseEntreFix, periodic=True)

    def timerCallback(self, timer):
        self.repetition -= 1
        if self.repetition < 0:
            gc.collect()
            self.stop()
        else:
            self.gps.coordinates()
            if self.gps.coordinates != (None, None, None):
                print(self.gps.coordinates)
                #lancer la copie en fichier
                #lancer ralo
            else:
                pass

    def stop(self):
        self.timer.cancel()
        gc.collect()
