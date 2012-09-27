# -*- coding: utf-8 -*-
"""
Created on Thu May  3 13:12:03 2012

Gridding and inverse gridding functions using the nfft library
This is an extensive wrapper for the nfft library which you can find online.
It not only wraps nfft but creates a class that was designed to reconstruct MRI images.

@author: eric
"""
    
class grid_etp:
    def __init__(self,N_py,datasize,fov_support=1,w=1,wI=None,coils=None,slices=None,blade_phase=None,use_nnfft=False,use_sense=None,use_bladewise=None,recon_blades=False,beta_eqn=0,time_res=8,alloc_type='some',overgridding_factor=1.2,gridding_kernel_size=2,bvec=None,bval=None):
        """This is a class which can be used for MRI reconstructions
        Inputs:
            self = this just means that it is initialized like this: gridder=grid_etp(N_py,M_py) (the most basic possible!)
            N_py [2,1] (int) = image size
            datasize [2,1] (int) = raw data size
            w [datasize] (floats) = 'density' weighting applied to the gridding (also used in the conjugate gradient section)
            wI [imagesize (N_py)] (floats) = weighting applied to the image (UNTESTED!)
            coils [imagesize,ncoils] (3D of floats) = coil sensitivity images for SENSE reconstructions (using cg_solve is required here for the real reconstruction)
            slices (int) = number of slices in a 3D matrix, but only if each slice is to be processed the same!
            blade_phase [imagesize,nblades] (3D of floats) = phase images for each propeller blade to be multiplied by the blade as it is reconstructed.
            use_nnfft (True/False) = use the nnfft gridding or not (nfft)
            use_sense (True/False) = force the SENSE processing to be used. typically set by the number of coils
            use_bladewise (True/False) = force the bladewise processing. typically set by the number of blades, which itself is set from blade_phase
            recon_blades (True/False) = force the reconstruction of each blade individually. useful for debugging or blade registration
            beta_eqn (0 or 1) = the beta equation for the conjugate gradient iterations. 0=Fletcher-Reeves, 1=Polak-Ribiere. I am not sure if this changes anything in linear CG, and the difference isn't tested!
            time_res (intever) = old parameter for nnfft gridding, but now it is outdated!
            alloc_type ('full','some','none') = allocation type passed to nfft. These are just some presets, 'some' is recommended as 'full' seems to not be any faster, and 'none' seems to not confer any other advantages.
            overgridding_factor (float) = the nfft overgridding factor
            gridding_kernel_size (float) = the nfft gridding kernel size
            bvec [N,3] (floats) = diffusion (b) vectors (directions) for the hackish direct to diffusion matrix reconstruction (requires b-values)
            bval [N] (floats) = diffusion (b) values for the hackish direct to diffusion matrix reconstruction (requires b-vectors)
        Outputs:
            None, it is used by calling gridder.grid(data) or gridder.cg_solve(data)
        Notes:
            It was designed to make repeatedly reconstructing images easy, as well as iterative reconstructions, so once it is constructed and initialized the data used can be changed as desired.
            This constructer was designed to make various types of reconstructions easy, and the initializer was designed to allow basic changes to that framework,
            however anything can be changed simply by accessing gridder.<variable>, nothing is private so use at your own risk!
            It has been expanded greatly beyond the original design, so some of the parameters don't work well together and there is very little error checking! I recommend that you copy setups if at all possible!
            Some basic setups are pretty simple, but be can hard to guess if you don't know, so just copy them if at all possible!
        """
        #TODO: add some parameter guessing here so I don't need to input as much
        #general parameters
        from numpy import shape
        #from numpy.linalg import pinv
        
        self.imsize=N_py
        self.use_nnfft=use_nnfft
        if blade_phase==None:
            self.nblades=1
        else:
            self.nblades=shape(blade_phase)[2]
        if coils==None:
            self.ncoils=1
        else:
            self.ncoils=shape(coils)[2]
        if use_sense==None:
            if self.ncoils==1:
                self.use_sense=False
            else:
                self.use_sense=True
        if use_bladewise==None:
            if self.nblades==1:
                self.use_bladewise=False
            else:
                self.use_bladewise=True
        else:
            self.use_bladewise=use_bladewise
        if slices==None:
            self.use_slices=False
        else:
            self.use_slices=True
            self.slices=slices
            self.datasize_slices=[datasize[0],datasize[1],slices]
            self.imsize_slices=[self.imsize[0],self.imsize[1],self.slices]
        self.beta_eqn=beta_eqn
        self.recon_blades=recon_blades
        self.g=[]
        self.g_inv=[]
        
        self.imsize_coil=[self.imsize[0],self.imsize[1],self.ncoils]
        self.imsize_blades=[self.imsize[0],self.imsize[1],self.nblades]
        self.imsize_coil_blades=[self.imsize[0],self.imsize[1],self.ncoils,self.nblades]
        self.imsize_direct=[self.imsize[0],self.imsize[1],6]
        if self.ncoils==1: #to prevent 1's from sitting around and messing up sizing
            self.datasize=[datasize[0],datasize[1]]
        else:
            self.datasize=[datasize[0],datasize[1],self.ncoils]
        self.datasize_coil=[datasize[0],datasize[1],self.ncoils]
        
        self.bladesize=[datasize[0],datasize[1]/self.nblades]
        self.reset_iters=10
        
        #gridding parameters
        #self.ksp_locs=[] #[readout,(phase,blade),xyz] #no need to save this
        #self.img_locs=[] #[readout,(phase,blade),xyz] #no need to save this
        self.time_res=time_res
        self.alloc_type=alloc_type
        self.overgridding_factor=overgridding_factor
        self.gridding_kernel_size=gridding_kernel_size
        self.gridder=[]
        self.gridder_allocated=False
        self.ngridders=1
        
        #additional parameters
        if wI==None: #Image weights
            self.wI=fov_support
        else:
            self.wI=wI
        self.fov=fov_support
        self.w=w
        self.coils=coils
        self.blade_phase=blade_phase
        self.deformation_matrix=None
        self.deformation_translation=None
        self.deformation_matrix_inv=None
        self.deformation_translation_inv=None
        self.bvec=bvec
        self.bval=bval
        
        
    def initialize_gridding(self,ksp_locs,defmat=None,img_locs=None,fieldmap=None,g=None,b=None):
        """locs is [readout,(phase,blade),xyz] for nnfft and
        [readout,(phase,blade)] for nfft!
        Maybe this should change in the future..."""
        from numpy.linalg import inv, pinv
        from numpy import zeros_like, linspace, meshgrid, concatenate, expand_dims, shape, zeros
        
        if g!=None:
            sg=shape(g)
            #g_inv=pinv(g).transpose()
            g_inv=g
            self.g=zeros([sg[0],6])
            self.g_inv=zeros([sg[0],6])
            self.b=b #this needs to come in with g
            for l in range(sg[0]):
                #print(shape([g[l,0]*g[l,0],g[l,1]*g[l,1],g[l,2]*g[l,2],g[l,0]*g[l,1],g[l,0]*g[l,2],g[l,1]*g[l,2]]))
                #print l
                self.g[l,:]=[g[l,0]*g[l,0],g[l,1]*g[l,1],g[l,2]*g[l,2],g[l,0]*g[l,1],g[l,0]*g[l,2],g[l,1]*g[l,2]]
                self.g_inv[l,:]=[g_inv[l,0]*g_inv[l,0],g_inv[l,1]*g_inv[l,1],g_inv[l,2]*g_inv[l,2],g_inv[l,0]*g_inv[l,1],g_inv[l,0]*g_inv[l,2],g_inv[l,1]*g_inv[l,2]]
            self.g=self.g.transpose()
            self.g_inv=pinv(self.g_inv).transpose()
        if defmat!=None:
            self.deformation_matrix=defmat[0:2,0:2,:]
            self.deformation_translation=defmat[0:2,3,:]
            self.deformation_matrix_inv=zeros_like(self.deformation_matrix)
            self.deformation_translation_inv=zeros_like(self.deformation_translation)
            for blade in range(self.nblades):
                tmat=inv(defmat[:,:,blade])
                self.deformation_matrix_inv[:,:,blade]=tmat[0:2,0:2]
                self.deformation_translation_inv[:,blade]=tmat[0:2,3]
        self.ksp_locs=ksp_locs
        if img_locs==None and fieldmap==None:
            self.use_nnfft=False
            for blade in range(self.nblades): #todo create new, sleeker functions for this
                self.gridder.append(init_nfft_2d(self.ksp_locs[:,self.bladesize[1]*blade:self.bladesize[1]*(blade+1)],self.imsize[0],1,self.alloc_type,self.overgridding_factor,self.gridding_kernel_size))
        else:
            self.use_nnfft=True
            if fieldmap==None:
                self.img_locs=img_locs
            else:
                y,x=meshgrid(linspace(-0.5,0.5,self.imsize[0],False),linspace(-0.5,0.5,self.imsize[1],False))
                #print shape(y)
                #print shape(fieldmap)
                self.img_locs=concatenate((expand_dims(x,2),expand_dims(y,2),expand_dims(fieldmap,2)),2)
            for blade in range(self.nblades): #TODO: implement the affine deformation in nnfft gridding! Note that the sensitivities should be warped to represent the original orientation!
                self.gridder.append(init_nnfft_2d(self.img_locs,self.ksp_locs[:,self.bladesize[1]*blade:self.bladesize[1]*(blade+1),:],self.imsize,1,self.time_res,self.alloc_type,self.overgridding_factor,self.gridding_kernel_size))
        self.gridder_allocated=True
        
    def grid(self,data):
        #data is 4D (readout,blades (phase),coil,blade,slice(just repeated images)), the output img is 3D (X,Y,blade,slice(just repeated images))
        #from copy import copy
        from numpy import zeros, shape, dot, concatenate, atleast_3d
        from numpy.fft import fftshift, ifftshift, fftn, ifftn
        from scipy.ndimage.interpolation import affine_transform
        
        if self.gridder_allocated:
            if self.use_nnfft==True:
                grid_fun=grid_nnfft_2d
            else:
                grid_fun=grid_nfft_2d
            
            if self.recon_blades==False:
                if self.use_bladewise==False:
                    if self.use_sense==False:
                        if self.use_slices==False:
                            #print('as simple as possible gridding')
                            img=grid_fun(self.gridder[0],data*self.w)*self.fov
                        else:
                            #print('slicewise gridding for direct diffusion computation')
                            img_slices=zeros(self.imsize_slices,complex)
                            for k in range(self.slices):
                                img_slices[:,:,k]=grid_fun(self.gridder[self.usegridder[k]],data[:,:,k]*self.w)*self.fov
                            #img=img_slices*self.fov #placeholder for more manipulations
                            b0=img_slices[:,:,0]
                            img_slices=fftshift(fftn(fftshift(img_slices[:,:,1:],axes=(0,1)),axes=(0,1)),axes=(0,1))                            
                            img_slices=img_slices.reshape([self.imsize_slices[0]*self.imsize_slices[1],self.imsize_slices[2]-1])
                            img=dot(img_slices,self.g_inv)
                            #print shape(img)
                            img=img.reshape(self.imsize_direct)
                            img=ifftshift(ifftn(ifftshift(img,axes=(0,1)),axes=(0,1)),axes=(0,1))
                            img=concatenate((atleast_3d(b0),img),2)
                            #for k in range(6):
                            #    img[:,:,k]=self.fov*(-1/self.b[1]*log(img[:,:,k]/b0)) #just 1 b-value for now!
                            
                    else: #sense with coil sensitivity
                        #print('gridding sense with coils')
                        img_coils=zeros(self.imsize_coil,complex)
                        #data=copy(data)*self.w
                        for coil in range(self.ncoils):
                            img_coils[:,:,coil]=grid_fun(self.gridder[0],data[:,:,coil]*self.w[:,:,coil])
                        img_coils*=self.coils.conj()
                        img_coils=fftshift(fftn(fftshift(img_coils,axes=(0,1)),axes=(0,1)),axes=(0,1))
                        img=img_coils.sum(2)
                        img=ifftshift(ifftn(ifftshift(img,axes=(0,1)),axes=(0,1)),axes=(0,1))*self.fov
                else: #if we do bladewise sense, a few extra fft's won't hurt so just combine sense and bladewise
                    #print 'bladewise gridding'
                    #data=copy(data)*self.w
                    img_coils=zeros(self.imsize_coil,complex)
                    for coil in range(self.ncoils):
                        for blade in range(self.nblades):
                            #print(coil,blade)
                            #print shape(data)
                            #print shape(self.w)
                            #print shape(self.blade_phase)
                            timg=grid_fun(self.gridder[blade],data[:,self.bladesize[1]*blade:self.bladesize[1]*(blade+1),coil]*self.w[:,self.bladesize[1]*blade:self.bladesize[1]*(blade+1),coil])*self.blade_phase[:,:,blade].conj()*self.coils[:,:,coil].conj()
                            if self.deformation_matrix!=None and self.use_nnfft==False:
                                timg=affine_transform(timg.real,self.deformation_matrix[:,:,blade],offset=self.deformation_translation[:,blade])+1j*affine_transform(timg.imag,self.deformation_matrix[:,:,blade],offset=self.deformation_translation[:,blade])
                            img_coils[:,:,coil]+=fftshift(fftn(fftshift(timg*self.fov)))
                    #img_coils=fftshift(ifftn(fftshift(img_coils,axes=(0,1)),axes=(0,1)),axes=(0,1))
                    #img_coils*=self.coils.conj()
                    #img_coils=fftshift(fftn(fftshift(img_coils,axes=(0,1)),axes=(0,1)),axes=(0,1))
                    img=img_coils.sum(2)
                    img=ifftshift(ifftn(ifftshift(img,axes=(0,1)),axes=(0,1)),axes=(0,1))#*self.fov
            else: #blades individually. assuming coils and blades here!
                img_coils=zeros(self.imsize_coil_blades,complex)
                for coil in range(self.ncoils):
                    for blade in range(self.nblades):
                        #print(coil, blade)
                        #print self.coils[:,:,coil].conj()
                        #print self.blade_phase[:,:,blade].conj()
                        #print shape(self.w[:,self.bladesize[1]*blade:self.bladesize[1]*(blade+1),coil])
                        #print shape(data[:,self.bladesize[1]*blade:self.bladesize[1]*(blade+1),coil])
                        timg=grid_fun(self.gridder[blade],data[:,self.bladesize[1]*blade:self.bladesize[1]*(blade+1),coil]*self.w[:,self.bladesize[1]*blade:self.bladesize[1]*(blade+1),coil])
                        timg*=self.blade_phase[:,:,blade].conj()*self.coils[:,:,coil].conj()
                        if self.deformation_matrix!=None and self.use_nnfft==False:
                            timg=affine_transform(timg.real,self.deformation_matrix[:,:,blade],offset=self.deformation_translation[:,blade])+1j*affine_transform(timg.imag,self.deformation_matrix[:,:,blade],offset=self.deformation_translation[:,blade])
                        img_coils[:,:,coil,blade]=timg
                img=img_coils.sum(2).squeeze()*self.fov
        else:
            print('gridder not allocated! grid returning nothing')
            img=[]
        #print('returning')
        return img
            
    def igrid(self,img):
        #img is 3D (X,Y,blade,slice(just repeated images)), the output data is 4D (readout,blades (phase),coil,blade,slice(just repeated images))
        from numpy import zeros, dot, shape
        from scipy.ndimage.interpolation import affine_transform
        #from numpy import fftshift, fftn, ifftn
        
        if self.gridder_allocated:
            if self.use_nnfft==True:
                igrid_fun=igrid_nnfft_2d
            else:
                igrid_fun=igrid_nfft_2d
            
            #img*=self.fov
            if self.recon_blades==False:
                if self.use_bladewise==False:
                    if self.use_sense==False: #simple gridding
                        if self.use_slices==False:
                            #print('as simple as possible igridding')
                            data=igrid_fun(self.gridder[0],img*self.fov)
                        else:
                            #print('slicewise igridding for direct diffusion computation')
                            data=zeros(self.datasize_slices,complex)
                            b0=img[:,:,0]
                            img=img[:,:,1:].reshape([self.imsize_slices[0]*self.imsize_slices[1],6])
                            img=dot(img,self.g)
                            img=img.reshape([self.imsize_slices[0],self.imsize_slices[1],self.imsize_slices[2]-1])
                            data[:,:,0]=igrid_fun(self.gridder[0],b0*self.fov)
                            #print shape(img)
                            #print shape(data)
                            for k in range(1,self.slices):
                                #print k
                                data[:,:,k]=igrid_fun(self.gridder[self.usegridder[k]],img[:,:,k-1]*self.fov)
                    else: #sense gridding
                        #print('igrid sense and coil')
                        data=zeros(self.datasize,complex)
                        img*=self.fov
                        for coil in range(self.ncoils):
                            data[:,:,coil]=igrid_fun(self.gridder[0],img*self.coils[:,:,coil])
                else: #sense and bladewise
                    #print 'bladewise igridding'
                    #img*=self.fov
                    data=zeros(self.datasize_coil,complex) #datasize or datasize_coil?
                    #print shape(x)
                    for coil in range(self.ncoils):
                        #data[:,:,coil]=igrid_nfft_2d(nfft_struct,x*coils[:,:,coil])
                        for blade in range(self.nblades):
                            #print(bladesize[1]*blade,bladesize[1]*(blade+1),blade)
                            timg=img*self.coils[:,:,coil]*self.blade_phase[:,:,blade]
                            if self.deformation_matrix!=None and self.use_nnfft==False:
                                timg=affine_transform(timg.real,self.deformation_matrix_inv[:,:,blade],offset=self.deformation_translation_inv[:,blade])+1j*affine_transform(timg.imag,self.deformation_matrix_inv[:,:,blade],offset=self.deformation_translation_inv[:,blade])
                            data[:,self.bladesize[1]*blade:self.bladesize[1]*(blade+1),coil]=igrid_fun(self.gridder[blade],timg*self.fov)
            else: #blades individually (assuming sense)
                img*=self.fov
                data=zeros(self.datasize,complex)
                #print shape(x)
                for coil in range(self.ncoils):
                    #data[:,:,coil]=igrid_nfft_2d(nfft_struct,x*coils[:,:,coil])
                    for blade in range(self.nblades):
                        #print(bladesize[1]*blade,bladesize[1]*(blade+1),blade)
                        timg=img[:,:,blade]*self.coils[:,:,coil]*self.blade_phase[:,:,blade]
                        if self.deformation_matrix!=None and self.use_nnfft==False:
                            timg=affine_transform(timg.real,self.deformation_matrix_inv[:,:,blade],offset=self.deformation_translation_inv[:,blade])+1j*affine_transform(timg.imag,self.deformation_matrix_inv[:,:,blade],offset=self.deformation_translation_inv[:,blade])
                        data[:,self.bladesize[1]*blade:self.bladesize[1]*(blade+1),coil]=igrid_fun(self.gridder[blade],timg)
        else:
            print('gridder not allocated! igrid returning nothing')
            data=[]
        return data
        
    def cg_kspace_solve(self,b,x,maxiter=20,tol=1e-6,verbose=False): #from sutton et al 2003, doesn't seem to support SENSE!
        #from scipy.linalg import norm
        from numpy import dot, reshape#, shape
        from time import time
        
        if self.recon_blades==False:
            imsize_cg=self.imsize
        else:
            imsize_cg=self.imsize_blades
        if verbose:
            t_start=time()
        x*=self.wI
        r=(b-self.igrid(x)).flatten() #testing weighting!
        x=x.flatten()
        #b=b.flatten()
        #normb=norm(b)
        #p=r.copy()
        #if self.beta_eqn==1:
        #    r_m1=r.copy()
        gnew=(self.wI*self.grid(reshape(r,self.datasize))).flatten()
        #gnew=g.copy()
        gold=gnew.copy()
        #d=gnew.copy()
        #Ap=g
        rsnew=dot(gnew.conj().transpose(),gnew)
        #print rsnew
        #improd=imsize_cg[0]*imsize_cg[1]
     
        niter=0
        #resid=rsnew**0.5/normb
        #resid=rsnew
        tol=abs(rsnew*tol**2) #from painless CG, a fraction of the original
        #print('tol=%f'%tol)
        lastrsnew=abs(rsnew)
        while niter<maxiter and tol<abs(rsnew) and abs(rsnew)<=lastrsnew:
            lastrsnew=abs(rsnew)
            #print(niter<maxiter,tol<rsnew,tol,rsnew)
            niter+=1
            #gnew=self.grid(reshape(r,self.datasize)).flatten()
            #rsnew=dot(gnew.conj().transpose(),gnew)
            if niter==1:
                #beta=0
                d=gnew
            else:
                gnew=(self.wI*(self.grid(reshape(r,self.datasize)))).flatten()
                rsnew=dot(gnew.conj().transpose(),gnew)
                beta=rsnew/dot(gold.conj().transpose(),gold)
                d=gnew+beta*d
            #print beta
            #d=gnew+beta*d
            q=self.igrid(self.wI*reshape(d,imsize_cg)).flatten()
            alpha=dot(d.conj().transpose(),gnew)/dot(q.conj().transpose(),q*self.w.flatten()) #weighting seems legit here
            #print alpha
            x=x+alpha*d
            gold=gnew.copy()
            if niter%self.reset_iters==0:
                r=(b-self.igrid(reshape(x,imsize_cg))).flatten() #is this right for wI images?
            else:
                r=r-alpha*q
            #gold=gnew.copy()
            if verbose:
                print('iter=%d residual=%f'%(niter,abs(rsnew)))

        x=reshape(x,imsize_cg)
        x*=self.wI
        if verbose:
            print('CG time = %f s' % (time()-t_start))
        return x,niter,rsnew
        
        
    def cg_solve(self,b,x,maxiter=20,tol=1e-6,verbose=False): #from pruessmann 2001
        from scipy.linalg import norm
        from numpy import dot, reshape, shape, isnan, vdot, nan_to_num, isfinite, zeros_like, atleast_3d
        from time import time
        
        if self.recon_blades==False:
            if self.use_slices==False: #this is getting complicated, maybe there is a better way?
                imsize_cg=self.imsize
                datasize_cg=self.datasize
                if self.use_bladewise:
                    datasize_cg=self.datasize_coil
                #print imsize_cg
                #print datasize_cg
            else:
                imsize_cg=[self.imsize[0],self.imsize[1],7]
                datasize_cg=self.datasize_slices
        else:
            imsize_cg=self.imsize_blades
            datasize_cg=self.datasize
        if verbose:
            t_start=time()
        #print shape(x)
        #print shape(b)
        #print shape(self.igrid(x*self.wI))
        #print self.imsize_coil
        #print shape(self.grid(b))
        #print shape(self.grid(b-self.igrid(x*self.wI)))
        
        r=(self.wI*self.grid(b-self.igrid(x*self.wI))).flatten() #testing weighting!
        #print(isnan(r).any())
        #r=nan_to_num(r) #lets try this!
        rsnew=dot(r.conj().transpose(),r)
        if ~isfinite(rsnew): #no idea why this is happening, I can't find nans or infs in there at all!
            print('WARNING: had to reinitialize CG with zeros because of the strange nan initialization error!')
            x=zeros_like(x)
            r=(self.wI*self.grid(b-self.igrid(x*self.wI))).flatten() #testing weighting!
            #print r
            rsnew=dot(r.conj().transpose(),r)
            #print rsnew
        
        x=x.flatten()
        b=b.flatten()
        #normb=norm(b)
        p=r.copy()
        if self.beta_eqn==1:
            r_m1=r.copy()
        
     
        niter=0
        #resid=rsnew**0.5/normb
        #resid=rsnew
        tol=abs(rsnew)*tol**2 #from painless CG, a fraction of the original
        lastrsnew=abs(rsnew)
        while niter<maxiter and tol<abs(rsnew) and abs(rsnew)<=lastrsnew:
            lastrsnew=abs(rsnew)
            niter+=1
            Ap=(self.wI*self.grid(self.igrid(reshape(p,imsize_cg)*self.wI))).flatten() #this could perhaps be performed faster in nfft
            alpha=rsnew/dot(p.conj().transpose(),Ap)
            #print alpha
            x=x+alpha*p
            if niter%self.reset_iters==0:
                #tmp=self.igrid(reshape(x,imsize_cg)*self.wI)
                #r=(self.wI*self.grid(reshape(b,self.datasize)-tmp)).flatten()
                r=(self.wI*self.grid(reshape(b,datasize_cg)-self.igrid(reshape(x,imsize_cg)*self.wI))).flatten() #I think I need to multiply by w in here...
            else:
                r=r-alpha*Ap
            rsold=rsnew.copy()
            if self.beta_eqn==0: #0 is FR, actually I don't think we want 1...
                rsnew=dot(r.conj().transpose(),r)
                #beta=rsnew/rsold
            else: #1 is PR, which should be identical to FR for linear CG, I think!
                rsnew=dot(r.conj().transpose(),r-r_m1)
                r_m1=r.copy()
                #beta=max(0,rsnew/rsold)
                
            beta=max(0,rsnew/rsold) #ETP I don't think we need this, but it may just help and can't hurt!
            #print rsnew
            #if sqrt(rsnew)<1e-10
            #      break;
            #end
            p=r+beta*p
            #resid=(rsnew**0.5)/normb
            #resid=rsnew
            if verbose:
                print('iter=%d residual=%f'%(niter,abs(rsnew)))
            #rsold=rsnew
        #print([tol,'<',rsnew])
        x=reshape(x,imsize_cg)
        x*=self.wI
        if verbose:
            print('CG time = %f s' % (time()-t_start))
        return x,niter,rsnew
        
        
    def comp_tensor_matrix(diff_img):
        #following I=GD where I are the diffusion images, G is the diffusion gradient playout,
        #and D is what we are solving for, the diffusion tensor matrix
        
        
        return diff_img
        
        
    def finalize(self):
        if self.gridder_allocated==True:
            if self.use_nnfft==True:
                for blade in range(self.nblades):
                    finalize_nnfft_2d(self.gridder[blade])
            else:
                for blade in range(self.nblades):
                    finalize_nfft_2d(self.gridder[blade])
        self.gridder_allocated=False
            
            
        

