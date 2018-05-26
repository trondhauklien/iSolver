import sys
import time
import ftrobopy

try:
    txt = ftrobopy.ftrobopy("auto")
except:
    txt = None

M = [ txt.C_OUTPUT, txt.C_OUTPUT, txt.C_OUTPUT, txt.C_OUTPUT ]
I = [ (txt.C_SWITCH, txt.C_DIGITAL ),
      (txt.C_SWITCH, txt.C_DIGITAL ),
      (txt.C_SWITCH, txt.C_DIGITAL ),
      (txt.C_SWITCH, txt.C_DIGITAL ),
      (txt.C_SWITCH, txt.C_DIGITAL ),
      (txt.C_SWITCH, txt.C_DIGITAL ),
      (txt.C_SWITCH, txt.C_DIGITAL ),
      (txt.C_SWITCH, txt.C_DIGITAL ) ]

txt.setConfig(M, I)
txt.updateConfig()

Motor1 = txt.motor(1)
Motor2 = txt.motor(2)
Motor3 = txt.motor(3)
Motor4 = txt.motor(4)

Button1 = txt.input(1)
Button2 = txt.input(2)

i = 4

def Reset():
    print("Reset")
    if Button1.state() == 0:
        Motor1.setSpeed(-512)
        Motor1.setDistance(5000, syncto = Motor2)
        Motor2.setSpeed(-512)
        Motor2.setDistance(5000, syncto = Motor1)

    while not Motor1.finished(): #Sjekk om Knapp 1 er trykket
        if Button1.state() == 1:
            Motor1.stop()
            Motor2.stop()
            Motor1.setSpeed(512)
            Motor1.setDistance(90, syncto = Motor2)
            Motor2.setSpeed(512)
            Motor2.setDistance(90, syncto = Motor1)

    if Button2.state() == 0:
        Motor3.setSpeed(-512)
        Motor3.setDistance(5000, syncto = None)

    while not Motor3.finished(): #Sjekk om Knapp 2 er trykket
        if Button2.state() == 1:
            Motor3.stop()
            Motor3.setSpeed(512)
            Motor3.setDistance(20, syncto = None)

def HeadUp():
    time.sleep(0.500)
    print("MC.HeadUp")
    Motor4.setSpeed(-512)
    Motor4.setDistance(1, syncto = None)
    time.sleep(0.400)
    Motor4.stop()

def HeadDown():
    time.sleep(0.500)
    print("MC.HeadDown")
    Motor4.setSpeed(512)
    Motor4.setDistance(1, syncto = None)
    time.sleep(0.350)
    Motor4.stop()

def NextCell():
    Motor3.setSpeed(512)
    Motor3.setDistance(20 * i, syncto = None)

def NextRow():
    Motor1.setSpeed(512)
    Motor1.setDistance(20 * i, syncto = Motor2)
    Motor2.setSpeed(512)
    Motor2.setDistance(20 * i, syncto = Motor1)
    Motor3.setSpeed(-512)
    Motor3.setDistance(180 * i, syncto = None)

def BeforeScan():
    Motor1.setSpeed(-512)
    Motor1.setDistance(20 * i, syncto = Motor2)
    Motor2.setSpeed(-512)
    Motor2.setDistance(20 * i, syncto = Motor1)
    time.sleep(0.500)

def AfterScan():
    Motor1.setSpeed(512)
    Motor1.setDistance(20 * i, syncto = Motor2)
    Motor2.setSpeed(512)
    Motor2.setDistance(20 * i, syncto = Motor1)
    time.sleep(0.500)

def Number1():
    State = 0

    while State <= 3:
        if State == 0:
            Motor3.setSpeed(512)
            Motor3.setDistance(4 * i, syncto = None)
            State = 1

        elif State == 1:
            if Motor3.finished():
                HeadDown()
                State = 2

        elif State == 2:
            if Motor1.finished():
                Motor1.setSpeed(512)
                Motor1.setDistance(10 * i, syncto = Motor2)
                Motor2.setSpeed(512)
                Motor2.setDistance(10 * i, syncto = Motor1)
                State = 3

        elif State == 3:
            if Motor1.finished():
                HeadUp()
                Motor1.setSpeed(-512)
                Motor1.setDistance(10 * i, syncto = Motor2)
                Motor2.setSpeed(-512)
                Motor2.setDistance(10 * i, syncto = Motor1)
                Motor3.setSpeed(512)
                Motor3.setDistance(16 * i, syncto = None)
                State = 4
                break

