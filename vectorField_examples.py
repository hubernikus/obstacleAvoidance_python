# coding: utf-8
""" -------------------------------------------------
# Start main function

@author lukashuber
@date 20181019

"""
# Command to automatically reload libraries -- in ipython before exectureion
import numpy as np
import matplotlib.pyplot as plt

#from math import sin, cos, atan2,
#first change the cwd to the script path
#scriptPath = os.path.realpath(os.path.dirname(sys.argv[0]))
#os.chdir(scriptPath)

import sys
 
# Custom libraries
from dynamicalSystem_lib import *


lib_string = "/home/lukas/Code/MachineLearning/ObstacleAvoidanceAlgroithm/lib_obstacleAvoidance/"
if not any (lib_string in s for s in sys.path):
    sys.path.append(lib_string)

from simulationVectorFields import *

options=[-2]
for option in options:
    if option==-2:

        xlim = [-0.8,7]
        ylim = [-3.3,3.3]

        xAttractor=[0,0]

        N_points=50
        saveFigures=False

        obs=[]
        # Obstacle 2
        a = [0.4,2.2]
        p = [1,1]
        x0 = [6,0]
        th_r = 0/180*pi
        sf = 1
        obs.append(Obstacle(a=a, p=p, x0=x0,th_r=th_r, sf=sf))
        #obs[n].center_dyn = np.array([2,1.4])

        
        Simulation_vectorFields(xlim, ylim, N_points, obs, xAttractor=xAttractor, saveFigure=saveFigures, figName='twoskewEllipses', noTicks=True, obs_avoidance_func=obs_avoidance_nonlinear_radial, dynamicalSystem=nonlinear_stable_DS, nonlinear=True)
    
    if option==-1:

        xlim = [-0.1,8]
        ylim = [-3,3]

        xAttractor=[0,0]

        N_points=50
        saveFigures=False

        obs = []
        a=[0.4, 0.4]
        p=[1,1]
        x0=[2,0.1]
        th_r=-50/180*pi
        sf=1
        obs.append(Obstacle(a=a, p=p, x0=x0,th_r=th_r, sf=sf))
        #obs[n].center_dyn = np.array([2,1.4])

        # Obstacle 2
        a = [0.4,0.4]
        p = [1,1]
        x0 = [6,-0.2]
        th_r = 50/180*pi
        sf = 1
        obs.append(Obstacle(a=a, p=p, x0=x0,th_r=th_r, sf=sf))
        #obs[n].center_dyn = np.array([2,1.4])

        a=[0.4, 0.4]
        p=[1,1]
        x0=[3,1.2]
        th_r=-50/180*pi
        sf=1
        obs.append(Obstacle(a=a, p=p, x0=x0,th_r=th_r, sf=sf))
        #obs[n].center_dyn = np.array([2,1.4])

        a=[0.4, 0.4]
        p=[1,1]
        x0=[5,-0.7]
        th_r=-50/180*pi
        sf=1
        obs.append(Obstacle(a=a, p=p, x0=x0,th_r=th_r, sf=sf))

        Simulation_vectorFields(xlim, ylim, N_points, obs, xAttractor=xAttractor, saveFigure=saveFigures, figName='twoskewEllipses', noTicks=True, obs_avoidance_func=obs_avoidance_nonlinear_radial, dynamicalSystem=nonlinear_wavy_DS, nonlinear=True)
    if option==0:

        xlim = [-0.1,8]
        ylim = [-3,3]

        xAttractor=[0,0]

        N_points=50
        saveFigures=False

        obs = []
        a=[0.3, 2.5]
        p=[1,1]
        x0=[2,0]
        th_r=-50/180*pi
        sf=1
        obs.append(Obstacle(a=a, p=p, x0=x0,th_r=th_r, sf=sf))
        #obs[n].center_dyn = np.array([2,1.4])

        # Obstacle 2
        a = [0.4,2.5]
        p = [1,1]
        x0 = [6,0]
        th_r = 50/180*pi
        sf = 1
        obs.append(Obstacle(a=a, p=p, x0=x0,th_r=th_r, sf=sf))
        #obs[n].center_dyn = np.array([2,1.4])

        
        Simulation_vectorFields(xlim, ylim, N_points, obs, xAttractor=xAttractor, saveFigure=saveFigures, figName='twoskewEllipses', noTicks=True)

    if option==1:
        ### Create obstacle 
        obs = []

        a = [5,1]
        p = [1,1]
        x0 = [5,0]
        th_r = 30/180*pi
        sf = 1
        obs.append(Obstacle(a=a, p=p, x0=x0,th_r=th_r, sf=sf))

        a = [7,2]
        p = [1,1]
        x0 = [7,1]
        th_r = -40/180*pi
        sf = 1
        obs.append(Obstacle(a=a, p=p, x0=x0,th_r=th_r, sf=sf))

    if option==2:
        ### One ellipse
        obs = []

        a = [2,0.5]
        p = [1,1]
        x0 = [2, 2.6]

        th_r = -30/180*pi
        sf = 1
        obs.append(Obstacle(a=a, p=p, x0=x0,th_r=th_r, sf=sf))

        obs[0].center_dyn = x0
        xlim = [-1,7]
        ylim = [-0.1,5]

        N_points = 100

        Simulation_vectorFields(xlim, ylim, N_points, obs, xAttractor=xAttractor, saveFigure=True,
                                figName='ellipse_centerMiddle')


    if option==3:
        ### One ellipse
        obs = []

        a = [2,0.5]
        p = [1,1]

        x0 = [2, 2.6]
        th_r = -30/180*pi

        sf = 1
        obs.append(Obstacle(a=a, p=p, x0=x0,th_r=th_r, sf=sf))

        rat = 0.6
        obs[0].center_dyn = [x0[0] - rat*np.cos(th_r)*a[0] + rat*np.sin(th_r)*a[1],
                             x0[1] - rat*np.sin(th_r)*a[0] + rat*np.cos(th_r)*a[1]]

        xlim = [-1,7]
        ylim = [-0.1,5]

        N_points = 100

        Simulation_vectorFields(xlim, ylim, N_points, obs, xAttractor=xAttractor, saveFigure=True,
                                figName='ellipse_center_bottomLeft')


    if option==4:
        ### Star // Three ellipses
        obs = []
        a = [2,0.25]
        p = [1,1]
        x0 = [2, 2.6]
        th_r = -60/180*pi
        sf = 1
        obs.append(Obstacle(a=a, p=p, x0=x0,th_r=th_r, sf=sf))

        a = [2,0.25]
        p = [1,1]
        x0 = [2, 2.6]
        th_r = +60/180*pi
        sf = 1
        obs.append(Obstacle(a=a, p=p, x0=x0,th_r=th_r, sf=sf))

        a = [2,0.25]
        p = [1,1]
        x0 = [2, 2.6]
        th_r = 00/180*pi
        sf = 1
        obs.append(Obstacle(a=a, p=p, x0=x0,th_r=th_r, sf=sf))

        obs[2].center_dyn = x0

        xlim = [-1,7]
        ylim = [-0.1,5]

        N_points = 100

        # NOT SAVING
        Simulation_vectorFields(xlim, ylim, N_points, obs, xAttractor=xAttractor, saveFigure=False,
                                figName='ellipse_starShape_noContour')

    if option==5:
        xAttractor = np.array([0,0])
        centr = [2, 2.5]
        ### Star // Three ellipses
        obs = []
        a = [0.6,0.6]
        p = [1,1]
        x0 = [2., 3.2]
        th_r = -60/180*pi
        sf = 1.2
        obs.append(Obstacle(a=a, p=p, x0=x0,th_r=th_r, sf=sf))
        obs[0].center_dyn = centr

        a = [1,0.4]
        p = [1,4]
        x0 = [1.6, 1.5]
        th_r = +60/180*pi
        sf = 1.2
        obs.append(Obstacle(a=a, p=p, x0=x0,th_r=th_r, sf=sf))
        obs[1].center_dyn = centr

        a = [1.2,0.2]
        p = [2,2]
        x0 = [3.3,2.1]
        th_r = -20/180*pi
        sf = 1.2
        obs.append(Obstacle(a=a, p=p, x0=x0,th_r=th_r, sf=sf))
        obs[2].center_dyn = centr

        xlim = [-1,7]
        ylim = [-0.1,5]

        N_points = 100

        Simulation_vectorFields(xlim, ylim, N_points, obs, xAttractor=xAttractor, saveFigure=True,
                                figName='three_obstacles_touching')

    if option==6:
        xAttractor = np.array([0,0])
        centr = [1.5, 3.0]
        ### Star // Three ellipses
        obs = []
        a = [0.6,0.6]
        p = [1,1]
        x0 = [1.5, 3.7]
        th_r = -60/180*pi
        sf = 1.2
        obs.append(Obstacle(a=a, p=p, x0=x0,th_r=th_r, sf=sf))

        a = [1,0.4]
        p = [1,4]
        x0 = [3, 2.2]
        th_r= +60/180*pi
        sf = 1.2
        obs.append(Obstacle(a=a, p=p, x0=x0,th_r=th_r, sf=sf))

        a = [1.2,0.2]
        p = [2,2]
        x0 = [2.3,3.1]
        th_r = 20/180*pi
        sf = 1.2
        obs.append(Obstacle(a=a, p=p, x0=x0,th_r=th_r, sf=sf))

        xlim = [-1,7]
        ylim = [-0.1,5]

        N_points = 100

        Simulation_vectorFields(xlim, ylim, N_points, obs, xAttractor=xAttractor, saveFigure=True,
                                figName='three_obstacles_touching_noConvergence')

    if option==7:
        xAttractor = np.array([0,0])
        centr = [2, 2.5]

        obs = []
        a = [0.45,0.9]
        p = [1,1]
        x0 = [1.5, 2.5]
        th_r = -60/180*pi
        sf = 1.2
        obs.append(Obstacle(a=a, p=p, x0=x0,th_r=th_r, sf=sf))

        a = [1.5,0.6]
        p = [1,1]
        x0 = [-2, 2.]
        th_r = -30/180*pi
        sf = 1.2
        obs.append(Obstacle(a=a, p=p, x0=x0,th_r=th_r, sf=sf))
        
        xlim = [-4,4]
        ylim = [-0.1,5]

        N_points = 100

        Simulation_vectorFields(xlim, ylim, N_points, obs, xAttractor=xAttractor, saveFigure=True,
                                figName='multiple_obstacles')

    if option==8:
        xAttractor = np.array([0,0])
        centr = [2, 2.5]

        obs = []
        a = [0.2,5]
        p = [1,1]
        x0 = [0.5, 5]
        th_r = -25/180*pi
        sf = 1.0
        obs.append(Obstacle(a=a, p=p, x0=x0,th_r=th_r, sf=sf))

        a = [1.1,1]
        p = [1,1]
        x0 = [0.5, 1.5]
        th_r = -30/180*pi
        sf = 1.0
        obs.append(Obstacle(a=a, p=p, x0=x0,th_r=th_r, sf=sf))
        
        xlim = [-4,4]
        ylim = [-0.1,5]

        #xlim = [-2,0]
        #ylim = [1,3]

        #xlim = [-0.7, 0.3]
        #ylim = [2.3,3.0]

        N_points = 50