def get_2D_nfft_values(ptr,l):
    from numpy import zeros
    from copy import copy
    
    try:
        z=zeros(l,complex)
        for i in range(l[0]):
            for j in range(l[1]):
                z[i,j]=ptr[i*l[1]+j][0]+1j*ptr[i*l[1]+j][1]
    except:
        z=zeros(l)
        for i in range(l[0]):
            for j in range(l[1]):
                z[i,j]=ptr[i*l[1]+j]
    return z

            
def set_2D_nfft_values(ptr,vals):
    from numpy import complex128, shape
    from copy import copy
    
    s=shape(vals)
    if vals.dtype.type is complex128: #setting k-space values
        try:
            for i in range(s[0]): #2D
                for j in range(s[1]):
                    ptr[i*s[1]+j][0]=vals[i,j].real
                    ptr[i*s[1]+j][1]=vals[i,j].imag
            print('warning: setting in 2D!')
        except: #vector
            for i in range(s[0]):
                ptr[i][0]=vals[i].real
                ptr[i][1]=vals[i].imag
    else: #set sampling locations
        try:
            for i in range(s[0]):
                for j in range(2): #[0,1]
                    ptr[i*2+j]=vals[i,j]
        except: #set real valued k-space values (density compensation points for example)
            for i in range(s[0]): #2D
                ptr[i]=vals[i]
                
                
