#!/usr/bin/env python
# -*-coding:utf-8-*-
import pygame
from pygame.locals import *
import copy
import pgwidth
class rect:

    def __init__(self,root=None,rt=None,ima_ima=None):
        ""
        self.   rt                      =       rt
        self.   root                    =       root
        self.   name                    =       "rect"
        self.   n_cola                  =       None
        
        
        self.   color                   =       [20,30,40]
        self.   pos                     =       [70,70]
        self.   size                    =       [50,50]
        self.   w                       =       1
        self.   w0                      =       2
        self.   w1                      =       7
        self.   unappuit                =       0
        self.   nu_ftouch               =       0   #nombre fois toucher activer
        #option ---------------------------------
        self.   on                      =       1
        self.   on_dis                  =       1
        self.   ms_touch                =       1
        #option mouse -----------------------------
        self.   move                    =       (1,0,0)
        
        self.   ms_cl1                  =       None
        self.   ms_cl2                  =       None
        self.   ms_cl3                  =       None
        #option font ----------------------------
        #self.   font_text               =       "VAVA" #ou None
        self.font_text              =           None
        self.   font_size               =       50
        self.   font_color              =       [0,128,0]
        self.   font_font               =       "comicsansms"
        
        #option image -----------------------
        #self.   ima_load                =       "tux.jpg"
        self.   ima_ima                 =       ima_ima
        self.ima_load               =           None
        #print self.ima_ima
        self.   re_rect                         ()
        
    def re_rect                                 (self):
    
        if self.ima_load !=  None and self.ima_ima ==None    :   self.re_ima()
        if self.    font_text       !=  None    :   self.re_font()
    def re_font                                 (self):
        "re_init option font "
        self.   font                    =       pygame.font.SysFont(self.font_font, self.font_size)
        self.   di_tx                   =       self.font.render(self.font_text, True, self.font_color)

    def re_ima                                  (self):
        "re_init option ima"
        self.   ima_ima                 =       pygame.image.load(self.ima_load).convert_alpha()
        self.   ima_ima                 =       pygame.transform.scale(self.ima_ima,self.size)
        
        
        
    

    def display                         (self,w=1):
        if self.on_dis              ==  1       :
            pygame.draw.rect(self.root,self.color,self.pos+self.size,self.w)
        if self.ima_load            !=  None    or self.ima_ima !=None:
            self.root.blit(self.ima_ima,self.pos)
        if self.font_text           !=  None    :
            self.root.blit(self.di_tx,(self.pos))



   

    def touch(self):
        "mouse touch"
        
        a,b                         =           self.pos[0],self.pos[1]
        c,d                         =           self.size[0],self.size[1]
        x,y                         =           pygame.mouse.get_pos()
        if a<x<a+c and b<y<+b+d             :   self.xy =15
        #if self.xy                  ==  15  :   self.display(w=self.w+1)
        if self.xy                  ==  15  :self.w =self.w1
        else:self.w =self.w0



                
    def mainloop(self):
        ""
        self.xy                     =           0

        #a,b     =pygame.mouse.get_rel()
        
        if self.ms_touch            ==  1   :   self.touch()
        
        #move mouse
        if self.xy                  ==  15  :
            
            self.rt.ms_touch.append(self)
            if pygame.mouse.get_pressed()   ==self.move:
                c,d                 =           pygame.mouse.get_rel()
                if c>20 or -20>c            :   c,d =0,0
                if d>20 or -20>d            :   c,d =0,0
                self.pos            =           [self.pos[0]+c,self.pos[1]+d]
        #-------------------- FIN move ------------
                
            if self.rt.unappuit                 ==  2           :
                self.rt.ms_app.append(self)
                if self.rt.mouse_pre            ==  (1,0,0)     :
                    if self.ms_cl1              !=  None        :
                        
                        if type(self.ms_cl1)    ==  type("")    :
                            exec(self.ms_cl1)
                        else                                    :
                            self.ms_cl1()
                        
                elif self.rt.mouse_pre          ==  (0,1,0)     :
                    if self.ms_cl2              !=  None        :
                        if type(self.ms_cl2)    ==  type("")    :
                            exec(self.ms_cl2)
                        else                                    :
                            self.ms_cl2()
                        
                elif self.rt.mouse_pre          ==  (0,0,1)     :
                    if self.ms_cl3              !=  None        :
                        if type(self.ms_cl3)    ==  type("")    :
                            exec(self.ms_cl3)
                        else                                    :
                            self.ms_cl3()

        
    def bye(self):
        "quit effacer tuer"
        try:
            self.rt.act.remove[self]
        except:
            ""
            
        

if __name__ == '__main__':

    
    
    def bb():
        global a
        z   =copy.copy(b)
        z.pos =[10,20]
        a.act.append(z)

        
    a   =pgwidth.width()
    a.width()

    im =pygame.image.load("vavi/im_vide.png").convert_alpha()
    im =pygame.transform.scale(im,[12,25])


    
    b   =rect(a.root,a)
    b.size =[12,25]
    b.ms_cl3 = "print 'essai_cl.py'"
    b.ms_cl2 =bb
    #b.ima_load="tux.jpg"
    b.pos   =[20,100]
    b.ima_ima=im
    #b.re_ima()
    c   =rect(a.root,a)
    c.color =[255,0,255]
    c.font_text ="anna"
    c.re_font()
    c.pos   =[200,100]
    #b.display()
    a.act.append(c)
    a.act.append(b)
    a.mainloop()
