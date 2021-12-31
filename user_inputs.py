"""THIS IS THE INPUT FILE WHERE THE USER STATES THEIR INTITIAL CONDITIONS"""

"""USER PLEASE STATE THE FOLLOWING:"""

# importing necessary libraries
import tkinter
from tkinter import *

"-------------------------------------- User Interface Generator ---------------------------------"
#Array to store the results of the User input in
#This array will help with assigning input values to values required by the python code
result = []


def Input_GUI():
    root = Tk()
    root.lift()
    root.attributes("-topmost", True)
    
    # Window details 
    root.title("Simulation Inputs")
    root.geometry("1200x550")
    
    # Title
    Title_label = Label(root, text =  "Simulation Inputs", font = ('bold' + 'underline',20))
    Title_label.grid(row = 0, column = 3)
    
    
    # Spacers
    spacer1 = Label(root, text =  "", padx = 20)
    spacer1.grid(row = 0, column = 0)
    
    spacer2 = Label(root, text =  "")
    spacer2.grid(row = 1, column = 3)
    
    spacer3 = Label(root, text =  "")
    spacer3.grid(row = 6, column = 1)
        
    spacer4 = Label(root, text =  "")
    spacer4.grid(row = 12, column = 1)
     
    spacer5 = Label(root, text =  "")
    spacer5.grid(row = 14, column = 1)
    
    spacer6 = Label(root, text =  "", padx = 20)
    spacer6.grid(row = 20, column = 3)
    
    spacer7 = Label(root, text =  "", pady = 20)
    spacer7.grid(row = 18, column = 3)
    
    spacer8 = Label(root, text =  "", padx = 40)
    spacer8.grid(row = 20, column = 4)
    
    #Labels - Left hand side of window
    diff_label = Label(root, text = "Diffusivity:")
    diff_label.grid(row = 3, column = 1)
    
    timestep_label = Label(root, text = "Timestep:")
    timestep_label.grid(row = 4, column = 1)
    
    time_label = Label(root, text = "Total simulation time:")
    time_label.grid(row = 5, column = 1)
    
    m_label = Label(root, text = "Mean:")
    m_label.grid(row = 8, column = 1)
    
    var_label = Label(root, text = "Variance:")
    var_label.grid(row = 9, column = 1)
    
    r_label = Label(root, text = "Circle radius:")
    r_label.grid(row = 10, column = 1)
    
    con_label = Label(root, text = "Concentration limit:")
    con_label.grid(row = 11, column = 1)
    
    n_label = Label(root, text = "Number of particles:")
    n_label.grid(row = 13, column = 1)
    
    gridsize_label = Label(root, text = "Circlular patch location:")
    gridsize_label.grid(row = 15, column = 2)
    
    circle_x_label = Label(root, text = "x:")
    circle_x_label.grid(row = 16, column = 1)
    
    circle_y_label = Label(root, text = "y:")
    circle_y_label.grid(row = 17, column = 1)
    
    
    # Labels - Right hand side of window
    lim_label = Label(root, text = "Graph limits:")
    lim_label.grid(row = 3, column = 4)
    
    xulim_label = Label(root, text = "x max:")
    xulim_label.grid(row = 4, column = 4)
    
    xllim_label = Label(root, text = "x min:")
    xllim_label.grid(row = 5, column = 4)
    
    yulim_label = Label(root, text = "y max:")
    yulim_label.grid(row = 6, column = 4)
    
    yllim_label = Label(root, text = "y min:")
    yllim_label.grid(row = 7, column = 4)
    
    df_label = Label(root, text = "Density Field")
    df_label.grid(row = 9, column = 4)
    
    dfx_label = Label(root, text = "Number of grids:")
    dfx_label.grid(row = 10, column = 4)
    
    vel_label = Label(root, text = "Velocity Function:")
    vel_label.grid(row = 12, column = 4)
    
    clr_label = Label(root,text = "Concentration list:")
    clr_label.grid(row = 13, column = 4)
    
    clr_exp = Label(root,text = "(A list of grids where the concentration is larger than the concentration limit)")
    clr_exp.grid(row = 14, column = 4)
    
    half_label = Label(root, text = "Split graph into halves:")
    half_label.grid(row = 15, column = 4)
    
    dim_label = Label(root, text = "Density Field Dimension:")
    dim_label.grid(row = 16, column = 4)
    
    
    # Input fields
    diff_box = Entry(root, width = 10)
    diff_box.grid(row = 3, column = 2)
    diff_box.insert(0,0.1)
    
    timestep_box = Entry(root, width = 10)
    timestep_box.grid(row = 4, column = 2)
    
    time_box = Entry(root, width = 10)
    time_box.grid(row = 5, column = 2)
    
    m_box = Entry(root, width = 5)
    m_box.grid(row = 8, column = 2)
    m_box.insert(0,0)
    
    var_box = Entry(root, width = 5)
    var_box.grid(row = 9, column = 2)
    var_box.insert(0,1)
    
    r_box = Entry(root, width = 5)
    r_box.grid(row = 10, column = 2)
    r_box.insert(0, 0)
    
    con_box = Entry(root, width = 5)
    con_box.grid(row = 11, column = 2)
    con_box.insert(0,0)
    
    n_box = Entry(root, width = 10)
    n_box.grid(row = 13, column = 2)
    
    circle_x_box = Entry(root, width = 5)
    circle_x_box.grid(row = 16, column = 2)
    circle_x_box.insert(0,0)
    
    circle_y_box = Entry(root, width = 5)
    circle_y_box.grid(row = 17, column = 2)
    circle_y_box.insert(0,0)
    
    xulim_box = Entry(root, width = 5)
    xulim_box.grid(row = 4, column = 5)
    xulim_box.insert(0,1)
    
    xllim_box = Entry(root, width = 5)
    xllim_box.grid(row = 5, column = 5)
    xllim_box.insert(0,-1)
    
    yulim_box = Entry(root, width = 5)
    yulim_box.grid(row = 6, column = 5)
    yulim_box.insert(0,1)
    
    yllim_box = Entry(root, width = 5)
    yllim_box.grid(row = 7, column = 5)
    yllim_box.insert(0,-1)
    
    dfx_box = Entry(root, width = 5)
    dfx_box.grid(row = 10, column = 5)
    dfx_box.insert(0,64)
    
    
    # Dropdown menu options
    half_options = [
        "Yes",
        "No (use circle details instead)"]
    
    vel_options = [
        "Yes",
        "No"]
   
    clr_options = [
        "Yes",
        "No"]
    
    dim_options = [
        "1D",
        "2D"]
    
    # Drop down menus
    click_dropdown1 = StringVar()
    click_dropdown1.set("---Select---")
    drop_half = OptionMenu(root, click_dropdown1, *half_options)
    drop_half.grid(row = 15, column = 5)
    
    click_dropdown2 = StringVar()
    click_dropdown2.set("---Select---")
    drop_vel = OptionMenu(root, click_dropdown2, *vel_options)
    drop_vel.grid(row = 12, column = 5)
    
    click_dropdown3 = StringVar()
    click_dropdown3.set("---Select---")
    drop_clr = OptionMenu(root, click_dropdown3, *clr_options)
    drop_clr.grid(row = 13, column = 5)
    
    click_dropdown4 = StringVar()
    click_dropdown4.set("---Select---")    
    drop_dim = OptionMenu(root, click_dropdown4, *dim_options)
    drop_dim.grid(row = 16, column = 5)

    clr = click_dropdown3.get()
    
    # Run button function
    def run_click():
        # Fetching data from entry boxes
        
        xulim = float(xulim_box.get())
        xllim = float(xllim_box.get())
        yulim = float(yulim_box.get())
        yllim = float(yllim_box.get())
        
        D = float(diff_box.get())
        h = float(timestep_box.get())
        
        t = float(time_box.get())
        
        m = float(m_box.get())
        var = float(var_box.get())
        r = float(r_box.get())
        
        
        n = int(n_box.get())
        
        circle_x = float(circle_x_box.get())
        circle_y = float(circle_y_box.get())
        
        Nx = int(dfx_box.get())
        concentration = float(con_box.get())
        
        # Dropdown menu choices
        
        half = click_dropdown1.get()
        Velocity = click_dropdown2.get()
        concentration_list_required = click_dropdown3.get()
        Dim = click_dropdown4.get()
        
        # Appending to result list
        result.append(n), result.append(t), result.append(h), result.append(Dim), result.append(Nx), result.append(half), result.append(r), result.append(circle_x), result.append(circle_y), result.append(Velocity), result.append(concentration_list_required), result.append(concentration), result.append(D), result.append(xllim), result.append(xulim), result.append(yllim), result.append(yulim), result.append(m), result.append(var)
        root.destroy()
        return 
    
    # Run button position/text
    run_button = Button(root, text = "Run simulation", padx = 60, pady = 20, fg = '#76EE00', command = run_click)
    run_button.grid(row = 18, column = 3)
    run_label = Label(root, text = "Run Simulation")
    run_label.grid(row = 18, column = 3)
    
    # Reset button function
    def reset_click():
                diff_box.delete(0, END)
                timestep_box.delete(0, END)
                time_box.delete(0, END)
                m_box.delete(0, END)
                var_box.delete(0, END)
                r_box.delete(0, END)
                circle_x_box.delete(0, END)
                circle_y_box.delete(0, END)
                click_dropdown2.set("---Select---")
                click_dropdown1.set("---Select---")
                click_dropdown3.set("---Select---")
                click_dropdown4.set("---Select---") 
                n_box.delete(0, END)
                con_box.delete(0, END)
                dfx_box.delete(0, END)
                xulim_box.delete(0, END)
                xllim_box.delete(0, END)
                yulim_box.delete(0, END)
                yllim_box.delete(0, END)
                
                diff_box.insert(0,0.1)
                m_box.insert(0,0)
                var_box.insert(0,1)
                dfx_box.insert(0,64)
                xulim_box.insert(0,1)
                xllim_box.insert(0,-1)
                yulim_box.insert(0,1)
                yllim_box.insert(0,-1)
                circle_y_box.insert(0,0)
                circle_x_box.insert(0,0)
                r_box.insert(0,0)
                
                
                con_box.insert(0,0)
                return
    
    # Reset button position/text
    reset_button = Button(root, text = "Reset all", padx = 40, pady = 10, fg = '#FFC125', command = reset_click)
    reset_button.grid(row = 18, column = 4)
    reset_label = Label(root, text = "Reset all")
    reset_label.grid(row = 18, column = 4)
    
    # Exit button function
    def exit_click():
                root.destroy()
                return
    
    # Exit button position/text
    exit_button = Button(root, text = "Exit", padx = 40, pady = 10, bg = "#EE2C2C", command = exit_click)
    exit_button.grid(row = 18, column = 5)
    exit_label = Label(root, text = "Exit")
    exit_label.grid(row = 18, column = 5)
    
    
    root.mainloop()
    return


