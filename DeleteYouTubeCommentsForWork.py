# -*- coding: utf-8 -*-
"""
Created on Wed May 22 11:33:51 2019
Needs pyautogui, opencv-python and likely a few other things. Depends on how
you install it all. 
Designed for delete comments relatively quickly. Created because -- I don't
Think I'm even allowed to explain. Oh well. If you need to self censor and
don't feel like wasting too much time, here you go.
@author: Johnny
"""
import pyautogui as py

def locator(): ### locates the delete menu in youtube
    test1 = 'DeleteMenu.png'
    cent = py.locateCenterOnScreen(test1, region = (1200,800, 400,400))
    py.moveTo(cent[0:2])
    py.click(button = 'left')

def locator2(): ###locates the delete button on the menu
    test2 = 'DeleteButton.png'
    cent = py.locateOnScreen(test2, region = (1200,800, 400,400))
    py.moveTo(cent[0:2])
    py.click(button = 'left')

def Delete(): ###Looks for the delete button, confidence lowered because the
    ###reply delete and comment delete text are ever so slightly different. Looked for
    ### how different in the CSS and HTML code of Youtube, couldn't find it
    test = 'Delete.png'
    test3 = py.locateOnScreen(test, confidence = .8)
    py.moveTo(test3[0:2])
    py.click(button = 'left')
        
def Mover(): ###Calls the functioms to move things###
    ### Change the range if you want, and the other positions that have been
    ###hardcoded as needed for the size of your screen
    for i in range(20000):
        py.moveTo(1200, 933)
        py.PAUSE = .2
        locator()
        locator2()
        Delete()
        
Mover()
