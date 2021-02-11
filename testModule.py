import TableClasses as TC
import matplotlib as mpl
import numpy as np
import EfficiencyAlgorithms as EA


tbl = TC.BinaryTable([200, 50, 300, 70, 600, 100, 1000, 500, 2500, 650, 4000, 900])

Depos = EA.BinaryAlgorithms(1000, tbl)