"--------------------------Getting Input Values from User and assigning them accordingly-------------------"

Input_GUI()

# Number of particles you would like to have in the simulation {n})

n = result[0] 

# Time you would like the simulation to run for {t}

t = result[1] 

# Timestep for the simulation {h}

h = result[2] 

# Would you like to do the 1D or 2D case {Dim}?

Dim = result[3] 

# Density field size Nx,Ny [Nx,Ny] for x and y respectively
# Ny does not need to be changed as there is an if statement 
# that does it for you if the 2D case is chosen

Nx = result[4] 

# Would you like to split the graph 50/50 with colored particles on the left-hand side ? yes/no

half = result[5] 

# If half is not selected, a circle will be generated where initially the 
# inside of the circle will contain a different coloured particle patch 

# Radius of the circle

r = result[6] 

# x,y locations for the centre of the circle

circle_x = result[7] 
circle_y = result[8] 

# Would you like to have the velocity function turned on? yes/no

user_input = result[9] 

# Would you like a list of coordinates [x,y] where the concentration exceeds
# a certain limit (2D only)?

concentration_list_required = result[10] 

# What is the lowest concentration [0,1] you would like to see on the density graph (2D only)?

concentration = result[11] 

# All concentration greater than value above will be stored and show at end

# Diffusivity value for the simulation {D}

