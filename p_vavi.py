#!/usr/bin/env python
# -*-coding:utf-8-*-
import pygame
from pygame.locals import *

import copy
import pgwidth
import pgrect
import pgrect_window


class rect:
    def __init__(self):

        ""

        self.ima_               =   ["vavi/im_vide.png",
                                  "vavi/im_vide_activ.png",
                                  "vavi/im_novide.png",
                                  "vavi/im_novide_activ.png"]
        self.ima                =   []
        self.rect_ima           =   []


        self.toto               =   pgwidth.width()
        
        self.toto.  size        =   [1200,900]
        self.toto.  ima_papier  =   [255,255,255]
        
        self.toto.  width()
        for i in self.ima_:
            self.ima.   append(pygame.image.load(i).convert_alpha())
            self.ima[-1]   =pygame.transform.scale(self.ima[-1],[12,25])

        for i in range(50):
            ""
            self.rect_ima.  append(pgrect.rect(self.toto.root,self.toto))
            self.rect_ima[-1]. size =[12,25]
            self.rect_ima[-1].  pos =[10+i*14,10]
            self.rect_ima[-1]. ima_ima =self.ima[0]
            self.toto.act.  append(self.rect_ima[-1])
            
            
            
       


    def mainloop(self):
        ""
        self.toto.mainloop()
        


if __name__ =='__main__':
    ""
    a =rect()
    a.mainloop()
