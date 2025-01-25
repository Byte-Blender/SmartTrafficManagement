from tkinter import *
from tkinter import filedialog
import car_count
import threading


def Calculate_traffic_timing(lane1,lane2,lane3,lane4,root):
    root.destroy()
    threshold_timing = 5
    TL1=30
    TL2=30
    TL3=30
    TL4=30

    if lane1>5:
        TL1 =TL1 + (lane1-5)*threshold_timing
        if TL1>120:
            TL1 = 120

    if lane2>5:
        TL2 =TL2 + (lane2-5)*threshold_timing
        if TL2>120:
            TL2 = 120

    if lane3>5:
        TL3 =TL3 + (lane3-5)*threshold_timing
        if TL3>120:
            TL3 = 120

    if lane4>5:
        TL4 =TL4 + (lane4-5)*threshold_timing
        if TL4>120:
            TL4 = 120


    traffic_timing_win = Tk()
    traffic_timing_win.geometry("950x480")
    traffic_timing_win.title("Traffic Management Timings")

    Label(traffic_timing_win, text='Calculated Timings', font=("Arial", 20)).grid(row=1,column=5)

    Label(traffic_timing_win, text='Lane 1', font=("Arial", 20)).grid(row=3, column=1)
    Label(traffic_timing_win, text=f'number of Vehicles ----- {lane1}', font=("Arial", 15)).grid(row=6, column=1)
    Label(traffic_timing_win, text=f'Time alloted for traffic ------- {TL1} sec', font=("Arial", 15)).grid(row=9, column=1)


    Label(traffic_timing_win, text='Lane 2', font=("Arial", 20)).grid(row=3, column=10)
    Label(traffic_timing_win, text=f'number of Vehicles ----- {lane2}', font=("Arial", 15)).grid(row=6, column=10)
    Label(traffic_timing_win, text=f'Time alloted for traffic ------- {TL2} sec', font=("Arial", 15)).grid(row=9, column=10)



    Label(traffic_timing_win, text='Lane 3', font=("Arial", 20)).grid(row=15, column=1)
    Label(traffic_timing_win, text=f'number of Vehicles ----- {lane3}', font=("Arial", 15)).grid(row=18, column=1)
    Label(traffic_timing_win, text=f'Time alloted for traffic ------- {TL3} sec', font=("Arial", 15)).grid(row=21, column=1)


    Label(traffic_timing_win, text='Lane 4', font=("Arial", 20)).grid(row=15, column=10)
    Label(traffic_timing_win, text=f'number of Vehicles ----- {lane4}', font=("Arial", 15)).grid(row=18, column=10)
    Label(traffic_timing_win, text=f'Time alloted for traffic ------- {TL4} sec', font=("Arial", 15)).grid(row=21, column=10)



def cameraFeed(videopath1,videopath2,videopath3,videopath4):

    lane1 = car_count.carDetect(videopath1)
    print("lane 1 -- ",lane1)
    try:
        lane2 = car_count.carDetect(videopath2) - lane1
    except:
        lane2=0
    print("lane 2 -- ",lane2)
    try:
        lane3 = car_count.carDetect(videopath3) - (lane2 + lane1)
    except:
        lane3=0
    print("lane 3 -- ",lane3)
    try:
        lane4 = car_count.carDetect(videopath4) - (lane3 + lane2)
    except:
        lane4=0
    print("lane 4 -- ",lane4)

    Calculate_traffic_timing(lane1,lane2,lane3,lane4,root)


def NumberOfCarOption():
    def GetEntryValue():
        value1 = int(c1.get())
        print("Entry value:", value1)
        value2 = int(c2.get())
        print("Entry value:", value2)
        value3 = int(c3.get())
        print("Entry value:", value3)
        value4 = int(c4.get())
        print("Entry value:", value4)

        Calculate_traffic_timing(value1,value2,value3,value4,NumberOfCar_win)




    root.destroy()

    NumberOfCar_win = Tk()
    NumberOfCar_win.geometry("950x480")
    NumberOfCar_win.title("Traffic Management System")

    Label(NumberOfCar_win, text='Number of cars on lane 1',font=("Arial",20)).grid(row=1)
    c1 = Entry(NumberOfCar_win)
    c1.grid(row=1,column=2)


    Label(NumberOfCar_win, text='Number of cars on lane 2',font=("Arial",20)).grid(row=4)
    c2 = Entry(NumberOfCar_win)
    c2.grid(row=4,column=2)


    Label(NumberOfCar_win, text='Number of cars on lane 3',font=("Arial",20)).grid(row=7)
    c3 = Entry(NumberOfCar_win)
    c3.grid(row=7,column=2)

    Label(NumberOfCar_win, text='Number of cars on lane 4',font=("Arial",20)).grid(row=10)
    c4 = Entry(NumberOfCar_win)
    c4.grid(row=10,column=2)

    Button(NumberOfCar_win, text="Calculate Timings", height=2, width=30, font=("Arial", 15), command=GetEntryValue).grid(row=15,column=4)


def input_vid_file():

    filepath1 = filedialog.askopenfilename(title="Lane 1")
    filepath2 = filedialog.askopenfilename(title="Lane 2")
    filepath3 = filedialog.askopenfilename(title="Lane 3")
    filepath4 = filedialog.askopenfilename(title="Lane 4")

    cameraFeed(filepath1,filepath2,filepath3,filepath4)

root = Tk()

root.geometry("950x480")
root.title("Traffic Management System")

Label(root, text="Welcome to traffic management App",font=("Arial",20)).pack()

Button(root, text="Start with camera feed",height= 2, width=30,font=("Arial",15),command=input_vid_file).pack()

Button(root, text="Start with Number of cars",height= 2, width=30,font=("Arial",15),command=NumberOfCarOption).pack()

root.mainloop()