def get_2D_nnfft_values(ptr,l):
    from numpy import zeros
    from copy import copy
    
    try:
        z=zeros(l,complex)
        for i in range(l[0]):
            for j in range(l[1]):
                z[i,j]=ptr[i*l[1]+j][0]+1j*ptr[i*l[1]+j][1]
    except:
        z=zeros(l)
        for i in range(l[0]):
            for j in range(l[1]):
                z[i,j]=ptr[i*l[1]+j]
    return z

            
            
def set_2D_nnfft_values(ptr,vals):
    from numpy import complex128, shape
    from copy import copy
    
    s=shape(vals)
    if vals.dtype.type is complex128: #setting k-space values
        try:
            for i in range(s[0]): #2D
                for j in range(s[1]):
                    ptr[i*s[1]+j][0]=vals[i,j].real
                    ptr[i*s[1]+j][1]=vals[i,j].imag
            print('warning: setting in 2D!')
        except: #vector
            for i in range(s[0]):
                ptr[i][0]=vals[i].real
                ptr[i][1]=vals[i].imag
    else: #set sampling locations
        try:
            for i in range(s[0]):
                for j in range(3): #[0,1]
                    ptr[i*3+j]=vals[i,j]
        except: #set real valued k-space values (density compensation points for example)
            print('nnfft real values!')
            for i in range(s[0]): #2D
                ptr[i]=vals[i]
                

        
    
    
    
    
