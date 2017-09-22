import GPSFIX
from machine import Timer

gpsfix=GPSFIX()

gpsfix.start(30,90,5)
