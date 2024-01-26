import time
from pyfirmata2 import Arduino, OUTPUT

# Initialize the Arduino board
port = "COM3"
board = Arduino(port)

# Define the LCD pin
RS_LCD = 12
ENALBE_LCD = 11
D4_LCD = 5
D5_LCD = 4
D6_LCD = 3
D7_LCD = 2

# Set the LCD pin modes to output
LCD_pins = [RS_LCD, ENALBE_LCD, D4_LCD, D5_LCD, D6_LCD, D7_LCD]
for pin in LCD_pins:
    board.digital[pin].mode = OUTPUT

# Define the LED pin
GRREN_LED = 8
ORANGE_LED = 7
RED_LED = 6

# Set the LED pin modes to output
LED_pins = [GRREN_LED, ORANGE_LED, RED_LED]
for pin in LED_pins:
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
    board.digital[RS_LCD].write(False)  # RS low for command
    board.digital[ENALBE_LCD].write(True)
    send_4bits(cmd >> 4)
    send_4bits(cmd)

# Function to send data to the LCD
def lcd_write(data):
    board.digital[RS_LCD].write(True)  # RS high for data
    board.digital[ENALBE_LCD].write(True)
    send_4bits(data >> 4)
    send_4bits(data)

# Function to send 4 bits to the LCD
def send_4bits(data):
    for i in range(4):
        board.digital[LCD_pins[i + 2]].write((data >> i) & 1)
    board.digital[ENALBE_LCD].write(False)
    time.sleep(0.001)
    board.digital[ENALBE_LCD].write(True)

# Function to set the cursor position
def lcd_set_cursor(row, col):
    offset = [0x00, 0x40]

    # Set the cursor position based on the row and column
    position = offset[row] + col
    command = 0x80 | position
    lcd_command(command)


def printLCD(text, row=0, col=0):
    lcd_command(0x01)  # Clear display
    time.sleep(0.01)
    
    # Set the cursor position
    lcd_set_cursor(row, col)
    
    # Write each character of the text to the LCD
    for char in text:
        lcd_write(ord(char))
    time.sleep(0.01)


def red_led(TIME = 0.5):
    board.digital[RED_LED].write(True)
    time.sleep(TIME)
    board.digital[RED_LED].write(False)
    time.sleep(TIME)

def orange_led(TIME = 0.5):
    board.digital[ORANGE_LED].write(True)
    time.sleep(TIME)
    board.digital[ORANGE_LED].write(False)
    time.sleep(TIME)

def green_led(TIME = 0.5):
    board.digital[GRREN_LED].write(True)
    time.sleep(TIME)
    board.digital[GRREN_LED].write(False)
    time.sleep(TIME)

def printSYSEMSTART():
    lcd_command(0x01)

    board.digital[RED_LED].write(True)
    board.digital[ORANGE_LED].write(True)
    board.digital[GRREN_LED].write(True)

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

    board.digital[RED_LED].write(False)
    board.digital[ORANGE_LED].write(False)
    board.digital[GRREN_LED].write(False)
    lcd_command(0x01)

def image_error():
    lcd_command(0x01)

    # Set the cursor position
    lcd_set_cursor(col=0, row=0)
    board.digital[RED_LED].write(True)

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

    time.sleep(2)

    board.digital[RED_LED].write(False)
    board.digital[ORANGE_LED].write(False)
    board.digital[GRREN_LED].write(False)
    lcd_command(0x01)

def camera_error():
    lcd_command(0x01)
    board.digital[ORANGE_LED].write(True)

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

    time.sleep(2)

    board.digital[RED_LED].write(False)
    board.digital[ORANGE_LED].write(False)
    board.digital[GRREN_LED].write(False)
    lcd_command(0x01)

def image_not_found():
    lcd_command(0x01)
    board.digital[RED_LED].write(True)
    board.digital[ORANGE_LED].write(True)
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

    time.sleep(2)

    board.digital[RED_LED].write(False)
    board.digital[ORANGE_LED].write(False)
    board.digital[GRREN_LED].write(False)
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
    board.digital[GRREN_LED].write(True)
    board.digital[ORANGE_LED].write(True)
    board.digital[RED_LED].write(True)
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

    time.sleep(2)

def loading(executionTime, exitEvent):
    samplingRate = 10
    for i in range(samplingRate):

        if exitEvent.is_set():
            break

        printLCD(f"sending {i*samplingRate}%")
        time.sleep(executionTime / samplingRate)