def init_nfft_2d(locs,N_py,fov_support=1,alloc_type='some',overgridding_factor=2,gridding_kernel_size=3):
    """This function initializes a nfft structure for 2D inputs
    
    inputs are as follows:
    locs: sampling locations. real is x, imaginary is y
    N_py: output of square image size (1)
    alloc_type: precomputation strategy for nfft and fftw, options are 'full', 'some', 'none'
        These are in order of most to least setup time, but least to most execution time (and accuracy)
    overgridding_factor: internal nfft grid size to improve gridding accuracy (1)
    gridding_kernel_size: internal nfft kernel size to improve gridding accuracy (1)
    
    outputs are as follows:
    p: the pointer to the nfft structure"""
    
    from warnings import warn
    from numpy import shape, expand_dims, concatenate, prod
    from ctypes import CDLL, cdll, pointer
    import nfft3
    import fftw3
    cdll.LoadLibrary('libnfft3.so')
    nfft=CDLL('libnfft3.so')
    N_init=nfft3.c_int*2
    #M_init=nfft3.c_int
    
    n_py=N_py*overgridding_factor
    if alloc_type=='full':
        nfft_args=nfft3.PRE_PHI_HUT | nfft3.PRE_FULL_PSI | nfft3.MALLOC_F_HAT | nfft3.MALLOC_X | nfft3.MALLOC_F | nfft3.FFTW_INIT | nfft3.FFT_OUT_OF_PLACE
        fft_args=fftw3.FFTW_MEASURE | fftw3.FFTW_DESTROY_INPUT
    elif alloc_type=='some':
        nfft_args=nfft3.PRE_PHI_HUT | nfft3.PRE_PSI | nfft3.MALLOC_F_HAT | nfft3.MALLOC_X | nfft3.MALLOC_F | nfft3.FFTW_INIT | nfft3.FFT_OUT_OF_PLACE
        fft_args=fftw3.FFTW_ESTIMATE | fftw3.FFTW_DESTROY_INPUT
    elif alloc_type=='none':
        nfft_args=nfft3.PRE_LIN_PSI | nfft3.MALLOC_F_HAT | nfft3.MALLOC_X | nfft3.MALLOC_F | nfft3.FFTW_INIT | nfft3.FFT_OUT_OF_PLACE
        fft_args=fftw3.FFTW_ESTIMATE | fftw3.FFTW_DESTROY_INPUT
    else:
        warn('I didnt understand the allocation type!')
    p=nfft3.nfft_plan()
    M=shape(locs)
    #print N_py
    #print M
    #print n_py
    #N_py=256
    #n_py=512
    nfft.nfft_init_guru(pointer(p), 2, N_init(int(N_py),int(N_py)), int(prod(M)), N_init(int(n_py),int(n_py)), gridding_kernel_size, nfft_args, fft_args)
    locs=concatenate((expand_dims(locs.real.flatten(),1),expand_dims(locs.imag.flatten(),1)),1)
    set_2D_nfft_values(p.x,locs) #commented 20120814
    nfft.nfft_precompute_one_psi(pointer(p)) #commented 20120814
    p.imsize=[N_py,N_py] #set my own variable in here, the image size!
    p.datasize=M #set my own variable in here, the data size!
    p.fov=fov_support
    return p


