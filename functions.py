"""FUNCTIONS CODE"""

"Importing needed packages/modules"

from math import sqrt
from random import gauss
import matplotlib.pyplot as plt
import random
from scipy.interpolate import interp2d, interp1d
import user_inputs as p
import numpy as np


"Generator of random uniform points function"

def random_initial_values(n,xllim,xulim,yllim,yulim,circle_x,circle_y,r):
    for i in range(n):
        p.x.append(random.uniform(p.wxllim, p.wxulim))
        p.y.append(random.uniform(p.wyllim, p.wyulim))
    for i in range(n-1,-1,-1):
        if p.half == "No (use circle details instead)" and (p.x[i] - p.circle_x)**2 + (p.y[i] - p.circle_y)**2 <= p.r**2:
            p.x_c.append(p.x[i])
            p.y_c.append(p.y[i])
            p.x.pop(i)
            p.y.pop(i)
        if p.half == 'Yes':
            if p.x[i] <= 0:
                p.x_c.append(p.x[i])
                p.y_c.append(p.y[i])
                p.x.pop(i)
                p.y.pop(i)
    return 

"Plotting function"

def plot(n,xllim,xulim,yllim,yulim):
    plt.figure()
    plt.grid( linestyle='--', linewidth=1)
    plt.scatter(p.x, p.y, s=5, facecolor='green')
    plt.scatter(p.x_c, p.y_c, s=5, facecolor = 'orange')
    plt.axis([p.xllim, p.xulim, p.yllim, p.yulim])
    plt.xlabel("x - axis")
    plt.ylabel("y - axis")
    return plt.show()
  

"Function that appends values to their respective arrays from the velocity file"

def velocity_profile_separation_into_arrays():
    i=0
    f = open("velocityCMM3.dat", "r")
    for line in f:          
       for number in line.split():
           if i == 0:              
               p.x_database.append(float(number))
               i += 1
           elif i == 1:
               p.y_database.append(float(number))
               i += 1
           elif i == 2:
               p.u_database.append(float(number))
               i += 1
           else:
               p.v_database.append(float(number))
               i = 0
    return 
velocity_profile_separation_into_arrays()

"Reference solution function that appends the values into arrays for later plotting"

def reference_solution_arrays():
    i=0
    p.ref_solution_x.clear(),p.ref_solution_y.clear()
    f = open("reference.dat", "r")
    for line in f:          
       for number in line.split():
           if i == 0:              
               p.ref_solution_x.append(float(number))
               i += 1
           else:
               p.ref_solution_y.append(float(number))
               i =0
    return 
reference_solution_arrays()

"Interpolating functions for {x, y}"

u_f = interp2d(p.x_database,p.y_database,p.u_database,'linear')
v_f = interp2d(p.x_database,p.y_database,p.v_database,'linear')
r_f = interp1d(p.ref_solution_x,p.ref_solution_y,'linear')



"Euler maruyama method for the x values of the points function"

def Euler_Maruyama_x_position(n,x_position,y_position):
    if x_position >= p.wxulim:
        x_position = x_position - 2*(x_position - p.wxulim)
    if x_position <= p.wxllim:
        x_position = x_position + 2*(p.wxllim - x_position)
    if p.user_input =='Yes':
        new_x_position = x_position + float(u_f(x_position,y_position)*p.h)+ sqrt(2*p.D)*sqrt(p.h)*gauss(p.m, sqrt(p.var))
    #if p.user_input =='no':
    else:
        new_x_position = x_position + sqrt(2*p.D)*sqrt(p.h)*gauss(p.m, sqrt(p.var))
    p.x_new.append(new_x_position)
    return 

"Euler maruyama method for the y values of the points function"

