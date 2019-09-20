#!/usr/bin/env python
# -*-coding:utf-8-*-
import              pygame
from pygame.locals import *
import              copy
import              time

class width:
    "2017"
    def __init__(self):
        ""
        pygame.init()
        self.rt                     =           None
        self.size                   =           [800,400]
        self.title                  =           "WIDTH 2017"
        self.ima_papier             =           [200,150,250]
        self.ima_papier             =          "payssage.jpg"
        
        self.ima_pos                =           [0,0]
        self.unappuit               =           0
        self.py_image               =           ""
        #----------------        
        self.time                   =           20
        self.ms_touch               =           []
        self.ms_app                 =           []
        self.act                    =           []

        self.ms_down_up             =           None
        self.tt                     =           time.time()
        self.   nu_col              =           0
        
        

    def re_init                         (self)  :
        ""

    def n_col                           (self)  :
        ""
        self.   nu_col              =       self.nu_col +1
        a,b,c                       =       0,0,0
        print self.act
        out0                        =   len(self.act)
        print out0
        
        if out0 <15626              :
            a                       =   out0/25
            out0                    =   out0-(a *25)
        if out0 <626                :
            b                       =   out0 /25
            out0                    =   out0-(b *25)
        if out0 <26                 :   c =out0
        return (a*25,b*25,c*25)

        
            
        
        

    def image(self):
        "load image"
        self.ima_ima                =           pygame.image.load(self.ima_papier)
        
    def width(self):
        ""
        self.root                   =           pygame.display.set_mode(self.size)
        
        self.fond_ecran()


    def fond_ecran(self):
        if type(self.ima_papier)     ==  type("")    :
            ""
            self.ima_ima                =           pygame.image.load(self.ima_papier)
            #if self.ima_move        ==1:self.ima_pos[1] =self.ima_pos[1]-1
            self.root.blit(self.ima_ima,self.ima_pos)
                
        else:
            self.root.fill(self.ima_papier)
   
        
    

    def mainloop(self):
        ""
        while 1:
            #self.mouse          =pygame.mouse
            
            
            for self.event in pygame.event.get()    :
                if(self.event.type==pygame.QUIT or (self.event.type==pygame.KEYDOWN and self.event.key==pygame.K_ESCAPE)):
                    #pygame.quit()
                    return
                
                if self.event.type == pygame.MOUSEBUTTONUP:
                    self.ms_down_up         =   0
                elif self.event.type == pygame.MOUSEBUTTONDOWN:
                    self.ms_down_up         =   1
                elif self.event.type == pygame.MOUSEMOTION:
                    self.ms_down_up         =   2

                if self.ms_down_up          ==  1     :
                    self.unappuit           =   1
                    self.mouse_pre          =   pygame.mouse.get_pressed()
                if self.ms_down_up          ==  0 and self.unappuit==1:
                    self.unappuit =2
                #print self.ms_down_up
                    

            if self.act         !=None:
                for i in self.act:
                    if i.on ==1:
                       
                        i.display()
                        i.mainloop()

            #print self.ms_touch  <---
            


                
            
            if self.unappuit                ==  2       :
                self.unappuit               =   0
                self.mouse_pre              =   (0,0,0)
            #pygame.time.wait(self.time)
      
            if time.time()-self.tt          >(self.time)/100:
                self.tt                     =   time.time()
                pygame.display.update()
                self.fond_ecran()
                self.ms_touch               =   []
            
            

if __name__ == '__main__':
    a =width()
    a.width()
    a.mainloop()
