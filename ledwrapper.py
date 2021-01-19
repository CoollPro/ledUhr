from rpi_ws281x import *
import colorsys
import time

class Wrapper:

   

    def __init__(self,strip):
        self.strip=strip
        self.ledArray=[]
        self.farbeStunde_Miute=0
        self.farbeSekunde=0
        self.brightness=0
        self.flag=True

        for i in range (strip.numPixels()):
            self.ledArray.append([0,0,0])

        self.ausgeben()

    def setpixel(self,index,h,s,v):
        
        self.ledArray[index]=[h,s,v]        
        
    def zahl_zu_bit_geradeReihe(self, zahl):
        '''eine Zahl von 0 bis 9 in Bitmuster'''
        if zahl == 0:
            return[1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1]
        elif zahl == 1:
            return[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1]
        elif zahl == 2:
            return[1,0,0,0,1,1,1,1,1,0,0,1,0,0,0,1,1,0,0,0,1,0,0,1,1,0,0,1,1,1,1,1]
        elif zahl == 3:
            return[1,0,0,0,1,0,0,1,1,0,0,1,0,0,0,1,1,0,0,0,1,0,0,1,1,1,1,1,1,1,1,1]
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
    
    def zahl_zu_bit_ungeradeReihe(self, zahl):
        '''eine Zahl von 0 bis 9 in Bitmuster'''
        if zahl == 0:
            return[1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1]
        elif zahl == 1:
            return[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1]
        elif zahl == 2:
            return[1,1,1,1,0,0,0,1,1,0,0,0,1,0,0,1,1,0,0,1,0,0,0,1,1,1,1,1,1,0,0,1]
        elif zahl == 3:
            return[1,0,0,1,0,0,0,1,1,0,0,0,1,0,0,1,1,0,0,1,0,0,0,1,1,1,1,1,1,1,1,1]
        elif zahl == 4:
            return[0,0,0,1,1,1,1,1,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,1,1,1,1,1,1,1,1]
        elif zahl == 5:
            return[1,0,0,1,1,1,1,1,1,0,0,0,1,0,0,1,1,0,0,1,0,0,0,1,1,0,0,0,1,1,1,1]
        elif zahl == 6:
            return[1,1,1,1,1,1,1,1,1,0,0,0,1,0,0,1,1,0,0,1,0,0,0,1,1,0,0,0,1,1,1,1]
        elif zahl == 7:
            return[0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1]
        elif zahl == 8:
            return[1,1,1,1,1,1,1,1,1,0,0,0,1,0,0,1,1,0,0,1,0,0,0,1,1,1,1,1,1,1,1,1]
        elif zahl == 9:
            return[1,0,0,1,1,1,1,1,1,0,0,0,1,0,0,1,1,0,0,1,0,0,0,1,1,1,1,1,1,1,1,1]

    def einzel_zahl_speichern(self,zahl,reihe,farbe):
        #zahlen müssen im geraden Bereich sein
        self.buffer=[]
        if reihe % 2:
            buffer=self.zahl_zu_bit_ungeradeReihe(zahl)
        else:
            buffer=self.zahl_zu_bit_geradeReihe(zahl)

        self.merke=(reihe*8)

        for i in range (self.merke,(self.merke+32)):
            
            self.bufferIndex=i-self.merke

            if (buffer[self.bufferIndex])==1:
                self.ledArray[i][2]=self.brightness
                self.ledArray[i][0]=farbe

            elif (buffer[self.bufferIndex])==0:
                self.ledArray[i][2]=0   
                self.ledArray[i][0]=farbe
    
    def doppelte_zahl_speichern(self,zahl,reihe,farbe):
        self.doppelpack=str(zahl)
        
        if len(self.doppelpack)==1:
            self.einzel_zahl_speichern(0,reihe,farbe)
            self.einzel_zahl_speichern(zahl,reihe+5,farbe)
        elif len(self.doppelpack)==2:
            self.einzel_zahl_speichern(int(self.doppelpack[0]),reihe,farbe)
            self.einzel_zahl_speichern(int(self.doppelpack[1]),reihe+5,farbe)

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

    def lichtEinstellen(self,h,s,v):
        
        if self.flag == False:
            self.brightness=v/100
            self.farbeStunde_Miute=(h/360)
            self.farbeSekunde=(h/360)+0.3
            self.setAllSaturation(s/100)
        
    def setFlag (self,flag):
        self.flag=flag
        if flag==True:
            brightness=0.35

    def automaticBrightness(self,morgen):
        if flag==True:
            if morgen==False:
                for i in range(101):
                    self.brightness=self.brightness-0.001
                    time.sleep(1/110)
            
            elif morgen==True:
                for i in range(101):
                    self.brightness=self.brightness+0.001
                    time.sleep(1/110)    

   
    