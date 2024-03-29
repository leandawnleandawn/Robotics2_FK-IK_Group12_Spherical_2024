import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
from tkinter.font import nametofont
import tkinter as tk
from PIL import ImageTk, Image
import numpy as np
from roboticstoolbox import SerialLink, RevoluteDH, PrismaticDH

class RoboticProgram(ttkb.Window):
    
    def __init__(self):
        super().__init__()
        
        self.title("Kinematic Analysis")
        self.geometry('1280x720')
        self.resizable(width=False, height=False)
        ML = ttkb.Labelframe(bootstyle='light')
        ML.place(x = 75, y = 150, relwidth=0.3, relheight=1)
        PL = ttkb.Canvas()
        PL.place(x = 512, y = 0, relwidth=0.7, relheight=1)
        self.windowTitle = ttkb.Label(ML, text="Kinematic Analysis Calculator", font = 'Helvetica 18 bold')
        self.windowTitle.pack(pady=20)
        
        palletizingRobot = ImageTk.PhotoImage(Image.open('robot.jpg').resize((1280, 720)))
        img_robot = tk.Label(PL, image=palletizingRobot)
        img_robot.dontloseit = palletizingRobot
        img_robot.pack(fill="both")
        
        FKin = ttkb.Button(ML, text = "Forward Kinematics", command = FkinWindow, bootstyle="primary")
        FKin.pack(pady=20, padx = 10)
        
        IKin = ttkb.Button(ML, text = "Inverse Kinematics", command= IkinWindow, bootstyle="primary")
        IKin.pack(pady=20, padx = 10)
        
        JBin = ttkb.Button(ML, text = "Jacobian Matrix", command= JBinWindow, bootstyle="primary")
        JBin.pack(pady=20, padx = 10)
        
        
class Window(RoboticProgram):
    def __init__(self):
        self.windowTitle = ttkb.Toplevel(master = robot)
        self.windowTitle.geometry("500x500")
        LL = ttkb.Labelframe(master=self.windowTitle, text = "Link Length and Joint Variables")
        LL.place(x=0, y=0, relwidth=0.5, relheight=0.5)
        LL.columnconfigure((0,1,2), weight=1, uniform="a")
        LL.rowconfigure((0,1,2), weight=1, uniform="a")
        a1L = ttkb.Label(LL, text = ("a1 = "))
        self.a1data = ttkb.Entry(LL,width=5)
        cm1 = ttkb.Label(LL, text = ("cm"))
        
        a2L = ttkb.Label(LL, text = ("a2 = "))
        self.a2data = ttkb.Entry(LL,width=5)
        cm2 = ttkb.Label(LL, text = ("cm"))
        
        a3L = ttkb.Label(LL, text = ("a3 = "))
        self.a3data = ttkb.Entry(LL,width=5)
        cm3 = ttkb.Label(LL, text = ("cm"))
        
        a1L.grid(row=0,column=0, padx=5, pady=5)
        self.a1data.grid(row=0,column=1, padx=5, pady=5)
        cm1.grid(row=0,column=2, padx=5, pady=5)
        
        a2L.grid(row=1,column=0, padx=5, pady=5)
        self.a2data.grid(row=1,column=1, padx=5, pady=5)
        cm2.grid(row=1,column=2, padx=5, pady=5)
        
        a3L.grid(row=2,column=0, padx=5, pady=5)
        self.a3data.grid(row=2,column=1, padx=5, pady=5)
        cm3.grid(row=2,column=2, padx=5, pady=5)
        
        JV= ttkb.Labelframe(master=self.windowTitle, text = "Joint Variables")
        JV.place(x=250, y=0, relwidth=0.5, relheight=0.5)
        JV.columnconfigure((0,1,2), weight=1, uniform="a")
        JV.rowconfigure((0,1,2), weight=1, uniform="a")
        t1L = ttkb.Label(JV, text = ("T1 = "))
        self.T1data = ttkb.Entry(JV,width=5)
        deg1 = ttkb.Label(JV, text = ("deg"))
        
        t2L = ttkb.Label(JV, text = ("T2 = "))
        self.T2data = ttkb.Entry(JV,width=5)
        deg2 = ttkb.Label(JV, text = ("deg"))
        
        d3L = ttkb.Label(JV, text = ("d3 = "))
        self.d3data = ttkb.Entry(JV,width=5)
        cm4 = ttkb.Label(JV, text = ("cm"))
        
        t1L.grid(row=0, column=0, padx=5, pady=5)
        self.T1data.grid(row=0,column=1,  padx=5, pady=5)
        deg1.grid(row=0, column=2, padx=5, pady=5)
        
        t2L.grid(row=1, column=0, padx=5, pady=5)
        self.T2data.grid(row=1, column=1, padx=5, pady=5)
        deg2.grid(row=1, column=2, padx=5, pady=5)
        
        d3L.grid(row=2, column=0, padx=5, pady=5)
        self.d3data.grid(row=2, column=1, padx=5, pady=5)
        cm4.grid(row=2, column=2, padx=5, pady=5)
        
        PV = ttkb.Labelframe(master=self.windowTitle, text = "Position Vector")
        PV.place(x=125, y=350, relwidth=0.5, relheight=0.25)
        PV.columnconfigure((0,1,2), weight=1, uniform="a")
        PV.rowconfigure((0,1,2), weight=1, uniform="a")
        XL = ttkb.Label(PV, text = ("X = "))
        self.Xdata = ttkb.Entry(PV,width=5)
        cm5 = ttkb.Label(PV, text = ("cm"))
        
        YL = ttkb.Label(PV, text = ("Y = "))
        self.Ydata = ttkb.Entry(PV,width=5)
        cm6 = ttkb.Label(PV, text = ("cm"))
        
        ZL = ttkb.Label(PV, text = ("Z = "))
        self.Zdata = ttkb.Entry(PV,width=5)
        cm7 = ttkb.Label(PV, text = ("cm"))
        
        XL.grid(row=0, column=0, padx=5, pady=5)
        self.Xdata.grid(row=0, column=1, padx=5, pady=5)
        cm5.grid(row=0, column=2, padx=5, pady=5)
        
        YL.grid(row=1, column=0, padx=5, pady=5)
        self.Ydata.grid(row=1, column=1, padx=5, pady=5)
        cm6.grid(row=1, column=2, padx=5, pady=5)
        
        ZL.grid(row=2, column=0, padx=5, pady=5)
        self.Zdata.grid(row=2, column=1, padx=5, pady=5)
        cm7.grid(row=2, column=2, padx=5, pady=5)
        
    def reset(self):        
        self.a1data.delete(0,'end')
        self.a2data.delete(0, 'end')
        self.a3data.delete(0, 'end')
        self.T1data.delete(0, 'end')
        self.T2data.delete(0,'end')
        self.d3data.delete(0, 'end')
        self.Xdata.delete(0, 'end')
        self.Ydata.delete(0, 'end')
        self.Zdata.delete(0, 'end')
        
