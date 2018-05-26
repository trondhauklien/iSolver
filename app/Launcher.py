#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import ftrobopy
from TxtStyle import *
import numpy as np
import MotorController as MC
import time
import SudokuSolver as solver

class FtcGuiApplication(TxtApplication):
    def __init__(self, args):
        TxtApplication.__init__(self, args)

        w = TxtWindow("Launcher")
        vbox = QVBoxLayout()
        global NumsToPrint
        NumsToPrint = []

        button = QPushButton("Solve!")              # create a button labeled "Solve!"
        button.clicked.connect(self.Solve)   # connect button to event handler
        vbox.addWidget(button)                      # attach it to the main output area

        button2 = QPushButton("Run!")
        button2.clicked.connect(self.Start)
        vbox.addWidget(button2)

        button3 = QPushButton("Reset!")
        button3.clicked.connect(self.Reset)
        vbox.addWidget(button3)

        #Show program
        w.centralWidget.setLayout(vbox)
        w.show()
        self.exec_()

    def Solve(self):
        MC.BeforeScan()
        global NumsToPrint
        NumsToPrint = solver.sudoku()
        print("NumsToPrint: ",NumsToPrint)
        MC.AfterScan()

    def Start(self):
        a = 0
        while a < len(NumsToPrint):
            if a % 9 == 0:
                    if a != 0:
                            MC.NextRow()
                            print("NextRow")
                            time.sleep(6.000)

            if NumsToPrint[a] == 0:
                    MC.NextCell()
                    print("NextCell")
                    time.sleep(1.250)

            elif NumsToPrint[a] == 1:
                    MC.Number1()
                    print("1")
                    time.sleep(0.500)

            elif NumsToPrint[a] == 2:
                    MC.Number2()
                    print("2")
                    time.sleep(0.500)

            elif NumsToPrint[a] == 3:
                    MC.Number3()
                    print("3")
                    time.sleep(0.500)

            elif NumsToPrint[a] == 4:
                    MC.Number4()
                    print("4")
                    time.sleep(0.500)

            elif NumsToPrint[a] == 5:
                    MC.Number5()
                    print("5")
                    time.sleep(0.500)

            elif NumsToPrint[a] == 6:
                    MC.Number6()
                    print("6")
                    time.sleep(0.500)

            elif NumsToPrint[a] == 7:
                    MC.Number7()
                    print("7")
                    time.sleep(0.500)

            elif NumsToPrint[a] == 8:
                    MC.Number8()
                    print("8")
                    time.sleep(0.500)

            elif NumsToPrint[a] == 9:
                    MC.Number9()
                    print("9")
                    time.sleep(0.500)

            a += 1
            print("Done",a)
        else:
            print("Manual Error -else-")
            MC.Reset()

    def Reset(self):
        MC.Reset()

if __name__ == "__main__":
    FtcGuiApplication(sys.argv)
