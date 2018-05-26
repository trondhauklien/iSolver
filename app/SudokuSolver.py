#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
import sys
from TouchStyle import *
import BoardReader as BR

def sudoku():
    # Creates an empty MainWindow
    a = TouchWindow("Solved")
    b = TouchWindow("Result")

    print("Solving...")
    solveable = BR.sudokuIn()

    if solveable:

        success = QLabel("We solved the sudoku!")
        success.setWordWrap(True)
        success.setAlignment(Qt.AlignCenter)
        a.setCentralWidget(success)
 

        out = QLabel("Solved sudoku: %r" %solveable)
        out.setWordWrap(True)
        out.setAlignment(Qt.AlignCenter)
        b.setCentralWidget(out)

        b.show()
        a.show()
        print("solveable: ",solveable)
        return(solveable)
        
    else:
        fail = QLabel("Sorry, the sudoku is invalid.")
        fail.setWordWrap(True)
        fail.setAlignment(Qt.AlignCenter)
        r.setCentralWidget(fail)

        r.show()