class FkinWindow(Window):	
    def __init__(self):
        super().__init__()
        
        self.Xdata.config(state= ttkb.DISABLED)
        self.Ydata.config(state= ttkb.DISABLED)
        self.Zdata.config(state= ttkb.DISABLED)
        
        self.windowTitle.title("Foward Kinematics")
        
        BF = ttkb.Labelframe(master=self.windowTitle)
        BF.place(x=125, y=250, relwidth=0.5, relheight=0.15)
        BF.columnconfigure((0,1), weight=1, uniform="a")
        BF.rowconfigure((0), weight=1, uniform="a")
        forward = ttkb.Button(BF, text = "Foward", command=self.fkin, bootstyle="primary-outline")
        forward.grid(row=0, column=0)
        reset = ttkb.Button(BF, text = "Reset", command=self.reset, bootstyle="secondary-outline")
        reset.grid(row=0, column=1)
        
        self.robotTB(1,0.5,0.5,0,0,0)
          
    def fkin(self):
        self.Xdata.config(state= ttkb.NORMAL)
        self.Ydata.config(state= ttkb.NORMAL)
        self.Zdata.config(state= ttkb.NORMAL)
        self.Xdata.delete(0, 'end')
        self.Ydata.delete(0, 'end')
        self.Zdata.delete(0, 'end')
        try:
            a1 = float(self.a1data.get()) / 100
            a2 = float(self.a2data.get()) / 100
            a3 = float(self.a3data.get()) / 100
            t1 = float(self.T1data.get()) * (np.pi/180)
            t2 = float(self.T2data.get()) * (np.pi/180)
            d3 = float(self.d3data.get()) / 100
        except ValueError:
            pop_up = ttkb.Toplevel(master= robot)
            label = ttkb.Label(pop_up, text = "Use the approriate syntax (float)")
            label.pack()
            
        parametric_table = [[t1, np.pi/2, 0, a1],
                            [np.pi/2 + t2, np.pi/2, 0, 0 ],
                            [0,0,0,a2+a3+d3]]
        htm = {}
        
        for i in range(3):
            htm[i] = self.dhMatrix(parametric_table[i][0], parametric_table[i][1], parametric_table[i][2], parametric_table[i][3])
            
        for i,j in htm.items():
            print(f"HTM # {i+1}")
            print(np.round(j, 2))
            
        result = np.dot(np.dot(htm[0], htm[1]), htm[2])
        print(np.round(result,2))
        
        if (t1 < -np.pi/2 or t1 > np.pi/2) or (t2 < -np.pi/2 or t2 > np.pi/2) or (d3 < 0 or d3 >=  0.5):
            another_pop_up = ttkb.Toplevel(master=robot)
            qlim_error = ttkb.Label(another_pop_up, text = "The Calculated Joint Limits exceeded the Acutal Joint Limits")
            qlim_error.pack()
        else:
            
            self.Xdata.insert(ttkb.END, np.round(result[0,3] * 100,2))
            self.Ydata.insert(ttkb.END, np.round(result[1,3] * 100,2))
            self.Zdata.insert(ttkb.END, np.round(result[2,3] * 100,2))
            self.Xdata.config(state= ttkb.DISABLED)
            self.Ydata.config(state= ttkb.DISABLED)
            self.Zdata.config(state= ttkb.DISABLED)
            self.robotTB(a1, a2, a3, t1, t2, d3)
        
    def dhMatrix(self, theta, alpha, radius, distance):
        return np.matrix([
            [np.cos(theta), -np.sin(theta)*np.cos(alpha), np.sin(theta)*np.sin(alpha), radius*np.cos(theta)],
            [np.sin(theta), np.cos(theta)*np.cos(alpha), -np.cos(theta)*np.sin(alpha), radius*np.sin(theta)],
            [0, np.sin(alpha), np.cos(alpha), distance],
            [0,0,0,1]
        ])
    def robotTB(self, a1, a2, a3, t1, t2, d3):
        
        H01 = RevoluteDH(a1, 0, np.pi/2, 0, [-np.pi/2, np.pi/2])
        H12 = RevoluteDH(0, 0, np.pi/2, np.pi/2, [-np.pi/2, np.pi/2])
        H23 = PrismaticDH(0,0,0,a2+a3,[0, 0.5])
        
        sphericalManipulator = SerialLink([H01, H12, H23])
        sphericalManipulator.plot([t1, t2, d3])

