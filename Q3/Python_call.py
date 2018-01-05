from ctypes import *
import math
import numpy as np
import matplotlib.pylab as plt

Diffusion_Libs = CDLL('./libhmwk6p3.so')

def zerolistmaker(n):
    listofzeros = [0] * n
    return listofzeros

rand_num=1000000
step_theta=5
step_phi=20
theta_bin=(90/step_theta)
phi_bin=(360/step_phi)


spec_prob = c_double(0.1)
theta_out = c_double(0.)
phi_out = c_double(0.)

theta_out00 = zerolistmaker(theta_bin)
theta_out30 = zerolistmaker(theta_bin)
theta_out60 = zerolistmaker(theta_bin)
phi_out45 = zerolistmaker(theta_bin)

itheta = c_int(0)

for i in range (0,rand_num):

    phi_in = c_double(0.)   
    theta_in = c_double(0.)
    #Diffusion_Libs.diffusion(spec_prob,theta_in,phi_in,byref(theta_out),byref(phi_out))
    #itheta = int(theta_out.value*180./math.pi/step_theta)
    #if (itheta < theta_bin): 
	#theta_out00[itheta] = theta_out00[itheta] + 1

    theta_in = c_double(30.*math.pi/180.)
    Diffusion_Libs.diffusion(spec_prob,theta_in,phi_in,byref(theta_out),byref(phi_out))
    itheta = int(theta_out.value*180./math.pi/step_theta)
    if (itheta < theta_bin):
        theta_out30[itheta] = theta_out30[itheta] + 1

    #theta_in = c_double(60.*math.pi/180.)
    #Diffusion_Libs.diffusion(spec_prob,theta_in,phi_in,byref(theta_out),byref(phi_out))
    #itheta = int(theta_out.value*180./math.pi/step_theta)
    #if (itheta < theta_bin):
    #   theta_out60[itheta] = theta_out60[itheta] + 1

    theta_in = c_double(45.*math.pi/180.)
    phi_in = c_double(math.pi)
    Diffusion_Libs.diffusion(spec_prob,theta_in,phi_in,byref(theta_out),byref(phi_out))
    iphi = int(phi_out.value*180./math.pi/step_theta)
    if (iphi < phi_bin):
       phi_out45[iphi] = phi_out45[iphi] + 1


x1=np.linspace(0,90,theta_bin)
x2=np.linspace(0,360,phi_bin)
y1=np.zeros(theta_bin)
y2=np.zeros(phi_bin)
for i in range(0,theta_bin):
	y1[i]=float(theta_out30[i])/rand_num
	y2[i]=float(phi_out45[i])/rand_num

(n1,bin1)=np.histogram(y1, theta_bin, normed=True) 
pltbin1=np.arange(0,90,step_theta)
plt.plot(pltbin1,n1) 
plt.xlabel('reflected angle(theta)')
plt.ylabel('distribution')
plt.title('histogram of reflection (incident angle=30)')
plt.show()
plt.savefig("hmwk6_poblem3a.jpeg")

(n2,bin2)=np.histogram(y2, phi_bin, normed=True) 
pltbin2=np.arange(0,360,step_phi)
plt.plot(pltbin2,n2) 
plt.xlabel('reflected angle(theta)')
plt.ylabel('distribution')
plt.title('histogram of reflection (incident angle=45&180)')
plt.show()
plt.savefig("hmwk6_poblem3b.jpeg")