def init_iterative_nfft_2d(p,density_comp):
    """This function initializes an iterative nfft structure for 2D inputs
    
    inputs are as follows:
    p: pointer to the nfft structure to use
    density_comp: density compensation values to use (is flattened before use)
    
    outputs are as follows:
    ip: pointer to the iterative nfft structure"""
    
    from ctypes import CDLL, cdll, pointer
    import nfft3
    cdll.LoadLibrary('libnfft3.so')
    nfft=CDLL('libnfft3.so')
    
    ip=nfft3.solver_plan_complex()
    nfft.solver_init_advanced_complex(pointer(ip),pointer(p), nfft3.CGNR | nfft3.PRECOMPUTE_DAMP | nfft3.PRECOMPUTE_WEIGHT)
    set_2D_nfft_values(ip.w,density_comp.flatten()) #density compensation weights
    set_2D_nfft_values(ip.w_hat,p.fov.flatten()) #image constraint (FOV in this case)
    return ip
    
def reinit_nfft_2d(p,locs):
    #from warnings import warn
    from numpy import shape, expand_dims, concatenate, prod
    from ctypes import CDLL, cdll, pointer
    import nfft3
    #import fftw3
    cdll.LoadLibrary('libnfft3.so')
    nfft=CDLL('libnfft3.so')
    #N_init=nfft3.c_int*2
    #nfft.nfft_init_guru(pointer(p), 2, N_init(p.imsize[0],p.imsize), int(prod(M)), N_init(n_py,n_py), gridding_kernel_size, nfft_args, fft_args)
    locs=concatenate((expand_dims(locs.real.flatten(),1),expand_dims(locs.imag.flatten(),1)),1)
    set_2D_nfft_values(p.x,locs)
    nfft.nfft_precompute_one_psi(pointer(p))
    
    
def reinit_nnfft_2d(np,img_locs,ksp_locs):
    #WARNING, this doesn't seem to work!
    #from warnings import warn
    from numpy import shape, expand_dims, concatenate, prod
    from ctypes import CDLL, cdll, pointer
    import nfft3
    #import fftw3
    cdll.LoadLibrary('libnfft3.so')
    nfft=CDLL('libnfft3.so')
    #N_init=nfft3.c_int*2
    #nfft.nfft_init_guru(pointer(p), 2, N_init(p.imsize[0],p.imsize), int(prod(M)), N_init(n_py,n_py), gridding_kernel_size, nfft_args, fft_args)
    img_locs=concatenate((expand_dims(img_locs[:,:,0].flatten(),1),expand_dims(img_locs[:,:,1].flatten(),1),expand_dims(img_locs[:,:,2].flatten(),1)),1)
    ksp_locs=concatenate((expand_dims(ksp_locs[:,:,0].flatten(),1),expand_dims(ksp_locs[:,:,1].flatten(),1),expand_dims(ksp_locs[:,:,2].flatten(),1)),1)
    #print shape(img_locs)
    set_2D_nnfft_values(np.x,ksp_locs)
    set_2D_nnfft_values(np.v,img_locs)
    
    #precompute psi, the entries of the matrix B
    if np.nnfft_flags & nfft3.PRE_PSI:
        nfft.nnfft_precompute_psi(pointer(np))
        #print 'psi'

    if np.nnfft_flags & nfft3.PRE_FULL_PSI:
        nfft.nnfft_precompute_full_psi(pointer(np))
        #print 'full psi'

    if np.nnfft_flags & nfft3.PRE_LIN_PSI:
        nfft.nnfft_precompute_lin_psi(pointer(np))
        #print 'lin psi'

    #precompute phi_hut, the entries of the matrix D
    if np.nnfft_flags & nfft3.PRE_PHI_HUT:
        nfft.nnfft_precompute_phi_hut(pointer(np))
        #print 'D'
    
    
    nfft.nnfft_precompute_phi_hut(pointer(np));
    
    
