#!/usr/bin/env python
# -*-coding:utf-8-*-
import              pygame
from pygame.locals import *

import              copy
import              pgwidth
import              pgrect
import              pgrect_window

class rect:
    ""
    def __init__(self,root,rt,rect_type):
        ""
        self.               root                =   root
        self.               rt                  =   rt
        self.               rect_type           =   rect_type
        self.               name                =   "win"
        self.               n_col               =   None
        self.               rect_type           =   0
        self.               rect_act            =   []

        self.               pos                 =   [100,100]
        self.               size                =   [100,80]
        self.               ima_load            =   "tux.jpg"
        self.               font_text           =   "et encore 1"
        self.               font_size           =   20
        self.               font_color          =   [0,255,125]

        self.               move                =   (1,0,0)
        self.               ms_touch            =   1
        
        self.rect_act.      append(pgrect.rect(self.root,self.rt))
        self.               rect_name           =   self.rect_act[-1]
        self.               rect_nm             =   self.rect_act.index(self.rect_name)
        

  
        
        


    def t_rect0(self):
        ""
        
        self.rect_act[self.rect_nm].  pos           =   self.pos
        self.rect_act[self.rect_nm].  size          =   self.size
        self.rect_act[self.rect_nm].  ima_load      =   self.ima_load
        self.rect_act[self.rect_nm].  font_text     =   self.font_text
        self.rect_act[self.rect_nm].  font_size     =   self.font_size
        self.rect_act[self.rect_nm].  font_color    =   self.font_color
        self.rect_type                              =   None
        self.rt.act.            append(self.rect_act[self.rect_nm])
        #return self.rect_name


    def t_rect1(self):
        ""
    def re_rect(self):
        #---------------------------
        if self.rect_type                   != None:
            if          self.rect_type      ==  0       :self.t_rect0()
            elif        self.rect_type      ==  1       :self.t_rect1()
            
        self.                   rect_nm     =   self.rect_act.index(self.rect_name)
        self.rect_act[self.rect_nm].  re_rect()

    
        

    
        
                             

    def dispaly(self):
        ""

    def mainloop(self):
        ""
    def bye(self):
        ""

if __name__=='__main__':
    ""
    a                       =               pgwidth.width()
    a.  width()
    b                       =   rect(a.root,a,0)
    b.  pos                 =   [10,10]

    b.  re_rect()

    

    a.  mainloop()
    

