import logging
import os, sys, csv, random
from PyQt5 import QtWidgets, QtGui, QtCore, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout,QMessageBox, QPushButton, QLineEdit
from PyQt5.QtGui import QPixmap, QImage, QIntValidator, QDoubleValidator, QIcon, QFont
from PyQt5.QtCore import Qt, QTimer, QSize, QEvent
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from datetime import datetime
import serial.tools.list_ports
from logging.handlers import RotatingFileHandler
import serial 
import time
from ResponsiveVirtualKeyboard import ResponsiveVirtualKeyboard
from PIL import Image, ImageOps
import cv2
import json
import numpy as np
base_path = "."


# To run this app in PC environment without building exe, comment the lines below  
# base_path = sys._MEIPASS
# To build this code make sure all paths have "/" to change directory.



class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(f'{base_path}/ui_epm.ui', self)
        log_file = "application.log"

        # Ensure the log file exists (create it if it doesn’t)
        if not os.path.exists(log_file):
            with open(log_file, "w"):  # Create an empty log file
                pass

        # Configure rotating log file (max 500 KB, keep last 5 log files)
        log_handler = RotatingFileHandler(
            "application.log", maxBytes=500000, backupCount=5
        )
        log_handler.setFormatter(logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        ))

        # Set up logging
        logging.basicConfig(
            handlers=[log_handler],
            level=logging.INFO
        )
        
        # Check if file exists
        print(f"Log file exists: {os.path.exists(log_file)}")
        logging.info("Application started successfully.")
        print("Logging get started.")
        
        self.graph_data_filename = os.path.join(os.path.expanduser("~"), "Documents", "graph_data.csv")
        self.keyboard = None
        # self.keyboard_enabled = False
        
        # self.load_settings()
        
        self.init_screen_1()
        
        self.remaining_time = None
        self.button_A.setIcon(QIcon(base_path+"/rsc/rsc3.png"))
        self.button_A.setIconSize(QSize(40, 40))
        font_52 = QFont('SF Pro Display', 52, QFont.Bold)
        font_27 = QFont('SF Pro Display', 27, QFont.Bold)
        font_19 = QFont('SF Pro Display', 19, QFont.Bold)
        font_12 = QFont('SF Pro Display', 12, QFont.Bold)
        
        # Create a font object
        font = QFont('SF Pro Display', 18, QFont.Bold)

        # Apply the font to button_7 and button_9
        self.button_7.setFont(font)
        self.button_8.setFont(font)
        self.button_9.setFont(font)
        self.show_password = False

        # Initialize password field
        self.input_2.setEchoMode(QLineEdit.Password)

        # Add toggle button next to password field
       #self.button_HS = QPushButton(self)
        #self.button_HS.setIcon(QIcon("C:\Projects\EPM_Code\icons\eye-slash-regular.svg"))  # Add your eye icon
        #self.button_HS.setGeometry(self.input_2.geometry().adjusted(200, 0, 250, 0))  # Adjust position as needed
        #self.button_HS.clicked.connect(self.toggle_password_visibility)
        


        self.mode = "READY"
        self.screen = 0
        self.int_validator = QIntValidator(self)
        self.process_config = []
        # self.time_data = []
        # self.force_data = []
        self.rx_temperature = 0
        # self.rx_force = 0
        # self.time_data = []
        # self.voltage_data = []
        # self.current_data = []
        self.rx_current = 1
        self.rx_voltage = 1
        # self.ser = None
        #self.ser = serial.Serial(port='COM5', baudrate=9600, timeout = 1000)
        self.heater=False
        self.motor_forward = False
        self.motor_reverse = False
        # self.camera = cv2.VideoCapture(0)
        self.timer = QTimer()
        # self.timer.timeout.connect(self.display_cam)
        self.timer2 = QTimer()
        
        self.last_command = None  # Or an empty string

        self.ser = None
        self.ser_2 = None
        # Other initializations
        self.remaining_time = None
        
        # Initialize empty data lists for plotting
        self.time_data = []
        self.voltage_data = []
        self.current_data = []

        # Initialize the time tracker `self.t`
        self.t = 0

        self.button_HS.clicked.connect(self.toggle_password_visibility)
        self.button_1.clicked.connect(self.handle_verify_login)
        self.button_A.pressed.connect(self.handle_button_A_pressed)
        self.button_A.clicked.connect(self.handle_back_pressed)
        self.button_2.clicked.connect(lambda: self.handle_screen_change(4))
        self.button_3.clicked.connect(lambda: self.handle_screen_change(3))
        self.button_4.clicked.connect(self.handle_create_config)
        self.button_5.clicked.connect(lambda: self.handle_screen_change(5))
        self.button_6.clicked.connect(self.populate_configlist)
        self.button_7.clicked.connect(self.start_process)
        self.button_8.clicked.connect(self.pause_process)
        self.button_9.clicked.connect(self.reset_process)
        
        # Make buttons checkable
        self.button_7.setCheckable(True)
        self.button_8.setCheckable(True)
        self.button_9.setCheckable(True)
        
        self.button_8.setDisabled(True)
        
        self.button_10.clicked.connect(self.handle_delete_configuration)
        self.button_11.clicked.connect(self.handle_delete)
        self.button_12.clicked.connect(self.handle_manual)
        self.button_28.pressed.connect(self.motor_forward_pressed)
       # self.button_13.pressed.connect(self.motor_forward_pressed) # Actuate Forward
        # self.button_13.released.connect(self.motor_forward_released) # Actuate Forward
        #self.button_14.clicked.connect(self.motor_reverse_pressed)  # Actuate Reverse
        self.button_26.clicked.connect(self.motor_reverse_pressed)
        # self.button_14.released.connect(self.motor_reverse_released)  # Actuate Reverse
        #self.button_15.clicked.connect(self.handle_heater)  # heater on/off
        self.button_27.clicked.connect(self.handle_heater)
        # self.button_16.clicked.connect(lambda: self.handle_screen_change(7))
        # self.button_17.clicked.connect(self.settings)
        #self.button_16.pressed.connect(self.valve_1_pressed)  # valve 1
        #self.button_16.released.connect(self.valve_1_released)  # valve 1
        #self.button_17.pressed.connect(self.valve_2_pressed)  # valve 1
        #self.button_17.released.connect(self.valve_2_released)  # valve 1
        self.configlist.itemClicked.connect(self.load_config)
        #self.input_4.setValidator(self.int_validator)
        #self.input_5.setValidator(self.int_validator)
        self.input_6.setValidator(self.int_validator)
        self.input_7.setValidator(self.int_validator)
        self.input_8.setValidator(self.int_validator)
        self.input_12.setValidator(self.int_validator)
        self.input_13.setValidator(self.int_validator)
        self.input_14.setValidator(self.int_validator)

        # self.showPopup2 = self.comboBox.showPopup 
        # self.comboBox.showPopup= self.load_comlist
        self.remaining_time_seconds = 0
        self.temperature_value = 0
        
        self.temperature_message_shown = False

        self.ser = None
        self.ser_2 = None
        self.initialize_ports()
        
        self.BackBtnPressedState = False




    def initialize_ports(self):
        # Initialize serial ports based on previously selected values or defaults
        self.load_comlist()
        self.load_comlist_2()

        # Connect signals for comboBox_2
        self.comboBox.currentIndexChanged.connect(self.set_serial)
        self.comboBox_2.currentIndexChanged.connect(self.handle_comboBox_2_change)
        
        
        # self.handle_screen_change(1)


    # # virtual keboard
    # def show_virtual_keyboard(self, input_field, event=None):
    #     # Check if the keyboard exists and is visible before proceeding
    #     if self.keyboard is None or not self.keyboard.isVisible():
    #         # If no keyboard is open, create a new one
    #         self.keyboard = VirtualKeyboard(input_field, self)
    #         self.keyboard.finished.connect(self.on_keyboard_closed)  # Reset the flag when the keyboard closes
    #         self.keyboard.show()
    #     else:
    #         # If a keyboard is already open, change the focused input field
    #         self.keyboard.input_field = input_field

    # def handle_focus_event(self, event):
    #     # Ensure that the keyboard opens only for the clicked input field
    #     self.show_virtual_keyboard(self.sender(), event)
    #     QLineEdit.focusInEvent(self.sender(), event)  # Call the original focus event

    # def on_keyboard_closed(self):
    #     # Safely reset the keyboard reference when it's closed
    #     self.keyboard = None
    
    def show_virtual_keyboard(self, input_field):
        """ Show the virtual keyboard when a QLineEdit is focused. """
        logging.debug("show_virtual_keyboard called with input field: %s", input_field.objectName())
        if self.keyboard is None or not self.keyboard.isVisible():
            logging.info("Creating a new virtual keyboard.")
            # If no keyboard is open, create a new one
            self.keyboard =ResponsiveVirtualKeyboard(input_field, self)
            # self.keyboard.finished.connect(self.on_keyboard_closed)  # Reset flag when closed
            self.keyboard.show()
        # else:
        #     # If keyboard exists but is hidden, bring it to the front
        #     logging.info("Bringing existing keyboard to the front.")
        #     self.keyboard.raise_()
        #     self.keyboard.activateWindow()
        #     self.keyboard.show()
    
        # Change focus to the currently clicked input field
        self.keyboard.input_field = input_field
        logging.info("Virtual keyboard shown successfully.")

    # def eventFilter(self, obj, event):
    #     """ Event filter to capture focus events on input fields. """
    #     if event.type() == QEvent.FocusIn and isinstance(obj, QLineEdit):
    #         logging.debug("Focus event detected on input field: %s", obj.objectName())
    #         self.show_virtual_keyboard(obj)  # Open keyboard when the QLineEdit gets focus
    #     return super().eventFilter(obj, event)
    def eventFilter(self, obj, event):
        """ Event filter to capture focus events on input fields. """
        if isinstance(obj, QLineEdit):  
            if event.type() == QEvent.FocusIn:
                logging.debug(f"Focus event detected on QLineEdit: {obj.objectName()}")
                # self.show_virtual_keyboard(obj)  # Open keyboard when the QLineEdit gets focus
                if self.keyboard is None or not self.keyboard.isVisible():
                    self.keyboard = ResponsiveVirtualKeyboard(obj, self)
                    self.keyboard.show()
                else:
                    self.keyboard.close()
                    self.keyboard = None
            return super().eventFilter(obj, event)
    
    # def on_keyboard_closed(self):
    #     # Safely reset the keyboard reference when it's closed
    #     logging.info("Virtual keyboard closed.")
    #     self.keyboard = None

    def handle_screen_change(self, value):
        logging.debug("handle screen change called with value: %d", value)
        # Close the virtual keyboard if it is open when changing screens
        if self.keyboard is not None and self.keyboard.isVisible():
            logging.info("Closing virtual keyboard due to screen change.")
            self.keyboard.close_keyboard()

        for widget in self.findChildren(QtWidgets.QPushButton):
            widget.setFocusPolicy(Qt.NoFocus)

        if value == 1:  # Login Screen
            self.screen = 1
            self.comboBox.hide()
            # self.comboBox.setDisabled(True)
            self.comboBox_2.hide()
            # self.comboBox_2.setDisabled(True)
            self.button_A.hide()
            self.button_HS.show()
            self.init_screen_1()

        elif value == 2:  # Menu Screen
            self.screen = 2
            self.comboBox.hide()
            self.comboBox_2.hide()
            self.button_A.show()
            self.init_screen_2()

        elif value == 3:  # Create Config Screen
            self.screen = 3
            self.comboBox.hide()
            self.comboBox_2.hide()
            self.init_screen_3()

        elif value == 4:  # Load Config Screen
            self.screen = 4
            self.comboBox.hide()
            self.comboBox_2.hide()
            self.init_screen_4(delete=False)

        elif value == 5:  # Process Screen
            self.screen = 5
            self.comboBox.show()
            self.comboBox.setDisabled(False)
            self.comboBox_2.show()
            self.comboBox_2.setDisabled(False)
            self.init_screen_5()

        elif value == 6:  # Manual Screen
            self.screen = 6
            self.comboBox.hide()  # Hide supply COM selection
            self.comboBox_2.show()
            self.comboBox_2.setDisabled(False)
            self.init_screen_6()

        # elif value == 7:  # Settings Screen
        #     self.screen = 7
        #     self.comboBox_2.show()
        #     self.comboBox.setDisabled(False)
        #     self.init_screen_7()

    def close_keyboard(self):
        logging.info("Attempting to close virtual keyboard.")
        try:
                if self.keyboard is not None:
                    self.keyboard.close_keyboard()
                    self.keyboard = None
                    self.keyboard_closed_manually = True  # Prevent reopening
                    logging.info("Virtual keyboard closed successfully.")
                else:
                    logging.debug("No virtual keyboard to close.")
        except Exception as e:
                logging.error(f"Error closing virtual keyboard: {e}")
               
    def handle_button_A_pressed(self):
        logging.debug("Button A pressed.")
        self.button_A.setIconSize(QSize(36, 36))

    def init_screen_1(self):
        logging.info("Initializing  Login Screen 1.")
        self.screen = 1
        self.screen_2.hide()
        self.screen_3.hide()
        self.screen_4.hide()
        self.screen_5.hide()
        self.screen_6.hide()
        # self.screen_7.hide()
        self.screen_1.show()
        self.setStyleSheet("background-color:white;")
        self.label_A.setPixmap(QPixmap(base_path+"/rsc/rsc2.png"))
        self.label_6.setStyleSheet("color:white;")
        self.label_6.setStyleSheet("background-color: white;")
        self.label_6.hide()
        self.label_10.hide()
        self.label_11.hide()
        self.label_12.hide()
        self.button_A.hide()
        self.button_HS.show()
        self.comboBox.hide()

        self.input_1.installEventFilter(self)
        self.input_2.installEventFilter(self)
  
    def init_screen_2(self):
        logging.info("Initializing Menu Screen 2.")
        if (self.mode == "operator"):
            logging.debug("Mode: Operator")
            self.screen = 2
            self.setStyleSheet("background-color:white;")
            self.label_A.setPixmap(QPixmap())
            self.label_A.setText("Main Menu")
            self.button_3.hide()
            self.button_10.hide()
            self.screen_1.hide()
            self.screen_3.hide()
            self.screen_4.hide()
            self.screen_5.hide()
            self.screen_6.hide()
            # self.screen_7.hide()
            self.screen_2.show()
            self.label_10.hide()
            self.label_11.hide()
        elif (self.mode == "admin"):  
            logging.debug("Mode: Admin")
            self.screen = 2
            self.setStyleSheet("background-color:white;")
            self.label_A.setPixmap(QPixmap())
            self.label_A.setText("Main Menu")
            self.button_3.show()
            self.button_10.show()
            self.screen_1.hide()
            self.screen_3.hide()
            self.screen_4.hide()
            self.screen_5.hide()
            self.screen_6.hide()
            # self.screen_7.hide()
            self.screen_2.show()
            self.label_10.hide()
            self.label_11.hide()
          
    def init_screen_3(self):
        logging.info("Initializing Create configuration Screen 3.")
        self.screen = 3
        self.label_A.setText("Create Configuration")
        self.screen_1.hide()
        self.screen_2.hide()
        self.screen_4.hide()
        self.screen_5.hide()
        self.screen_6.hide()
        # self.screen_7.hide()
        self.screen_3.show()
        self.setStyleSheet("background-color:white;")
        self.label_23.setStyleSheet("color:white;")
        self.label_23.setText("")
        self.input_3.clear()
        #self.input_4.clear()
        #self.input_5.clear()
        self.input_6.clear()
        self.input_7.clear()
        self.label_10.hide()
        self.label_11.hide()
        
        self.input_3.installEventFilter(self)
        self.input_6.installEventFilter(self)
        self.input_7.installEventFilter(self)
        self.input_8.installEventFilter(self)
        self.input_12.installEventFilter(self)
        self.input_13.installEventFilter(self)
        self.input_14.installEventFilter(self)     

    def init_screen_4(self,delete):
       
        self.screen = 4
        if(delete):
            logging.info("Initializing Screen 4. Delete Mode: %s", delete)
            self.label_A.setText("Delete Configuration")
            self.button_5.hide()
            #self.button_12.hide()
            self.button_11.show()
            self.button_11.setEnabled(False)
        else:
            logging.info("Initializing Screen 4. Load Configuration: %s")
            self.label_A.setText("Load Configuration")
            self.button_5.setEnabled(False)
            self.button_11.hide()
            #self.button_12.show()
            self.button_5.show()

        self.screen_1.hide()
        self.screen_2.hide()
        self.screen_3.hide()
        self.screen_5.hide()
        self.screen_6.hide()
        # self.screen_7.hide()
        self.screen_4.show()
        self.setStyleSheet("background-color:white;")
        self.configlist.hide()
        self.label_29.setText("")
        #self.label_30.setText("")
        #self.label_31.setText("")
        self.label_32.setText("")
        self.label_33.setText("")
        self.label_42.setText("")
        self.label_10.hide()
        self.label_11.hide()
        
        
    def init_screen_5(self):
        logging.info("Initializing Process Screen 5.")
        self.screen = 5
        self.label_A.setText("Process Mode")
        self.screen_1.hide()
        self.screen_2.hide()
        self.screen_3.hide()
        self.screen_4.hide()
        self.screen_6.hide()
        # self.screen_7.hide()
        self.screen_5.show()
        self.setStyleSheet("background-color:white;")
        self.input_6.setText(self.label_32.text())
        self.input_7.setText(self.label_33.text())
        self.input_8.setText(self.label_42.text())
        self.label_10.show()
        self.label_11.show()
        self.label_20.setText("Ready")
        self.label_20.setStyleSheet("color:rgb(0,0,0); background-color:transparent;")
       
        # self.load_comlist()
        # self.comboBox.currentIndexChanged.connect(self.set_serial)
        self.timer2.setInterval(100)  # Set interval to 1 second for rx_data
        self.timer2.timeout.connect(self.rx_data)
        self.timer2.start()


    def init_screen_6(self):
        logging.info("Initializing Service Mode Screen 6.")
        self.screen = 6
        self.label_A.setText("Service Mode")
        self.screen_1.hide()
        self.screen_2.hide()
        self.screen_3.hide()
        self.screen_4.hide()
        self.screen_5.hide()
        # self.screen_7.hide()
        self.screen_6.show()
        self.comboBox_2.show()
        self.comboBox_2.setDisabled(False)
        self.label_10.hide()
        self.label_11.show()
        self.button_28.setStyleSheet("background-color:transparent;")
        self.button_28.setIcon(QIcon(base_path+"/rsc/Forward.png"))
        self.button_28.setIconSize(QSize(100, 100)) 
        self.button_26.setStyleSheet("background-color:transparent;")
        self.button_26.setIcon(QIcon(base_path+"/rsc/reverse.png"))
        self.button_26.setIconSize(QSize(100, 100)) 
        self.button_27.setStyleSheet("background-color:transparent;")
        self.button_27.setIcon(QIcon(base_path+"/rsc/cttm_heater.png"))
        self.button_27.setIconSize(QSize(100, 100)) 
        # self.load_comlist_2()
        
        self.setStyleSheet("background-color:white;")
        print("Screen 6 - Manual Operation")
        
        self.timer2.setInterval(100)  # Set interval to 100 milisecond for rx_data
        self.timer2.timeout.connect(self.rx_data)
        self.timer2.start()


    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Confirm Exit', 
                                    "Are you sure you want to exit?", 
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            try:
                logging.info("User confirmed exit.")
                # Unconditionally send the command to turn off the power supply
                self.tx_data("OUTP:GEN OFF *IDN\n")
                logging.info("Power supply turned off before closing GUI.")
                print("Power supply turned off before closing GUI")

                # Send the command to the MCU to stop the process
                self.tx_data("*1:0:0#", port='mcu')  # Send stop command to MCU
                logging.info("Stop protocol *1:0:0# sent to MCU.")
                print("Stop protocol *1:0:0# sent to MCU")
                
                # Close serial ports and reset combo boxes
                self.close_serial_ports()  # Close serial ports when navigating away from screens 5, 6, or 7
                self.comboBox.setCurrentIndex(0)  # Clear the comboBox
                self.comboBox_2.setCurrentIndex(0)  # Clear the comboBox_2
                logging.info("Serial ports closed and combo boxes reset.")
                
                # Check if the virtual keyboard is open and close it
                if self.keyboard is not None and self.keyboard.isVisible():
                    self.close_keyboard()
                    logging.info("Virtual keyboard closed.")
                    event.accept()
                    print("Virtual keyboard closed")
                                
                if hasattr(self, 'countdown_timer') and self.countdown_timer.isActive():
                    self.countdown_timer.stop()  # Stop the countdown timer
                    logging.info("Countdown timer stopped.")
                self.remaining_time_seconds = 0  # Reset the remaining time
                self.label_45.setText("00 : 00")  # Reset the label to 00:00
                logging.info("Process stopped and timer reset.")
                print("Process stopped and timer reset.")
                
                # # Close serial ports and reset combo boxes
                # self.close_serial_ports()  # Close serial ports when navigating away from screens 5, 6, or 7
                # self.comboBox.setCurrentIndex(0)  # Clear the comboBox
                # self.comboBox_2.setCurrentIndex(0)  # Clear the comboBox_2
                
            except Exception as e:
                print(f"Error turning off power supply or sending stop command to MCU: {e}")
                logging.error(f"Error in closeEvent: {e}", exc_info=True)
            finally:
                logging.info("Closing application.")
                logging.shutdown()  # Ensure logs are written
                event.accept()  # Proceed with closing the window
        else:
            logging.info("User canceled exit.")
            event.ignore()  # Ignore the close event and keep the window open




    def populate_configlist(self):
        if self.configlist.isVisible():
            logging.info("Config list hidden.")
            self.configlist.hide()
        else:
            self.configlist.show()
            self.configlist.clear()
            logging.info("Config list displayed and cleared.")
            if os.path.exists('ConfigFile.csv'):
                logging.info("Loading configurations from ConfigFile.csv.")
                with open('ConfigFile.csv', 'r') as file:
                    reader = csv.reader(file)
                    next(reader, None) 
                    for row in reader:
                        if row: 
                            self.configlist.addItem(row[0])  
                logging.info("Config list populated successfully.")
            list_height = (self.configlist.count()*42) + 2
            # if(list_height>350): list_height = 350
            # self.configlist.setFixedHeight(list_height)
            logging.shutdown()  # Ensure logs are saved immediately

    # def load_config(self):
    #     selected_items_list = self.configlist.selectedItems()
    #     if selected_items_list:
    #         selected_item = selected_items_list[0].text()
    #         print(f"Selected item text: {selected_item}")

    #         if os.path.exists('ConfigFile.csv'):
    #             with open('ConfigFile.csv', 'r') as file:
    #                 reader = csv.reader(file)
    #                 next(reader, None)
    #                 for row in reader:
    #                     if row[0] == selected_item:
    #                         self.process_config = row
    #                         break
    #         print("Process Config:", self.process_config)
    #         self.label_29.setText(self.process_config[0])
    #         self.label_65.setText(self.process_config[0])
    #         #self.label_30.setText(self.process_config[1])
    #         #self.label_31.setText(self.process_config[2])
    #         self.label_32.setText(self.process_config[1])
    #         self.label_67.setText(self.process_config[1])
    #         self.label_33.setText(self.process_config[2])
    #         self.label_70.setText(self.process_config[2])
    #         self.label_42.setText(self.process_config[3])
    #         self.label_72.setText(self.process_config[3])
    #         self.button_5.setEnabled(True)
    #         self.button_11.setEnabled(True)
    

    def load_config(self):
        selected_items_list = self.configlist.selectedItems()
        logging.info("Attempting to load configuration.")

        if not selected_items_list:  # If no item is selected
            logging.error("No configuration selected. Displaying warning message.")
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Configuration Selection")
            msg.setText("Select a configuration to Start a process.")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            return  # Stop further execution

        selected_item = selected_items_list[0].text()
        logging.info(f"Selected configuration: {selected_item}")
        print(f"Selected item text: {selected_item}")

        if os.path.exists('ConfigFile.csv'):
            with open('ConfigFile.csv', 'r') as file:
                reader = csv.reader(file)
                next(reader, None)  # Skip header row
                for row in reader:
                    if row[0] == selected_item:
                        self.process_config = row
                        break
            logging.debug(f"Loaded configuration: {self.process_config}")
            
        print("Process Config:", self.process_config)

        # Updating labels with configuration values
        self.label_29.setText(self.process_config[0])
        self.label_65.setText(self.process_config[0])
        self.label_32.setText(self.process_config[1])
        self.label_67.setText(self.process_config[1])
        self.label_33.setText(self.process_config[2])
        self.label_70.setText(self.process_config[2])
        self.label_42.setText(self.process_config[3])
        self.label_72.setText(self.process_config[3])
        self.label_61.setText(self.process_config[4])
        self.label_81.setText(self.process_config[4])
        self.label_77.setText(self.process_config[5])
        self.label_84.setText(self.process_config[5])
        self.label_79.setText(self.process_config[6])
        self.label_87.setText(self.process_config[6])
        logging.info("Configuration labels updated successfully.")

        # Enable buttons after loading configuration
        self.button_5.setEnabled(True)
        self.button_11.setEnabled(True)
        logging.info("Start and Process buttons enabled.")
        
        try:
            # Retrieve current values from input fields
            current_temperature = self.process_config[5]
            current_distance = self.process_config[6]
            current_speed = self.process_config[4]
            logging.debug(f"Retrieved values - Temperature: {current_temperature}, Distance: {current_distance}, Speed: {current_speed}")

            # Check if any field is empty
            if not current_temperature or not current_distance or not current_speed:
                logging.error("One or more fields are empty. Prompting user to fill all fields.")
                QMessageBox.warning(self, "Incomplete Settings", "Fill all the fields to submit the settings!")
                return

            # Define protocols
            protocol_temperature = f"*3:1:{current_temperature}#"
            protocol_distance = f"*3:2:{current_distance}#"
            protocol_speed = f"*3:3:{current_speed}#"
            protocol_save = "*3:4:1#"

            # Function to send data and log feedback
            def send_and_log(protocol):
                try:
                    logging.info(f"Sending protocol to MCU: {protocol}")
                    print(f"Sending protocol to MCU: {protocol}")
                    self.tx_data(protocol, port='mcu')
                    time.sleep(1)  # Consider replacing this with a QTimer
                    mcu_feedback = self.rx_data()

                    if mcu_feedback is None:
                        logging.debug(f"Received feedback from MCU: {mcu_feedback}")
                        raise ValueError("No response from MCU.")

                    print(f"Received feedback from MCU: {mcu_feedback}")
                    return mcu_feedback
                except Exception as e:
                    print(f"Error communicating with MCU: {e}")
                    logging.error(f"Error communicating with MCU: {e}")
                    return None

            # Send temperature, distance, and speed settings
            if not send_and_log(protocol_temperature):
                QMessageBox.critical(self, "Error", "Failed to update temperature settings!")
                return

            if not send_and_log(protocol_distance):
                QMessageBox.critical(self, "Error", "Failed to update distance settings!")
                return

            if not send_and_log(protocol_speed):
                QMessageBox.critical(self, "Error", "Failed to update speed settings!")
                return

            # Send the save protocol
            self.tx_data(protocol_save, port='mcu')
            logging.info("Sent save protocol to MCU. Waiting for response...")

            # Wait for "*SET:SAV#" within 10 seconds
            received_correct_feedback = False
            
            for _ in range(100):  # Loop for 10 seconds
                # time.sleep(1)  # Wait 1 second before checking again
                feedback = self.rx_data()
                # logging.debug(f"Checking feedback: {feedback}")
                print(f"Checking feedback: {feedback}")

                if feedback == "*SET:SAV#":
                    received_correct_feedback = True
                    logging.info("Settings successfully saved to MCU.")
                    break  # Exit loop early if we get the correct response

            if received_correct_feedback:
                logging.info("")
            else:
                logging.error("No response from MCU! Settings not saved.")
                QMessageBox.critical(self, "Error", "No response from MCU! Settings not saved.")

        except Exception as e:
            logging.critical(f"Error occurred during settings update: {e}", exc_info=True)
            print(f"Error occurred during settings update: {e}")
            QMessageBox.critical(self, "Critical Error", "An unexpected error occurred!")  
        self.label_61.clear()
        self.label_77.clear()
        self.label_79.clear() 

    def toggle_password_visibility(self):
        logging.debug("Toggling password visibility.")
        if self.show_password:
            self.input_2.setEchoMode(QLineEdit.Password)
            self.button_HS.setIcon(QIcon("C:\Projects\EPM_Code\icons\eye-slash-regular.svg"))  # Eye icon for hiding password
            logging.info("Password hidden.")
        else:
            self.input_2.setEchoMode(QLineEdit.Normal)
            self.button_HS.setIcon(QIcon("C:\Projects\EPM_Code\icons\eye-regular.svg"))  # Closed eye icon for showing password
            logging.info("Password visible.")
        self.show_password = not self.show_password        
    
    def handle_verify_login(self):
        logging.info("User attempted to verify login.")
        if(self.input_1.text() == "admin" and self.input_2.text() == "admin"):
            self.mode = "admin"
            self.handle_screen_change(2)
            logging.info("Admin login successful.")
        elif(self.input_1.text() == "" and self.input_2.text() == ""):
            self.label_6.setText("Please enter credentials.")
            self.label_6.show()
            self.label_6.setStyleSheet("background-color: white; color:rgb(255,0,0);")
            logging.error("Login failed: Please enter credentials.")
        elif(self.input_1.text() == "operator" and self.input_2.text() == "123"):
            self.mode = "operator"
            self.handle_screen_change(2)
            logging.info("Operator login successful.")
        else:
            self.label_6.setText("Invalid Credentials.")
            self.label_6.show()
            self.label_6.setStyleSheet("background-color: white; color:rgb(255,0,0);")
            logging.error("Login failed: Invalid credentials.")
            
            

   
    # def handle_create_config(self):
    #     # Retrieve text from inputs
    #     input_7_value = self.input_7.text()
    #     input_8_value = self.input_8.text()
    #     input_3_value = self.input_3.text()
    #     input_6_value = self.input_6.text()

    #     # Check if any field is empty
    #     if not input_3_value or not input_6_value or not input_7_value or not input_8_value:
    #         # Show a dialog box to inform the user
    #         dialog = QMessageBox(self)
    #         dialog.setIcon(QMessageBox.Warning)
    #         dialog.setWindowTitle("Incomplete Fields")
    #         dialog.setText("All the feilds must be filled to create configuration.")
    #         dialog.setStandardButtons(QMessageBox.Ok)
    #         dialog.exec_()
    #         return

    #     # Check if the input values are numeric and within the specified limits
    #     try:
    #         input_7_number = float(input_7_value)
    #         input_8_number = float(input_8_value)

    #         # Check if the value of input_7 is greater than 32
    #         if input_7_number > 32:
    #             self.label_23.setText("Error: Value of Voltage cannot exceed 32")
    #             self.label_23.setStyleSheet("color:#FF0000;")
    #             return
    #         # Check if the value of input_8 is greater than 10
    #         elif input_8_number > 10:
    #             self.label_23.setText("Error: Value of Current cannot exceed 10")
    #             self.label_23.setStyleSheet("color:#FF0000;")
    #             return

    #         # If both conditions are met, proceed with configuration creation
    #         data = [
    #             input_3_value,
    #             input_6_value,
    #             input_7_value,
    #             input_8_value
    #         ]

    #         # Further code to handle the creation of the configuration
    #         self.label_23.setText("Configuration created successfully!")
    #         self.label_23.setStyleSheet("color:#009900;")
        
    #     except ValueError:
    #         # Handle the case where the input values are not numeric
    #         self.label_23.setText("Error: Invalid input. Please enter numeric values.")
    #         self.label_23.setStyleSheet("color:#FF0000;")
    #         return

    #     # Check for existing configuration
    #     file_exists = os.path.exists('ConfigFile.csv')

    #     if file_exists:
    #         with open('ConfigFile.csv', 'r') as file:
    #             reader = csv.reader(file)
    #             next(reader, None)
    #             for row in reader:
    #                 if input_3_value == row[0]:  # Check if input_3 text exists in the first column
    #                     self.label_23.setText("Error: Configuration Name already exists")
    #                     self.label_23.setStyleSheet("color:#FF0000;")
    #                     return

    #     with open('ConfigFile.csv', 'a', newline='') as file:
    #         writer = csv.writer(file)
    #         if not file_exists:
    #             writer.writerow(['ConfigName', 'Linear Speed', 'Distance', 'Temperature', 'Voltage', 'Current'])  # Replace with appropriate header names
    #         writer.writerow(data)
    #         self.label_23.setText("Configuration has been saved successfully!")
    #         self.label_23.setStyleSheet("color:#009900;")
    
    def setup_validators(self):
        # Setting up validators for numeric input (0-9 only) for the respective input fields
        logging.info("Setting up input validators for numeric fields.")
        int_validator = QIntValidator(0, 9, self)
        self.input_6.setValidator(int_validator)  # Only allows digits (0-9)
        self.input_7.setValidator(int_validator)  # Only allows digits (0-9)
        self.input_8.setValidator(int_validator)  # Only allows digits (0-9)
        self.input_12.setValidator(int_validator)  # Only allows digits (0-9)
        self.input_13.setValidator(int_validator)  # Only allows digits (0-9)
        self.input_14.setValidator(int_validator)  # Only allows digits (0-9)
        logging.debug("Validators applied to input fields: Time, Voltage, Current, Distance, Speed, Temperature")
        
        
    def handle_create_config(self):
        # Retrieve text from inputs
        logging.info("Initiating configuration creation process.")
        input_7_value = self.input_7.text()
        input_8_value = self.input_8.text()
        input_3_value = self.input_3.text()
        input_6_value = self.input_6.text()
        input_12_value = self.input_12.text()
        input_13_value = self.input_13.text()
        input_14_value = self.input_14.text()
        logging.debug(f"Collected input values - Config Name: {input_3_value}, Time: {input_6_value}, "
                  f"Voltage: {input_7_value}, Current: {input_8_value}, "
                  f"Distance: {input_12_value}, Speed: {input_13_value}, Temperature: {input_14_value}")


        # Check if any field is empty
        if not input_3_value or not input_6_value or not input_7_value or not input_8_value:
            logging.error("Some required fields are empty. Prompting user to complete the form.")
            # Show a dialog box to inform the user
            dialog = QMessageBox(self)
            dialog.setIcon(QMessageBox.Warning)
            dialog.setWindowTitle("Incomplete Fields")
            dialog.setText("All the fields must be filled to create configuration.")
            dialog.setStandardButtons(QMessageBox.Ok)
            dialog.exec_()
            return

        # Ensure inputs are strictly numeric due to validators
        try:
            input_7_number = int(input_7_value)  # Convert to integer
            input_8_number = int(input_8_value)  # Convert to integer
            input_12_number = int(input_12_value)
            input_13_number = int(input_13_value)
            input_14_number = int(input_14_value)
            

            # Check if the value of input_6 is within 1-2000
            # if int(self.input_6.text()) < 1 or int(self.input_6.text()) > 2000:
            #     logging.error("Time value is out of range (1-2000).")
            #     self.label_23.setText("Error: Value of Time is out of range.")
            #     self.label_23.setStyleSheet("color:#FF0000;")
            #     return
            # # Check if the value of input_7 is within 1-32
            # if int(self.input_7.text()) < 1 or int(self.input_7.text()) > 32:
            #     logging.error("Voltage value is out of range (1-32).")
            #     self.label_23.setText("Error: Value of Voltage is out of range.")
            #     self.label_23.setStyleSheet("color:#FF0000;")
            #     return
            # # Check if the value of input_8 is within 1-10
            # elif int(self.input_8.text()) < 1 or int(self.input_8.text()) > 10:
            #     logging.error("Current value is out of range (1-10).")
            #     self.label_23.setText("Error: Value of Current is out of range.")
            #     self.label_23.setStyleSheet("color:#FF0000;")
            #     return
            # # Check if the value of input_12 is within 1-12
            # elif int(self.input_12.text()) < 1 or int(self.input_12.text()) > 20:
            #     logging.error("Distance value is out of range (1-20).")
            #     self.label_23.setText("Error: Value of Distance is out of range.")
            #     self.label_23.setStyleSheet("color:#FF0000;")
            #     return
            # # Check if the value of input_14 is within 60-80
            # elif int(self.input_14.text()) < 1 or int(self.input_14.text()) > 80:
            #     logging.error("Temperature value is out of range (1-80).")
            #     self.label_23.setText("Error: Value of Temperature is out of range.")
            #     self.label_23.setStyleSheet("color:#FF0000;")
            #     return
            # # Check if the value of input_13 is within 1-15
            # elif int(self.input_13.text()) < 1 or int(self.input_13.text()) > 100:
            #     logging.error("Speed value is out of range (1-100).")
            #     self.label_23.setText("Error: Value of Speed is out of range.")
            #     self.label_23.setStyleSheet("color:#FF0000;")
                # return

            # If both conditions are met, proceed with configuration creation
            data = [
                input_3_value,
                input_6_value,
                input_7_value,
                input_8_value,
                input_12_value,
                input_13_value,
                input_14_value
            ]

            # Further code to handle the creation of the configuration
            logging.info("All input values are valid. Proceeding with configuration creation.")
            self.label_23.setText("Configuration created successfully!")
            self.label_23.setStyleSheet("color:#009900;")
        
        except ValueError:
            # Handle the case where the input values are not numeric
            logging.error("Invalid numeric input detected. Prompting user to enter valid numbers.")
            dialog = QMessageBox(self)
            dialog.setIcon(QMessageBox.Warning)
            dialog.setWindowTitle("Invalid Input")
            dialog.setText("Invalid values! Please enter numeric values.")
            dialog.setStandardButtons(QMessageBox.Ok)
            dialog.exec_()
            return

        # Check for existing configuration
        file_exists = os.path.exists('ConfigFile.csv')

        if file_exists:
            with open('ConfigFile.csv', 'r') as file:
                reader = csv.reader(file)
                next(reader, None)
                for row in reader:
                    if input_3_value == row[0]:  # Check if input_3 text exists in the first column
                        logging.error(f"Configuration name '{input_3_value}' already exists. Aborting creation.")
                        self.label_23.setText("Error: Configuration Name already exists")
                        self.label_23.setStyleSheet("color:#FF0000;")
                        return

        with open('ConfigFile.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(['ConfigName', 'Time', 'Voltage', 'Current', 'Distance','Speed','Temperature'])  # Replace with appropriate header names
            writer.writerow(data)
            logging.info(f"Configuration '{input_3_value}' saved successfully.")
            self.label_23.setText("Configuration has been saved successfully!")
            self.label_23.setStyleSheet("color:#009900;")
        self.input_3.clear()
        self.input_6.clear() 
        self.input_7.clear()
        self.input_8.clear()
        self.input_12.clear()
        self.input_13.clear()
        self.input_14.clear()
        self.close_keyboard()
        
    def handle_delete_configuration(self):
        logging.info("Initializing delete configuration process.")
        self.init_screen_4(True)
        logging.debug("Screen_4 initialized with delete configuration mode.")

    # def handle_delete(self):
    #     # Display a confirmation dialog box
    #     reply = QMessageBox.question(
    #         self,
    #         'Confirm',
    #         'Are you sure you want to delete this?',
    #         QMessageBox.Yes | QMessageBox.No,
    #         QMessageBox.No
    #     )

    #     if reply == QMessageBox.Yes:
    #         if os.path.exists('ConfigFile.csv'):
    #             # Read existing rows
    #             with open('ConfigFile.csv', 'r') as file:
    #                 reader = csv.reader(file)
    #                 rows = list(reader)

    #             # Write back all rows except the one matching `self.process_config[0]`
    #             with open('ConfigFile.csv', 'w', newline='') as file:
    #                 writer = csv.writer(file)
    #                 for row in rows:
    #                     if row[0] != self.process_config[0]:
    #                         writer.writerow(row)
    #             # Show success message instead of navigating screens
    #             QMessageBox.information(
    #                 self,
    #                 'Success',
    #                 'Configuration deleted successfully.'
    #             )
    #     else:
    #         # Log the action as canceled
    #         print("Action canceled")

    #     # Remove automatic screen transition
    #     print("delete pressed")

    def handle_delete(self):
        logging.info("Delete button pressed")
        # Display a confirmation dialog box
        reply = QMessageBox.question(
            self,
            'Confirm',
            'Are you sure you want to delete this?',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            logging.debug("User confirmed deletion")
            if os.path.exists('ConfigFile.csv'):
                logging.debug("ConfigFile.csv exists, proceeding with deletion")
                # Read existing rows
                with open('ConfigFile.csv', 'r') as file:
                    reader = csv.reader(file)
                    rows = list(reader)

                # Write back all rows except the one matching `self.process_config[0]`
                with open('ConfigFile.csv', 'w', newline='') as file:
                    writer = csv.writer(file)
                    for row in rows:
                        if row[0] != self.process_config[0]:
                            writer.writerow(row)
                logging.info(f"Configuration '{self.process_config[0]}' deleted successfully.")
                # Show success message
                QMessageBox.information(
                    self,
                    'Success',
                    'Configuration deleted successfully.'
                )

                # Refresh the configuration list
                self.populate_configlist()

            else:
                logging.error("ConfigFile.csv does not exist.")
                QMessageBox.warning(
                    self,
                    'Error',
                    'Configuration file does not exist.'
                )
        else:
            logging.info("Deletion action canceled by user")
            print("Action canceled")
        logging.debug("Clearing UI labels after delete action")
        print("delete pressed")
        self.label_29.clear()
        self.label_65.clear()
        self.label_32.clear()
        self.label_67.clear()
        self.label_33.clear()
        self.label_70.clear()
        self.label_42.clear()
        self.label_72.clear()
        self.label_61.clear()
        self.label_77.clear()
        self.label_79.clear()
        logging.info("Delete process completed")
    # def start_process(self):
    #     self.timer.start(1)
        
    #     if self.mode == "READY":
    #         if self.feed_graph.layout() is None:
    #             print("Creating new layout")
    #             self.fig, self.ax = plt.subplots(figsize=(4.25, 4.125), dpi=80)
    #             self.canvas = FigureCanvas(self.fig)
    #             layout = QVBoxLayout()
    #             layout.addWidget(self.canvas)
    #             self.feed_graph.setLayout(layout)

    #         self.ax.set(xlabel='time (s)', ylabel='force (g)')
    #         self.ax.grid()
    #         self.line, = self.ax.plot([], [], color=(0,0.5,0.5))
    #         self.canvas.draw() 
    #         self.t = 1


        # # Initialize GUI components
        # self.setWindowTitle("Process with Delay")
        # self.resize(400, 300)

        # Setup button
        # self.button_7 = QPushButton("Start", self)
        # self.button_7.clicked.connect(self.on_button_7_pressed)

        # Feed graph widget
        # self.feed_graph = QWidget(self)

        # # Set up layout
        # layout = QVBoxLayout(self)
        # layout.addWidget(self.button_7)
        # layout.addWidget(self.feed_graph)
        # self.setLayout(layout)

        # # Set mode
        # self.mode = "READY"

        # # Initialize timer
        # self.timer = QTimer(self)
        # self.timer.setSingleShot(True)  # Make the timer single-shot so it fires only once
        # self.timer.timeout.connect(self.start_process)  # Connect the timer's timeout signal to the start_process method

    # def on_button_7_pressed(self):
    #     # Start the timer with a 10-second delay
    #     print(" Starting 10-second delay...")
        # self.timer.start(10000)  # 10 seconds = 10000 milliseconds

    # def start_process(self):
    #     try:
    #         # Update label_20 to show "Start"
    #         self.label_20.setText("Start")
    #         self.label_20.setStyleSheet("color:#00FF00;")  # Optional: Set color to green
            
    #         # Retrieve the threshold values from inputs
    #         try:
    #             voltage_threshold = float(self.input_9.text())
    #             current_threshold = float(self.input_10.text())
    #         except ValueError:
    #             self.label_23.setText("Error: Invalid threshold values")
    #             self.label_23.setStyleSheet("color:#FF0000;")
    #             return

    #         # Retrieve the time limit from input_11
    #         try:
    #             self.time_limit = int(self.input_11.text())  # Time in seconds
    #         except ValueError:
    #             self.label_23.setText("Error: Invalid time limit")
    #             self.label_23.setStyleSheet("color:#FF0000;")
    #             return

    #         # Check if voltage * current exceeds 160
    #         if voltage_threshold * current_threshold > 160:
    #             # Switch to channel 2 if the product exceeds 160
    #             command_CHN_SEL = "INST OUT2 *IDN\n"
    #             print(f"Switching to channel 2: {command_CHN_SEL}")
    #             self.tx_data(command_CHN_SEL)

    #             # Set current to current_threshold / 2
    #             current_threshold /= 2
    #             print(f"Adjusted current threshold: {current_threshold}")

    #         # Transmit the voltage and current setting commands
    #         set_voltage_cmd = f"VOLT {voltage_threshold} *IDN\n"
    #         set_current_cmd = f"CURR {current_threshold} *IDN\n"
    #         self.tx_data(set_voltage_cmd)
    #         self.tx_data(set_current_cmd)

    #         # Open the power supply channel
    #         self.tx_data("OUTP:GEN ON\n")

    #         # Send protocol to the MCU to indicate the process has started
    #         self.tx_data("*1:1:1#", port='mcu')  # Send start command to the MCU
    #         print("Start protocol *1:1:1# sent to MCU")

    #         # Initialize the plot if not done already
    #         if self.feed_graph.layout() is None:
    #             print("Creating new layout for the plot")
    #             self.fig, self.ax = plt.subplots(figsize=(4.25, 4.125), dpi=80)
    #             self.canvas = FigureCanvas(self.fig)
    #             layout = QVBoxLayout()
    #             layout.addWidget(self.canvas)
    #             self.feed_graph.setLayout(layout)

    #             # Initialize empty data lists for plotting
    #             self.time_data = []
    #             self.voltage_data = []  # Store voltage data
    #             self.current_data = []  # Store current data

    #             # Initialize the time tracker `self.t`
    #             self.t = 0  # Initialize `self.t` to keep track of time

    #             # Set labels and grid for the plot
    #             self.ax.set(xlabel='Time (s)', ylabel='Voltage (V) / Current (A)')
    #             self.ax.grid()

    #             # Initialize the two lines for voltage and current
    #             self.voltage_line, = self.ax.plot([], [], label='Voltage (V)', color='blue')
    #             self.current_line, = self.ax.plot([], [], label='Current (A)', color='red')

    #             # Add a legend to differentiate the lines
    #             self.ax.legend()

    #             # Draw the canvas to update the plot
    #             self.canvas.draw()

    #         # Start or resume the process timer
    #         if self.remaining_time is None:  # First start or after reset
    #             self.process_timer = QTimer()
    #             self.process_timer.timeout.connect(self.on_process_complete)  # Modified to send completion protocol when time runs out
    #             self.process_timer.setSingleShot(True)  # Ensure it only runs once
    #             self.process_timer.start(self.time_limit * 1000)  # Convert to milliseconds
    #         else:  # Resuming after pause
    #             self.process_timer = QTimer()
    #             self.process_timer.timeout.connect(self.on_process_complete)
    #             self.process_timer.setSingleShot(True)
    #             self.process_timer.start(self.remaining_time)  # Start with the remaining time
    #             print(f"Resuming process with {self.remaining_time / 1000} seconds left.")
    #             self.remaining_time = None  # Reset after resuming

    #         # Start the update timer as usual for updating the plot
    #         if not hasattr(self, 'update_timer') or not self.update_timer.isActive():
    #             self.update_timer = QTimer()
    #             self.update_timer.timeout.connect(self.display_plot)
    #             self.update_timer.start(1000)  # Update the plot every 1 second

    #     except Exception as e:
    #         self.label_23.setText(f"Error: {e}")
    #         self.label_23.setStyleSheet("color:#FF0000;")
    #         print(f"Exception in start_process: {e}")

    # # New method to handle process completion
    # def on_process_complete(self):
    #     try:
    #         # Send protocol to the MCU to indicate the process is complete
    #         self.tx_data("*1:1:0#", port='mcu')  # Send completion command to the MCU
    #         print("Completion protocol *1:1:0# sent to MCU")
            
    #         # Turn off the power supply channel
    #         command_GEN_OFF = "OUTP:GEN OFF *IDN\n"
    #         self.tx_data(command_GEN_OFF)
    #         print("Power supply turned off: OUTP:GEN OFF *IDN")

    #         self.label_20.setText("Complete")
    #         self.label_20.setStyleSheet("color:#0000FF;")  # Optional: Set color to blue

    #         # Call the reset_process or any other function to stop/reset the process
    #         self.reset_process()
    #     except Exception as e:
    #         print(f"Error in on_process_complete: {e}")

    # def start_process(self):
    #     self.label_A.setText("Auto Operation")
    #      # Check if the MCU port is selected
    #     if not self.comboBox_2.currentText():
    #         QMessageBox.critical(self, "Error", "Please select a COM port for MCU to start the process.")
    #         return  # Exit the function if no port is selected

    #     # Check if the Supply port is selected (if needed)
    #     if not self.comboBox.currentText():
    #         QMessageBox.critical(self, "Error", "Please select a COM port for Supply to start the process.")
    #         return  # Exit the function if no port is selected
        
    
            
    #      # Disable the button to prevent multiple presses
    #     self.button_7.setEnabled(True)
    #     self.button_A.setEnabled(False)
        
    #      # Retrieve user-defined time from labels
    #     try:
    #         self.time_limit = int(self.label_32.text())  # Assuming time is in seconds
    #     except ValueError:
    #         self.label_45.setText("Invalid Time")
    #         return
       
     
    #     if self.button_7.text() == "START":
    #         # First start or after reset
    #         self.remaining_time_seconds = self.time_limit  # Set full time
    #         self.label_45.setText(f"00 : {self.remaining_time_seconds} sec")
            
    #         # Start process timer
    #         self.process_timer = QTimer()
    #         self.process_timer.timeout.connect(self.on_process_complete)
    #         self.process_timer.setSingleShot(True)
    #         self.process_timer.start(self.time_limit * 1000)  # Start with full time

    #         # Start countdown timer
    #         self.countdown_timer = QTimer()
    #         self.countdown_timer.timeout.connect(self.update_countdown)
    #         self.countdown_timer.start(1000)  # Update every second

    #     elif self.button_7.text() == "RESUME":
    #         # Resuming from pause
    #         if self.remaining_time_seconds is not None:
    #             # Resume process timer from remaining time
    #             self.process_timer = QTimer()
    #             self.process_timer.timeout.connect(self.on_process_complete)
    #             self.process_timer.setSingleShot(True)
    #             self.process_timer.start(self.remaining_time_seconds * 1000)  # Resume from remaining time

    #             print(f"Resuming process with {self.remaining_time_seconds / 1000} seconds left.")

    #             # Update label_45 with the correct remaining time
    #             minutes, seconds = divmod(self.remaining_time_seconds, 60)
    #             self.label_45.setText(f"{minutes:02d} : {seconds:02d}")
            
    #         # Resume countdown timer
    #         if not hasattr(self, 'countdown_timer') or not self.countdown_timer.isActive():
    #             self.countdown_timer = QTimer()
    #             self.countdown_timer.timeout.connect(self.update_countdown)
    #             self.countdown_timer.start(1000)  # Update every second

    #     # Prepare the CSV file for saving graph data
    #     self.graph_data_filename = "real_time_graph_data.csv"  # Change filename as needed
    #     with open(self.graph_data_filename, 'w', newline='') as file:
    #         writer = csv.writer(file)
    #         # Write header row
    #         writer.writerow(["Time (s)", "Voltage (V)", "Current (A)"])
    #     # Check if the MCU port is selected
    #     if not self.comboBox_2.currentText():
    #         self.label_9.setText("Error: Please select a COM port for MCU.")
    #         self.label_9.setStyleSheet("color:#FF0000;")
    #         return  # Exit the function if no port is selected
        
    #     # Check if the Supply port is selected (if needed)
    #     if not self.comboBox.currentText():
    #         self.label_12.setText("Error: Please select a COM port for Supply.")
    #         self.label_12.setStyleSheet("color:#FF0000;")
    #         return  # Exit the function if no port is selected
    #     try:
    #         # Send start protocol to the MCU
    #         start_protocol = "*1:1:1#"
    #         print(f"Sending start protocol to MCU: {start_protocol}")
    #         self.tx_data(start_protocol, port='mcu')  # Send start command to the MCU

    #         # Initialize a variable to track feedback status
    #         feedback_received = False
    #         feedback_timeout = 300  # Timeout period in seconds
    #         check_interval = 5  # Interval to check for feedback

    #         # Check for feedback from the MCU for up to 300 seconds
    #         for elapsed_time in range(0, feedback_timeout, check_interval):
    #             # Sleep for the check interval
    #             time.sleep(check_interval)

    #             # Check for feedback from the MCU
    #             mcu_feedback = self.rx_data()  # Receive feedback
    #             print(f"Checking feedback from MCU: {mcu_feedback}")

    #             if mcu_feedback == "*PRS:STR#":  # Expected feedback for start
    #                 feedback_received = True
    #                 break  # Exit loop if feedback is received
    #             else:
    #                 print("MCU not connected.   ")

    #         if not feedback_received:
    #             # If feedback is not received after 300 seconds, display error
    #             self.label_9.setText("Error: No response from MCU within 300 seconds.")
    #             self.label_9.setStyleSheet("color:#FF0000;")
    #             print("No feedback received from MCU within the timeout period.")
    #             return  # Exit the method early

    #         # Continue with the process if feedback is received
    #         self.label_20.setText("Start")
    #         self.label_20.setStyleSheet("background-color:transparent;color:#00FF00;")  # Optional: Set color to green

    #         # Retrieve the threshold values from inputs
    #         try:
    #             voltage_threshold = float(self.input_9.text())
    #             current_threshold = float(self.input_10.text())
    #         except ValueError:
    #             self.label_23.setText("Error: Invalid threshold values")
    #             self.label_23.setStyleSheet("color:#FF0000;")
    #             return

    #         # Retrieve the time limit from input_11
    #         try:
    #             self.time_limit = int(self.input_11.text())  # Time in seconds
    #         except ValueError:
    #             self.label_23.setText("Error: Invalid time limit")
    #             self.label_23.setStyleSheet("color:#FF0000;")
    #             return

    #         # Check if voltage * current exceeds 160
    #         if voltage_threshold * current_threshold > 160:
    #             # Switch to Channel 2 and set values
    #             command_CHN_SEL = "INST OUT2 *IDN\n"
    #             print(f"Switching to Channel 2: {command_CHN_SEL}")
    #             self.tx_data(command_CHN_SEL)

    #             # Set voltage and current for Channel 2 (with adjusted current)
    #             current_threshold_channel2 = current_threshold / 2
    #             set_voltage_cmd = f"VOLT {voltage_threshold} *IDN\n"
    #             set_current_cmd = f"CURR {current_threshold_channel2} *IDN\n"
    #             self.tx_data(set_voltage_cmd)
    #             self.tx_data(set_current_cmd)
    #             print(f"Voltage set to {voltage_threshold} and current set to {current_threshold_channel2} on Channel 2")

    #             # Open Channel 2
    #             self.tx_data("OUTP:SEL ON *IDN\n")
    #             print("Channel 2 turned on")

    #             # Switch back to Channel 1 and set values
    #             command_CHN_SEL = "INST OUT1 *IDN\n"
    #             print(f"Switching to Channel 1: {command_CHN_SEL}")
    #             self.tx_data(command_CHN_SEL)
    #             current_threshold_channel1 = current_threshold / 2
    #             set_voltage_cmd = f"VOLT {voltage_threshold} *IDN\n"
    #             set_current_cmd = f"CURR {current_threshold_channel1} *IDN\n"
    #             self.tx_data(set_voltage_cmd)
    #             self.tx_data(set_current_cmd)
    #             print(f"Voltage set to {voltage_threshold} and current set to {current_threshold_channel1} on Channel 1")

    #             # Open Channel 1
    #             self.tx_data("OUTP:SEL ON *IDN\n")
    #             print("Channel 1 turned on")
    #             self.tx_data("OUTP:GEN ON *IDN\n")

    #         else:
    #             # Normal case: Set voltage and current for Channel 1
    #             command_CHN_SEL = "INST OUT1 *IDN\n"
    #             print(f"Switching to Channel 1: {command_CHN_SEL}")
    #             self.tx_data(command_CHN_SEL)
    #             set_voltage_cmd = f"VOLT {voltage_threshold} *IDN\n"
    #             set_current_cmd = f"CURR {current_threshold} *IDN\n"
    #             self.tx_data(set_voltage_cmd)
    #             self.tx_data(set_current_cmd)
    #             print(f"Voltage set to {voltage_threshold} and current set to {current_threshold} on Channel 1")

    #             # Open Channel 1
    #             self.tx_data("OUTP:SEL ON *IDN\n")
    #             print("Channel 1 turned on")
    #             self.tx_data("OUTP:GEN ON *IDN\n")

    #         # Initialize the plot if not done already
    #         if self.feed_graph.layout() is None:
    #             print("Creating new layout for the plot")
    #             self.fig, self.ax = plt.subplots(figsize=(4.25, 4.125), dpi=80)
    #             self.canvas = FigureCanvas(self.fig)
    #             layout = QVBoxLayout()
    #             layout.addWidget(self.canvas)
    #             self.feed_graph.setLayout(layout)

    #             # Initialize empty data lists for plotting
    #             self.time_data = []
    #             self.voltage_data = []  # Store voltage data
    #             self.current_data = []  # Store current data

    #             # Initialize the time tracker `self.t`
    #             self.t = 0  # Initialize `self.t` to keep track of time

    #             # Set labels and grid for the plot
    #             self.ax.set(xlabel='Time (s)', ylabel='Voltage (V) / Current (A)')
    #             self.ax.grid()

    #             # Initialize the two lines for voltage and current
    #             self.voltage_line, = self.ax.plot([], [], label='Voltage (V)', color='blue')
    #             self.current_line, = self.ax.plot([], [], label='Current (A)', color='red')

    #             # Add a legend to differentiate the lines
    #             self.ax.legend()

    #             # Draw the canvas to update the plot
    #             self.canvas.draw()

    #     except Exception as e:
    #         self.label_23.setText(f"Error: {e}")
    #         self.label_23.setStyleSheet("color:#FF0000;")
    #         print(f"Exception in start_process: {e}")
    
    
    def update_countdown(self):
        logging.debug(f"Countdown update triggered: {self.remaining_time_seconds} sec left")
        if self.remaining_time_seconds > 0:
            self.remaining_time_seconds -= 1  # Decrement time
            minutes, seconds = divmod(self.remaining_time_seconds, 60)
            self.label_45.setText(f"{minutes:02d} : {seconds:02d}")
            print(f"Updating countdown: {self.remaining_time_seconds} sec left")
            logging.info(f"Updating countdown: {self.remaining_time_seconds} sec left")
        else:
            logging.info("Countdown reached zero, stopping timer.")
            print("Countdown reached zero, stopping timer.")
            self.countdown_timer.stop()
            self.label_45.setText("00 : 00")  # Or trigger process completion
            print("Countdown finished.")  
            logging.debug("Countdown finished.")  
            
            
    def get_saved_temperature(self):
        logging.debug("Attempting to read temperature from settings.json")
        try:
            with open("settings.json", "r") as file:
                settings = json.load(file)
              
            return float(settings.get("temperature", 0))  # Convert to float for numeric comparisons
            logging.info(f"Retrieved saved temperature: {temperature}")
        except (FileNotFoundError, json.JSONDecodeError):
            print("Error: Could not read settings.json")
            logging.error("Error: Could not read settings.json")
            return None  # Return None if the file is missing or corrupted
            
            
    def start_process(self):
        logging.info("Starting process...")
        self.label_20.setText("Ready")
        if not self.comboBox_2.currentText() and not self.comboBox.currentText():
            QMessageBox.critical(self, "Port Selection Error", "Please select COM ports for both MCU and Supply.")
            logging.error("No COM ports selected for MCU and Supply.")
            return  # Exit the function

        if not self.comboBox_2.currentText():
            QMessageBox.critical(self, "Port Selection Error", "Please select a COM port for MCU.")
            logging.error("No COM port selected for MCU.")
            return  # Exit the function

        if not self.comboBox.currentText():
            QMessageBox.critical(self, "Port Selection Error", "Please select a COM port for Supply.")
            logging.error("No COM port selected for Supply.")
            return  # Exit the function

        # If both ports are selected, proceed with the process
        self.label_9.setText(f"MCU Port: {self.comboBox_2.currentText()}")
        self.label_9.setStyleSheet("color:#00FF00;")  # Green color for success

        self.label_12.setText(f"Supply Port: {self.comboBox.currentText()}")
        self.label_12.setStyleSheet("color:#00FF00;")  # Green color for success

        logging.info(f"Selected MCU Port: {self.comboBox_2.currentText()}")
        logging.info(f"Selected Supply Port: {self.comboBox.currentText()}")
        
        
        # # Check if the MCU port is selected
        # if not self.comboBox_2.currentText():
        #     self.label_9.setText("Error: Please select a COM port for MCU.")
        #     self.label_9.setStyleSheet("color:#FF0000;")
        #     logging.error("No COM port selected for MCU.")
        #     return  # Exit the function if no port is selected

        # # Check if the Supply port is selected (if needed)
        # if not self.comboBox.currentText():
        #     self.label_12.setText("Error: Please select a COM port for Supply.")
        #     self.label_12.setStyleSheet("color:#FF0000;")
        #     logging.error("No COM port selected for Supply.")
        #     return  # Exit the function if no port is selected

        # Retrieve the saved temperature from settings.json
        saved_temp = self.get_saved_temperature()
        if saved_temp is None:
            QMessageBox.critical(self, "Error", "Failed to load saved temperature!")
            logging.critical("Failed to load saved temperature!")
            return
        elif float(self.temperature_value) >= saved_temp:
            logging.info("Temperature is sufficient. Proceeding...")
            print("Ready to go===========================>>>> COOL!")
        else:
            QMessageBox.critical(self, "An error occurred:", "Low Temperature! Turning on Heater.")
            logging.error("Low Temperature detected. Turning on Heater.")
            if not self.heater:
                self.handle_heater()
            return

        try:
            # Send start protocol to the MCU
            start_protocol = "*1:1:1#"
            print(f"Sending start protocol to MCU: {start_protocol}")
            logging.debug(f"Sending start protocol to MCU: {start_protocol}")
            self.tx_data(start_protocol, port='mcu')  # Send start command to the MCU

            # Start countdown timer
            self.countdown_timer = QTimer()
            self.countdown_timer.timeout.connect(self.update_countdown)
            self.countdown_timer.start(1000)  # Update every second

            # Update UI on success
            self.label_20.setText("Started")
            self.label_20.setStyleSheet("color:#00FF00; background-color: transparent;")
            
            

            # Retrieve the threshold values from inputs
            try:
                voltage_threshold = float(self.input_7.text())
                current_threshold = float(self.input_8.text())
                logging.debug(f"Voltage Threshold: {voltage_threshold}, Current Threshold: {current_threshold}")
            except ValueError:
                self.label_23.setText("Error: Invalid threshold values")
                self.label_23.setStyleSheet("color:#FF0000;")
                logging.error("Invalid threshold values entered.")
                return

            # Retrieve the time limit from input_11
            try:
                self.time_limit = int(self.input_6.text())  # Time in seconds
                logging.debug(f"Time Limit: {self.time_limit} seconds")
            except ValueError:
                self.label_23.setText("Error: Invalid time limit")
                self.label_23.setStyleSheet("color:#FF0000;")
                logging.error("Invalid time limit entered.")
                return

            # Check if voltage * current exceeds 160
            if voltage_threshold * current_threshold > 160:
                logging.info("High power detected. Splitting load across channels.")
                # Switch to Channel 2 and set values
                command_CHN_SEL = "INST OUT2 *IDN\n"
                print(f"Switching to Channel 2: {command_CHN_SEL}")
                self.tx_data(command_CHN_SEL)

                # Set voltage and current for Channel 2 (with adjusted current)
                current_threshold_channel2 = current_threshold / 2
                set_voltage_cmd = f"VOLT {voltage_threshold} *IDN\n"
                set_current_cmd = f"CURR {current_threshold_channel2} *IDN\n"
                logging.debug(f"Channel 2 set: Voltage {voltage_threshold}, Current {current_threshold_channel2}")
                self.tx_data(set_voltage_cmd)
                self.tx_data(set_current_cmd)
                print(f"Voltage set to {voltage_threshold} and current set to {current_threshold_channel2} on Channel 2")

                # Open Channel 2
                self.tx_data("OUTP:SEL ON *IDN\n")
                print("Channel 2 turned on")

                # Switch back to Channel 1 and set values
                command_CHN_SEL = "INST OUT1 *IDN\n"
                print(f"Switching to Channel 1: {command_CHN_SEL}")
                self.tx_data(command_CHN_SEL)
                current_threshold_channel1 = current_threshold / 2
                set_voltage_cmd = f"VOLT {voltage_threshold} *IDN\n"
                set_current_cmd = f"CURR {current_threshold_channel1} *IDN\n"
                logging.debug(f"Channel 2 set: Voltage {voltage_threshold}, Current {current_threshold_channel2}")
                self.tx_data(set_voltage_cmd)
                self.tx_data(set_current_cmd)
                print(f"Voltage set to {voltage_threshold} and current set to {current_threshold_channel1} on Channel 1")

                # Open Channel 1
                self.tx_data("OUTP:SEL ON *IDN\n")
                print("Channel 1 turned on")
                self.tx_data("OUTP:GEN ON *IDN\n")

            else:
                logging.info("Setting power values for Channel 1.")
                # Normal case: Set voltage and current for Channel 1
                command_CHN_SEL = "INST OUT1 *IDN\n"
                print(f"Switching to Channel 1: {command_CHN_SEL}")
                self.tx_data(command_CHN_SEL)
                set_voltage_cmd = f"VOLT {voltage_threshold} *IDN\n"
                set_current_cmd = f"CURR {current_threshold} *IDN\n"
                self.tx_data(set_voltage_cmd)
                self.tx_data(set_current_cmd)
                print(f"Voltage set to {voltage_threshold} and current set to {current_threshold} on Channel 1")

                # Open Channel 1
                logging.debug(f"Channel 1 set: Voltage {voltage_threshold}, Current {current_threshold}")
                self.tx_data("OUTP:SEL ON *IDN\n")
                print("Channel 1 turned on")
                self.tx_data("OUTP:GEN ON *IDN\n")

            # Initialize the plot if not done already
            if self.feed_graph.layout() is None:
                logging.info("Initializing new plot layout.")
                print("Creating new layout for the plot")
                self.fig, self.ax = plt.subplots(figsize=(4.25, 4.125), dpi=80)
                self.canvas = FigureCanvas(self.fig)
                layout = QVBoxLayout()
                layout.addWidget(self.canvas)
                self.feed_graph.setLayout(layout)

                # Initialize empty data lists for plotting
                self.time_data = []
                self.voltage_data = []  # Store voltage data
                self.current_data = []  # Store current data

                # Initialize the time tracker `self.t`
                self.t = 0  # Initialize `self.t` to keep track of time

                # Set labels and grid for the plot
                self.ax.set(xlabel='Time (s)', ylabel='Voltage (V) / Current (A)')
                self.ax.grid()

                # Initialize the two lines for voltage and current
                self.voltage_line, = self.ax.plot([], [], label='Voltage (V)', color='blue')
                self.current_line, = self.ax.plot([], [], label='Current (A)', color='red')

                # Add a legend to differentiate the lines
                self.ax.legend()

                # Draw the canvas to update the plot
                self.canvas.draw()

            # Start or resume the process timer
            if self.remaining_time is None:  # First start or after reset
                self.process_timer = QTimer()
                self.process_timer.timeout.connect(self.on_process_complete)  # Send completion protocol
                self.process_timer.setSingleShot(True)
                self.process_timer.start(self.time_limit * 1000)  # Convert to milliseconds

                # Initialize remaining_time_seconds for countdown display
                self.remaining_time_seconds = self.time_limit

            else:  # Resuming after pause
                self.process_timer = QTimer()
                self.process_timer.timeout.connect(self.on_process_complete)
                self.process_timer.setSingleShot(True)
                self.process_timer.start(self.remaining_time)  # Start with the remaining time

                self.remaining_time_seconds = self.remaining_time // 1000  # Convert ms to seconds
                logging.debug(f"Resuming process with {self.remaining_time_seconds} seconds left.")
                print(f"Resuming process with {self.remaining_time_seconds} seconds left.")
                self.remaining_time = None  # Reset after resuming

            # **Manually update label_45 before starting countdown**
            self.label_45.setText(str(self.remaining_time_seconds))  

            # Ensure real-time countdown update in label_45
            if not hasattr(self, 'countdown_timer') or not self.countdown_timer.isActive():
                self.countdown_timer = QTimer()
                self.countdown_timer.timeout.connect(self.update_label_45)
                self.countdown_timer.start(1000)  # Update every second

            # Start the update timer as usual for updating the plot
            if not hasattr(self, 'update_timer') or not self.update_timer.isActive():
                self.update_timer = QTimer()
                self.update_timer.timeout.connect(self.display_plot)
                self.update_timer.start(1000)  # Update the plot every 1 second

        except Exception as e:
            self.label_23.setText(f"Error: {e}")
            self.label_23.setStyleSheet("color:#FF0000;")
            print(f"Exception in start_process: {e}")
            logging.exception("Exception in start_process:")
        finally:
            self.comboBox.setEnabled(False)
            self.comboBox_2.setEnabled(False)
            self.button_7.setEnabled(False)
            logging.info("Process started successfully.")


    def update_label_45(self):
        """Update label_45 every second to show remaining time in real-time."""
        logging.debug(f"Updating label_45. Remaining time: {self.remaining_time_seconds}")
        if self.remaining_time_seconds > 0:
            self.remaining_time_seconds -= 1
            self.label_45.setText(str(self.remaining_time_seconds))  # Update countdown
            
        else:
            self.countdown_timer.stop()  # Stop when countdown reaches zero
            logging.info("Countdown reached zero. Timer stopped.")
            self.label_45.setText("Time's up!")

    def on_process_complete(self):
        try:
            logging.info("Process completion initiated.")
            if self.heater:
                self.heater = False
                logging.debug("Heater turned off.")
            
            # Send protocol to the MCU to indicate the process is complete
            self.tx_data("*1:1:0#", port='mcu')  # Send completion command to the MCU
            print("Completion protocol *1:1:0# sent to MCU")
            logging.info("Completion protocol *1:1:0# sent to MCU.")

            # Turn off the power supply channel
            command_GEN_OFF = "OUTP:GEN OFF *IDN\n"
            self.tx_data(command_GEN_OFF)
            self.tx_data("*RST *IDN\n")
            logging.info("Power supply turned off: OUTP:GEN OFF *IDN.")
            print("Power supply turned off: OUTP:GEN OFF *IDN")

            # Update label to show "Complete"
            self.label_20.setText("Completed")
            logging.debug("Label updated to 'Completed'.")
            self.label_20.setStyleSheet("color:#0000FF; background-color: transparent;")  # Optional: Set color to blue

            # Stop the update timer to stop plotting
            if hasattr(self, 'update_timer') and self.update_timer.isActive():
                self.update_timer.stop()
                logging.debug("Update timer stopped.")
                print("Update timer stopped.")

            # Clear the graph data and reset the plot
            if hasattr(self, 'ax'):
                self.time_data = []
                self.voltage_data = []
                self.current_data = []

                # Clear the plot lines
                self.ax.clear()  # Clear the axes
                self.ax.set(xlabel='Time (s)', ylabel='Voltage (V) / Current (A)')
                self.ax.grid()
                self.voltage_line, = self.ax.plot([], [], label='Voltage (V)', color='blue')
                self.current_line, = self.ax.plot([], [], label='Current (A)', color='red')
                self.ax.legend()

                # Redraw the canvas to update the cleared plot
                self.canvas.draw()
                logging.info("Graph reset and updated.")
                print("Graph reset.")
                
            # Close serial ports and reset combo boxes
            self.close_serial_ports()  # Close serial ports when navigating away from screens 5, 6, or 7
            logging.debug("Serial ports closed.")
            self.comboBox.setCurrentIndex(0)  # Clear the comboBox
            self.comboBox_2.setCurrentIndex(0)  # Clear the comboBox_2
            
            self.label_25.setText("--")
            self.label_26.setText("--")
            self.label_37.setText("--")
            logging.info("Process completion steps executed successfully.")
        except Exception as e:
            logging.error(f"Error in on_process_complete: {e}")
            print(f"Error in on_process_complete: {e}")
        finally:
            self.temperature_message_shown = False
            self.comboBox.setEnabled(True)
            self.comboBox_2.setEnabled(True)
            self.button_7.setEnabled(True)
            self.button_7.setText("START")
            self.label_20.setText("Ready")
            logging.debug("Final UI elements reset for next process.")


    def get_voltage_from_power_supply(self):
        try:
            logging.debug("Sending voltage request command to power supply.")
            # Send command to the power supply to check the voltage
            self.tx_data("VOLT? *IDN\n")
            
            # Read the response from the power supply
            voltage_data = self.read_until_delimiter(self.ser)  # Pass self.ser here
            
            # Check if the response is None or empty
            if voltage_data is None or voltage_data.strip() == "":
                logging.error("No data received from the power supply.")
                print("No data received from the power supply.")
                return 0.0  # Return default value if no data is received
            
            # Strip and convert the response to a float
            voltage_value = float(voltage_data.strip())
            logging.info(f"Voltage data received: {voltage_value}")
            print(f"Voltage data received: {voltage_value}")
            return voltage_value
        
        
        except ValueError as ve:
            logging.error(f"ValueError: {ve} - Cannot convert voltage data to float.")
            print(f"ValueError: {ve} - Cannot convert voltage data to float.")
            return 0.0  # Return default value if conversion fails
        except Exception as e:
            print(f"Error: {e}")
            logging.exception("Unexpected error in get_voltage_from_power_supply")
            return 0.0  # Return default value in case of other errors

    def get_current_from_power_supply(self):
        try:
            logging.debug("Sending current request command to power supply.")
            # Send command to the power supply to check the current
            self.tx_data("MEAS:CURR? *IDN\n")
            
            # Read the response from the power supply
            current_data = self.read_until_delimiter(self.ser)  # Pass self.ser here
            
            # Check if the response is None or empty
            if current_data is None or current_data.strip() == "":
                logging.error("No data received from the power supply.")
                print("No data received from the power supply.")
                return 0.0  # Return default value if no data is received
            
            # Convert the response to a float
            current_value = float(current_data.strip())
            
            print(f"Current data received: {current_value}")
            logging.info(f"Current data received: {current_value}")
            return current_value

        except ValueError as ve:
            print(f"ValueError: {ve} - Cannot convert current data to float.")
            logging.error(f"ValueError: {ve} - Cannot convert current data to float.")
            return 0.0  # Return default value if conversion fails
        except Exception as e:
            print(f"Error: {e}")
            logging.exception("Unexpected error in get_current_from_power_supply")
            return 0.0  # Return default value in case of other errors


        
    # def tx_data(self, data):
    #     # Simulate data transmission
    #     print(f"Transmitting data: {data}")



        # Comment out the serial port closing to keep the port open for subsequent communication
        # finally:
        #     if self.ser.is_open:
        #         self.ser.close()
        #         print(f"Closed serial port: {self.ser.port}")

        

    # def complete_process(self):
    # # Send the COMPLETE CMD
    #     cmd = "*1:0:0#"
    #     print(cmd)
    #     self.tx_data(cmd)

    #     # Turn off the power supply channel
    #     self.tx_data("OUTP:GEN OFF *IDN\n")  # Sending GEN_OFF command

    def pause_process(self):
        logging.info("Pausing process...")

        # Stop update timer if active
        if hasattr(self, 'update_timer') and self.update_timer.isActive():
            self.update_timer.stop()
            logging.debug("Update timer stopped.")
            print("Update timer stopped.")
            
            

        # Stop process timer and save remaining time
        if hasattr(self, 'process_timer') and self.process_timer.isActive():
            self.remaining_time = self.process_timer.remainingTime()  # Save remaining time in milliseconds
            self.process_timer.stop()
            logging.debug(f"Paused with {self.remaining_time / 1000} seconds left.")
            print(f"Paused with {self.remaining_time / 1000} seconds left.")

        # Stop countdown timer and save the remaining time
        if hasattr(self, 'countdown_timer') and self.countdown_timer.isActive():
            # Extract time before stopping
            time_text = self.label_45.text().strip()  # Ensure no extra spaces
            try:
                self.remaining_time_seconds = int(time_text.split(":")[-1].strip())  # Get last numeric part
                print(f"Process paused with {self.remaining_time_seconds} seconds remaining.")
                logging.debug(f"Process paused with {self.remaining_time_seconds} seconds remaining.")
            except ValueError:
                print(f"Error extracting time from label_45: {time_text}")
                logging.error(f"Error extracting time from label_45: {time_text}")
                self.remaining_time_seconds = 0  # Fallback value

            self.countdown_timer.stop()
            logging.debug("Countdown timer stopped.")
            print("Countdown timer stopped.")

        # Send pause command to MCU
        # pause_cmd = "*1:0:0#"
        pause_cmd = "*1:1:0#"
        logging.info(f"Sending pause protocol to MCU: {pause_cmd}")
        print(f"Sending pause protocol to MCU: {pause_cmd}")
        self.tx_data(pause_cmd, port='mcu')  # Send command

        # Wait for MCU feedback
        mcu_feedback = self.rx_data()
        if mcu_feedback == "*PRS:STP#":
            logging.info("Pause feedback received from MCU: *PRS:STP#")
            print("Pause feedback received from MCU: *PRS:STP#")
        else:
            logging.error(f"Unexpected feedback from MCU: {mcu_feedback}")
            print(f"Unexpected feedback from MCU: {mcu_feedback}")

        # Update UI labels
        self.label_20.setText("Paused")
        self.label_20.setStyleSheet("color:#FFA500; background-color: transparent;")  # Set color to orange

        # Enable Resume button, disable pause button
        self.button_7.setEnabled(True)
        self.button_7.setText("RESUME")
        
        if hasattr(self, 'button_A'):  # Ensure button_A exists
            self.button_A.setEnabled(False)
  
        
    def reset_process(self):
        logging.info("Resetting process...")

        # Create a confirmation dialog
        if self.heater:
            self.heater = False
                # self.handle_heater()
        reply = QMessageBox.question(
            self,
            "Confirm Reset",
            "Are you sure you want to stop the process?",
            QMessageBox.Yes | QMessageBox.Cancel
        )

        if reply == QMessageBox.Cancel:
            logging.info("Reset process canceled by the user.")
            print("Reset process canceled by the user.")
            self.handle_screen_change(5)
            return
        # Check the user's response
        elif reply == QMessageBox.Yes:
            
            # Stop timers if they are active
            if hasattr(self, 'update_timer') and self.update_timer.isActive():
                self.update_timer.stop()
                logging.debug("Update timer stopped.")
                print("Update timer stopped.")

            if hasattr(self, 'process_timer') and self.process_timer.isActive():
                self.process_timer.stop()
                logging.debug("Process timer stopped.")
                print("Process timer stopped.")

            # Turn off the power supply output and reset the device
            self.tx_data("OUTP:GEN OFF *IDN\n")
            self.tx_data("*RST *IDN\n")

            # Close the serial port if open
            if self.ser is not None and self.ser.is_open:
                self.ser.close()
                logging.debug(f"Serial port {self.ser.port} closed.")
                print(f"Serial port {self.ser.port} closed.")

            # Reset the data and stop the process
            self.time_data = []
            self.voltage_data = []
            self.current_data = []
            self.remaining_time = None  # Reset the remaining time

            # Send the stop protocol to the MCU
            cmd = "*1:1:0#"  # Complete stop protocol
            logging.info(f"Sending stop protocol to MCU: {cmd}")
            print(f"Sending stop protocol to MCU: {cmd}")
            self.tx_data(cmd, port='mcu')  # Specify MCU port for sending the command

            # Receive and validate MCU feedback
            mcu_feedback = self.rx_data()  # Call rx_data without port argument
            if mcu_feedback == "*PRS:STP#":
                logging.info("Reset feedback received from MCU: *PRS:STP#")
                logging.info("Process reset successfully.")
                print("Reset feedback received from MCU: *PRS:STP#")
                print("Process reset successfully.")
            else:
                logging.error(f"Unexpected feedback from MCU: {mcu_feedback}")
                print(f"Unexpected feedback from MCU: {mcu_feedback}")

            # Close serial ports and reset combo boxes
            self.close_serial_ports()  # Close serial ports when navigating away from screens 5, 6, or 7
            self.comboBox.setCurrentIndex(0)  # Clear the comboBox
            self.comboBox_2.setCurrentIndex(0)  # Clear the comboBox_2
            
            # Clear the graph data and reset the plot
            if hasattr(self, 'ax'):
                self.time_data = []
                self.voltage_data = []
                self.current_data = []

                # Clear the plot lines
                self.ax.clear()  # Clear the axes
                self.ax.set(xlabel='Time (s)', ylabel='Voltage (V) / Current (A)')
                self.ax.grid()
                self.voltage_line, = self.ax.plot([], [], label='Voltage (V)', color='blue')
                self.current_line, = self.ax.plot([], [], label='Current (A)', color='red')
                self.ax.legend()

                # Redraw the canvas to update the cleared plot
                self.canvas.draw()
                logging.debug("Graph reset.")
                print("Graph reset.")
                
            self.label_25.setText("--")
            self.label_26.setText("--")
            self.label_37.setText("--")
                
            if hasattr(self, 'countdown_timer') and self.countdown_timer.isActive():
                self.countdown_timer.stop()  # Stop the countdown timer
            self.remaining_time_seconds = 0  # Reset the remaining time
            self.label_45.setText("00 : 00")  # Reset the label to 00:00
            logging.debug("Process stopped and timer reset.")
            print("Process stopped and timer reset.")
            # Update label_20 to show "Reset"
            self.label_20.setText("Stopped")
            self.label_20.setStyleSheet("color:#FF0000; background-color:transparent;")  # Optional: Set color to red
            logging.info("Process stopped.")

            print("Process stopped.")

            # Re-enable the start button
            self.button_7.setEnabled(True)
            self.button_7.setText("START")
            self.button_A.setEnabled(True)
            
            self.temperature_message_shown = False
            if self.BackBtnPressedState:
                self.handle_screen_change(4)
                self.BackBtnPressedState = False
                self.label_61.clear()
                self.label_77.clear()
                self.label_79.clear()
            
            self.comboBox.setEnabled(True)
            self.comboBox_2.setEnabled(True)
            self.button_7.setEnabled(True)

        else:
            logging.info("Reset process canceled by the user.")
            print("Reset process canceled by the user.")
            self.handle_screen_change(5)
            return

            


    # def display_cam(self):
    #     ret, frame = self.camera.read()
    #     if ret:
    #         frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    #         q_img = QImage(frame.data, 640, 480, 1920, QImage.Format_RGB888)
    #         self.feed_cam.setPixmap(QPixmap.fromImage(q_img))
    #     else:
    #         self.feed_cam.setText("Failed to load Camera!")

    # def display_plot(self):
    #     self.t = self.t + 1
    #     self.label_36.setText(str(self.rx_force))
    #     self.label_37.setText(str(self.rx_temperature))
    #     self.time_data.append(self.t)
    #     self.force_data.append(self.rx_force)
        
    #     if len(self.time_data) > 25:
    #         t_data = self.time_data[-25:]
    #         f_data = self.force_data[-25:]        
    #         self.line.set_data(t_data, f_data)

    #     else:
    #         self.line.set_data(self.time_data, self.force_data)
        
    #     self.ax.relim()
    #     self.ax.autoscale_view()
    #     self.canvas.draw()

    # def display_plot(self):
    #     self.t += 1
    #     voltage_actual = self.get_voltage_from_power_supply()
    #     current_actual = self.get_current_from_power_supply()

    #     self.label_16.setText(f"Voltage: {voltage_actual} V")
    #     self.label_17.setText(f"Current: {current_actual} A")


    #     try:
    #         voltage_threshold = float(self.input_9.text()) if self.input_9.text() else float('inf')
    #         current_threshold = float(self.input_10.text()) if self.input_10.text() else float('inf')
    #     except ValueError:
    #         self.label_23.setText("Error: Invalid threshold values")
    #         self.label_23.setStyleSheet("color:#FF0000;")
    #         return

    #     if voltage_actual > voltage_threshold:
    #         voltage_actual = voltage_threshold
    #         self.label_16.setText(f"Voltage (Exceeded): {voltage_actual} V")

    #     if current_actual > current_threshold:
    #         current_actual = current_threshold
    #         self.label_17.setText(f"Current (Exceeded): {current_actual} A")
            
    #     # print(f"Voltage data received: {voltage_actual}\nCurrent data received: {current_actual}")

    #     self.time_data.append(self.t)
    #     self.voltage_data.append(voltage_actual)
    #     self.current_data.append(current_actual)

    #     t_data = self.time_data[0:]
    #     v_data = self.voltage_data[0:]
    #     c_data = self.current_data[0:]
        
    #     print(f"Voltage data received: {v_data}\nCurrent data received: {c_data}")

    #     self.voltage_line.set_data(t_data, v_data)
    #     self.current_line.set_data(t_data, c_data)

    #     if len(t_data) > 0:
    #         self.ax.set_xlim(min(t_data), max(t_data))
    #     if len(v_data) > 0 and len(c_data) > 0:
    #         self.ax.set_ylim(min(min(v_data), min(c_data)), max(max(v_data), max(c_data)))

    #     self.canvas.draw()


    def display_plot(self):
        self.t += 1
        voltage_actual = self.get_voltage_from_power_supply()
        current_actual = self.get_current_from_power_supply()
        
        logging.info(f"Updating real-time values: Voltage={voltage_actual} V, Current={current_actual} A")
        
         # Update the labels with the real-time values
        self.label_25.setText(f" {voltage_actual} ")  # Update label_25
        self.label_26.setText(f" {current_actual} ")   # Update label_26

        # self.label_16.setText(f"Voltage: {voltage_actual} V")
        # self.label_17.setText(f"Current: {current_actual} A")

        try:
            voltage_threshold = float(self.input_7.text()) if self.input_7.text() else float('inf')
            current_threshold = float(self.input_8.text()) if self.input_8.text() else float('inf')
        except ValueError:
            logging.error("Invalid threshold values entered")
            self.label_23.setText("Error: Invalid threshold values")
            self.label_23.setStyleSheet("color:#FF0000;")
            return

        if voltage_actual > voltage_threshold:
            logging.error(f"Voltage exceeded threshold: {voltage_actual} V (Limit: {voltage_threshold} V)")
            voltage_actual = voltage_threshold
            self.label_16.setText(f"Voltage (Exceeded): {voltage_actual} V")

        if current_actual > current_threshold:
            logging.error(f"Current exceeded threshold: {current_actual} A (Limit: {current_threshold} A)")
            current_actual = current_threshold
            self.label_17.setText(f"Current (Exceeded): {current_actual} A")

        self.time_data.append(self.t)
        self.voltage_data.append(voltage_actual)
        self.current_data.append(current_actual)
        
        logging.debug("Updated plot data arrays")

        t_data = self.time_data
        v_data = self.voltage_data
        c_data = self.current_data

        self.voltage_line.set_data(t_data, v_data)
        self.current_line.set_data(t_data, c_data)
        if len(t_data) > 1:  # Ensure there are at least 2 points to avoid identical limits
            self.ax.set_xlim(min(t_data), max(t_data))
        if len(v_data) > 0 and len(c_data) > 0:
            self.ax.set_ylim(min(min(v_data), min(c_data)) - 1, max(max(v_data), max(c_data)) + 1)

        self.canvas.draw()
        
        logging.info("Graph updated and redrawn")
        
         # Save data to the CSV file
        with open(self.graph_data_filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Time (s)", "Voltage (V)", "Current (A)"])

        logging.debug("Data written to CSV file")


 
 # for handling Back pressed
        
    def handle_back_pressed(self):
        logging.info("Back button pressed")
        self.button_A.setIconSize(QSize(40, 40))
        self.label_9.setText("")

        # Check if the current screen is 5, and if so, call reset_process
        if self.screen == 5:
            logging.info("Navigating away from screen 5, calling reset_process")
            self.BackBtnPressedState = True
            self.reset_process()  # Call reset_process when navigating away from screen 5
            return

        # Check if the current screen is 5, 6, or 7, and if so, close the serial ports before changing screens
        if self.screen in [5, 6]:
            logging.info(f"Closing serial ports before leaving screen {self.screen}")
            self.close_serial_ports()  # Close serial ports when navigating away from screens 5, 6, or 7
            self.comboBox.setCurrentIndex(0)  # Clear the comboBox
            self.comboBox_2.setCurrentIndex(0)  # Clear the comboBox_2
            

        # Determine the new screen based on current screen value
        if self.screen > 1: 
            if self.screen == 6:
                self.screen = 2
            elif self.screen == 4:
                self.screen = 2
            elif self.screen == 5:
                self.screen = 2
            else:
                self.screen -= 1
            logging.info(f"Screen changed from {self.screen} to {self.screen}")
        print(self.screen)
        self.handle_screen_change(self.screen)

    # def handle_back_pressed(self):
    #     self.button_A.setIconSize(QSize(40, 40))
    #     self.label_9.setText("")

    #     # Check if the current screen is 5, and if so, call reset_process
    #     if self.screen == 5:
    #         self.reset_process()  # Call reset_process when navigating away from screen 5

    #     # Check if the current screen is 5 or 7, and if so, close the serial ports before changing screens
    #     if self.screen in [5, 7]:
    #         self.close_serial_ports()  # Close serial ports when navigating away from screens 5 or 7
    #         self.comboBox.setCurrentIndex(0)  # Clear the comboBox
    #         self.comboBox_2.setCurrentIndex(0)  # Clear the comboBox_2

    #     # Determine the new screen based on the current screen value
    #     if self.screen > 1:
    #         if self.screen == 7:
    #             self.screen = 2  # Navigate back to screen 2 from screen 7
    #         elif self.screen == 5:
    #             self.screen = 4  # Navigate back to screen 4 from screen 5
    #         elif self.screen == 4:
    #             self.screen = 2  # Navigate back to screen 2 from screen 4
    #         else:
    #             self.screen -= 1  # General case for decrementing screen number

    #     print(f"Navigating to screen: {self.screen}")
    #     self.handle_screen_change(self.screen)

    def handle_app_quit(self):
        logging.info("Application quit initiated.")
        self.close()
        self.close_keyboard()
        logging.info("Application closed successfully.")

        
    def close_serial_ports(self):
        logging.info("Closing serial ports if open.")
        # Close the serial ports if they are open
        if self.ser and self.ser.is_open:
            self.ser.close()
            logging.info("Power Supply serial port closed.")
            print("Power Supply serial port closed.")
        
        if self.ser_2 and self.ser_2.is_open:
            self.ser_2.close()
            self.comboBox.setCurrentIndex(0)  # Clear the comboBox
            self.comboBox_2.setCurrentIndex(0)  # Clear the comboBox_2
            logging.info("MCU serial port closed.")
            print("MCU serial port closed.")

        # Clear the labels to indicate ports are closed
        self.label_12.setText("")
        self.label_9.setText("")
        logging.debug("Labels cleared after closing serial ports.")

        # Reset serial port objects to None
        self.ser = None
        self.ser_2 = None
        logging.debug("Serial port objects reset to None.")

     
    # def rx_data(self):
    #     try:
    #         print("Im in rx_data")
    #         self.ser = serial.Serial(port='COM3', baudrate=9600, timeout=10)
    #         self.ser.open()
    #         if self.ser and self.ser.in_waiting > 0:
    #             my_data = self.read_until_delimiter()
    #             ## condition to check formating of data i.e. data[0]=='*'
    #             # Print the received data for debugging
    #             print(f"Data received: {my_data}")
    #             # if data is TEMP
    #             if my_data[1:3]=='T:':
    #                 self.rx_temperature = int(my_data[3:len(my_data)-1])
    #             #if data is FORCE
    #             elif my_data[1:3]=='F:':
    #                 self.rx_force=(int(my_data[3:len(my_data)-1]))
    #                 # print(self.rx_force)
    #             #if data is MODE
    #             elif my_data[1:3]=='M:':
    #                 print("Data received:", my_data)
    #                 if my_data[3:5]=='RD':
    #                     self.mode="READY"
    #                 elif my_data[3:5]=='ST':
    #                     self.mode="PROCESSING"
    #                 elif my_data[3:5]=='PS':
    #                     self.mode="PAUSED"
    #                 elif my_data[3:5]=='HM':
    #                     self.mode="HOMING"
    #             self.label_38.setText("Status:  " + self.mode)
    #         self.handle_screen5()
    #     except serial.SerialException as e:
    #         print(f"SerialException: {e}")  
  
  
 


    # def settings(self):
    #     try:
    #         # Retrieve current values from input fields
    #         current_temperature = self.input_14.text()
    #         current_distance = self.input_12.text()
    #         current_speed = self.input_13.text()

    #         # Define protocols
    #         protocol_temperature = f"*3:1:{current_temperature}#"
    #         protocol_distance = f"*3:2:{current_distance}#"
    #         protocol_speed = f"*3:3:{current_speed}#"
    #         protocol_save = "*3:4:1#"

    #         # Function to send data and print feedback
    #         def send_and_log(protocol):
    #             print(f"Sending protocol to MCU: {protocol}")
    #             self.tx_data(protocol, port='mcu')
    #             time.sleep(1)
    #             mcu_feedback = self.rx_data()
    #             # time.sleep(1)
    #             print(f"Received feedback from MCU: {mcu_feedback}")
    #             return mcu_feedback

    #         # Send temperature, distance, and speed protocols and log feedback
    #         send_and_log(protocol_temperature)
    #         send_and_log(protocol_distance)
    #         send_and_log(protocol_speed)

    #         # Send the save protocol and check the feedback
    #         feedback = send_and_log(protocol_save)

    #         # Check if the expected feedback is received
    #         if feedback == "*SET:SAV#":
    #             # Prepare data for JSON
    #             settings_data = {
    #                 "temperature": current_temperature,
    #                 "distance": current_distance,
    #                 "speed": current_speed
    #             }
    #             print("Data to save:", settings_data)  # Debug print

    #             # Save the values to a JSON file
    #             try:
    #                 with open("settings.json", "w") as settings_file:
    #                     json.dump(settings_data, settings_file)
    #                     print("Settings saved successfully.")  # Debug print

    #                 # Update label_38 to indicate success
    #                 self.label_38.setText("Saved")
    #                 self.label_38.setStyleSheet("color:#009900;")
    #             except Exception as e:
    #                 print(f"Error saving settings: {e}")  # Debug print

    #         else:
    #             # If feedback is not as expected, show an error message
    #             self.label_23.setText("Error: Failed to save settings.")
    #             self.label_23.setStyleSheet("color:#FF0000;")

    #         # Regardless of feedback for the save command, update label_23
    #         self.label_23.setText("Settings have been processed.")
    #         self.label_23.setStyleSheet("color:#009900;")

    #     except Exception as e:
    #         print(f"Error occurred during settings update: {e}")
    #         self.label_23.setText("Error: An unexpected error occurred.")
    #         self.label_23.setStyleSheet("color:#FF0000;")
    # def settings(self): 
    #     try:
    #         # Retrieve current values from input fields
    #         current_temperature = self.input_14.text().strip()
    #         current_distance = self.input_12.text().strip()
    #         current_speed = self.input_13.text().strip()

    #         # Check if any field is empty
    #         if not current_temperature or not current_distance or not current_speed:
    #             # Display dialog box with error message
    #             QMessageBox.warning(self, "Incomplete Settings", "Fill all the fields to submit the settings!")
    #             return  # Stop further execution if fields are incomplete

    #         # Define protocols
    #         protocol_temperature = f"*3:1:{current_temperature}#"
    #         protocol_distance = f"*3:2:{current_distance}#"
    #         protocol_speed = f"*3:3:{current_speed}#"
    #         protocol_save = "*3:4:1#"

    #         # Function to send data and print feedback
    #         def send_and_log(protocol):
    #             print(f"Sending protocol to MCU: {protocol}")
    #             self.tx_data(protocol, port='mcu')
    #             time.sleep(1)
    #             mcu_feedback = self.rx_data()
    #             print(f"Received feedback from MCU: {mcu_feedback}")
    #             return mcu_feedback

    #         # Send temperature, distance, and speed protocols and log feedback
    #         send_and_log(protocol_temperature)
    #         send_and_log(protocol_distance)
    #         send_and_log(protocol_speed)

    #         # Send the save protocol and check the feedback
    #         feedback = send_and_log(protocol_save)

    #         # Check if the expected feedback is received
    #         if feedback == "*SET:SAV#":
    #             # Prepare data for JSON
    #             settings_data = {
    #                 "temperature": current_temperature,
    #                 "distance": current_distance,
    #                 "speed": current_speed
    #             }
    #             print("Data to save:", settings_data)  # Debug print

    #             # Save the values to a JSON file
    #             try:
    #                 with open("settings.json", "w") as settings_file:
    #                     json.dump(settings_data, settings_file)
    #                     print("Settings saved successfully.")  # Debug print

    #                 # Update label_38 to indicate success
    #                 self.label_38.setText("Saved")
    #                 self.label_38.setStyleSheet("color:#009900;")
    #             except Exception as e:
    #                 print(f"Error saving settings: {e}")  # Debug print

    #         else:
    #             # If feedback is not as expected, show an error message
    #             self.label_23.setText("Error: Failed to save settings.")
    #             self.label_23.setStyleSheet("color:#FF0000;")

    #         # Regardless of feedback for the save command, update label_23
    #         self.label_23.setText("Settings have been processed.")
    #         self.label_23.setStyleSheet("color:#009900;")

    #     except Exception as e:
    #         print(f"Error occurred during settings update: {e}")
    #         self.label_23.setText("Error: An unexpected error occurred.")
    #         self.label_23.setStyleSheet("color:#FF0000;")
            
    # def settings(self): 
    #     try:
    #         # Retrieve current values from input fields
    #         current_temperature = self.input_14.text().strip()
    #         current_distance = self.input_12.text().strip()
    #         current_speed = self.input_13.text().strip()

    #         # Check if any field is empty
    #         if not current_temperature or not current_distance or not current_speed:
    #             QMessageBox.warning(self, "Incomplete Settings", "Fill all the fields to submit the settings!")
    #             return

    #         # Define protocols
    #         protocol_temperature = f"*3:1:{current_temperature}#"
    #         protocol_distance = f"*3:2:{current_distance}#"
    #         protocol_speed = f"*3:3:{current_speed}#"
    #         protocol_save = "*3:4:1#"

    #         # Function to send data and log feedback
    #         def send_and_log(protocol):
    #             try:
    #                 print(f"Sending protocol to MCU: {protocol}")
    #                 self.tx_data(protocol, port='mcu')
    #                 time.sleep(1)  # Consider replacing this with a QTimer
    #                 mcu_feedback = self.rx_data()

    #                 if mcu_feedback is None:
    #                     print("No response from MCU.")
    #                     self.label_23.setText("Error: No response received.")
    #                     self.label_23.setStyleSheet("color:#FF0000;")
    #                     return None

    #                 print(f"Received feedback from MCU: {mcu_feedback}")
    #                 return mcu_feedback
    #             except Exception as e:
    #                 print(f"Error communicating with MCU: {e}")
    #                 self.label_23.setText("Communication error with MCU.")
    #                 self.label_23.setStyleSheet("color:#FF0000;")
    #                 return None

    #         # Send temperature, distance, and speed settings
    #         send_and_log(protocol_temperature)
    #         send_and_log(protocol_distance)
    #         send_and_log(protocol_speed)

    #         # Send the save protocol and check feedback
    #         feedback = send_and_log(protocol_save)

    #         if feedback == "*SET:SAV#":
    #             # Prepare JSON data
    #             settings_data = {
    #                 "temperature": current_temperature,
    #                 "distance": current_distance,
    #                 "speed": current_speed
    #             }

    #             try:
    #                 with open("settings.json", "w") as 
    # _file:
    #                     json.dump(settings_data, settings_file)
    #                     print("Settings saved successfully.")

    #                 # Indicate success on UI
    #                 self.label_38.setText("Saved")
    #                 self.label_38.setStyleSheet("color:#009900;")
    #                 self.label_23.setText("Settings have been processed.")
    #                 self.label_23.setStyleSheet("color:#009900;")
    #             except Exception as e:
    #                 print(f"Error saving settings: {e}")
    #                 self.label_23.setText("Error: Could not save settings.")
    #                 self.label_23.setStyleSheet("color:#FF0000;")
    #         else:
    #             self.label_23.setText("Error: Failed to save settings.")
    #             self.label_23.setStyleSheet("color:#FF0000;")

    #     except Exception as e:
    #         print(f"Error occurred during settings update: {e}")
    #         self.label_23.setText("Error: An unexpected error occurred.")
    #         self.label_23.setStyleSheet("color:#FF0000;")
        
    
    # def settings(self):
    #     try:
    #         self.button_17.setEnabled(False)
    #         self.button_A.setEnabled(False)
            
    #         # Retrieve current values from input fields
    #         current_temperature = self.input_14.text().strip()
    #         current_distance = self.input_12.text().strip()
    #         current_speed = self.input_13.text().strip()

    #         # Check if any field is empty
    #         if not current_temperature or not current_distance or not current_speed:
    #             QMessageBox.warning(self, "Incomplete Settings", "Fill all the fields to submit the settings!")
    #             return

    #         # Define protocols
    #         protocol_temperature = f"*3:1:{current_temperature}#"
    #         protocol_distance = f"*3:2:{current_distance}#"
    #         protocol_speed = f"*3:3:{current_speed}#"
    #         protocol_save = "*3:4:1#"

    #         # Function to send data and log feedback
    #         def send_and_log(protocol):
    #             try:
    #                 print(f"Sending protocol to MCU: {protocol}")
    #                 self.tx_data(protocol, port='mcu')
    #                 time.sleep(1)  # Consider replacing this with a QTimer
    #                 mcu_feedback = self.rx_data()

    #                 if mcu_feedback is None:
    #                     raise ValueError("No response from MCU.")

    #                 print(f"Received feedback from MCU: {mcu_feedback}")
    #                 return mcu_feedback
    #             except Exception as e:
    #                 print(f"Error communicating with MCU: {e}")
    #                 return None

    #         # Send temperature, distance, and speed settings
    #         if not send_and_log(protocol_temperature):
    #             QMessageBox.critical(self, "Error", "Failed to update temperature settings!")
    #             return

    #         if not send_and_log(protocol_distance):
    #             QMessageBox.critical(self, "Error", "Failed to update distance settings!")
    #             return

    #         if not send_and_log(protocol_speed):
    #             QMessageBox.critical(self, "Error", "Failed to update speed settings!")
    #             return

    #         # Send the save protocol
    #         self.tx_data(protocol_save, port='mcu')

    #         # Wait for "*SET:SAV#" within 10 seconds
    #         received_correct_feedback = False
    #         for _ in range(10):  # Loop for 10 seconds
    #             time.sleep(1)  # Wait 1 second before checking again
    #             feedback = self.rx_data()
    #             print(f"Checking feedback: {feedback}")

    #             if feedback == "*SET:SAV#":
    #                 received_correct_feedback = True
    #                 break  # Exit loop early if we get the correct response

    #         if received_correct_feedback:
    #             settings_data = {
    #                 "temperature": current_temperature,
    #                 "distance": current_distance,
    #                 "speed": current_speed
    #             }

    #             try:
    #                 with open("settings.json", "w") as settings_file:
    #                     json.dump(settings_data, settings_file)
    #                     print("Settings saved successfully.")

    #                 # Indicate success on UI
    #                 self.label_38.setText("Settings updated successfully!")
    #                 self.label_38.setStyleSheet("color:#009900;")
    #                 self.label_23.setText("Settings have been processed.")
    #                 self.label_23.setStyleSheet("color:#009900;")

    #                 QMessageBox.information(self, "Success", "Settings saved successfully!")
    #             except Exception as e:
    #                 print(f"Error saving settings: {e}")
    #                 QMessageBox.critical(self, "Error", "Could not save settings!")
    #         else:
    #             QMessageBox.critical(self, "Error", "No response from MCU! Settings not saved.")

    #     except Exception as e:
    #         print(f"Error occurred during settings update: {e}")
    #         QMessageBox.critical(self, "Critical Error", "An unexpected error occurred!")  

    #     finally:
    #             # Re-enable the button after the function completes
    #             self.button_17.setEnabled(True)
    #             self.button_A.setEnabled(True)
        
    # # Function to load the settings from the JSON file at startup
    # def load_settings(self):
    #     if os.path.exists("settings.json"):
    #         try:
    #             with open("settings.json", "r") as settings_file:
    #                 settings_data = json.load(settings_file)
    #                 self.input_14.setText(settings_data.get("temperature", ""))
    #                 self.input_12.setText(settings_data.get("distance", ""))
    #                 self.input_13.setText(settings_data.get("speed", ""))
    #                 print("Settings loaded successfully:", settings_data)  # Debug print
    #         except Exception as e:
    #             print(f"Error loading settings: {e}")  # Debug print



        
    def tx_data(self, data, port='supply'):
        try:
            # Determine the correct serial object based on the port parameter
            ser = self.ser if port == 'supply' else self.ser_2
            
            if ser and ser.is_open:
                logging.info(f"Transmitting data on {ser.port}: {data}")
                print(f"Transmitting data on {ser.port}: {data}")
                
                # Write data to the selected serial port
                ser.write(data.encode())
            else:
                logging.error(f"Serial port for {port} not open.")
                print(f"Serial port for {port} not open.")
        
        except serial.SerialException as e:
            logging.error(f"Serial communication error on {port}: {e}")
            print(f"Serial communication error on {port}: {e}")
        
        except Exception as e:
            logging.error(f"Unexpected error on {port}: {e}")
            print(f"Unexpected error on {port}: {e}")

            
            
    def rx_data(self):
        feedback = None  # Initialize feedback variable
        try:
            # Check for data from the power supply
            if self.ser and self.ser.is_open:
                if self.ser.in_waiting > 0:
                    my_data = self.read_until_delimiter(self.ser)
                    print(f"Data received from supply: {my_data}")
                    logging.info(f"Data received from supply: {my_data}")
                    self.process_received_data(my_data, port='supply')

            # Check for data from the MCU
            if self.ser_2 and self.ser_2.is_open:
                if self.ser_2.in_waiting > 0:
                    my_data = self.read_until_delimiter(self.ser_2)
                    # print(f"Data received from MCU: {my_data}")
                    logging.info(f"Data received from MCU: {my_data}")
                    self.process_received_data(my_data, port='mcu')
                    feedback = my_data  # Store feedback from MCU

        except serial.SerialException as e:
            logging.error(f"SerialException: {e}")
            print(f"SerialException: {e}")
        # except Exception as e:
        #     # logging.error(f"Error during data reception: {e}")
        #     print(f"Error during data reception: {e}")
        finally:
            return feedback  # Return the received feedback




    # def process_received_data(self, data, port):
    #     if port == 'supply':
    #         if "VOLT?" in data:
    #             voltage_value = float(data.split()[-1])  # Extract voltage
    #             print(f"Voltage data received: {voltage_value}")
    #             self.voltage_data.append(voltage_value)  # Store voltage value

    #         elif "MEAS:CURR?" in data:
    #             current_value = float(data.split()[-1])  # Extract current
    #             print(f"Current data received: {current_value}")
    #             self.current_data.append(current_value)  # Store current value

    #     elif port == 'mcu':
    #         # Check for MCU-specific protocols
    #         if "*PRS:STR#" in data:
    #             print("MCU acknowledged process start with *PRS:STR#")
    #         elif "*PRS:CMP#" in data:
    #             print("MCU acknowledged process complete with *PRS:CMP#")
    #         elif "*PRS:STP#" in data:
    #             print("MCU acknowledged process pause with *PRS:STP#")
            
    #         # Check for motor feedback for manual motor commands
    #         elif "*MAN:MOT#" in data:
    #             print("MCU acknowledged motor command with *MAN:MOT#")

    #         # Check for real-time temperature data (*1:2:temperature_value#)
    #         elif data.startswith("*1:2:"):
    #             try:
    #                 # Extract the temperature value
    #                 temperature_value = data.split(":")[2].replace("#", "")  # Get the temperature value
    #                 self.label_37.setText(f" {temperature_value} ")
    #                 self.label_48.setText(f" {temperature_value} ")
    #                 print(f" {temperature_value} °C")  # Print for confirmation
    #             except IndexError:
    #                 print("Error: Invalid temperature data format received.")

    # def process_received_data(self, data, port):
    #     if port == 'supply':
    #         if "VOLT?" in data:
    #             voltage_value = float(data.split()[-1])  
    #             print(f"Voltage data received: {voltage_value}")
    #             self.voltage_data.append(voltage_value)  

    #         elif "MEAS:CURR?" in data:
    #             current_value = float(data.split()[-1])  
    #             print(f"Current data received: {current_value}")
    #             self.current_data.append(current_value)  

    #     elif port == 'mcu':
    #         if "*PRS:STR#" in data:
    #             print("MCU acknowledged process start with *PRS:STR#")
    #         elif "*PRS:CMP#" in data:
    #             print("MCU acknowledged process complete with *PRS:CMP#")
    #         elif "*PRS:STP#" in data:
    #             print("MCU acknowledged process pause with *PRS:STP#")
    #         elif "*MAN:MOT#" in data:
    #             print("MCU acknowledged motor command with *MAN:MOT#")

    #         # Handle real-time temperature data
    #         elif data.startswith("*1:2:"):
    #             try:
    #                 print(f"Received raw data: {data}")  # Debugging line

    #                 # Extract the temperature value
    #                 temperature_value = data.split(":")[2].replace("#", "").strip()
                    
    #                 print(f"Extracted Temperature: '{temperature_value}'")  # Debugging line
                    
    #                 if hasattr(self, 'label_37') and hasattr(self, 'label_48'):
    #                     self.label_37.setText(f" {temperature_value} ")
                        
                        
    #                     # Force UI Update
    #                     self.label_37.repaint()
                    

    #                     # Ensure updates in the main thread
    #                     from PyQt5.QtCore import QMetaObject, Qt
    #                     QMetaObject.invokeMethod(self.label_48, "setText", Qt.QueuedConnection, f" {temperature_value} ")

    #                 else:
    #                     print("Error: label_37 or label_48 is not initialized properly.")

    #             except IndexError:
    #                 print("Error: Invalid temperature data format received.")

    def process_received_data(self, data, port):
            logging.debug(f"Processing received data from {port}: {data}")
            if port == 'supply':
                if "VOLT?" in data:
                    try:
                        voltage_value = float(data.split()[-1])  # Extract voltage
                        logging.info(f"Voltage data received: {voltage_value}")
                        print(f"Voltage data received: {voltage_value}")
                        self.voltage_data.append(voltage_value)  # Store voltage value
                    except ValueError:
                        logging.error(f"Failed to parse voltage data: {data}")

                elif "MEAS:CURR?" in data:
                    try:
                        current_value = float(data.split()[-1])  # Extract current
                        logging.info(f"Current data received: {current_value}")
                        print(f"Current data received: {current_value}")
                        self.current_data.append(current_value)  # Store current value
                    except ValueError:
                        logging.error(f"Failed to parse current data: {data}")


            elif port == 'mcu':
                # Check for MCU-specific protocols
                if "*PRS:STR#" in data:
                    logging.info("MCU acknowledged process start with *PRS:STR#")
                    print("MCU acknowledged process start with *PRS:STR#")
                elif "*PRS:CMP#" in data:
                    logging.info("MCU acknowledged process complete with *PRS:CMP#")
                    print("MCU acknowledged process complete with *PRS:CMP#")
                elif "*PRS:STP#" in data:
                    logging.info("MCU acknowledged process pause with *PRS:STP#")
                    print("MCU acknowledged process pause with *PRS:STP#")
                
                # Check for motor feedback for manual motor commands
                elif "*MAN:MOT#" in data:
                    logging.info("MCU acknowledged motor command with *MAN:MOT#")
                    print("MCU acknowledged motor command with *MAN:MOT#")

                # Check for real-time temperature data (*1:2:temperature_value#)
                elif data.startswith("*1:2:"):
                    try:
                        # Extract the temperature value
                        self.temperature_value = data.split(":")[2].replace("#", "")  # Get the temperature value
                        logging.info(f"Temperature data received: {self.temperature_value} °C")
                        if self.screen == 6:
                            self.label_48.setText(f" {self.temperature_value} ")
                            logging.debug(f"Displayed {self.temperature_value} °C in Screen 6")
                            print(f" {self.temperature_value} °C in Screen 6")  # Print for confirmation
                        elif self.screen == 5:
                            self.label_37.setText(f" {self.temperature_value} ")
                            logging.debug(f"Displayed {self.temperature_value} °C in Screen 5")
                            print(f" {self.temperature_value} °C in Screen 5")  # Print for confirmation
                            # if not hasattr(self, 'temperature_message_shown'):
                            #     self.temperature_message_shown = False  # Initialize flag if not set

                            if float(self.temperature_value) >= float(self.input_14.text()) and not self.temperature_message_shown:
                                print(f"Set Temp: {self.input_14.text()}")
                                logging.info(f"Temperature threshold reached: {self.input_14.text()} °C")
                                QMessageBox.information(self, "Temperature Status", "Temperature is enough to start the process!")
                                self.temperature_message_shown = True  # Set flag to prevent showing again


                                
                        # print(f" {temperature_value} °C")  # Print for confirmation
                    except IndexError:
                        logging.error("Invalid temperature data format received.")
                        print("Error: Invalid temperature data format received.")

    
        # save function here

    # def tx_data(self,data):
    #     try:
    #         print("tx_data")
    #         self.ser.write(data.encode())
    #     except Exception as err:
    #         self.label_9.setText("ERROR: NO SERIAL PORT")
               
    def handle_screen5(self):
        logging.debug(f"Handling Screen 5 UI updates. Current mode: {self.mode}")

        if self.mode == "Complete":
            logging.info("Mode set to 'Complete'. Updating UI elements accordingly.")
            self.button_7.setEnabled(True)
            self.button_8.setEnabled(False)
            self.button_9.setEnabled(False)
            self.comboBox.setEnabled(True)
            self.comboBox.setEnabled(True)
            #self.button_A.setEnabled(True)
        elif self.mode == "Start":
            logging.info("Mode set to 'Start'. Updating UI elements accordingly.")
            self.button_7.setEnabled(False)
            self.button_8.setEnabled(True)
            self.button_9.setEnabled(True)
            self.comboBox.setEnabled(False)
            self.comboBox.setEnabled(False)
           # self.button_A.setEnabled(False)
           # self.button_A.setEnabled(False)
            self.display_plot()
        elif self.mode == "Stop":
            logging.info("Mode set to 'Stop'. Updating UI elements accordingly.")
            self.button_7.setEnabled(True)
            self.button_8.setEnabled(False)
            self.button_9.setEnabled(True)
            self.comboBox.setEnabled(True)
            self.comboBox.setEnabled(True)
           # self.button_A.setEnabled(False)
        # elif self.mode == "HOMING":
        #     self.button_7.setEnabled(False)
        #     self.button_8.setEnabled(False)
        #     self.button_9.setEnabled(False)
        #     self.button_A.setEnabled(False)

    # Prevent auto-selection of COM1 when clicking comboBox drop-down
    
    def load_comlist(self):
        logging.debug("Loading available COM ports for comboBox.")
        # Clear previous items
        self.comboBox.clear()
        self.comboBox.addItem("")  # Add empty item for default selection

        # Get available COM ports
        com_ports = serial.tools.list_ports.comports()

        # Add available COM ports to comboBox
        for port in com_ports:
            hwid = port.hwid  # Get the HWID string
            if f"SER=VCP120588" in hwid:  # Check if SER matches
                logging.info(f"Matching COM port found: {port.device}, Description: {port.description}, HWID: {port.hwid}")
                print(f"Match found! Port: {port.device}, Description: {port.description}, HWID: {port.hwid}")
                self.comboBox.addItem(f"{port.device}")

    def load_comlist_2(self):
        logging.debug("Loading available COM ports for comboBox_2.")
        # Clear previous items
        self.comboBox_2.clear()
        self.comboBox_2.addItem("")  # Add empty item for default selection

        # Get available COM ports
        com_ports = serial.tools.list_ports.comports()

        # Add available COM ports to comboBox_2
        for port in com_ports:
            hwid = port.hwid  # Get the HWID string
            if f"SER=317C39553131" in hwid:  # Check if SER matches
                logging.info(f"Matching COM port found: {port.device}, Description: {port.description}, HWID: {port.hwid}")
                print(f"Match found! Port: {port.device}, Description: {port.description}, HWID: {port.hwid}")
                self.comboBox_2.addItem(f"{port.device}")

        

    def read_until_delimiter(self, ser):
        
        # Set delimiter based on the serial port (power supply = '\n', MCU = '#')
        logging.debug(f"Reading data from serial port {ser.port}. Delimiter set to: {delimiter}")
        print(f"Reading data from serial port {ser.port}. Delimiter set to: {delimiter}")
        # delimiter = b'\n' if ser == self.ser else b'#'
        delimiter = b'#'
        
        # Collect incoming data
        data = bytearray()
        
        while True:
            if ser.in_waiting > 0:
                byte = ser.read(1)  # Read one byte at a time
                data.extend(byte)
                if byte == delimiter:
                    break  # Exit loop when delimiter is encountered
                    
        # Decode and return the complete data as a string
        logging.info(f"Received data from serial port {ser.port}: {data.decode.strip()}")
        return data.decode('utf-8')


    def set_serial(self):
        try:
            # Get the selected port from comboBox (power supply)
            comPort = self.comboBox.currentText()
            logging.debug(f"Selected power supply COM port: {comPort}")

            # If an empty port is selected, close the serial connection if it's open
            if comPort == "":
                if self.ser and self.ser.is_open:
                    self.ser.close()  # Close the port if it's already open
                    logging.info("Power Supply serial port closed.")
                    print("Power Supply serial port closed.")
                    self.label_12.setText("")

                return  # Exit the method if no port is selected

            # If a port is selected and not already opened, open the serial connection
            if self.ser is None or not self.ser.is_open or self.ser.port != comPort:
                if self.ser and self.ser.is_open:
                    self.ser.close()  # Close the port if it's already open
                    logging.debug("Closing previously open Power Supply port.")

                self.ser = serial.Serial(port=comPort, baudrate=9600, timeout=10000)
                logging.info(f"Power Supply serial port opened: {self.ser.port}")
                print(f"Power Supply serial port opened: {self.ser.port}")
                self.label_12.setText("")
                self.tx_data("*IDN?\n")
                logging.debug("Sent identification command to Power Supply.")
                print("Identified")
            else:
                logging.error("Attempted to open an already open Power Supply port.")
                self.label_12.setText("No port selected or already open for power supply")

            # Check for errors between the selected ports (power supply and MCU)
            self.check_ports_and_error()

        except Exception as e:
            # Handle any errors during serial port opening
            logging.error(f"Error opening Power Supply port: {e}")
            self.label_12.setText(f"Error: {e}")

    def handle_comboBox_2_change(self):
        try:
            # Get the selected port from comboBox_2 (MCU)
            comPort2 = self.comboBox_2.currentText()
            logging.debug(f"Selected MCU COM port: {comPort2}")

            # If an empty port is selected, close the serial connection if it's open
            if comPort2 == "":
                if self.ser_2 and self.ser_2.is_open:
                    self.ser_2.close()  # Close the port if it's already open
                    logging.info("MCU serial port closed.")
                    print("MCU serial port closed.")
                    self.label_9.setText("")

                return  # Exit the method if no port is selected

            # If a port is selected and not already opened, open the serial connection
            if self.ser_2 is None or not self.ser_2.is_open or self.ser_2.port != comPort2:
                if self.ser_2 and self.ser_2.is_open:
                    self.ser_2.close()  # Close the port if it's already open
                    logging.debug("Closing previously open MCU port.")

                self.ser_2 = serial.Serial(port=comPort2, baudrate=9600, timeout=10000)
                print(f"MCU serial port opened: {self.ser_2.port}")
                logging.info(f"MCU serial port opened: {self.ser_2.port}")
                self.label_9.setText("")
            else:
                self.label_9.setText("No port selected or already open for MCU")
                logging.error("Attempted to open an already open MCU port.")

            # Check for errors between the selected ports (power supply and MCU)
            self.check_ports_and_error()

        except Exception as e:
            # Handle any errors during serial port opening
            logging.error("Error opening MCU COM Port: MCU COM Port in use")
            self.label_9.setText(f"Error: MCU COM Port in use")



    def check_ports_and_error(self):
        # Check if the power supply or MCU port is empty
        if self.comboBox.currentText() == "" or self.comboBox_2.currentText() == "":
            logging.debug("One or both COM ports are empty, clearing errors.")
            # Clear error messages if either port is empty
            self.label_12.setText("")
            self.label_9.setText("")
            return  # Exit the method as there's no conflict

        # Ensure the selected ports for power supply and MCU are not the same
        if self.ser and self.ser_2 and self.ser.port == self.ser_2.port:
            logging.error("Power Supply and MCU ports are the same. Closing both ports.")
            # Display error message for both labels
            self.label_12.setText("Port Error")
            self.label_9.setText("Port Error")

            # Close both serial ports to prevent communication errors
            if self.ser.is_open:
                self.ser.close()
            if self.ser_2.is_open:
                self.ser_2.close()
        else:
            # If the ports are different, clear the error messages
            logging.debug("Power Supply and MCU ports are different. No errors.")
            self.label_12.setText("")
            self.label_9.setText("")



            
            
    def handle_manual(self):
        logging.info("Navigating to Screen 6")
        print("on screen 6")
        self.init_screen_6()
        # if not self.comboBox_2.currentText():
        #     QMessageBox.critical(self, "Error", "Please select a COM port for MCU to start the process.")
        #     return  # Exit the function if no port is selected
        
        # self.label_48.setText(f" {temperature_value} ")
        # print(f" {temperature_value} °C")  # Print for confirmation

  

    def motor_forward_pressed(self):
        # Set the pressed icon when the button is clicked
        print("Motor forward pressed")
        logging.info("Motor forward pressed")
        self.button_28.setIcon(QIcon(base_path + "/rsc/forward_pressed.png"))  # Set forward pressed icon

        # Send the command to move forward
        cmd = "*2:2:0#"
        logging.info(f"Sending command: {cmd}")
        print(f"Sending command: {cmd}")
        self.tx_data(cmd, port='mcu')  # Send the command to the MCU

        # Receive and validate MCU feedback
        feedback = self.rx_data()
        if feedback == "*MAN:MOT#":
            logging.info("Feedback received: Motor forward command successful")
            print("Feedback received: Motor forward command successful")
        else:
            logging.error(f"Unexpected feedback from MCU: {feedback}")
            print(f"Unexpected feedback from MCU: {feedback}")
            self.label_23.setText("Error: Failed to start motor forward.")
            self.label_23.setStyleSheet("color:#FF0000;")

        # Use QTimer to set the normal forward icon after a short delay
        QTimer.singleShot(200, lambda: self.button_28.setIcon(QIcon(base_path + "/rsc/forward.png")))


    def motor_reverse_pressed(self):
        logging.info("Motor reverse pressed")
        # Set the pressed icon when the button is clicked
        print("Motor reverse pressed")
        self.button_26.setIcon(QIcon(base_path + "/rsc/reverse_pressed.png"))  # Set reverse pressed icon
        
        # Disable the forward button (button_13) for 3 seconds
        # self.button_28.setEnabled(False)
        # print("Forward button disabled for 3 seconds")
        
        # Re-enable the forward button after a delay
        # QTimer.singleShot(3000, lambda: self.button_28.setEnabled(True))
        # print("Forward button will be re-enabled after 3 seconds")

        # Send the command to reverse
        cmd = "*2:2:1#"
        logging.info(f"Sending command: {cmd}")
        print(f"Sending command: {cmd}")
        self.tx_data(cmd, port='mcu')  # Send the command to the MCU

        # Receive and validate MCU feedback
        feedback = self.rx_data()
        if feedback == "*MAN:MOT#":
            logging.info("Feedback received: Motor reverse command successful")
            print("Feedback received: Motor reverse command successful")
        else:
            logging.error(f"Unexpected feedback from MCU: {feedback}")
            print(f"Unexpected feedback from MCU: {feedback}")
            self.label_23.setText("Error: Failed to start motor reverse.")
            self.label_23.setStyleSheet("color:#FF0000;")

        # Use QTimer to set the normal reverse icon after a short delay
        QTimer.singleShot(200, lambda: self.button_26.setIcon(QIcon(base_path + "/rsc/reverse.png")))


    def handle_heater(self):
        self.heater = not self.heater  # Toggle the heater state
        if self.heater:
            cmd = "*2:1:1#"  # Command to turn the heater ON
            logging.info(f"Sending command: {cmd}")
            print(f"Sending command: {cmd}")
            self.tx_data(cmd, port='mcu')  # Send the command to the MCU
            
            time.sleep(0.1)  # Small delay to allow for feedback
            feedback = self.rx_data()  # Check for feedback
            logging.info(f"Expected feedback: {feedback}")
            print(f"Expected feedback: *MAN:HTR#")
            if feedback:
                logging.info(f"Actual feedback: {feedback}")
                print(f"Actual feedback: {feedback}")
            else:
                logging.error("No feedback received.")
                print("No feedback received.")
            
            # Update button state
            self.button_27.setText("")
            self.button_27.setIcon(QIcon(base_path+"/rsc/cttm_heater_pressed.png"))
        else:
            cmd = "*2:1:0#"  # Command to turn the heater OFF
            print(f"Sending command: {cmd}")
            self.tx_data(cmd, port='mcu')  # Send the command to the MCU
            
            time.sleep(0.1)  # Small delay to allow for feedback
            feedback = self.rx_data()  # Check for feedback
            print(f"Expected feedback: *MAN:HTR#")
            if feedback:
                print(f"Actual feedback: {feedback}")
            else:
                print("No feedback received.")
            
            # Update button state
            self.button_27.setText("")
            self.button_27.setIcon(QIcon(base_path+"/rsc/cttm_heater.png"))
        logging.info(f"Heater state: {'ON' if self.heater else 'OFF'}")
        print("Heater state:", "ON" if self.heater else "OFF")
    
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    # window.showFullScreen()
    window.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()