D = result[12] 

# Upper and lower bounds of the graph for x,y respectively {xllim, xulim, yllim, yulim}

xllim = result[13] # x - lower limit
xulim = result[14] # x - upper limit
yllim = result[15] # y - lower limit
yulim = result[16] # y - upper limit

# Mean for the Brownian motion part of the Euler-Maruyama equation {m}

m = result[17]

# Variance for the Brownian motion part of the Euler-Maruyama equation {var}

var = result[18]

"""---------------USER PLEASE DO NOT CHANGE ANYTHING PAST THIS SENTENCE!!!-------------------"""

# This is just so the user does not have to change Ny

if Dim == '1D':
    Ny = 1
    error_input = 'Yes'
else:
    Ny = Nx
    error_input = 'no'
# Wall constant

k = 0.01

# Wall boundaries
wxllim = xllim + k # x - lower limit
wxulim = xulim - k # x - upper limit
wyllim = yllim + k # y - lower limit
wyulim = yulim - k # y - upper limit

# Wall bouncing boundaries

# timer for checking the time it takes the simulation to run

timer = 0

# Initial random x,y coordinates for the particles within deifned circle region in the simulation

x_c = []
y_c =[]

# Initial random x,y coordinates for the particles in the simulation

x = [] 
y = [] 

# x,y coordinates of the new positions of the random uniform particles 
# after Euler-Maruyama equations have been used for the calculations

x_new = []
y_new = []

# x,y coordinates and their velocities u,v in the x,y 
# directions respectively from the velocityCMM3 dat file.

x_database = []
y_database = []
u_database = []
v_database = []

# arrays for the reference solution

ref_solution_x = []
ref_solution_y = []

# error array where the Root Mean Square Error results will be listed

error = []

# concentration list for which the x and y values of the concentration position will be stored
# only used if concetration list is requested by user

concentration_list = []

# Difference between the Simulation values and the reference solution

diff = []
