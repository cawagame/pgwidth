#!/usr/bin/env python
# -*-coding:utf-8-*-
import pygame
from pygame.locals import *
import pgwidth
import window

def bb():
    global a
    z   =copy.copy(b)
    z.pos =[10,20]
    a.act.append(z)

        
a   =pgwidth.width()
a.width()
b   =window.window(a.root,a)
b.ms_cl3 = "print 'essai_cl.py'"
b.ms_cl2 =bb

c   =window.window(a.root,a)
c.color =[255,0,255]
c.pos   =[4,100]
    #b.display()
a.act.append(c)
a.act.append(b)
a.mainloop()
