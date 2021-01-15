from rpi_ws281x import *
import colorsys


class Wrapper:


    def __init__(self,strip):
        self.strip=strip
        self.ledArray=[]

        for i in range (strip.numPixels()):
            self.ledArray.append([0,0,0])

        self.ausgeben()


    def setpixel(self,index,h,s,v):
        
        self.ledArray[index]=[h,s,v]        
        

    def zahl_zu_bit(self, zahl,reihe):
        '''eine Zahl von 0 bis 9 in Bitmuster'''

   

    def setAllColour (self,h):
        print(self.ledArray)
        for i in self.ledArray:
            i[0]=h        
        print(self.ledArray)


    def setHelligkeit(self,v):
        for i in self.ledArray:
            i[2]=v

    def ausgeben(self):
        
        for (i,color) in enumerate(self.ledArray):
            test_color = colorsys.hsv_to_rgb(color[0],color[1],color[2])
            self.strip.setPixelColor(i,Color(test_color[0],test_color[1],test_color[2]))
            print(test_color)

        self.strip.show()