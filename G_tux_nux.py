#!/usr/bin/env python
# -*-coding:utf-8-*-
import              pygame
from pygame.locals import *

import              copy
import              pgwidth
import              pgrect
import              pgrect_window
import time


class rect:
    def __init__                (self,root,rt,ima_lo)      :
        ""
        self.   root                                =   root
        self.   rt                                  =   rt
        self.   act                                 =   []
        self.   ima_lo                            =   ima_lo
        

    def re_rect                 (self,n_rect=10,ima_ima=None ):
        ""
        
        for y in range(1,22):
            self.dessi_1(n_rect,y)
        #0-38 39-
        self.dessin_off     =[4,5,6,7,12,13,14,15,16,17,38,37,36,35,39,40]
        #for i in self.dessin_off:
         #   self.act[i].on      =None        
        
    def dessi_1                 (self,n_rect,y):
        for i in range(1,n_rect):
            ""
            self.act.append(    pgrect.rect(self.root,self.rt))
            self.act[-1].   size                    =   [20,20]
            self.act[-1].   pos                     =   [0+i*33,800-y*33]
            self.act[-1].   ima_load                =   self.ima_lo
            self.act[-1].   font_text               =   None
            self.act[-1].   name                    =   str([i,y])
            self.act[-1].   re_rect()
            self.act[-1].ms_cl1                     =   self.close_block
            self.rt.act.append(self.act[-1])
    

    def close_block(self):
        print self.rt.ms_app[-1].name
        


if __name__=='__main__':
    ""
   
    print time.time()
    a           =   pgwidth.width()
    a.size      =   (1600,800)
    a.ima_papier=[250,250,250]
    a.width()
    
    
    bock0       =   rect(a.root,a,"block.jpg")
    
    bock0.re_rect()
    print time.time()
    a.mainloop()
    print time.time()
    
