# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 10:15:54 2012

parallel imaging fake coil sensitivity generator

@author: eric
"""

from scipy.ndimage import distance_transform_edt
from numpy import zeros, array, exp, pi, around


def coil_gen(sz,phases=None):
    cmaps=zeros([sz[0],sz[1],sz[2]],complex)
    vecs=array([-sz[0]/2+2+4j,-sz[0]/2+2-4j])
    #print vecs
    step=exp(-1j*2*pi/sz[2])
    #print step
    for coil in range(sz[2]):
        #print int(vecs.real)
        
        #print vecs
        #step=exp(-1j*coil*pi/sz[2])
        cmaps[around(vecs.real+sz[0]/2).astype(int),around(vecs.imag+sz[0]/2).astype(int),coil]=1
        vecs*=step
        cmaps[:,:,coil]=distance_transform_edt(cmaps[:,:,coil]==0)
        cmaps[:,:,coil]=max(cmaps[:,:,coil].flatten())-cmaps[:,:,coil]
        if phases!=None:
            cmaps[:,:,coil]*=phases[coil]
    return cmaps  