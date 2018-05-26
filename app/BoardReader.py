import sys
import os
import imutils
import numpy as np
import cv2
import sudoku as SS
import ftrobopy
from time import sleep

Squares = [(0, 0), (100, 0), (200, 0), (300, 0), (400, 0), (500, 0), (600, 0), (700, 0), (800, 0),
           (0, 100), (100, 100), (200, 100), (300, 100), (400, 100), (500, 100), (600, 100), (700, 100), (800, 100),
           (0, 200), (100, 200), (200, 200), (300, 200), (400, 200), (500, 200), (600, 200), (700, 200), (800, 200),
           (0, 300), (100, 300), (200, 300), (300, 300), (400, 300), (500, 300), (600, 300), (700, 300), (800, 300),
           (0, 400), (100, 400), (200, 400), (300, 400), (400, 400), (500, 400), (600, 400), (700, 400), (800, 400),
           (0, 500), (100, 500), (200, 500), (300, 500), (400, 500), (500, 500), (600, 500), (700, 500), (800, 500),
           (0, 600), (100, 600), (200, 600), (300, 600), (400, 600), (500, 600), (600, 600), (700, 600), (800, 600),
           (0, 700), (100, 700), (200, 700), (300, 700), (400, 700), (500, 700), (600, 700), (700, 700), (800, 700),
           (0, 800), (100, 800), (200, 800), (300, 800), (400, 800), (500, 800), (600, 800), (700, 800), (800, 800)]

DIGITS_LOOKUP = {(1, 1, 1, 0, 1, 1, 1): 0,
                 (0, 0, 1, 0, 0, 1, 0): 1,
                 (1, 0, 1, 1, 1, 0, 1): 2,
                 (1, 0, 1, 1, 0, 1, 1): 3,
                 (0, 1, 1, 1, 0, 1, 0): 4,
                 (1, 1, 0, 1, 0, 1, 1): 5,
                 (1, 1, 0, 1, 1, 1, 1): 6,
                 (1, 0, 1, 0, 0, 1, 0): 7,
                 (1, 1, 1, 1, 1, 1, 1): 8,
                 (1, 1, 1, 1, 0, 1, 1): 9}

def sudokuIn():
    #alt 1
    CAM_DEV = os.environ.get('FTC_CAM')
    if CAM_DEV == None: 
        CAM_DEV = 0
    else: 
        CAM_DEV = int(CAM_DEV)
    cam = cv2.VideoCapture(CAM_DEV)
    s, im = cam.read() # captures image
    #cv2.imshow("Test Picture", im) # displays captured image
    cv2.imwrite("/opt/ftc/apps/user/deb7b8f8-d237-420d-bfa3-788702bb58d2/test.bmp",im) # writes image test.bmp to disk
    #alt 2
    #txt = ftrobopy.ftrobopy('auto')
    #sleep(2)
    #txt.startCameraOnline()
    #sleep(2.5)
    #pic = txt.getCameraFrame()
    #with open('/opt/ftc/apps/user/3a2bee00-1bdd-11e8-b566-0800260c9a66/txtimg.jpg','wb') as f:
    #    f.write(bytearray(pic))
    #txt.stopCameraOnline()
    image = cv2.imread("/opt/ftc/apps/user/deb7b8f8-d237-420d-bfa3-788702bb58d2/test.bmp",0)
    image = imutils.resize(image, height = 500)
    #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.GaussianBlur(image, (9, 9), 1)
    edged = cv2.Canny(image, 1, 50)
    _, cnts, _ = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:10]
    screenCnt = None

    for c in cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.1 * peri, True)

        if len(approx) == 4:
            screenCnt = approx
            break

    pts1 = np.float32([screenCnt[0], screenCnt[3], screenCnt[1], screenCnt[2]])
    pts2 = np.float32([[0,0],[900,0],[0,900],[900,900]])
    M = cv2.getPerspectiveTransform(pts1,pts2)
    dst = cv2.warpPerspective(image,M,(900,900))
    #dst = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
    dst = cv2.adaptiveThreshold(dst, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 135, 35)
    cv2.imwrite("/opt/ftc/apps/user/deb7b8f8-d237-420d-bfa3-788702bb58d2/output.png", dst)

    NumSquares = []
    Nums = []
    a = 0
    while a < len(Squares):
            im = dst[Squares[a][1]:Squares[a][1] + 100, Squares[a][0]:Squares[a][0] + 100]
            NumSquares.append(im)
            im = im[10:90, 10:90]
            cv2.imwrite("/opt/ftc/apps/user/deb7b8f8-d237-420d-bfa3-788702bb58d2/num.png", im)

            cnts = cv2.findContours(im.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnts = cnts[0] if imutils.is_cv2() else cnts[1]
            digitCnts = []

            for c in cnts:
                (x, y, w, h) = cv2.boundingRect(c)
                if (w >= 10 and w < 100) and (h >= 50 and h <= 100):
                    digitCnts.append(c)

            if len(digitCnts) == 0:
                    Nums.append(0)

            digits = []
            for c in digitCnts:
                (x, y, w, h) = cv2.boundingRect(c)
                roi = im[y:y + h, x:x + w]
                (roiH, roiW) = roi.shape
                (dW, dH) = (int(roiW * 0.25), int(roiH * 0.15))
                dHC = int(roiH * 0.05)

                segments = [
                    ((0, 0), (w, dH)),	# top
                    ((0, 0), (dW, h // 2)),	# top-left
                    ((w - dW, 0), (w, h // 2)),	# top-right
                    ((0, (h // 2) - dHC) , (w, (h // 2) + dHC)), # center
                    ((0, h // 2), (dW, h)),	# bottom-left
                    ((w - dW, h // 2), (w, h)),	# bottom-right
                    ((0, h - dH), (w, h))	# bottom
                            ]
                on = [0] * len(segments)

                for (i, ((xA, yA), (xB, yB))) in enumerate(segments):
                    segROI = roi[yA:yB, xA:xB]
                    total = cv2.countNonZero(segROI)
                    area = (xB - xA) * (yB - yA)
                    if total / float(area) > 0.60:
                        on[i]= 1

                if w >= 25:
                      digit = DIGITS_LOOKUP[tuple(on)]
                elif w < 25:
                      digit = 1
                Nums.append(digit)

            a += 1
    Nums_1 = Nums
    Answer = []
    while Nums_1:
            group = Nums_1[:9]
            Nums_1 = Nums_1[9:]
            Answer.extend([group])
    SS.solveSudoku(Answer)

    t = 0
    tt = 0
    Solved = []
    while t < 9:
            while tt < 9:
                    Solved.append(Answer[t][tt])
                    tt += 1
            tt = 0
            t += 1

    k = 0
    NumsToPrint = []
    while k < len(Nums):
            if Nums[k] + Solved[k] == Solved[k]:
                    NumsToPrint.append(Solved[k])
            else:
                    NumsToPrint.append(0)
            k += 1
    print(Nums)
    print(Solved)
    #return (Nums)
    #return (Solved)
    return (NumsToPrint)