def Euler_Maruyama_y_position(n,x_position,y_position):
    if y_position >= p.wyulim:
        y_position = y_position - 2*(y_position - p.wyulim )
    if y_position <= p.wyllim:
        y_position = y_position + 2*(p.wyllim - y_position)
    if p.user_input =='Yes':
        new_y_position = y_position + float(v_f(x_position,y_position)*p.h) + sqrt(2*p.D)*sqrt(p.h)*gauss(p.m, sqrt(p.var))
    #if p.user_input =='no':
    else:
        new_y_position = y_position + sqrt(2*p.D)*sqrt(p.h)*gauss(p.m, sqrt(p.var))
    p.y_new.append(new_y_position)
    return 

"The functions that combine moving the new values from Euler functions into previous arrays and clears them" 

def counter(n,x,y,x_c,y_c):
    for element, element1 in zip(x,y):
        Euler_Maruyama_x_position(p.n, element, element1)
        Euler_Maruyama_y_position(p.n, element, element1)
    p.x.clear(), p.y.clear()
    for i in range(0,len(p.x_new)):
        p.x.append(p.x_new[i])
        p.y.append(p.y_new[i]) 
    p.x_new.clear(), p.y_new.clear()
    
    for element, element1 in zip(x_c,y_c):
        Euler_Maruyama_x_position(p.n, element, element1)
        Euler_Maruyama_y_position(p.n, element, element1)
    p.x_c.clear(), p.y_c.clear()
    for i in range(0,len(p.x_new)):
        p.x_c.append(p.x_new[i])
        p.y_c.append(p.y_new[i]) 
    p.x_new.clear(), p.y_new.clear()
    
    return    

"Function that returns either a 2D or a 1D density solution"

def density_phi(n,x_c,y_c,Nx,Ny,x,y):
    colored_particles,xedges,yedges = np.histogram2d(x_c,y_c, bins=[Nx, Ny], range = [[p.xllim, p.xulim], [p.yllim, p.yulim]]) 
    particles,_,_ = np.histogram2d(x,y, bins=[Nx, Ny], range = [[p.xllim, p.xulim], [p.yllim, p.yulim]])
    x_grid, y_grid = np.meshgrid([xedges], [yedges])
    particles = np.where(particles == 0, 1, particles)
    concentration = colored_particles/(particles + colored_particles)
    big_concentration = colored_particles/(particles + colored_particles)>p.concentration
        
    if Ny != 1:
        fig = plt.figure(figsize=(8, 6))
        ax = plt.pcolormesh(y_grid,x_grid, concentration, cmap='rainbow')
        plt.xlabel("x - axis")
        plt.ylabel('y_axis')
        fig.colorbar(ax)
    
    else:
        plt.xlabel("x - axis")
        plt.ylabel('density function \u03C6')
        plt.plot(xedges[1:], concentration, 'o-',label = "experimental")
        plt.plot(p.ref_solution_x,p.ref_solution_y, label="reference")
        plt.legend()
        plt.show()
    if p.error_input == 'Yes':
        jstep = round((abs(p.ref_solution_x[0])*2 /p.Nx), 3)
        j = round(p.ref_solution_x[0],3)
        for i in concentration:
            rmse_1 = abs(i-r_f(j))
            rmse = float((i-r_f(j))**2)
            p.error.append(rmse)
            p.diff.append(rmse_1)
            j = j + jstep
        print("The Root Mean Square Error is:", {sqrt(sum(p.error)/p.Nx)})    
        plt.xlabel("x-axis")
        plt.ylabel('Difference')
        plt.plot(np.linspace(-1,1,len(p.error)),p.diff, label = "Difference")
        plt.legend()
        plt.show()
      
  
    if p.concentration_list_required == 'Yes' and p.Dim == '2D':
        xstep = (p.xulim - p.xllim)/(len(big_concentration))
        ystep = (p.yulim-p.yllim)/(len(big_concentration))
        u = p.xllim + xstep/2
        v = p.yllim + ystep/2
        for i in big_concentration:
            for j in i:
                if j == True:
                    p.concentration_list.append([u,v])
                v = v+ystep
            v = p.yllim - ystep/2
            u = u+xstep
        print(f"The coordinates of points where concentration > {p.concentration}")
        print(p.concentration_list)
        return