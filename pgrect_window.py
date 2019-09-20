#!/usr/bin/env python
# -*-coding:utf-8-*-
import pygame
from pygame.locals import *

import copy
import pgwidth
import pgrect
class rect:
    ""
    def __init__(self,root=None,rt=None):
        ""
        self.root                       =   root
        self.rt                         =   rt
        self.name                       =   "window"
        self.n_col                      =   None
        self.on                         =   1
        self.color                      =   [125,255,90]
        self.pos                        =   [100,20]
        self.size                       =   [180,70]
        
        self.w0                         =   1
        self.w1                         =   2
        self.on                         =   1
        self.color_fo                   =   [255,250,250]

        self.text                       =   None
        self.ima_load                   =   None
        
        self.font_size                  =   20
        self.font_color                 =   [0,0,0]

        self.act                        =   []
        #self.re_rect()
       



    def re_rect(self):
        ""
        self.act                        =   []  #purge act en car de re_
        
        self.rect0_fo                   =   pgrect.rect(self.root,self.rt)
        self.rect0_fo.on                =   self.on
        self.rect0_fo.ms_touch          =   None
        self.rect0_fo.move              =   None
        self.rect0_fo.pos               =   self.pos
        self.rect0_fo.size              =   [self.size[0],20]
        self.rect0_fo.color             =   self.color_fo
        self.rect0_fo.w                 =   0
        self.rect0_fo.font_text         =   None
        self.rect0_fo.ima_load          =   None
        

        self.rect_fo                    =   copy.copy(self.rect0_fo)
        self.rect_fo.pos                =   [self.pos[0],self.pos[1]+21]
        self.rect_fo.size               =   self.size
    
    

        self.rect0                      =   copy.copy(self.rect0_fo)
        #î_!
        self.rect_fo.ima_load   =   self.ima_load
           
        
        self.rect0.ms_touch             =   1
        self.rect0.move                 =   (1,0,0)
        self.rect0.color                =   self.color
           
        self.rect0.w0                   =   self.w0
        self.rect0.w1                   =   self.w1

        
        self.rect                       =   copy.copy(self.rect0)
        self.rect.move                  =   None
        self.rect.pos                   =   [self.pos[0],self.pos[1]+21]
        self.rect.size                  =   self.size

        self.rect_bye                   =   copy.copy(self.rect0_fo)
        self.rect_bye.ms_touch          =   1
        self.rect_bye.pos               =   [self.pos[0]+self.size[0]-10,self.pos[1]+1]
        #self.rect_bye.size              =   [self.size[0]-(self.pos[0]+60),self.pos[1]-2]
        self.rect_bye.size              =   [20,20]
        self.rect_bye.color             =   self.color
        self.rect_bye.w0                =   0
        self.rect_bye.w1                =   1

        self.rect0.font_text            =   self.text
        self.rect0.font_size            =   self.font_size
        self.rect0.font_color           =   self.font_color
        self.rect0.re_font()

        

        

        self.rt.act.    append          (   self.rect0_fo   )
        self.rt.act.    append          (   self.rect_fo    )
        self.rt.act.    append          (   self.rect0      )
        self.rt.act.    append          (   self.rect_bye   )
        self.rt.act.    append          (   self.rect       )
        
        self.act.       append          (    self.rect      )                            
        self.act.       append          (    self           )
        self.act.       append          (    self.rect0_fo  )
        self.act.       append          (    self.rect_fo   )
        self.act.       append          (    self.rect0     )
        self.act.       append          (    self.rect_bye  )


        self.rect0.ms_cl3               =self.act_rect0_3
        self.rect_bye.ms_cl1            =self.bye

        if self.ima_load                !=None:
            self.rect_fo.re_ima()
            self.rt.act.remove(self.rect0)
            self.rt.act.remove(self.rect0_fo)
            
            self.act.remove(self.rect0)
            self.act.remove(self.rect0_fo)
            self.rect.ms_touch          =   1
            self.rect.move              =   (1,0,0)
            
            a   =self.rect.pos[0]+self.rect.size[0]-20
            b   =self.rect.pos[1]
            self.rect_bye.pos           =   [a,b]
            #self.rect_bye.on            =   None
        
           

    def act_rect0_3(self):
        if self.rect_fo.        on      !=  None:
            self.rect_fo.       on      =   None
            self.rect.          on      =   None
        else:
            self.rect_fo.       on      =   1
            self.rect.          on      =   1

   

    def display(self):
        ""



    def mainloop(self):
        
        if      self.ima_load           !=  None    :   self.mainloop_ima()
        elif    self.ima_load           == None     :   self.mainloop_tex()
        #print self.rt.ms_touch
    def mainloop_tex(self):
        ""
        
        if self.rect0.xy                ==  15      :
            self.   pos                 =   self.   rect0.pos
            self.   rect0_fo.   pos     =   self.   pos
            self.   rect0.      pos     =   self.   pos
            self.   rect_fo.    pos     =   [self.pos[0],self.pos[1]+21]
            self.   rect.       pos     =   [self.pos[0],self.pos[1]+21]
            self.   rect_bye.   pos     =   [self.pos[0]+self.size[0]-10,self.pos[1]+1]
            
        


    def mainloop_ima(self):
        ""
        
        if self.rect.xy                 ==  15      :
            self.rect_fo.pos            =   self.rect.pos
            self.rect_bye.pos           =   [20,20]
            d       =self.rect.pos[0]+self.rect.size[0]-20
            b       =self.rect.pos[1]
            self.rect_bye.pos           =   [d,b]
            self.rect_bye.on            =   1
        else:
            self.rect_bye.on            =   None

    

    

    def bye(self):
        ""
        for i in self.act:
            self.rt.act.remove(i)
        

if __name__=='__main__':
    ""
    a               =pgwidth.width()
    a.width()
    
    w               =rect(a.root,a)
    w.text          ="Moi TOI"
    w.ima_load      =None
    w.pos           =[0,40]
    w.re_rect()
    a.act.append(w)
    
    wi              =rect(a.root,a)
    wi.ima_load     ="tux.jpg"
    wi.pos          =[200,40]
    wi.re_rect()
    a.act.append(wi)

    wi1             =rect(a.root,a)
    wi1.ima_load    ="tux noir.jpg"
    wi1.pos         =[400,40]
    wi1.re_rect()
    a.act.append(wi1)

    wt              =rect(a.root,a)
    wt.text         ="moi toi present"
    wt.pos          =[0,150]
    wt.re_rect()
    wt.rect.font_text   ="et apres"
    wt.rect.font_size   =30
    wt.rect.font_color  =[250,55,120]
    wt.rect.re_font()
    a.act.append (wt)

    wte             =   pgrect.rect(a.root,a)
    wte.pos         =   [200,150]
    wte.size        =   [180,70]
    wte.color       =   [255,255,255 ]
    wte.w           =   0
    wte.ms_touch    =   1
    wte.ima_load    ="tux trans.gif"
    wte.re_ima()
    a.act.append(wte)
    
    

    
    a.mainloop()

    

    

        
        