def init_iterative_nnfft_2d(np,density_comp):
    """This function initializes an iterative nnfft structure for 2D inputs
    
    inputs are as follows:
    np: pointer to the nnfft structure to use
    density_comp: density compensation values to use (is flattened before use)
    
    outputs are as follows:
    inp: pointer to the iterative nnfft structure"""
    return init_iterative_nfft_2d(np,density_comp)
    
    
    
def init_nnfft_2d(img_locs,ksp_locs,N_py,fov_support=1,time_res=8,alloc_type='some',overgridding_factor=1.2,gridding_kernel_size=2,m=6): #m=9 and m=6 works well!
    """This function initializes a nfft structure for 2D inputs
    
    inputs are as follows:
    img_locs: sampling locations. [N,N,3] z=0 is x, z=1 is y, z=3 is time
    ksp_locs: sampling locations. [Mx,My,3] z=0 is x, z=1 is y, z=3 is time
    N_py: output of square image size (1)
    fov_support: mask to use to correct the FOV
    alloc_type: precomputation strategy for nfft and fftw, options are 'full', 'some', 'none'
        These are in order of most to least setup time, but least to most execution time (and accuracy)
    overgridding_factor: internal nfft grid size to improve gridding accuracy (1)
    gridding_kernel_size: internal nfft kernel size to improve gridding accuracy (1)
    
    outputs are as follows:
    np: the pointer to the nfft structure"""
    
    from warnings import warn
    from numpy import shape, expand_dims, concatenate, prod
    from ctypes import CDLL, cdll, pointer
    import nfft3
    #from time import sleep
    #import fftw3
    cdll.LoadLibrary('libnfft3.so')
    nfft=CDLL('libnfft3.so')
    N_init=nfft3.c_int*3
    
    #n_py=N_py*overgridding_factor
    if alloc_type=='full':
        nfft_args=nfft3.PRE_PHI_HUT | nfft3.PRE_FULL_PSI | nfft3.MALLOC_F_HAT | nfft3.MALLOC_X | nfft3.MALLOC_F | nfft3.MALLOC_V | nfft3.FFTW_INIT | nfft3.FFT_OUT_OF_PLACE
        #fft_args=fftw3.FFTW_MEASURE | fftw3.FFTW_DESTROY_INPUT
    elif alloc_type=='some':
        nfft_args=nfft3.PRE_PHI_HUT | nfft3.PRE_PSI | nfft3.MALLOC_F_HAT | nfft3.MALLOC_X | nfft3.MALLOC_F | nfft3.MALLOC_V | nfft3.FFTW_INIT | nfft3.FFT_OUT_OF_PLACE
        #fft_args=fftw3.FFTW_ESTIMATE | fftw3.FFTW_DESTROY_INPUT
    elif alloc_type=='none':
        nfft_args=nfft3.PRE_LIN_PSI | nfft3.MALLOC_F_HAT | nfft3.MALLOC_X | nfft3.MALLOC_F | nfft3.MALLOC_V | nfft3.FFTW_INIT | nfft3.FFT_OUT_OF_PLACE
        #fft_args=fftw3.FFTW_ESTIMATE | fftw3.FFTW_DESTROY_INPUT
    else:
        warn('I didnt understand the allocation type!')
    np=nfft3.nnfft_plan()
    #M=shape(locs)
    #print shape(img_locs)
    #print shape(ksp_locs)
    
    #switching img and ksp because N is ksp, and M is image!!!!
    N=shape(img_locs)
    N_total=prod(N[0:2]) #0:2
    M=shape(ksp_locs)
    M_total=prod(M[0:2]) #0:2
    #print int(N_total)
    #print int(M_total)
    #just guessing at the time resolution needed for gridding...
    #nfft.nnfft_init_guru(pointer(np), 3, int(N_total), int(M_total), N_init(N[0],N[1],time_res), N_init(int(N[0]*overgridding_factor),int(N[1]*overgridding_factor),int(time_res*overgridding_factor)), time_res*gridding_kernel_size, nfft_args)
    #nfft.nnfft_init_guru(pointer(np), 3, int(N_total), int(M_total), N_init(N[0],N[1],time_res), N_init(int(N[0]*overgridding_factor),int(N[1]*overgridding_factor),int(time_res*overgridding_factor)), m, nfft_args)
    #nfft.nnfft_init_guru(pointer(np), 3, int(N_total), int(M_total), N_init(int(N[0]),int(N[1]),int(1)), N_init(int(N[0]*overgridding_factor),int(N[1]*overgridding_factor),int(1)), int(m), nfft_args) #this was good!
    nfft.nnfft_init(pointer(np), 3, int(N_total), int(M_total), N_init(int(N[0]),int(N[1]),int(1))) #this was good!
    #nfft.nnfft_init_guru(pointer(np), 2, int(N_total), int(M_total), N_init(int(N[0]),int(N[1])), N_init(int(N[0]*overgridding_factor),int(N[1]*overgridding_factor)), int(m), nfft_args)
    #nfft.nnfft_init_guru(pointer(np), 2, int(N_total), int(M_total), N_init(N[0],N[1]), N_init(int(N[0]*overgridding_factor),int(N[1]*overgridding_factor)), time_res*gridding_kernel_size, nfft_args)
    #sleep(5)
    img_locs=concatenate((expand_dims(img_locs[:,:,0].flatten(),1),expand_dims(img_locs[:,:,1].flatten(),1),expand_dims(img_locs[:,:,2].flatten(),1)),1)
    ksp_locs=concatenate((expand_dims(ksp_locs[:,:,0].flatten(),1),expand_dims(ksp_locs[:,:,1].flatten(),1),expand_dims(ksp_locs[:,:,2].flatten(),1)),1)
    #print shape(img_locs)
    set_2D_nnfft_values(np.x,ksp_locs) #swapped v and x
    set_2D_nnfft_values(np.v,img_locs)
    
    #precompute psi, the entries of the matrix B
    if np.nnfft_flags & nfft3.PRE_PSI:
        nfft.nnfft_precompute_psi(pointer(np))
        #print 'psi'

    if np.nnfft_flags & nfft3.PRE_FULL_PSI:
        nfft.nnfft_precompute_full_psi(pointer(np))
        #print 'full psi'

    if np.nnfft_flags & nfft3.PRE_LIN_PSI:
        nfft.nnfft_precompute_lin_psi(pointer(np))
        #print 'lin psi'

    #precompute phi_hut, the entries of the matrix D
    if np.nnfft_flags & nfft3.PRE_PHI_HUT:
        nfft.nnfft_precompute_phi_hut(pointer(np))
        #print 'D'
    
    
    #nfft.nnfft_precompute_phi_hut(pointer(np));
    np.imsize=N[0:2] #set my own variable in here, the image size!
    np.datasize=M[0:2] #set my own variable in here, the data size!
    np.fov=fov_support
    return np
    
    
