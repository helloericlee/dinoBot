from PIL import ImageGrab, ImageOps
import pyautogui
import time
from numpy import array

class cordinates():
    replayBtn=(322,388)
##    dino=(407,365)
#447= x cordinate of tree
#379= y cordinate of tree
    
def restartGame():
    pyautogui.click(cordinates.replayBtn)

def pressUp():
    pyautogui.press('up')
    time.sleep(0.05)
   
def imageGrab():
   box=(162,397,203,419)
   image=ImageGrab.grab(box)
   grayImage=ImageOps.grayscale(image)
   a=array(grayImage.getcolors())
   return(a.sum())

##def main():
##    print(10)
##    
##restartGame()
##imageGrab()

def main():
    print('Starting Game...')
    x=0
    while(1):
        if(imageGrab()!=1149):
            pressUp()
            x=x+1
            print('Jump ' + str(x)+ ' times')


restartGame()
main()



