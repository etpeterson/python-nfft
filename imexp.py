# -*- coding: utf-8 -*-
"""
Created on Fri May 25 11:50:58 2012

Inputs: same as imshow
Outputs: None
This is the sqme as imshow, except it displays the cursor location and pixel value
under the cursor, as well as allows scrolling through 3D images and intensity rescaling
using a right click and drag. Pressing w resets the window/level parameters. It
also contains a figure() call, so no need to do that manually!

@author: eric
"""

from matplotlib.pyplot import imshow, gca, show, figure, figtext
from numpy import shape, zeros, exp, atleast_3d
from phantom import phantom

    
class mouseloc:
    def __init__(self):
        self.x=0
        self.y=0
        self.press=0
        
class visualizationvalues:
    def __init__(self):
        self.vmin=0
        self.vmax=0
        self.slice=0
    
def imexp(img,*args,**kwargs):
    #print format_coord(1,1)
    img=atleast_3d(img)
    #print shape(img)
    mloc=mouseloc()
    vvals=visualizationvalues()
    sx=float(shape(img)[0])
    sy=float(shape(img)[1])
    sz=shape(img)[2]
    vmin_orig=min(img.flatten())
    vmax_orig=max(img.flatten())
        
    def format_coord(x, y):
        x = int(x + 0.5)
        y = int(y + 0.5)
        try:
            return "%g [%i, %i]" % (img[y,x,vvals.slice], y, x)
        except IndexError:
            return ""
    
    fig=figure()
    ims=imshow(img[:,:,sz/2],vmin=vmin_orig,vmax=vmax_orig,*args,**kwargs)
    #vmin_orig,vmax_orig=ims.get_clim()
    gca().format_coord = format_coord
    figtxt=figtext(0.5,0.95,"[%.2g,%.2g] of [%.2g,%.2g]" % (vvals.vmin,vvals.vmax,vmin_orig,vmax_orig))
    sltxt=figtext(0.5,0.05,"slice = %d" % vvals.slice)
    vvals.vmax=vmax_orig
    vvals.vmin=vmin_orig
    vvals.slice=sz/2
    #return fig
            
    def onclick(event):
        #print(event.button,event.x,event.y,event.xdata,event.ydata) #xdata and ydata are the coordinates
        #print(x,y)
        if event.xdata!=None:
            if event.button==3:
                mloc.x=event.xdata
                mloc.y=event.ydata
                mloc.press=1
                #print [mloc.x,mloc.y]
            
    
            
    def onrelease(event):
        #print event
        if event.xdata!=None:
            if event.button==3:
                mloc.press=0
                #print [mloc.x,mloc.y]
                vvals.vmax+=(vmax_orig-vmin_orig)*(event.xdata-mloc.x)/sx
                vvals.vmin+=(vmax_orig-vmin_orig)*(event.ydata-mloc.y)/sy
                vvals.vmax=max(vvals.vmax,vvals.vmin)
                #print [vvals.vmin,vvals.vmax]
                ims.set_clim(vvals.vmin,vvals.vmax)
                figtxt.set_text("[%.2g,%.2g] of [%.2g,%.2g]" % (vvals.vmin,vvals.vmax,vmin_orig,vmax_orig))
                fig.canvas.draw()
        else:
            mloc.press=0
            
            
    def onmotion(event):
        if event.xdata!=None:
            if mloc.press:
                if event.button==3:
                    vmax=(vmax_orig-vmin_orig)*(event.xdata-mloc.x)/sx+vvals.vmax
                    vmin=(vmax_orig-vmin_orig)*(event.ydata-mloc.y)/sy+vvals.vmin
                    vmax=max(vmax,vmin)
                    #print [vmin,vmax]
                    ims.set_clim(vmin,vmax)
                    figtxt.set_text("[%.2g,%.2g] of [%.2g,%.2g]" % (vmin,vmax,vmin_orig,vmax_orig))
                    fig.canvas.draw()
        else:
            #vvals.vmax=vmax
            #vvals.vmin=vmin
            mloc.press=0
            
    def onscroll(event):
        vvals.slice-=event.step
        vvals.slice=max(vvals.slice,0)
        vvals.slice=min(vvals.slice,sz-1)
        ims.set_data(img[:,:,vvals.slice])
        sltxt.set_text("slice = %d" % vvals.slice)
        fig.canvas.draw()
        
    def onkey(event):
        #print event.key
        if event.key=='w':
            vvals.vmin=vmin_orig
            vvals.vmax=vmax_orig
            ims.set_clim(vvals.vmin,vvals.vmax)
            figtxt.set_text("[%.2g,%.2g] of [%.2g,%.2g]" % (vvals.vmin,vvals.vmax,vmin_orig,vmax_orig))
            fig.canvas.draw()
                
            
            
        
    fig.canvas.mpl_connect('button_press_event', onclick)
    fig.canvas.mpl_connect('motion_notify_event', onmotion)
    fig.canvas.mpl_connect('button_release_event',onrelease)
    fig.canvas.mpl_connect('scroll_event',onscroll)
    fig.canvas.mpl_connect('key_press_event',onkey)
    
    
    

    #p_base=phantom(128)
    #p=zeros([128,128,10])
    #for k in range(10):
    #    #print k
    #    #print exp(-k/10.0)
    #    p[:,:,k]=p_base*exp(-k/10.0)
    ##f=figure()
    #
    #imexp(p/100) #and it accepts arguments!
    #show()