def reinit_nnfft_2d(np,img_locs,ksp_locs):
    """This function initializes a nfft structure for 2D inputs
    
    inputs are as follows:
    img_locs: sampling locations. [N,N,3] z=0 is x, z=1 is y, z=3 is time
    ksp_locs: sampling locations. [Mx,My,3] z=0 is x, z=1 is y, z=3 is time
    N_py: output of square image size (1)
    fov_support: mask to use to correct the FOV
    alloc_type: precomputation strategy for nfft and fftw, options are 'full', 'some', 'none'
        These are in order of most to least setup time, but least to most execution time (and accuracy)
    overgridding_factor: internal nfft grid size to improve gridding accuracy (1)
    gridding_kernel_size: internal nfft kernel size to improve gridding accuracy (1)
    
    outputs are as follows:
    np: the pointer to the nfft structure"""
    
    from warnings import warn
    from numpy import shape, expand_dims, concatenate, prod
    from ctypes import CDLL, cdll, pointer
    import nfft3
    #import fftw3
    cdll.LoadLibrary('libnfft3.so')
    nfft=CDLL('libnfft3.so')
    #N_init=nfft3.c_int*3
    
    #n_py=N_py*overgridding_factor
#    if alloc_type=='full':
#        nfft_args=nfft3.PRE_PHI_HUT | nfft3.PRE_FULL_PSI | nfft3.MALLOC_F_HAT | nfft3.MALLOC_X | nfft3.MALLOC_F | nfft3.MALLOC_V | nfft3.FFTW_INIT | nfft3.FFT_OUT_OF_PLACE
#        #fft_args=fftw3.FFTW_MEASURE | fftw3.FFTW_DESTROY_INPUT
#    elif alloc_type=='some':
#        nfft_args=nfft3.PRE_PHI_HUT | nfft3.PRE_PSI | nfft3.MALLOC_F_HAT | nfft3.MALLOC_X | nfft3.MALLOC_F | nfft3.MALLOC_V | nfft3.FFTW_INIT | nfft3.FFT_OUT_OF_PLACE
#        #fft_args=fftw3.FFTW_ESTIMATE | fftw3.FFTW_DESTROY_INPUT
#    elif alloc_type=='none':
#        nfft_args=nfft3.PRE_LIN_PSI | nfft3.MALLOC_F_HAT | nfft3.MALLOC_X | nfft3.MALLOC_F | nfft3.MALLOC_V | nfft3.FFTW_INIT | nfft3.FFT_OUT_OF_PLACE
#        #fft_args=fftw3.FFTW_ESTIMATE | fftw3.FFTW_DESTROY_INPUT
#    else:
#        warn('I didnt understand the allocation type!')
#    np=nfft3.nnfft_plan()
    #M=shape(locs)
    #N=shape(img_locs)
    #N_total=prod(N[0:2])
    #M=shape(ksp_locs)
    #M_total=prod(M[0:2])
    #print int(N_total)
    #print int(M_total)
    #just guessing at the time resolution needed for gridding...
    #nfft.nnfft_init_guru(pointer(np), 3, int(N_total), int(M_total), N_init(N[0],N[1],time_res), N_init(N[0]*overgridding_factor,N[1]*overgridding_factor,time_res*overgridding_factor), gridding_kernel_size, nfft_args)
    
    img_locs=concatenate((expand_dims(img_locs[:,:,0].flatten(),1),expand_dims(img_locs[:,:,1].flatten(),1),expand_dims(img_locs[:,:,2].flatten(),1)),1)
    ksp_locs=concatenate((expand_dims(ksp_locs[:,:,0].flatten(),1),expand_dims(ksp_locs[:,:,1].flatten(),1),expand_dims(ksp_locs[:,:,2].flatten(),1)),1)
    #print shape(img_locs)
    set_2D_nnfft_values(np.x,ksp_locs)
    set_2D_nnfft_values(np.v,img_locs)
    
    #precompute psi, the entries of the matrix B
    if np.nnfft_flags & nfft3.PRE_PSI:
        nfft.nnfft_precompute_psi(pointer(np))
        #print 'psi'

    if np.nnfft_flags & nfft3.PRE_FULL_PSI:
        nfft.nnfft_precompute_full_psi(pointer(np))
        #print 'full psi'

    if np.nnfft_flags & nfft3.PRE_LIN_PSI:
        nfft.nnfft_precompute_lin_psi(pointer(np))
        #print 'lin psi'

    #precompute phi_hut, the entries of the matrix D
    if np.nnfft_flags & nfft3.PRE_PHI_HUT:
        nfft.nnfft_precompute_phi_hut(pointer(np))
        #print 'D'
    
    
    nfft.nnfft_precompute_phi_hut(pointer(np));
    #np.imsize=N[0:2] #set my own variable in here, the image size!
    #np.datasize=M[0:2] #set my own variable in here, the data size!
    #np.fov=fov_support
    #return np
    
    

def grid_nfft_2d(p,data):
    """This function runs a 2D gridding. K-space to image space.
    
    inputs are as follows:
    p: pointer to the nfft structure (generated by init_nfft_2d)
    data: the data to grid (is flattened inside)
    
    outputs are as follows:
    img: the image data in numpy matrix format (NxN)"""
    
    from ctypes import CDLL, cdll, pointer
    cdll.LoadLibrary('libnfft3.so')
    nfft=CDLL('libnfft3.so')
    
    set_2D_nfft_values(p.f,data.flatten())
    nfft.nfft_adjoint(pointer(p))
    img=get_2D_nfft_values(p.f_hat,p.imsize)
    img*=p.fov
    return img
    
def grid_nfft_2d_slicewise(p,data):
    """This function runs a 2D slicewise gridding K-space to image space.
    
    The inputs and outputs are the same as grid_nfft_2d, just slicewise"""
    
    from numpy import shape, zeros
    from ctypes import CDLL, cdll, pointer
    cdll.LoadLibrary('libnfft3.so')
    nfft=CDLL('libnfft3.so')
    
    s=[p.imsize[0],p.imsize[1],shape(data)[2]]
    img=zeros(s,complex)
    for d3 in range(s[2]):
        set_2D_nfft_values(p.f,data[:,:,d3].flatten())
        nfft.nfft_adjoint(pointer(p))
        img[:,:,d3]=get_2D_nfft_values(p.f_hat,p.imsize)*p.fov
    return img
        


