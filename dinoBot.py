from PIL import ImageGrab, ImageOps
import pyautogui
from numpy import array

class cordinates():
    replayBtn=(480,399)
    
def restartGame():
    pyautogui.click(cordinates.replayBtn)

def pressUp():
    pyautogui.press('up')
       
def imageGrab():
   box=(258,410,300,434) #space between dino and tree before jump
   image=ImageGrab.grab(box)
   grayImage=ImageOps.grayscale(image) #converts space into gray 
   a=array(grayImage.getcolors()) #collection of all the pixel in the box
   return(a.sum()) #replace return with print #sum of the pixels in the area


##def main():
##    print()
##    
##restartGame()
##imageGrab()

def main():
    print('Starting Game...')
    x=0
    while(1):
        if(imageGrab()!=1255):
            pressUp()
            x=x+1
            print('Jump ' + str(x)+ ' times')


restartGame()
main()


