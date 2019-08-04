#!/usr/bin/python3
"""
Python Practical Template
Keegan Crankshaw
Readjust this Docstring as follows:
Names: Mbaliyethemba Shangase
Student Number: SHNMBA004
Prac: Prac1
Date: 04/08/2019
"""

# import Relevant Librares
import RPi.GPIO as GPIO

import time #import sleep library

#set the buttons 
GPIO.setup(11,GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #incremental button
GPIO.setup(13,GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #decremental button

#set the LED
GPIO.setup(18,GPIO.OUT)  #LED3
GPIO.setup(16,GPIO.OUT)  #LED2
GPIO.setup(15,GPIO.OUT)  #LED1

#set the LED to low
GPIO.setup(18,GPIO.LOW)  #LED3
GPIO.setup(16,GPIO.LOW)  #LED2
GPIO.setup(15,GPIO.LOW)  #LED1

counter = 0;

# Logic that you write
def main():
    print("write your logic here")


# Only run the functions if 
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except Exception as e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)
