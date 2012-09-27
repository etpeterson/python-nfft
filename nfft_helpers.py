# -*- coding: utf-8 -*-
"""
Created on Thu May  3 15:27:18 2012

These are helper functions that aid gridding.
Note that many of these started as projection imaging functions which were modified
to do propeller sampling, so some of the calls and naming may be awkward!


@author: eric
"""

from numpy import meshgrid, linspace, zeros, sin, cos

def voronoi2D(xpt,ypt):
    #this function computes the voronoi diagram using qhull
    #I found this online somewhere, so the credit is not mine!
     
    # write the data file
    pts_filename = 'ETP_recon_voronoi_input.vri'
    pts_F = open(pts_filename,'w')
    pts_F.write('2 # this is a 2-D input set\n')
    pts_F.write('%i # number of points\n' % len(xpt))
    for i,(x,y) in enumerate(zip(xpt,ypt)):
        pts_F.write('%f %f # data point %i\n' % (x,y,i))
    pts_F.close()
 
    # trigger the shell command
    import subprocess
    p = subprocess.Popen('qvoronoi o < ETP_recon_voronoi_input.vri >ETP_recon_voronoi_output.vri', shell=True) #QJ0.00000001
    p.wait()
 
    # open the results file and parse results
    results = open('ETP_recon_voronoi_output.vri','r')
 
    # get 'p' results - the vertices of the voronoi diagram
    voronoi_verticies = []
    data = results.readline() #just to move to the right line
    data = results.readline() #just to move to the right line
    #data = results.readline() #just to move to the right line
    voronoi_regions = []
    dupe_counter=0
    #for i in range(0,int(data[0])):
    for line in results:
        #data = results.readline()
        data=line.split(' ')
        data=filter(None,data) #filter out any empty elements (doesn't filter '\n')
        #print data
        #if data[0]=='':
        #    data=data[1:]
        #print line

        if len(data)==3: #2 numbers plus a '\n'
            #xx,yy,dummy = line.split(' ')   
            voronoi_verticies.append([float(data[0]),float(data[1])])
        #voronoi_y_list.append(float(yy))
         
        #print voronoi_list
        # get 'FV' results - pairs of points which define a voronoi edge
        # combine these results to build a complete representation of the
        #data = results.readline()
        
        #for i in range(0,int(data)):
    #for data in results:
        else:
            #print len(voronoi_verticies)
            #print data
            #print data[1:]

            if int(data[0])==0: #duplicate point!
                dupe_counter+=1
                voronoi_regions.append(dupe_counter)
            else:
                dupe_counter=0
                tmp_regions=[]
                #if isempty(data):
                #    print data
                for elem in data[1:]:
                    #int(elem)!=0: #crop the vertex at infinity
                    #tmp=min([0.5,0.5],voronoi_verticies[int(elem)]) #crop outside of [0.5,0.5] in x and y
                    #tmp=max([-0.5,-0.5],tmp) #crop outside of [0.5,0.5] in x and y
                    #if tmp==voronoi_verticies[int(elem)]:
                    tmp_regions.append(voronoi_verticies[int(elem)])
                    #else:
                    #    print('dropping index=',voronoi_verticies[int(elem)])
                voronoi_regions.append(tmp_regions)
    results.close()
    
        
    return voronoi_regions, voronoi_verticies #voronoi_regions #voronoi_list,voronoi_idx_list
    
def calc_density_weights(M_py,ro_loc_pad=0,ph_loc_pad=0,blade=[],nblades=[],sense_factor=1):
    #This function calculates the density weights for a propeller sequence using qhull (voronoi2D).
    #Inputs:
    #M_py = size of raw data matrix
    #ro_loc_pad = padding to apply in the readout direction, this reduces edge effects of areas extending to infinity.
    #ph_loc_pad = same as ro_loc_pad, just in the phase encode direction. Use these carefully and keep in mind blade overlap!
    #blade = the blade number we want to compute (rather than all of them together)
    #nblades = the total number of blades for propeller scans
    #sense_factor = the MRI SENSE factor to use for the sampling, this is essentially a phase encode spacing change
    #Output: a matrix of density weights to be used for gridding
    from copy import copy
    from numpy import zeros, reshape, mean, bitwise_and, shape
    M_py_extra=copy(M_py)
    M_py_extra[0]+=2*ro_loc_pad
    
    #print(M_py,ro_loc_pad,ph_loc_pad,nblades)
    if not nblades:
        locs_extra,locs_extra_mat=projection_sampling_location_generator(M_py_extra)
    else:
        M_py_extra[1]+=2*ph_loc_pad*nblades
        blade_extra=copy(blade)
        blade_extra[0]+=2*ro_loc_pad
        blade_extra[1]+=2*ph_loc_pad
        locs_extra,locs_extra_mat=propeller_sampling_location_generator(blade_extra,nblades,sense_factor=sense_factor)
        
    vor_reg,vor_vert=voronoi2D(locs_extra[:,0],locs_extra[:,1])
    w_vor=zeros(M_py_extra).flatten()
    #print(shape(vor_reg),shape(w_vor))
    #figure()
    k=0
    k_lastgood=0
    for elem in vor_reg:
        
        #scan and correct for duplicates, or at least try
        if type(elem) is int: #we have a duplicate
            kk=k
            while type(vor_reg[kk]) is int:
                kk+=1
            if type(vor_reg[k-1]) is not int:
                #print(w_vor[k],'/',vor_reg[kk-1]+1)
                w_vor[k_lastgood]/=vor_reg[kk-1]+1
            w_vor[k]=w_vor[k_lastgood]
        #argh, duplicates suck!
        
        else: #this is the normal processing section!
            k_lastgood=k
            w_vor[k]=polyarea(elem)
        #try:
        #    k=k
        #    print(k)