#        Simulation_vectorFields(xlim, ylim, N_points, [obs[0]], xAttractor=xAttractor, saveFigure=True, figName='linearCombination_obstacle0_zoom', noTicks=False)

 #       Simulation_vectorFields(xlim, ylim, N_points, [obs[1]], xAttractor=xAttractor, saveFigure=True, figName='linearCombination_obstacle1_zoom', noTicks=False)

        Simulation_vectorFields(xlim, ylim, N_points, obs, xAttractor=xAttractor, saveFigure=True, figName='linearCombination_obstacles_zoom', noTicks=False)

    if option==9:
        xAttractor = np.array([0,0])
        centr = [2, 2.5]

        obs = []
        N = 16
        R = 5
        th_r0 = 35/180*pi
        rCent=2.4
        for n in range(N):
            obs.append(Obstacle(
                a = [0.2,3],
                p = [1,1],
                x0 = [R*cos(2*pi/N*n), R*sin(2*pi/N*n)],
                th_r = th_r0 + 2*pi/N*n,
                sf = 1.0))
            obs[n].center_dyn=[obs[n].x0[0]-rCent*sin(obs[n].th_r),
                               obs[n].x0[1]+rCent*cos(obs[n].th_r)]
              
            

        xlim = [-10,10]
        ylim = [-8,8]

        xlim = [-3,3]
        ylim = [-7,-3]

        #xlim = [-0.7, 0.3]
        #ylim = [2.3,3.0]

        N_points = 100

#        Simulation_vectorFields(xlim, ylim, N_points, [obs[0]], xAttractor=xAttractor, saveFigure=True, figName='linearCombination_obstacle0_zoom', noTicks=False)

 #       Simulation_vectorFields(xlim, ylim, N_points, [obs[1]], xAttractor=xAttractor, saveFigure=True, figName='linearCombination_obstacle1_zoom', noTicks=False)

        Simulation_vectorFields(xlim, ylim, N_points, obs, xAttractor=xAttractor, saveFigure=False, figName='linearCombination_obstacles_zoom', noTicks=False)
    

#N_points = 100

#xAttractor = np.array([0,1.3])
p
#Simulation_vectorFields(xlim, ylim, N_points, obs, xAttractor=xAttractor)

#Simulation_vectorFields([-10,10],[-10,10], 30, 30, obs)

# # For testing reasons
# pos = np.array([0,3])
# xd_init = linearAttractor(pos, x0 = posAttractor ) # initial DS
# xd_IFD = IFD(pos, xd_init,obs) # modulataed DS with IFD

print('finished script')
