import time
from pyfirmata2 import Arduino, OUTPUT

# Define the pin mappings
rs_pin = 12
enable_pin = 11
d4_pin = 5
d5_pin = 4
d6_pin = 3
d7_pin = 2
port = "COM9"
# Initialize the Arduino board
board = Arduino(port)

GRREN_LED = board.get_pin('d:8:o')
ORANGE_LED = board.get_pin('d:7:o')
RED_LED = board.get_pin('d:6:o')


# Set the pin modes
pins = [rs_pin, enable_pin, d4_pin, d5_pin, d6_pin, d7_pin]
for pin in pins:
    board.digital[pin].mode = OUTPUT

# Function to initialize the LCD
def lcd_init():
    # Wait for the LCD to power up (greater than 40ms)
    time.sleep(0.05)

    # Initialize the LCD in 4-bit mode
    lcd_command(0x03)
    time.sleep(0.0045)
    lcd_command(0x03)
    time.sleep(0.0045)
    lcd_command(0x03)
    time.sleep(0.0015)

    # Set 4-bit data, 2-line display, 5x8 font
    lcd_command(0x02)
    lcd_command(0x28)

    # Display on, cursor off, blink off
    lcd_command(0x0C)

    # Clear display
    lcd_command(0x01)
    time.sleep(0.002)

    # Set entry mode: increment cursor, no shift
    lcd_command(0x06)

# Function to send a command to the LCD
def lcd_command(cmd):
    board.digital[rs_pin].write(0)  # RS low for command
    board.digital[enable_pin].write(1)
    send_4bits(cmd >> 4)
    send_4bits(cmd)

# Function to send data to the LCD
def lcd_write(data):
    board.digital[rs_pin].write(1)  # RS high for data
    board.digital[enable_pin].write(1)
    send_4bits(data >> 4)
    send_4bits(data)

# Function to send 4 bits to the LCD
def send_4bits(data):
    for i in range(4):
        board.digital[pins[i + 2]].write((data >> i) & 1)
    board.digital[enable_pin].write(0)
    time.sleep(0.001)
    board.digital[enable_pin].write(1)

# Function to set the cursor position
def lcd_set_cursor(row, col):
    offset = [0x00, 0x40]  # Line offset for a 2-line display
    lcd_command(0x80 + offset[row] + col)

def printLCD(text, row=0, col=0):
    lcd_command(0x01)
    # Set the cursor position
    lcd_set_cursor(row, col)

    # Write each character of the text to the LCD
    for char in text:
        lcd_write(ord(char))
    time.sleep(0.1)

def red_led(TIME = 0.5):
    RED_LED.write(True)
    time.sleep(TIME)
    RED_LED.write(False)
    time.sleep(TIME)

def orange_led(TIME = 0.5):
    ORANGE_LED.write(True)
    time.sleep(TIME)
    ORANGE_LED.write(False)
    time.sleep(TIME)

def green_led(TIME = 0.5):
    GRREN_LED.write(True)
    time.sleep(TIME)
    GRREN_LED.write(False)
    time.sleep(TIME)

def printSYSEMSTART():
    lcd_command(0x01)
    RED_LED.write(True)
    ORANGE_LED.write(True)
    GRREN_LED.write(True)

    # Set the cursor position
    lcd_set_cursor(col=0, row=0)
    # Write each character of the text to the LCD
    for char in "SYSTEM IS":
        lcd_write(ord(char))
    # Set the cursor position
        
    lcd_set_cursor(col=3, row=1)
    # Write each character of the text to the LCD
    for char in "STARTING ...":
        lcd_write(ord(char))

    time.sleep(2)

    RED_LED.write(False)
    ORANGE_LED.write(False)
    GRREN_LED.write(False)
    lcd_command(0x01)

def image_error():
    RED_LED.write(True)

    # Set the cursor position
    lcd_set_cursor(col=0, row=0)
    # Write each character of the text to the LCD
    for char in "IMG .JPG or .PNG":
        lcd_write(ord(char))
    # Set the cursor position
        
    lcd_set_cursor(col=0, row=1)
    # Write each character of the text to the LCD
    for char in "ERROR #1":
        lcd_write(ord(char))

    time.sleep(100)

    RED_LED.write(False)
    ORANGE_LED.write(False)
    GRREN_LED.write(False)
    lcd_command(0x01)

def camera_error():
    lcd_command(0x01)
    ORANGE_LED.write(True)

    # Set the cursor position
    lcd_set_cursor(col=0, row=0)
    # Write each character of the text to the LCD
    for char in "Camera Not Found":
        lcd_write(ord(char))
    # Set the cursor position
        
    lcd_set_cursor(col=0, row=1)
    # Write each character of the text to the LCD
    for char in "ERROR #2":
        lcd_write(ord(char))

    time.sleep(100)

    RED_LED.write(False)
    ORANGE_LED.write(False)
    GRREN_LED.write(False)
    lcd_command(0x01)

def image_not_found():
    lcd_command(0x01)
    RED_LED.write(True)
    ORANGE_LED.write(True)
    # Set the cursor position
    lcd_set_cursor(col=0, row=0)
    # Write each character of the text to the LCD
    for char in "No Images Found":
        lcd_write(ord(char))
    # Set the cursor position
        
    lcd_set_cursor(col=0, row=1)
    # Write each character of the text to the LCD
    for char in "ERROR #3":
        lcd_write(ord(char))

    time.sleep(100)

    RED_LED.write(False)
    ORANGE_LED.write(False)
    GRREN_LED.write(False)
    lcd_command(0x01)

def endLCD():
    lcd_command(0x01)
    lcd_set_cursor(col=0, row=0)
    for char in "Check you mail":
        lcd_write(ord(char))
        
    lcd_set_cursor(col=0, row=1)
    for char in "Thank you!":
        lcd_write(ord(char))

def no_internet():
    lcd_command(0x01)
    GRREN_LED.write(True)
    ORANGE_LED.write(True)
    RED_LED.write(True)
    # Set the cursor position
    lcd_set_cursor(col=0, row=0)
    # Write each character of the text to the LCD
    for char in "No internet":
        lcd_write(ord(char))
    # Set the cursor position
        
    lcd_set_cursor(col=0, row=1)
    # Write each character of the text to the LCD
    for char in "ERROR #4":
        lcd_write(ord(char))

    time.sleep(100)