def Number2():
    State = 0
    HeadDown()

    while State <= 5:
        if State == 0:
            Motor3.setSpeed(512)
            Motor3.setDistance(5 * i, syncto = None)
            State = 1

        elif State == 1:
            if Motor3.finished():
                Motor1.setSpeed(512)
                Motor1.setDistance(5 * i, syncto = Motor2)
                Motor2.setSpeed(512)
                Motor2.setDistance(5 * i, syncto = Motor1)
                State = 2

        elif State == 2:
            if Motor1.finished():
                Motor3.setSpeed(-512)
                Motor3.setDistance(5 * i, syncto = None)
                State = 3

        elif State == 3:
            if Motor3.finished():
                Motor1.setSpeed(512)
                Motor1.setDistance(5 * i, syncto = Motor2)
                Motor2.setSpeed(512)
                Motor2.setDistance(5 * i, syncto = Motor1)
                State = 4

        elif State == 4:
            if Motor2.finished():
                Motor3.setSpeed(512)
                Motor3.setDistance(5 * i, syncto = None)
                State = 5

        elif State == 5:
            if Motor3.finished():
                HeadUp()
                Motor1.setSpeed(-512)
                Motor1.setDistance(10 * i, syncto = Motor2)
                Motor2.setSpeed(-512)
                Motor2.setDistance(10 * i, syncto = Motor1)
                Motor3.setSpeed(512)
                Motor3.setDistance(15 * i, syncto = None)
                State = 6
                break

def Number3():
    State = 0
    HeadDown()

    while State <= 5:
        if State == 0:
            Motor3.setSpeed(512)
            Motor3.setDistance(5 * i, syncto = None)
            State = 1

        elif State == 1:
            if Motor3.finished():
                Motor1.setSpeed(512)
                Motor1.setDistance(10 * i, syncto = Motor2)
                Motor2.setSpeed(512)
                Motor2.setDistance(10 * i, syncto = Motor1)
                State = 2

        elif State == 2:
            if Motor1.finished():
                Motor3.setSpeed(-512)
                Motor3.setDistance(5 * i, syncto = None)
                State = 3

        elif State == 3:
            if Motor3.finished():
                HeadUp()
                Motor1.setSpeed(-512)
                Motor1.setDistance(5 * i, syncto = Motor2)
                Motor2.setSpeed(-512)
                Motor2.setDistance(5 * i, syncto = Motor1)
                State = 4

        elif State == 4:
            if Motor2.finished():
                HeadDown()
                Motor3.setSpeed(512)
                Motor3.setDistance(5 * i, syncto = None)
                State = 5

        elif State == 5:
            if Motor3.finished():
                HeadUp()
                Motor1.setSpeed(-512)
                Motor1.setDistance(5 * i, syncto = Motor2)
                Motor2.setSpeed(-512)
                Motor2.setDistance(5 * i, syncto = Motor1)
                Motor3.setSpeed(512)
                Motor3.setDistance(15 * i, syncto = None)
                State = 6
                break

def Number4():
    State = 0
    HeadDown()

    while State <= 4:
        if State == 0:
            Motor1.setSpeed(512)
            Motor1.setDistance(5 * i, syncto = Motor2)
            Motor2.setSpeed(512)
            Motor2.setDistance(5 * i, syncto = Motor1)
            State = 1

        elif State == 1:
            if Motor1.finished():
                Motor3.setSpeed(512)
                Motor3.setDistance(5 * i, syncto = None)
                State = 2

        elif State == 2:
            if Motor3.finished():
                HeadUp()
                Motor1.setSpeed(512)
                Motor1.setDistance(5 * i, syncto = Motor2)
                Motor2.setSpeed(512)
                Motor2.setDistance(5 * i, syncto = Motor1)
                State = 3

        elif State == 3:
            if Motor1.finished():
                HeadDown()
                Motor1.setSpeed(-512)
                Motor1.setDistance(10 * i, syncto = Motor2)
                Motor2.setSpeed(-512)
                Motor2.setDistance(10 * i, syncto = Motor1)
                State = 4

        elif State == 4:
            if Motor1.finished():
                HeadUp()
                Motor3.setSpeed(512)
                Motor3.setDistance(15 * i, syncto = None)
                State = 5
                break

