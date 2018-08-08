import tkinter as Tkinter
from serial import Serial
from time import sleep
import TMCL

class App:
    def __init__(self, master):
        frame = Tkinter.Frame(master)

        ######
        self.communication_options = Tkinter.LabelFrame(frame, text="Communication Options", borderwidth=10, relief=Tkinter.GROOVE, padx=10, pady=10)
        self.communication_options.grid(row=0, column=0, padx=10, pady=10)

        self.com_label = Tkinter.Label(self.communication_options, text="Com Port")
        self.com_label.grid(row=0, column=0, padx=10, pady=10)

        self.com_port = Tkinter.StringVar()
        self.com_port.set("COM14")
        self.com_entry = Tkinter.Entry(self.communication_options, textvariable=self.com_port)
        self.com_entry.grid(row=1, column=0, padx=10, pady=10)

        self.com_button = Tkinter.Button(self.communication_options, text="Create Port", bd=10, height=5, width=10, command=lambda: self.createPort(self.com_port.get()))
        self.com_button.grid(row=2, column=0, padx=5, pady=5)
        #######
        self.movement_options = Tkinter.LabelFrame(frame, text="Movement Options", borderwidth=10, relief=Tkinter.GROOVE, padx=10, pady=10)
        self.movement_options.grid(row=0, column=1, padx=10, pady=10)

        self.rotate_left_label = Tkinter.Label(self.movement_options, text="Rotate Left Velocity")
        self.rotate_left_label.grid(row=0, column=0, padx=10, pady=10)

        self.rotate_left_value = Tkinter.StringVar()
        self.rotate_left_value.set("1000")
        self.rotate_left_entry = Tkinter.Entry(self.movement_options, textvariable=self.rotate_left_value)
        self.rotate_left_entry.grid(row=1,column=0, padx=5, pady=5)

        self.rotate_left_button = Tkinter.Button(self.movement_options, text="Rotate Left", bd=10, height=5, width=10, command=lambda: self.rotateLeft(int(self.rotate_left_value.get())))
        self.rotate_left_button.grid(row=2, column=0, padx=5, pady=5)

        self.rotate_right_label = Tkinter.Label(self.movement_options, text="Rotate Right Velocity")
        self.rotate_right_label.grid(row=0, column=1, padx=10, pady=10)

        self.rotate_right_value = Tkinter.StringVar()
        self.rotate_right_value.set("1000")
        self.rotate_right_entry = Tkinter.Entry(self.movement_options, textvariable=self.rotate_right_value)
        self.rotate_right_entry.grid(row=1,column=1, padx=5, pady=5)

        self.rotate_right_button = Tkinter.Button(self.movement_options, text="Rotate Right", bd=10, height=5, width=10, command=lambda: self.rotateRight(int(self.rotate_right_value.get())))
        self.rotate_right_button.grid(row=2, column=1, padx=5, pady=5)
        ########################

        self.rotate_absolute_label = Tkinter.Label(self.movement_options, text="Rotate Absolute Position")
        self.rotate_absolute_label.grid(row=0, column=2, padx=10, pady=10)

        self.rotate_absolute_value = Tkinter.StringVar()
        self.rotate_absolute_value.set("1000")
        self.rotate_absolute_entry = Tkinter.Entry(self.movement_options, textvariable=self.rotate_absolute_value)
        self.rotate_absolute_entry.grid(row=1,column=2, padx=5, pady=5)

        self.rotate_absolute_button = Tkinter.Button(self.movement_options, text="Absolute", bd=10, height=5, width=10, command=lambda: self.rotateAbsolute(int(self.rotate_absolute_value.get())))
        self.rotate_absolute_button.grid(row=2, column=2, padx=5, pady=5)

        self.rotate_relative_label = Tkinter.Label(self.movement_options, text="Rotate Relative (+CW -CCW)")
        self.rotate_relative_label.grid(row=0, column=3, padx=10, pady=10)

        self.rotate_relative_value = Tkinter.StringVar()
        self.rotate_relative_value.set("1000")
        self.rotate_relative_entry = Tkinter.Entry(self.movement_options, textvariable=self.rotate_relative_value)
        self.rotate_relative_entry.grid(row=1,column=3, padx=5, pady=5)

        self.rotate_relative_button = Tkinter.Button(self.movement_options, text="Relative", bd=10, height=5, width=10, command=lambda: self.rotateRelative(int(self.rotate_relative_value.get())))
        self.rotate_relative_button.grid(row=2, column=3, padx=5, pady=5)
        ##############################
        '''
        self.right_limit_button = Tkinter.Button(self.movement_options, text="Right Limit", bd=10, height=5, width=10, command=self.rightLimit)
        self.right_limit_button.grid(row=1, column=4, padx=5, pady=5)

        self.left_limit_button = Tkinter.Button(self.movement_options, text="Left Limit", bd=10, height=5, width=10, command=self.leftLimit)
        self.left_limit_button.grid(row=2, column=4, padx=5, pady=5)
        '''
        ##############################
        self.stop_button = Tkinter.Button(self.movement_options, text="STOP", bd=10, height=5, width=10, command=self.stopMotor)
        self.stop_button.grid(row=3, column=0, padx=5, pady=5)

        self.read_button = Tkinter.Button(self.movement_options, text="READ", bd=10, height=5, width=10, command=self.readSerial)
        self.read_button.grid(row=3, column=1, padx=5, pady=5)

        self.home_button = Tkinter.Button(self.movement_options, text="Home", bd=10, height=5, width=10, command=lambda: self.home(1))
        self.home_button.grid(row=3, column=2, padx=5, pady=5)

        self.next_port = Tkinter.Button(self.movement_options, text="Next Port", bd=10, height=5, width=10, command=lambda: self.nextPort(3))
        self.next_port.grid(row=3, column=3, padx=5, pady=5)
        #################################
        self.mikes_options = Tkinter.LabelFrame(frame, text="Mikes Test", borderwidth=10, relief=Tkinter.GROOVE, padx=10, pady=10)
        self.mikes_options.grid(row=0, column=4, padx=20, pady=20)

        self.backlash_value_label = Tkinter.Label(self.mikes_options, text="Calculated Backlash Value from Test")
        self.backlash_value_label.grid(row=0, column=0, padx=20, pady=20)

        self.backlash_value = Tkinter.StringVar()
        self.backlash_value.set("Run The Test")
        self.backlash_entry = Tkinter.Entry(self.mikes_options, textvariable=self.backlash_value)
        self.backlash_entry.grid(row=1,column=0, padx=5, pady=5)

        self.backlash_button = Tkinter.Button(self.mikes_options, text="Mikes Test", bd=10, height=5, width=10, command=lambda: self.mikesTest(0, 0)) #command= self.mikesTest2) #
        self.backlash_button.grid(row=2, column=0, padx=5, pady=5)
        ###################################
        self.specific_test = Tkinter.LabelFrame(frame, text="Specific Test", borderwidth=10, relief=Tkinter.GROOVE, padx=10, pady=10)
        self.specific_test.grid(row=0, column=5, padx=20, pady=20)

        self.port_label = Tkinter.Label(self.specific_test, text="Enter Port Number")
        self.port_label.grid(row=0, column=0, padx=20, pady=20)

        self.port_value = Tkinter.StringVar()
        self.port_value.set("3")
        self.port_entry = Tkinter.Entry(self.specific_test, textvariable=self.port_value)
        self.port_entry.grid(row=1,column=0, padx=5, pady=5)

        self.backlash_button = Tkinter.Button(self.specific_test, text="Move to Port", bd=10, height=5, width=10, command=lambda: self.specifiedPort(3, int(self.port_value.get()), 0)) #command= self.mikesTest2) #
        self.backlash_button.grid(row=2, column=0, padx=5, pady=5)

        #self.snowObj = {}
        #self.snowObj["clockwise"] = {}
        #self.snowObj["anticlockwise"] = {}
        #self.snowObj["clockwise"]["1"] = {}
        #self.snowObj["clockwise"]["1"]["start"] = 0
        #self.snowObj["clockwise"]["1"]["end"] = 0
        #print(self.snowObj)

        frame.grid(row=0, column=0, padx=20, pady=20)

    def mikesTest(self, status, i):
        self.serial_port.flushInput()
        if status == 0:
            #We're currently on the port
            #So we're going to move off it 1 microstep at a time
            x = self.motor.axis.right_limit_status
            if x == 0:
                self.rotateRelative(-1)
                i += 1
                print(i)
                root.after(100, self.mikesTest(0, i))
            if x == 1:
                self.backlash_value.set(str(i))
                print('over')
        #if status == 1:

    def mikesTest2(self):
        self.serial_port.flushInput()
        i = 0
        while self.motor.axis.right_limit_status == 0:
            self.rotateRelative(-1)
            i += 1
            print(i)
            root.after(100)
            if self.motor.axis.right_limit_status == 1:
                break

        self.backlash_value.set(str(i))
        print("all done")

    def createPort(self, com):
        MODULE_ADDRESS = 1
        self.serial_port = Serial(com)
        self.serial_port.flushInput()
        bus = TMCL.connect(self.serial_port)
        self.motor = bus.get_motor(MODULE_ADDRESS)
        self.motor.axis.set(6, 255)
        self.motor.axis.set(140, 4)


    def home(self, homing):
        self.serial_port.flushInput()
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
        self.serial_port.flushInput()
        if status == 1:
            #print('Should be not on port and starting to rotate')
            self.rotateRight(50)
            root.after(50, self.nextPort(2))
        elif status == 2:
            x = self.motor.axis.right_limit_status
            if x == 1:
                #print('It\'s still not on the port' )
                root.after(50, self.nextPort(2))
            else:
                #print('its at the port')
                self.stopMotor()
        elif status == 3:
            y = self.motor.axis.right_limit_status
            if y == 1:
                #print('It\'s not on the port and we don\'t need to move off before positoning loop')
                root.after(50, self.nextPort(1))
            else:
                #print('It\'s on the port and we need to move off before positoning loop so we rotate')
                self.rotateRight(10)
                root.after(50, self.nextPort(4))
        elif status == 4:
            z = self.motor.axis.right_limit_status
            if z == 1:
                self.stopMotor()
                #print('off the original port begin positioning')
                root.after(50, self.nextPort(1))
            else:
                #print('still on the port')
                root.after(50, self.nextPort(4))
        else:
            pass

    def rotateLeft(self, value):
        self.motor.rotate_left(value)

    def rotateRight(self, value):
        self.motor.rotate_right(value)

    def rotateAbsolute(self, value):
        self.motor.move_absolute(value)

    def rotateRelative(self, value):
        self.motor.move_relative(value)

    def stopMotor(self):
        self.motor.stop()

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

    def specifiedPort(self, status, port, initialPort):
        self.serial_port.flushInput()
        if status == 1:
            #print('Should be not on port and starting to rotate')
            self.rotateRight(50)
            root.after(50, self.specifiedPort(2, port, initialPort))
        elif status == 2:
            x = self.motor.axis.right_limit_status
            if x == 1:
                #print('It\'s still not on the port' )
                root.after(50, self.specifiedPort(2, port, initialPort))
            else:
                initialPort += 1
                if initialPort == port:
                    self.stopMotor()
                else:
                    self.specifiedPort(3, port, initialPort)
        elif status == 3:
            y = self.motor.axis.right_limit_status
            if y == 1:
                #print('It\'s not on the port and we don\'t need to move off before positoning loop')
                root.after(50, self.specifiedPort(1, port, initialPort))
            else:
                #print('It\'s on the port and we need to move off before positoning loop so we rotate')
                self.rotateRight(10)
                root.after(50, self.specifiedPort(4, port, initialPort))
        elif status == 4:
            z = self.motor.axis.right_limit_status
            if z == 1:
                self.stopMotor()
                #print('off the original port begin positioning')
                root.after(50, self.specifiedPort(1, port, initialPort))
            else:
                #print('still on the port')
                root.after(50, self.specifiedPort(4, port, initialPort))
        else:
            pass

    def snowTest(self):
        self.snowLoop(1, 1, 0)

    def snowLoop(self, status, port, counter):
        if status == 1:
            self.rotateRelative(100)
            counter += 100
            root.after(50, self.snowLoop(2, 1, counter))
        elif status == 2:
            y = self.motor.axis.right_limit_status
            if y == 1:
                root.after(50, self.specifiedPort(3, port, initialPort))
            else:
                self.rotateRelative(100)
                counter += 100
                root.after(50, self.specifiedPort(2, port, ))
        elif status == 3:
            self.rotateRelative(5)
            counter =+ 5

root = Tkinter.Tk()
app = App(root)
root.mainloop()
