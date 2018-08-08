import tkinter as Tkinter
from serial import Serial
from time import sleep
import TMCL

class App:
    def __init__(self, master):
        MODULE_ADDRESS = 1
        self.serial_port = Serial("COM14")
        bus = TMCL.connect(self.serial_port)
        self.motor = bus.get_motor(MODULE_ADDRESS)

        frame = Tkinter.Frame(master)

        self.rotate_left_value = Tkinter.StringVar()
        self.rotate_left_value.set("1000")
        self.rotate_left_entry = Tkinter.Entry(frame, textvariable=self.rotate_left_value)
        self.rotate_left_entry.grid(row=0,column=0, padx=5, pady=5)

        self.rotate_left_button = Tkinter.Button(frame, text="Rotate Left", bd=10, height=5, width=10, command=lambda: self.rotateLeft(int(self.rotate_left_value.get())))
        self.rotate_left_button.grid(row=1, column=0, padx=5, pady=5)

        self.rotate_right_value = Tkinter.StringVar()
        self.rotate_right_value.set("1000")
        self.rotate_right_entry = Tkinter.Entry(frame, textvariable=self.rotate_right_value)
        self.rotate_right_entry.grid(row=0,column=1, padx=5, pady=5)

        self.rotate_right_button = Tkinter.Button(frame, text="Rotate Right", bd=10, height=5, width=10, command=lambda: self.rotateRight(int(self.rotate_right_value.get())))
        self.rotate_right_button.grid(row=1, column=1, padx=5, pady=5)
        ########################
        self.rotate_absolute_value = Tkinter.StringVar()
        self.rotate_absolute_value.set("1000")
        self.rotate_absolute_entry = Tkinter.Entry(frame, textvariable=self.rotate_absolute_value)
        self.rotate_absolute_entry.grid(row=0,column=2, padx=5, pady=5)

        self.rotate_absolute_button = Tkinter.Button(frame, text="Absolute", bd=10, height=5, width=10, command=lambda: self.rotateAbsolute(int(self.rotate_absolute_value.get())))
        self.rotate_absolute_button.grid(row=1, column=2, padx=5, pady=5)

        self.rotate_relative_value = Tkinter.StringVar()
        self.rotate_relative_value.set("1000")
        self.rotate_relative_entry = Tkinter.Entry(frame, textvariable=self.rotate_relative_value)
        self.rotate_relative_entry.grid(row=0,column=3, padx=5, pady=5)

        self.rotate_relative_button = Tkinter.Button(frame, text="Relative", bd=10, height=5, width=10, command=lambda: self.rotateRelative(int(self.rotate_relative_value.get())))
        self.rotate_relative_button.grid(row=1, column=3, padx=5, pady=5)
        ##############################
        self.right_limit_button = Tkinter.Button(frame, text="Right Limit", bd=10, height=5, width=10, command=self.rightLimit)
        self.right_limit_button.grid(row=1, column=4, padx=5, pady=5)

        self.left_limit_button = Tkinter.Button(frame, text="Left Limit", bd=10, height=5, width=10, command=self.leftLimit)
        self.left_limit_button.grid(row=2, column=4, padx=5, pady=5)
        ##############################
        self.stop_button = Tkinter.Button(frame, text="STOP", bd=10, height=5, width=10, command=self.stopMotor)
        self.stop_button.grid(row=2, column=0, padx=5, pady=5)

        self.read_button = Tkinter.Button(frame, text="READ", bd=10, height=5, width=10, command=self.readSerial)
        self.read_button.grid(row=2, column=1, padx=5, pady=5)

        self.home_button = Tkinter.Button(frame, text="Home", bd=10, height=5, width=10, command=lambda: self.home(1))
        self.home_button.grid(row=2, column=2, padx=5, pady=5)

        self.next_port = Tkinter.Button(frame, text="Next Port", bd=10, height=5, width=10, command=lambda: self.nextPort(1))
        self.next_port.grid(row=2, column=3, padx=5, pady=5)

        frame.grid(row=0, column=0, padx=20, pady=20)

    def home(self, homing):
        if homing == 1:
            self.rotateRight(50)
            root.after(50, self.home(2))
        elif homing == 2:
            x = self.motor.axis.left_limit_status
            if x == 1:
                root.after(50, self.home(2))
            else:
                self.stopMotor()
        else:
            pass

    def nextPort(self, status):
        if status == 1:
            self.rotateRight(50)
            root.after(50, self.nextPort(2))
        elif status == 2:
            x = self.motor.axis.right_limit_status
            if x == 1:
                root.after(50, self.nextPort(2))
            else:
                self.stopMotor()
                #return
        elif status == 3:
            y = self.motor.axis.right_limit_status
            if y == 1:
                root.after(50, self.nextPort(1))
            else:
                self.rotateRight(10)
                root.after(50, self.nextPort(4))
        elif status == 4:
            z = self.motor.axis.right_limit_status
            if z == 1:
                self.stopMotor()
                root.after(50, self.nextPort(1))
            else:
                root.after(50, self.nextPort(4))
        else:
            pass

    def rotateLeft(self, value):
        self.motor.rotate_left(value)
        return

    def rotateRight(self, value):
        self.motor.rotate_right(value)
        return

    def rotateAbsolute(self, value):
        self.motor.move_absolute(value)
        return

    def rotateRelative(self, value):
        self.motor.move_relative(value)
        return

    def stopMotor(self):
        self.motor.stop()
        return

    def readSerial(self):
        #x = 'nothing'
        #if self.serial_port.inWaiting() > 1:
        #    x = self.serial_port.readline()
        #print(x)
        print("right: ", self.motor.axis.right_limit_status)
        print("left: ", self.motor.axis.left_limit_status)
        root.after(1000, self.readSerial)
        #return

    def rightLimit(self):
        print(self.motor.axis.right_limit_status)

    def leftLimit(self):
        print(self.motor.axis.left_limit_status)

root = Tkinter.Tk()
app = App(root)
root.mainloop()
