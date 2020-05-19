import os
import numpy as np
import matplotlib.pyplot as plt

dir = 'airfoil_data/'
airfoil_files = os.listdir(dir)

def get_foil(n=0, draw_foil=False):

    filename = dir+airfoil_files[n]
    array = np.loadtxt(filename, skiprows=1)
    foilx, foily = array[:,0], array[:,1]
    
    if draw_foil:
        plt.figure(figsize=(12,10))
        plt.plot(foilx, foily,'.-')
        plt.xlim(-.2,1.2)
        plt.ylim(-0.2,0.2)
        plt.title(filename[:-4])
        plt.axes().set_aspect(1.0)
   
    return foilx, foily

def get_panel_centers(foilx,foily):
    
    xc = (foilx[1:]+foilx[:-1])/2
    yc = (foily[1:]+foily[:-1])/2
    
    return xc,yc

def get_panel_normals(foilx,foily):
    tx = foilx[1:]-foilx[:-1]
    ty = foily[1:]-foily[:-1]
    l = np.sqrt(tx**2 + ty**2)
    tx = tx /l
    ty = ty /l
    nx,ny = ty,-tx
    return nx,ny
    

x,y = get_foil(n=0, draw_foil=True)
xc,yc = get_panel_centers(x,y)
nx,ny = get_panel_normals(x,y)

#plt.plot(xc,yc,'o')    
plt.quiver(xc,yc,
           nx,ny,
           scale=10,
           scale_units='xy',
           alpha=0.1)

##projection of (ux,uy) vector along the normal (nx,ny) vector
#ux,uy = 1.0, 0.0
#projection = nx*ux + ny*uy
#plt.quiver(xc,yc,
#           projection*nx,projection*ny,
#           scale=5,
#           scale_units='xy',
#           alpha=0.75)



#n=5
#plt.quiver(xc[n],yc[n],
#           nx[n],ny[n],
#           scale=10,
#           scale_units='xy',
#           alpha=1.0)




X,Y = xc,yc
ux = np.ones_like(X)*10.0
uy = np.zeros_like(X)


#vortex_x = [0.0,0.5,1.0]
#vortex_y = [0.0,0.0,0.0]
#vortex_i = [1.0,-2.0,-1.0]

vortex_x = x
vortex_y = y
vortex_i = np.random.randn(len(x))/3


for i,j,k in zip(vortex_x,vortex_y,vortex_i):
  R = ((X-i)**2+(Y-j)**2)
  vx = -k*(Y-j)/R
  vy = k*(X-i)/R
  
  ux += vx
  uy += vy

  

#projection of (ux,uy) flow vector along the normal (nx,ny) vector
projection = nx*ux + ny*uy
plt.quiver(xc,yc,
           projection*nx,projection*ny,
           scale=250,
           scale_units='xy',
           alpha=0.25)




x_ = np.linspace(-.2,1.2,50)
y_ = np.linspace(-.2,.2,50)
X,Y = np.meshgrid(x_,y_)

ux = np.ones_like(X)*20.0
uy = np.zeros_like(X)

for i,j,k in zip(vortex_x,vortex_y,vortex_i):
  R = ((X-i)**2+(Y-j)**2)
  vx = -k*(Y-j)/R
  vy = k*(X-i)/R
  
  ux += vx
  uy += vy

plt.streamplot(X,Y,ux,uy)
