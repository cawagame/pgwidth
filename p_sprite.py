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

        self.ima_               = "sprite_megaman.jpg"
        self.toto               =   pgwidth.width()
        
        self.toto.  size        =   [1200,900]
        self.toto.  ima_papier  =   [255,255,255]
        
        self.toto.  width()

        self.sp_im              =   pgrect.rect(self.toto.root,self.toto.rt)
        


    def totoact(self):

        self.toto.act.append(self.sp_im)
        
            
            
            
       


    def mainloop(self):
        ""
        self.toto.mainloop()
        


if __name__ =='__main__':
    ""
    a =rect()
    a.totoact()
    a.mainloop()
