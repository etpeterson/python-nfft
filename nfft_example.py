# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 17:33:44 2012

NFFT example script
This script simply demonstrates how to use the basic gridding functionality of
NFFT as well as using the conjugate gradient function to perform a SENSE reconstruction.

@author: Eric Peterson
"""

from phantom import phantom
from math import pi
from matplotlib.pyplot import show, title
from scipy.signal import medfilt2d
from numpy import exp, tile, expand_dims, ones_like
from coil_gen import coil_gen
from imexp import imexp
from nfft_wrappers import *
from nfft_helpers import *




use_propeller=True
if use_propeller==True:
    blade=[128,25]  #size of each blade, probably [128,25],[128,51]
    nblades=4   #number of blades, probably 4,8
    M_py=[blade[0],blade[1]*nblades] #data size
else: #radial
    M_py=[128,64]

#ONLY SQUARE OUTPUT IMAGES!!!
N_py=[128,128] #input/output image size
num_iters=20 #CG iterations to perform
ro_loc_pad=2 #weighting padding, don't change!!!
sensefactor=2 #sense factor for propeller phase encode spacing
ncoils=4 #number of coils


#generate the phantom
phan=phantom(N_py[0])+1j*0 #complex but no real complex information




#initialize the sampling locations
if use_propeller==1:
    locs_vec,locs=propeller_sampling_location_generator(blade,nblades,sense_factor=sensefactor)
else:
    locs_vec,locs=projection_sampling_location_generator(M_py)

    
#FOV support
fov=comp_fov(N_py,thresh=1)
phan*=fov #limit the FOV, not really necessary with a digital phantom


#calculate the density weighting
if use_propeller==1:
    w=calc_density_weights(M_py,ro_loc_pad,blade=blade,nblades=nblades)
    w=medfilt2d(w,7) #make the weights better, voronoi isn't quite right for some reason...
else:
    w=calc_density_weights(M_py,ro_loc_pad)


#generate coil images, each coil has a certain phase as well
csize=(N_py[0],N_py[1],ncoils)
coils=coil_gen(csize,[exp(1j*pi/3),exp(-1j*pi/2),exp(1j*pi/4),exp(-1j*pi/6),exp(1j*pi/8),exp(-1j*pi/8),exp(1j*pi/10),exp(-1j*pi/13)])
coils/=max(abs(coils).flatten())

    
#test the gridding framework
#basic gridding
grid_struct=grid_etp(N_py,M_py,fov_support=fov,w=w)
grid_struct.initialize_gridding(locs)

data=grid_struct.igrid(phan)
img=grid_struct.grid(data)

#let's reconstruct using CG even though it can't recover the full image
grid_struct.w=ones_like(grid_struct.w) #to get the best noise performance set w to ones
img_nosense_cg,niter_cg,resid_cg=grid_struct.cg_solve(data,img,maxiter=num_iters,verbose=True)

#SENSE
grid_sense_struct=grid_etp(N_py,M_py,fov_support=fov,w=tile(expand_dims(w,2),[1,1,ncoils]),coils=coils)
grid_sense_struct.initialize_gridding(locs)

data_sense=grid_sense_struct.igrid(phan)
img_sense=grid_sense_struct.grid(data_sense)

#to use SENSE we need to solve using an iterative conjugate gradient method
grid_sense_struct.w=ones_like(grid_sense_struct.w) #to get the best noise performance set w to ones
img_sense_cg,niter_sense_cg,resid_sense_cg=grid_sense_struct.cg_solve(data_sense,img_sense,maxiter=num_iters,verbose=True)


imexp(abs(phan))
title('truth')
imexp(abs(img))
title('gridding without coil information')
imexp(abs(img_nosense_cg))
title('CG iterations without coil information') #this looks pretty good because the center is fully sampled with the 4 blades all overlapping there!
imexp(abs(img_sense))
title('gridding with coil information')
imexp(abs(img_sense_cg))
title('CG iterations with coil information (SENSE)') #this image is the SENSE result
show()
