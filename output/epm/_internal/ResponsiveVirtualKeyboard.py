import sys, os
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QLineEdit, QVBoxLayout, QPushButton
from PyQt5 import uic
from PyQt5.QtWidgets import QToolButton

base_path = "."

class ResponsiveVirtualKeyboard(QMainWindow):
    def __init__(self, input_field, parent=None):
        super().__init__(parent)
        self.setGeometry(970,452,500,400)
        
        base_path = os.path.dirname(os.path.abspath(__file__))  # Get current script directory
        ui_file = os.path.join(base_path, "Virtual_Keyboard.ui")  # Construct absolute path

        uic.loadUi(ui_file, self)  # Load UI file

        self.input_field = input_field
        self.caps_lock_on = False

        self.buttons = self.findChildren(QToolButton)
        for button in self.buttons:
            button.clicked.connect(self.button_pressed)

    def button_pressed(self):
        sender = self.sender()
        if not sender:
            return

        key = sender.text().strip()

        if key.lower() == "capslock":
            self.toggle_caps_lock()
            return  # Prevent further execution
        elif key == "<--":
            self.backspace()
        elif key == "Enter":
            self.close()  # Close the keyboard when Enter is pressed
        elif key == "Space":
            self.insert_text(" ")
        else:
            if self.caps_lock_on and key.isalpha():
                key = key.upper()
            self.insert_text(key)

    def insert_text(self, text):
        current_text = self.input_field.text()
        self.input_field.setText(current_text + text)

    def backspace(self):
        current_text = self.input_field.text()
        self.input_field.setText(current_text[:-1])

    def toggle_caps_lock(self):
        self.caps_lock_on = not self.caps_lock_on
        for button in self.buttons:
            text = button.text().strip()
            if len(text) == 1 and text.isalpha():  # Ensure it's a single letter
                button.setText(text.upper() if self.caps_lock_on else text.lower())
                
    # def close_keyboard(self):
    #     # # Close the keyboard unconditionally
    #     # self.main_window.keyboard_open = False  # Reset flag on close
    #     # self.accept()  # Use accept() to properly close the QDialog
    #     self.close()
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Main Window with Virtual Keyboard")
        self.setGeometry(100, 100, 400, 200)

        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText("Click to type...")
        self.input_field.setGeometry(50, 50, 300, 40)
        self.input_field.mousePressEvent = self.show_virtual_keyboard  # Open keyboard on click

        self.keyboard = None

    def show_virtual_keyboard(self, event):
        if not self.keyboard or not self.keyboard.isVisible():
            self.keyboard = ResponsiveVirtualKeyboard(self.input_field, self)
            # self.keyboard.finished.connect(self.on_keyboard_closed)

            self.keyboard.show()
            
            
    # def on_keyboard_closed(self):
    #     self.keyboard_open = False  # Reset the flag when keyboard is closed
    #     self.keyboard_closed_manually = False
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