def Number5():
    State = 0

    while State <= 7:
        if State == 0:
            Motor3.setSpeed(512)
            Motor3.setDistance(5 * i, syncto = None)
            State = 1

        elif State == 1:
            if Motor3.finished():
                HeadDown() #Endret
                State = 2

        elif State == 2:
            if Motor4.finished():
                Motor3.setSpeed(-512)
                Motor3.setDistance(5 * i, syncto = None)
                State = 3

        elif State == 3:
            if Motor3.finished():
                Motor1.setSpeed(512)
                Motor1.setDistance(5 * i, syncto = Motor2)
                Motor2.setSpeed(512)
                Motor2.setDistance(5 * i, syncto = Motor1)
                State = 4

        elif State == 4:
            if Motor1.finished():
                Motor3.setSpeed(512)
                Motor3.setDistance(5 * i, syncto = None)
                State = 5

        elif State == 5:
            if Motor3.finished():
                Motor1.setSpeed(512)
                Motor1.setDistance(5 * i, syncto = Motor2)
                Motor2.setSpeed(512)
                Motor2.setDistance(5 * i, syncto = Motor1)
                State = 6

        elif State == 6:
            if Motor1.finished():
                Motor3.setSpeed(-512)
                Motor3.setDistance(5 * i, syncto = None)
                State = 7

        elif State == 7:
            if Motor3.finished():
                HeadUp()
                Motor1.setSpeed(-512)
                Motor1.setDistance(10 * i, syncto = Motor2)
                Motor2.setSpeed(-512)
                Motor2.setDistance(10 * i, syncto = Motor1)
                Motor3.setSpeed(512)
                Motor3.setDistance(20 * i, syncto = None)
                State = 8
                break

def Number6():
    State = 0

    while State <= 7:
        if State == 0:
            Motor3.setSpeed(512)
            Motor3.setDistance(5 * i, syncto = None)
            State = 1

        elif State == 1:
            if Motor3.finished():
                HeadDown()
                State = 2

        elif State == 2:
            if Motor4.finished():
                    Motor3.setSpeed(-512)
                    Motor3.setDistance(5 * i, syncto = None)
                    State = 3

        elif State == 3:
            if Motor3.finished():
                Motor1.setSpeed(512)
                Motor1.setDistance(10 * i, syncto = Motor2)
                Motor2.setSpeed(512)
                Motor2.setDistance(10 * i, syncto = Motor1)
                State = 4

        elif State == 4:
            if Motor1.finished():
                Motor3.setSpeed(512)
                Motor3.setDistance(5 * i, syncto = None)
                State = 5

        elif State == 5:
            if Motor3.finished():
                Motor1.setSpeed(-512)
                Motor1.setDistance(5 * i, syncto = Motor2)
                Motor2.setSpeed(-512)
                Motor2.setDistance(5 * i, syncto = Motor1)
                State = 6

        elif State == 6:
            if Motor1.finished():
                Motor3.setSpeed(-512)
                Motor3.setDistance(5 * i, syncto = None)
                State = 7

        elif State == 7:
            if Motor3.finished():
                HeadUp()
                Motor1.setSpeed(-512)
                Motor1.setDistance(5 * i, syncto = Motor2)
                Motor2.setSpeed(-512)
                Motor2.setDistance(5 * i, syncto = Motor1)
                Motor3.setSpeed(512)
                Motor3.setDistance(20 * i, syncto = None)
                State = 8
                break

