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
        self.com_port.set("COM29")
        self.com_entry = Tkinter.Entry(self.communication_options, textvariable=self.com_port)
        self.com_entry.grid(row=1, column=0, padx=10, pady=10)

        self.com_button = Tkinter.Button(self.communication_options, text="Create Port", bd=10, height=5, width=10, command=lambda: self.createPort(self.com_port.get()))
        self.com_button.grid(row=2, column=0, padx=5, pady=5)
        #####################################################
        #####################################################
        self.pump_parameter_options = Tkinter.LabelFrame(frame, text="Pump Parameters", borderwidth=10, relief=Tkinter.GROOVE, padx=10, pady=10)
        self.pump_parameter_options.grid(row=0, column=1, padx=10, pady=10)

        self.pump_home_button = Tkinter.Button(self.pump_parameter_options, text="HOME", bd=10, height=5, width=10, command=self.home_pump)
        self.pump_home_button.grid(row=0, column=0, padx=5, pady=5)

        self.pump_stop_button = Tkinter.Button(self.pump_parameter_options, text="STOP", bd=10, height=5, width=10, command=self.stop_pump)
        self.pump_stop_button.grid(row=1, column=0, padx=5, pady=5)

        self.pump_acceleration_label = Tkinter.Label(self.pump_parameter_options, text="Acceleration")
        self.pump_acceleration_label.grid(row=2, column=0, padx=10, pady=10)

        self.pump_acceleration_value = Tkinter.StringVar()
        self.pump_acceleration_value.set("1000")
        self.pump_acceleration_entry = Tkinter.Entry(self.pump_parameter_options, textvariable=self.pump_acceleration_value)
        self.pump_acceleration_entry.grid(row=3,column=0, padx=5, pady=5)

        self.pump_acceleration_button = Tkinter.Button(self.pump_parameter_options, text="Set Acceleration", bd=10, height=5, width=10, command=lambda: self.set_pump_acceleration(int(self.pump_acceleration_value.get())))
        self.pump_acceleration_button.grid(row=4, column=0, padx=5, pady=5)

        self.pump_velocity_label = Tkinter.Label(self.pump_parameter_options, text="Velocity")
        self.pump_velocity_label.grid(row=5, column=0, padx=10, pady=10)

        self.pump_velocity_value = Tkinter.StringVar()
        self.pump_velocity_value.set("1000")
        self.pump_velocity_entry = Tkinter.Entry(self.pump_parameter_options, textvariable=self.pump_acceleration_value)
        self.pump_velocity_entry.grid(row=6,column=0, padx=5, pady=5)

        self.pump_velocity_button = Tkinter.Button(self.pump_parameter_options, text="Set Velocity", bd=10, height=5, width=10, command=lambda: self.set_pump_velocity(int(self.pump_velocity_value.get())))
        self.pump_velocity_button.grid(row=7, column=0, padx=5, pady=5)

        self.pump_tpi_label = Tkinter.Label(self.pump_parameter_options, text="Threads Per Inch")
        self.pump_tpi_label.grid(row=8, column=0, padx=10, pady=10)

        self.pump_tpi_value = Tkinter.StringVar()
        self.pump_tpi_value.set("20")
        self.pump_tpi_entry = Tkinter.Entry(self.pump_parameter_options, textvariable=self.pump_tpi_value)
        self.pump_tpi_entry.grid(row=9,column=0, padx=5, pady=5)

        ###############################################################
        ###############################################################

        self.pump_movement_options = Tkinter.LabelFrame(frame, text="Dispense Options", borderwidth=10, relief=Tkinter.GROOVE, padx=10, pady=10)
        self.pump_movement_options.grid(row=0, column=2, padx=10, pady=10)

        self.pump_aspirate_label = Tkinter.Label(self.pump_movement_options, text="Aspirate")
        self.pump_aspirate_label.grid(row=0, column=0, padx=10, pady=10)

        self.pump_aspirate_value = Tkinter.StringVar()
        self.pump_aspirate_value.set("5")
        self.pump_aspirate_entry = Tkinter.Entry(self.pump_movement_options, textvariable=self.pump_aspirate_value)
        self.pump_aspirate_entry.grid(row=1,column=0, padx=5, pady=5)

        self.pump_aspirate_button = Tkinter.Button(self.pump_movement_options, text="Custom Aspirate", bd=10, height=5, width=10, command=lambda: self.aspirate_percent(int(self.pump_aspirate_value.get())))
        self.pump_aspirate_button.grid(row=2, column=0, padx=5, pady=5)

        self.pump_dispense_label = Tkinter.Label(self.pump_movement_options, text="Dispense")
        self.pump_dispense_label.grid(row=0, column=1, padx=10, pady=10)

        self.pump_dispense_value = Tkinter.StringVar()
        self.pump_dispense_value.set("5")
        self.pump_dispense_entry = Tkinter.Entry(self.pump_movement_options, textvariable=self.pump_dispense_value)
        self.pump_dispense_entry.grid(row=1,column=1, padx=5, pady=5)

        self.pump_dispense_button = Tkinter.Button(self.pump_movement_options, text="Custom Dispense", bd=10, height=5, width=10, command=lambda: self.dispense_percent(int(self.pump_dispense_value.get())))
        self.pump_dispense_button.grid(row=2, column=1, padx=5, pady=5)

        self.pump_aspirate_1_button = Tkinter.Button(self.pump_movement_options, text="Aspirate 1", bd=10, height=5, width=10, command=lambda: self.aspirate_percent(1))
        self.pump_aspirate_1_button.grid(row=3, column=0, padx=5, pady=5)

        self.pump_aspirate_10_button = Tkinter.Button(self.pump_movement_options, text="Aspirate 10", bd=10, height=5, width=10, command=lambda: self.aspirate_percent(10))
        self.pump_aspirate_10_button.grid(row=4, column=0, padx=5, pady=5)

        self.pump_aspirate_50_button = Tkinter.Button(self.pump_movement_options, text="Aspirate 50", bd=10, height=5, width=10, command=lambda: self.aspirate_percent(50))
        self.pump_aspirate_50_button.grid(row=5, column=0, padx=5, pady=5)

        self.pump_aspirate_100_button = Tkinter.Button(self.pump_movement_options, text="Aspirate 100", bd=10, height=5, width=10, command=lambda: self.aspirate_percent(100))
        self.pump_aspirate_100_button.grid(row=6, column=0, padx=5, pady=5)

        self.pump_dispense_1_button = Tkinter.Button(self.pump_movement_options, text="Dispense 1", bd=10, height=5, width=10, command=lambda: self.dispense_percent(1))
        self.pump_dispense_1_button.grid(row=3, column=1, padx=5, pady=5)

        self.pump_dispense_10_button = Tkinter.Button(self.pump_movement_options, text="Dispense 10", bd=10, height=5, width=10, command=lambda: self.dispense_percent(10))
        self.pump_dispense_10_button.grid(row=4, column=1, padx=5, pady=5)

        self.pump_dispense_50_button = Tkinter.Button(self.pump_movement_options, text="Dispense 50", bd=10, height=5, width=10, command=lambda: self.dispense_percent(50))
        self.pump_dispense_50_button.grid(row=5, column=1, padx=5, pady=5)

        self.pump_dispense_100_button = Tkinter.Button(self.pump_movement_options, text="Dispense 100", bd=10, height=5, width=10, command=lambda: self.dispense_percent(100))
        self.pump_dispense_100_button.grid(row=6, column=1, padx=5, pady=5)

        ########################################################################
        ########################################################################

        self.erv_movement_options = Tkinter.LabelFrame(frame, text="ERV Options", borderwidth=10, relief=Tkinter.GROOVE, padx=10, pady=10)
        self.erv_movement_options.grid(row=0, column=3, padx=10, pady=10)

        self.erv_stop_button = Tkinter.Button(self.erv_movement_options, text="STOP", bd=10, height=5, width=10, command=self.stop_erv)
        self.erv_stop_button.grid(row=0, column=0, padx=5, pady=5)

        self.erv_home_button = Tkinter.Button(self.erv_movement_options, text="HOME", bd=10, height=5, width=10, command=self.home_erv)
        self.erv_home_button.grid(row=1, column=0, padx=5, pady=5)

        self.erv_next_port_button = Tkinter.Button(self.erv_movement_options, text="Next Port", bd=10, height=5, width=10, command=lambda: self.next_port_erv(3))
        self.erv_next_port_button.grid(row=2, column=0, padx=5, pady=5)

        self.erv_port_label = Tkinter.Label(self.erv_movement_options, text="Enter Port Number")
        self.erv_port_label.grid(row=4, column=0, padx=20, pady=20)

        self.erv_port_value = Tkinter.StringVar()
        self.erv_port_value.set("1")
        self.erv_port_entry = Tkinter.Entry(self.erv_movement_options, textvariable=self.erv_port_value)
        self.erv_port_entry.grid(row=5,column=0, padx=5, pady=5)

        self.erv_port_button = Tkinter.Button(self.erv_movement_options, text="Move to Port", bd=10, height=5, width=10, command=lambda: self.erv_specific_port(3, int(self.erv_port_value.get()), 0))
        self.erv_port_button.grid(row=6, column=0, padx=5, pady=5)


        ########################################################################
        ########################################################################

        self.pump_stop = 0
        self.erv_stop = 0
        self.erv_home = 0
        frame.grid(row=0, column=0, padx=20, pady=20)

    ###########################################################################
    ##Communication############################################################
    ###########################################################################

    def createPort(self, com):
        MODULE_ADDRESS = 1
        self.serial_port = Serial(com, 115200)
        self.serial_port.flushInput()
        bus = TMCL.Bus( self.serial_port )
        module = bus.get_module(1)
        self.motor = module.get_motor(0)
        self.motor1 = module.get_motor(1)
        self.motor.axis.set(6, 255)
        self.motor.axis.set(140, 4)
        self.motor1.axis.set(6, 255)
        self.motor1.axis.set(140, 4)

    ###########################################################################
    ######Pump#################################################################
    ###########################################################################

    def home_pump(self):
        self.pump_stop = 0
        rep = self.motor.send(15, 4, self.motor.motor_id, 0)
        if rep.value == 0:
            self.rotate_pump_left()
            self.wait_for_home_left()
        else:
            self.rotate_pump_right()
            self.wait_for_home_right()

    def rotate_pump_right(self):
        self.motor.rotate_right(5000)

    def rotate_pump_left(self):
        self.motor.rotate_left(5000)

    def wait_for_home_left(self):
        if self.pump_stop == 0:
            rep = self.motor.send(15, 4, self.motor.motor_id, 0)
            print(rep.value)
            if rep.value == 0:
                root.after(50, self.wait_for_home_left)
            else:
                self.motor.stop()
                print('else')
                self.stop_pump

    def stop_pump(self):
        print('here')
        self.motor.stop()
        self.pump_stop = 1

    def wait_for_home_right(self):
        if self.pump_stop == 0:
            rep = self.motor.send(15, 4, self.motor.motor_id, 0)
            print(rep.value)
            if rep.value == 1:
                root.after(50, self.wait_for_home_right)
            else:
                self.motor.stop()
                print('else')
                self.stop_pump

    def dispense_percent(self, percent):
        threads = int(self.pump_tpi_value.get())
        steps = 16 * threads * percent
        self.motor.move_relative(steps)

    def aspirate_percent(self, percent):
        threads = int(self.pump_tpi_value.get())
        steps = 16 * threads * percent * -1
        self.motor.move_relative(steps)

    def set_pump_acceleration(self, accel):
        self.motor.set(5, accel)


    def set_pump_velocity(self, velocity):
        self.motor.max_positioning_speed(velocity)

    ###########################################################################
    ########ERV################################################################
    ###########################################################################

    def stop_erv(self):
        self.erv_stop = 1
        self.motor1.stop()

    def home_erv(self):
        self.serial_port.flushInput()
        self.erv_stop = 0
        self.rotate_erv_right(250)
        self.wait_for_erv_home()

    def wait_for_erv_home(self):
        if self.erv_stop == 0:
            rep = self.motor.send(15, 5, self.motor.motor_id, 0)
            if rep.value == 1:
                root.after(50, self.wait_for_erv_home)
            else:
                self.motor1.stop()

    def wait_for_erv_next(self):
        if self.erv_stop == 0:
            rep = self.motor.send(15, 6, self.motor.motor_id, 0)
            if rep.value == 1:
                root.after(50, self.wait_for_erv_next)
            else:
                self.motor1.stop()

    def wait_for_off_port(self):
        if self.erv_stop == 0:
            rep = self.motor.send(15, 6, self.motor.motor_id, 0)
            if rep.value == 0:
                root.after(50, self.wait_for_off_port)
            else:
                self.wait_for_erv_next()

    def next_port_erv(self, status):
        self.serial_port.flushInput()
        self.erv_stop = 0
        self.rotate_erv_right(250)
        rep = self.motor.send(15, 6, self.motor.motor_id, 0)
        if rep.value == 1:
            self.wait_for_erv_next()
        else:
            self.wait_for_off_port()

    def rotate_erv_right(self, value):
        self.motor1.rotate_right(value)

    def rotate_erv_left(self, value):
        self.motor1.rotate_left(value)
    
    def erv_specific_port(self, status, port, initialPort):
        self.serial_port.flushInput()
        if status == 1:
            self.rotate_erv_right(50)
            root.after(50, self.erv_specific_port(2, port, initialPort))
        elif status == 2:
            x = self.motor1.send(15, 6, self.motor1.motor_id, 0)
            if x.value == 1:
                root.after(50, self.erv_specific_port(2, port, initialPort))
            else:
                initialPort += 1
                if initialPort == port:
                    self.stop_erv()
                else:
                    self.erv_specific_port(3, port, initialPort)
        elif status == 3:
            y = self.motor1.send(15, 6, self.motor1.motor_id, 0)
            if y.value == 1:
                root.after(50, self.erv_specific_port(1, port, initialPort))
            else:
                self.rotate_erv_right(10)
                root.after(50, self.erv_specific_port(4, port, initialPort))
        elif status == 4:
            z = self.motor1.send(15, 6, self.motor1.motor_id, 0)
            if z.value == 1:
                self.stop_erv()
                root.after(50, self.erv_specific_port(1, port, initialPort))
            else:
                root.after(50, self.erv_specific_port(4, port, initialPort))
        else:
            pass

    ############################################################################
    ############################################################################

root = Tkinter.Tk()
app = App(root)
root.mainloop()
