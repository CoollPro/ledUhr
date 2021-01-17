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
        

    def zahl_zu_bit(self, zahl):
        '''eine Zahl von 0 bis 9 in Bitmuster'''
        if zahl == 0:
            return[1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1]
        elif zahl == 1:
            return[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1]
        elif zahl == 2:
            return[1,0,0,0,1,1,1,1,1,0,0,1,0,0,0,1,1,0,0,0,1,0,0,1,1,0,0,1,1,1,1,1]
        elif zahl == 3:
            return[1,0,0,1,0,0,0,1,1,0,0,0,1,0,0,1,1,0,0,1,0,0,0,1,1,1,1,1,1,1,1,1]
        elif zahl == 4:
            return[1,1,1,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,1,1,1,1,1,1,1,1]
        elif zahl == 5:
            return[1,1,1,1,1,0,0,1,1,0,0,1,0,0,0,1,1,0,0,0,1,0,0,1,1,1,1,1,0,0,0,1]
        elif zahl == 6:
            return[1,1,1,1,1,1,1,1,1,0,0,1,0,0,0,1,1,0,0,0,1,0,0,1,1,1,1,1,0,0,0,1]
        elif zahl == 7:
            return[1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1]
        elif zahl == 8:
            return[1,1,1,1,1,1,1,1,1,0,0,1,0,0,0,1,1,0,0,0,1,0,0,1,1,1,1,1,1,1,1,1]
        elif zahl == 9:
            return[1,1,1,1,1,0,0,1,1,0,0,1,0,0,0,1,1,0,0,0,1,0,0,1,1,1,1,1,1,1,1,1]
    

    def zahl_speichern(self,zahl,reihe,helligkeit):

        self.buffer=[]
        buffer=self.zahl_zu_bit(zahl)
        self.merke=(reihe*8)
        

        for i in range (self.merke,(self.merke+32)):
            
            self.bufferIndex=i-self.merke

            if (buffer[self.bufferIndex])==1:
                self.ledArray[i][2]=helligkeit

            elif (buffer[self.bufferIndex])==0:
                self.ledArray[i][2]=0   
                
    


    def setAllColour (self,h):
        for i in self.ledArray:
            i[0]=h        
        


    def setHelligkeit(self,v):
        for i in self.ledArray:
            i[2]=v

    def setAllSaturation(self,s):
        for i in self.ledArray:
            i[1]=s


    def ausgeben(self):
        
        for (i,color) in enumerate(self.ledArray):
            test_color = colorsys.hsv_to_rgb(color[0],color[1],color[2])
            r=int(test_color[0]*255)
            g=int(test_color[1]*255)
            b=int(test_color[2]*255)
            self.strip.setPixelColor(i,Color(r,g,b))
            
        self.strip.show()