import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
import tkinter.font as tkFont

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.pyplot import figure


class dataFrameHandling:
    def __init__(self) -> None:
         pass
    
    def setDataFrame(self, passed_df):
        self._df = passed_df
        
    def getFirstPlot(self):   
        
        
        self.chart1.get_tk_widget().pack(side=tk.BOTTOM,fill=tk.BOTH,expand=True)
        self.ax1.clear()
        janind = self.__subdf.columns.get_loc("KWH JANUARY 2010")
        self.ax1.bar(     range(1, 13),
                    (self.__subdf.iloc[ : ,  range(janind, (janind + 12))  ]).mean()     )
        self.chart1.draw()
    
        
    def getSecondPlot(self):
        #UP RIGHT FIGURE
        self.chart2.get_tk_widget().pack(side=tk.BOTTOM,fill=tk.BOTH,expand=True)
        self.ax2.clear()
        janind = self.__subdf.columns.get_loc("THERM JANUARY 2010")
        self.ax2.bar(    range(1, 13),
                    (self.__subdf.iloc[ : ,  range(janind, (janind + 12))  ]).mean()     )
        self.chart2.draw()
    def getThirdPlot(self):
    #BOTTOM LEFT FIGURE
        self.chart3.get_tk_widget().pack(side=tk.BOTTOM,fill=tk.BOTH,expand=True)
        self.ax3.clear()
        janind = self.__subdf.columns.get_loc("KWH JANUARY 2010")
        self.ax3.plot(     range(1, 13),
                    (self.__subdf.iloc[ : ,  range(janind, (janind + 12))  ]).max(),
                    color='red', marker ='*'    )
        self.ax3.plot(     range(1, 13),
                    (self.__subdf.iloc[ : ,  range(janind, (janind + 12))  ]).mean(),
                    color='blue', marker ='s'    )
        self.chart3.draw()  
        
    def getFourthPlot(self):
        self.chart4.get_tk_widget().pack(side=tk.BOTTOM,fill=tk.BOTH,expand=True)
        self.ax4.clear()
        janind = self.__subdf.columns.get_loc("THERM JANUARY 2010")
        self.ax4.plot(     range(1, 13),
                    (self.__subdf.iloc[ : ,  range(janind, (janind + 12))  ]).max(),
                    color='red', marker ='*'    )
        self.ax4.plot(     range(1, 13),
                    (self.__subdf.iloc[ : ,  range(janind, (janind + 12))  ]).mean(),
                    color='blue', marker ='s'    )
        self.chart4.draw() 
        

        
def main():
    root = tk.Tk()
    root.mainloop()

if __name__ == "__main__":
    main()