def igrid_nfft_2d(p,img):
    """This function runs a 2D gridding. Image space to k-space.
    
    inputs are as follows:
    p: pointer to the nfft structure (generated by init_nfft_2d)
    data: the image to inverse grid (is flattened inside)
    
    outputs are as follows:
    data: the kspace data in numpy matrix format"""
    
    from ctypes import CDLL, cdll, pointer
    cdll.LoadLibrary('libnfft3.so')
    nfft=CDLL('libnfft3.so')
    
    img*=p.fov
    set_2D_nfft_values(p.f_hat,img.flatten()) #setting f_hat is setting the image
    nfft.nfft_trafo(pointer(p)) #image space to k-space
    data=get_2D_nfft_values(p.f,p.datasize) #getting f is getting the k-space
    return data
    
    
def igrid_nfft_2d_slicewise(p,img):
    """This function runs a 2D slicewise gridding Image space to k-space.
    
    The inputs and outputs are the same as igrid_nfft_2d, just slicewise"""
    
    from numpy import shape, zeros
    from ctypes import CDLL, cdll, pointer
    cdll.LoadLibrary('libnfft3.so')
    nfft=CDLL('libnfft3.so')
    
    s=[p.datasize[0],p.datasize[1],shape(img)[2]]
    data=zeros(s,complex)
    for d3 in range(s[2]):
        img[:,:,d3]*=p.fov
        set_2D_nfft_values(p.f_hat,img[:,:,d3].flatten())
        nfft.nfft_trafo(pointer(p))
        data[:,:,d3]=get_2D_nfft_values(p.f,p.datasize)
    return data
    
    
def iterative_nfft_2d(p,ip,data,init_img=[],iters=30,dot_r_iter=0.05,verbosity=0):
    """This function runs a 2D iterative gridding. K-space to image space.
    
    inputs are as follows:
    p: pointer to the nfft structure (generated by init_nfft_2d)
    ip: pointer to the iterative nfft structure (generated by init_iterative_nfft_2d)
    data: the data to grid (is flattened inside)
    init_img: initializing image
    iters: maximum number of iterations to perform
    dot_r_iter: stop iterating when the residual drops below this number
    verbosity: be verbose (1) and print the residual each iteration
    
    outputs are as follows:
    data: the image in numpy matrix format"""
                
    from numpy import zeros
    from ctypes import CDLL, cdll, pointer
    cdll.LoadLibrary('libnfft3.so')
    nfft=CDLL('libnfft3.so')

    set_2D_nfft_values(ip.y,data.flatten()) #acquired data
    if type(init_img) is list: #if the input image is empty
        init_img=zeros(p.imsize,complex)
    set_2D_nfft_values(ip.f_hat_iter,init_img.flatten()) #image initial guess
    nfft.solver_before_loop_complex(pointer(ip))
    k=0
    while k<iters and ip.dot_r_iter>dot_r_iter:
        nfft.solver_loop_one_step_complex(pointer(ip))
        k+=1
        if verbosity==1:
            print('iter='+str(k)+' residual='+str(ip.dot_r_iter))
    if verbosity==1 and k==0:
        print('no need to iterate!'+' residual='+str(ip.dot_r_iter))
    img=get_2D_nfft_values(ip.f_hat_iter,p.imsize)
    return img
    
def iterative_nnfft_2d(np,inp,data,init_img=[],iters=30,dot_r_iter=0.05,verbosity=0):
    """This function runs a 2D iterative gridding. K-space to image space.
    
    inputs are as follows:
    p: pointer to the nfft structure (generated by init_nfft_2d)
    ip: pointer to the iterative nfft structure (generated by init_iterative_nfft_2d)
    data: the data to grid (is flattened inside)
    init_img: initializing image
    iters: maximum number of iterations to perform
    dot_r_iter: stop iterating when the residual drops below this number
    verbosity: be verbose (1) and print the residual each iteration
    
    outputs are as follows:
    data: the image in numpy matrix format"""
    return iterative_nfft_2d(np,inp,data,init_img,iters,dot_r_iter,verbosity)
    
    
def grid_nnfft_2d(np,data):
    """This function runs a 2D gridding. K-space to image space.
    
    inputs are as follows:
    np: pointer to the nfft structure (generated by init_nnfft_2d)
    data: the data to grid (is flattened inside)
    
    outputs are as follows:
    img: the image data in numpy matrix format (NxN)"""
    
    #from time import sleep
    from ctypes import CDLL, cdll, pointer
    cdll.LoadLibrary('libnfft3.so')
    nfft=CDLL('libnfft3.so')
    
    set_2D_nnfft_values(np.f,data.flatten())
    nfft.nnfft_adjoint(pointer(np))
    img=get_2D_nnfft_values(np.f_hat,np.imsize)
    img*=np.fov
    return img
        


def igrid_nnfft_2d(np,img):
    """This function runs a 2D gridding. Image space to k-space.
    
    inputs are as follows:
    np: pointer to the nfft structure (generated by init_nnfft_2d)
    data: the image to inverse grid (is flattened inside)
    
    outputs are as follows:
    data: the kspace data in numpy matrix format"""
    
    from ctypes import CDLL, cdll, pointer
    cdll.LoadLibrary('libnfft3.so')
    nfft=CDLL('libnfft3.so')
    
    img*=np.fov
    #print('pre setting f_hat')
    set_2D_nnfft_values(np.f_hat,img.flatten()) #setting f_hat is setting the image
    #print('post setting f_hat')
    nfft.nnfft_trafo(pointer(np)) #image space to k-space
    #print('post trafo')
    data=get_2D_nnfft_values(np.f,np.datasize) #getting f is getting the k-space
    return data
    
    
def finalize_nfft_2d(p):
    """This fuction deallocates all the memory from the nfft allocator
    
    inputs are as follows:
    p: pointer to the nfft structure (generated by init_nfft_2d)
    """
    
    from ctypes import CDLL, cdll, pointer
    cdll.LoadLibrary('libnfft3.so')
    nfft=CDLL('libnfft3.so')
    nfft.nfft_finalize(pointer(p))
    
def finalize_iterative_nfft_2d(ip):
    """This fuction deallocates all the memory from the iterative nfft allocator
    
    inputs are as follows:
    ip: pointer to the iterative nfft structure (generated by init_iterative_nfft_2d)
    """
    
    from ctypes import CDLL, cdll, pointer
    cdll.LoadLibrary('libnfft3.so')
    nfft=CDLL('libnfft3.so')
    nfft.solver_finalize_complex(pointer(ip))
    
def finalize_iterative_nnfft_2d(inp):
    """This fuction deallocates all the memory from the iterative nnfft allocator
    
    inputs are as follows:
    inp: pointer to the iterative nfft structure (generated by init_iterative_nnfft_2d)
    """
    finalize_iterative_nfft_2d(inp)
    
    
def finalize_nnfft_2d(np):
    """This fuction deallocates all the memory from the nfft allocator
    
    inputs are as follows:
    p: pointer to the nfft structure (generated by init_nfft_2d)
    """
    
    from ctypes import CDLL, cdll, pointer
    cdll.LoadLibrary('libnfft3.so')
    nfft=CDLL('libnfft3.so')
    nfft.nnfft_finalize(pointer(np))