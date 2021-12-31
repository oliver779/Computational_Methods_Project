"""MAIN CODE"""

"Importing needed packages/modules"

import timeit
import functions as f
import user_inputs as p

"Initializing the simulation by importing random points"

f.random_initial_values(p.n, p.xllim, p.xulim, p.yllim, p.yulim, p.circle_x, p.circle_y, p.r)

"Timer start to see how long the simulation took"

start1 = timeit.default_timer()

"Main program: working out the position of each particle and plotting it on a graph and as a heatmap/density function"

if p.Dim == '2D':
    if p.user_input == 'yes':
        f.velocity_profile_separation_into_arrays()     #importing velocity field
        while p.timer < p.t:
            f.counter(p.n,p.x,p.y, p.x_c, p.y_c)    #calculating new positions
            f.plot(p.n,p.xllim,p.xulim,p.yllim,p.yulim)
            p.timer+=p.h 
        f.density_phi(p.n,p.x_c,p.y_c,p.Nx,p.Ny,p.x,p.y)
    else:
        while p.timer < p.t:
            f.counter(p.n,p.x,p.y, p.x_c, p.y_c)    #calculating new positions
            f.plot(p.n,p.xllim,p.xulim,p.yllim,p.yulim)
            p.timer+=p.h
        f.density_phi(p.n,p.x_c,p.y_c,p.Nx,p.Ny,p.x,p.y)
if p.Dim == '1D':
    f.reference_solution_arrays()   #importing reference solution provided
    f.velocity_profile_separation_into_arrays()     #importing velocity field
    while p.timer < p.t:
        f.counter(p.n,p.x,p.y, p.x_c, p.y_c)    #calculating new positions
        f.plot(p.n,p.xllim,p.xulim,p.yllim,p.yulim)
        p.timer+=p.h
    f.density_phi(p.n,p.x_c,p.y_c,p.Nx,p.Ny,p.x,p.y)

"Timer end to show the time it took for the simulation to run"

stop1 = timeit.default_timer()

print('Time taken to run simulation: ', stop1 - start1) 