#            w_vor[k]=polyarea(elem)
#        except:
#            w_vor[k]=-1
    #        if k<5000 and k>512: #k<4256 and k>4128:
    #            #print(k,' ',w_new[k])
    #            x=[sublist[0] for sublist in elem]
    #            y=[sublist[1] for sublist in elem]
    #            #print[x,y]
    #            fill(x,y,'g',alpha=0.25)
        k+=1
    #check for repeated values (-1 now)
#    for k in range(len(w_vor)):
#        #print val
#        if w_vor[k]==-1:
#            x=locs_extra[k,0]
#            y=locs_extra[k,1]
#            #print [x,y]
#            matching_locs=locs_extra==[x,y]
#            #print matching_locs
#            matching_locs=bitwise_and(matching_locs[:,0],matching_locs[:,1])
#            #print matching_locs
#            #print matching_locs
#            print sum(matching_locs)
#            vals=w_vor[matching_locs]
#            #print shape(vals)
#            vals[vals==-1]=0
#            print shape(vals)
#            replacement_value=mean(vals)/len(vals)
#            #print replacement_value
#            w_vor[matching_locs]=replacement_value
        
    w_vor=reshape(w_vor,M_py_extra) #,order='F' for propeller?
    #print(shape(w_vor))
    if ro_loc_pad!=0:
        w_vor=w_vor[ro_loc_pad:-ro_loc_pad,:]
    if ph_loc_pad!=0: #for short axis propeller
        w_vor=reshape(w_vor,[M_py_extra[0],M_py_extra[1]/nblades,nblades])
        w_vor=w_vor[:,ph_loc_pad:-ph_loc_pad,:]
        w_vor=reshape(w_vor,M_py)
    #print(shape(w_vor))
    return w_vor
        
        
def polyarea(p): #super cool function to calculate the area of a polygon
    return 0.5 * abs(sum(x0*y1 - x1*y0
                         for ((x0, y0), (x1, y1)) in segments(p)))

def segments(p): #helper for polyarea
    return zip(p, p[1:] + [p[0]])
    
    
def projection_sampling_location_generator(M_py):
    #A projection sampling generator function
    #Inputs: matrix size of samples [readout,angles] (assumes readout x angles through an angle of 2*pi)
    #Outputs: locations [Nx2] for x and y, locations size of M_py x is real and y is imaginary
    from numpy import prod, linspace, exp, concatenate, reshape, dot
    from math import pi
    r=dot(reshape(linspace(-0.5,0.5,M_py[0],False),[M_py[0],1]),reshape(exp(-1j*linspace(0,pi,M_py[1],False)),[1,M_py[1]]))
    locs=concatenate((reshape(r.real.flatten(),[prod(M_py),1]),reshape(r.imag.flatten(),[prod(M_py),1])),1)
    return locs,r
    