def Number7():
    State = 0
    HeadDown()

    while State <= 2:
        if State == 0:
            Motor3.setSpeed(512)
            Motor3.setDistance(5 * i, syncto = None)
            State = 1

        elif State == 1:
            if Motor3.finished():
                Motor1.setSpeed(512)
                Motor1.setDistance(10 * i, syncto = Motor2)
                Motor2.setSpeed(512)
                Motor2.setDistance(10 * i, syncto = Motor1)
                State = 2

        elif State == 2:
            if Motor1.finished():
                HeadUp()
                Motor1.setSpeed(-512)
                Motor1.setDistance(10 * i, syncto = Motor2)
                Motor2.setSpeed(-512)
                Motor2.setDistance(10 * i, syncto = Motor1)
                Motor3.setSpeed(512)
                Motor3.setDistance(15 * i, syncto = None)
                State = 3
                break

def Number8():
    State = 0
    HeadDown()

    while State <= 6:
        if State == 0:
            Motor1.setSpeed(512)
            Motor1.setDistance(10 * i, syncto = Motor2)
            Motor2.setSpeed(512)
            Motor2.setDistance(10 * i, syncto = Motor1)
            State = 1

        elif State == 1:
            if Motor1.finished():
                Motor3.setSpeed(512)
                Motor3.setDistance(5 * i, syncto = None)
                State = 2

        elif State == 2:
            if Motor3.finished():
                Motor1.setSpeed(-512)
                Motor1.setDistance(10 * i, syncto = Motor2)
                Motor2.setSpeed(-512)
                Motor2.setDistance(10 * i, syncto = Motor1)
                State = 3

        elif State == 3:
            if Motor1.finished():
                Motor3.setSpeed(-512)
                Motor3.setDistance(5 * i, syncto = None)
                State = 4

        elif State == 4:
            if Motor3.finished():
                HeadUp()
                Motor1.setSpeed(512)
                Motor1.setDistance(5 * i, syncto = Motor2)
                Motor2.setSpeed(512)
                Motor2.setDistance(5 * i, syncto = Motor1)
                State = 5

        elif State == 5:
            if Motor1.finished():
                HeadDown()
                Motor3.setSpeed(512)
                Motor3.setDistance(5 * i, syncto = None)
                State = 6

        elif State == 6:
            if Motor3.finished():
                HeadUp()
                Motor1.setSpeed(-512)
                Motor1.setDistance(5 * i, syncto = Motor2)
                Motor2.setSpeed(-512)
                Motor2.setDistance(5 * i, syncto = Motor1)
                Motor3.setSpeed(512)
                Motor3.setDistance(15 * i, syncto = None)
                State = 7
                break

def Number9():
    State = 0

    while State <= 7:
        if State == 0:
            Motor1.setSpeed(512)
            Motor1.setDistance(5 * i, syncto = Motor2)
            Motor2.setSpeed(512)
            Motor2.setDistance(5 * i, syncto = Motor1)
            Motor3.setSpeed(512)
            Motor3.setDistance(5 * i, syncto = None)
            State = 1

        elif State == 1:
            if Motor1.finished():
                HeadDown()
                State = 2

        elif State == 2:
            if Motor4.finished():
                Motor3.setSpeed(-512)
                Motor3.setDistance(5 * i, syncto = None)
                State = 3

        elif State == 3:
            if Motor3.finished():
                Motor1.setSpeed(-512)
                Motor1.setDistance(5 * i, syncto = Motor2)
                Motor2.setSpeed(-512)
                Motor2.setDistance(5 * i, syncto = Motor1)
                State = 4

        elif State == 4:
            if Motor1.finished():
                Motor3.setSpeed(512)
                Motor3.setDistance(5 * i, syncto = None)
                State = 5

        elif State == 5:
            if Motor3.finished():
                Motor1.setSpeed(512)
                Motor1.setDistance(10 * i, syncto = Motor2)
                Motor2.setSpeed(512)
                Motor2.setDistance(10 * i, syncto = Motor1)
                State = 6

        elif State == 6:
            if Motor1.finished():
                Motor3.setSpeed(-512)
                Motor3.setDistance(5 * i, syncto = None)
                State = 7

        elif State == 7:
            if Motor3.finished():
                HeadUp()
                Motor1.setSpeed(-512)
                Motor1.setDistance(10 * i, syncto = Motor2)
                Motor2.setSpeed(-512)
                Motor2.setDistance(10 * i, syncto = Motor1)
                Motor3.setSpeed(512)
                Motor3.setDistance(20 * i, syncto = None)
                State = 7
                break