class IkinWindow(Window):
    def __init__(self):
        super().__init__()
        
        self.T1data.config(state= ttkb.DISABLED)
        self.T2data.config(state= ttkb.DISABLED)
        self.d3data.config(state= ttkb.DISABLED)
        
        self.windowTitle.title("Inverse Kinematics")
        
        BF = ttkb.Labelframe(master=self.windowTitle)
        BF.place(x=125, y=250, relwidth=0.5, relheight=0.15)
        BF.columnconfigure((0,1), weight=1, uniform="a")
        BF.rowconfigure((0), weight=1, uniform="a")
        inverse= ttkb.Button(BF, text = "Inverse", command=self.ikin, bootstyle="primary-outline")
        inverse.grid(row=0, column=0)
        reset = ttkb.Button(BF, text = "Reset", command=self.reset, bootstyle="secondary-outline")
        reset.grid(row=0, column=1)
        
    def ikin(self):
        self.T1data.config(state= ttkb.NORMAL)
        self.T2data.config(state= ttkb.NORMAL)
        self.d3data.config(state= ttkb.NORMAL)
        self.T1data.delete(0, 'end')
        self.T2data.delete(0,'end')
        self.d3data.delete(0, 'end')
        
        try:
            a1 = float(self.a1data.get()) / 100
            a2 = float(self.a2data.get()) / 100
            a3 = float(self.a3data.get()) / 100
            x = float(self.Xdata.get()) / 100
            y = float(self.Ydata.get()) / 100
            z = float(self.Zdata.get()) / 100
        except ValueError:
            pop_up = ttkb.Toplevel(master= robot)
            label = ttkb.Label(pop_up, text = "Use the approriate syntax (float)")
            label.pack()
        try:
            t1, t2, d3 = self.invKins(a1, a2, a3, x, y, z)
        except ZeroDivisionError:
            pop_up = ttkb.Toplevel(master= robot)
            label = ttkb.Label(pop_up, text = "The Inverse Kinematic Calculation is undefined")
            label.pack()
            
        self.T1data.insert(ttkb.END, t1)
        self.T2data.insert(ttkb.END, t2)
        self.d3data.insert(ttkb.END, d3)
        self.T1data.config(state= ttkb.DISABLED)
        self.T2data.config(state= ttkb.DISABLED)
        self.d3data.config(state= ttkb.DISABLED)
            
    def invKins(self, a1, a2, a3, x_03, y_03, z_03):
        s = z_03 - a1
        r = np.sqrt((x_03**2) + (y_03**2))
        theta1 = np.arctan(y_03/x_03) * 180/np.pi
        theta2 = np.arctan(s/r) * 180/np.pi
        d3 = (np.sqrt((r**2) + (s**2)) - a2 - a3) * 100
        return theta1, theta2, d3


class JBinWindow():
    def __init__(self):
        self.windowTitle = tk.Toplevel(master = robot)
        
robot = RoboticProgram()
robot.style.theme_use('simplex')

default_font = nametofont('TkDefaultFont')
default_font.configure(family="Helvetica", size=12)
robot.mainloop()