def propeller_sampling_location_generator(blade,nblades,blade_return=0,sense_factor=1,pause_time=0.02,x_true=None,y_true=None):
    #A propeller sampling function generator
    #Inputs:
    #blade (int vector) = blade size [readout,phase encoding]
    #nblades (int) = number of blades
    #blade_return (int) = sets a rotation based on the number of blades. For example for 4 blades, a value of 2 rotates the set by 90 degrees.
    #sense_factor (float) = sets the spacing in the phase encode direction (see other SENSE parameters)
    #pause_time (float) = if using 3D locations, this gives the pause time in seconds between readouts
    #x_true (float vector) = allows the input of actual x locations, from a calibration for example
    #y_true (float vector) = allows the input of actual y locations, from a calibration for example
    #Outputs:
    #locs_vec (float Nx3) = 3D locations x,y,z
    #locs (float matrix complex) = 2D locations real is x and y is imaginary (this contains the same x and y information as locs)
    from numpy import prod, meshgrid, linspace, exp, concatenate, expand_dims, reshape, tile, zeros#, shape#, flipud
    from math import pi
    from copy import copy
    r=sense_factor*blade[1]/float(blade[0])
    #print('sense_factor',sense_factor,r,blade)
    rr=1
    if r>1:
        #print('thin blade propeller!')
        rr=(sense_factor**2)/r #this should work with sense now
        r=1
        #print(rr,r)
    #total_pts=prod(blade)*nblades
    if x_true==None:
        if blade[0]%2==0:
            x=linspace(-0.5*rr,0.5*rr,blade[0],False)
        else:
            x=linspace(-0.5*rr,0.5*rr,blade[0])
        x90=x
        #print x
        #print x90
    else:
        x=x_true
        x90=y_true
        
    if blade[1]%2==0:
        y=linspace(-0.5*r,0.5*r,blade[1],False)
    else:
        y=linspace(-0.5*r,0.5*r,blade[1])#+0.5*r/(float(blade[1])*blade[1])
    #x,y=meshgrid(x,y)
    #the first blade_angles= line gives results that look more like what the scanner returns - in simulations
    #the second actually works with the data the scanner returns
    #blade_angles=exp(1j*linspace(0,pi,nblades,False))*exp(-1j*pi*blade_return)*exp(1j*pi/2.0) #the final exp() gives the correct base angle
    bangles=linspace(0,pi,nblades,False)
    blade_angles=exp(-1j*bangles)*exp(-1j*pi*blade_return)*exp(-1j*pi/2.0) #the final exp() gives the correct base angle
    
    #old time code
    #time=linspace(-0.5,0.5,prod(blade),False)
    #time=reshape(time,blade,'F')
    
    #new time code with pauses between readouts (pause_time is a fraction of the total readout time that is added to each readout to account for blips)
    time=zeros(blade)
    for ph in range(blade[1]):
        time[:,ph]=linspace(pause_time/2.0,1.0/blade[1]-pause_time/2.0,blade[0],False)+(ph-blade[1]/2.0)/blade[1]
    #time[:,1:blade[1]:2]=copy(time[::-1,1:blade[1]:2]) #flip alternating readouts
    time[:,0:blade[1]:2]=copy(time[::-1,0:blade[1]:2]) #flip alternating readouts (the others)
    time=tile(time,[1,nblades])
    locs=[]
    for bnum in range(nblades):
        #print bangles[bnum]
        #print(cos(bangles[bnum]),sin(bangles[bnum]))
        #print #cos(bangles[bnum])*x+sin(bangles[bnum])*x90
        xuse=(abs(cos(bangles[bnum]))*x+abs(sin(bangles[bnum]))*x90)/(abs(cos(bangles[bnum]))+abs(sin(bangles[bnum])))
        xmesh,ymesh=meshgrid(xuse,y)
        #xmesh90,ymesh90=meshgrid(x90,y)
        #xmesh=xmesh*cos(bangles[bnum])-ymesh*
        blocs=(xmesh+1j*ymesh)*blade_angles[bnum]
        try:
            locs=concatenate((locs,blocs.transpose()),1)
        except:
            locs=blocs.transpose()
    #flip the image left-right
    locs.imag*=-1
    #print shape(locs)
    #print shape(time)
    locs_vec=concatenate((expand_dims(locs.real.flatten(),1),expand_dims(locs.imag.flatten(),1),expand_dims(time.flatten(),1)),1)
    return locs_vec,locs
    
def comp_fov(s,thresh=1.0):
    #This function returns a circular field of view mask.
    #Inputs:
    #s (float vector [2,1] or float) = size of the image
    #thresh (float) = threshold radius to use, 1 is full FOV, less is smaller, more is bigger.
    #Outputs:
    #fov (float matrix [s,s]) = mask the size of s
    try:
        x,y=meshgrid(linspace(-1,1,s,False),linspace(-1,1,s,False))
        fov=zeros([s,s])
    except:
        x,y=meshgrid(linspace(-1,1,s[1],False),linspace(-1,1,s[0],False))
        fov=zeros(s)
    dist=pow(pow(x,2)+pow(y,2),0.5)
    fov[dist<thresh]=1
    return fov
    
    
def center_matvec(mat,off,center):
        from numpy import eye, dot
        from numpy.linalg import inv
        tmat=eye(3) #translation
        amat=eye(3) #affine transform
        tmat[0:2,2]=off-center
        amat[0:2,0:2]=mat
        tfmat=dot(dot(inv(tmat),amat),tmat)
        return tfmat
        
def read_bval_bvec(basename):
    #reads bval and bvec files, returns a bvec matrix and bval vector
    from csv import reader
    #from numpy import array, shape
    
    bval_file=reader(open(basename+'.bval'),delimiter=' ')
    bval=[]
    for line in bval_file:
        for vec in line:
            #print vec
            #print bval
            try:
                bval.append(float(vec))
            except:
                pass
            #print vec
    #print bval
    s=len(bval)
            
    bvec_file=reader(open(basename+'.bvec'),delimiter=' ')
    bvec=zeros([s,3])
    l=0
    v=0
    for line in bvec_file:
        #print(len(line))
        for vec in line:
            #print(v,l,vec)
            try:
                bvec[v,l]=float(vec)
            except:
                pass
            v+=1
            #print vec
        l+=1
        v=0
    #print bvec
    
    return bval, bvec
    