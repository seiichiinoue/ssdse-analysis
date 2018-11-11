# this is setup file for my ssdse-analysis repository

import os
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

os.system("matplotlib inline")

class ssdse:
    
    def __init__(self, file_name="SSDSE.csv") -> None:

        plt.style.use('ggplot')
        if os.name == "nt":
            # on Windows
            font = {"family":"Yu Mincho"}
        font = {"family":"IPAGothic"}
        mpl.rc('font', **font)
        print("matplotlib lang set to Ja, using IPA-Gothic font.")
        
        self.ssdse = pd.read_csv(file_name, header=1)

        f_per_capita = lambda x: (x / self.ssdse["人口総数"]) * 100
        self.per_capita = self.ssdse.iloc[:, 3:].apply(f_per_capita)
        self.per_capita = pd.concat([self.ssdse.iloc[:, :3],
                                     self.per_capita], axis=1)
        
        print("imported DataFrames from {}".format(file_name))

        display(self.ssdse.head(5))


if (__name__ == "__main__") or (__name__ == "setup"):
    ssdse = ssdse()
    