from __future__ import division
import time
import RPi.GPIO as GPIO
import Adafruit_PCA9685


pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)

PWM_init = 300  # angle about 90°
PWM_Min = 100   # angle about 0°
PWM_Max = 500   # angle about 180°

Channel = 0   # PWM port number.

# Set the value of PWM to control rotation.
def servo_value(Channel, value):  # The value range is between 100-500.
    pwm.set_pwm(Channel, 0, value)

# Set the angle of pwm to control the rotation.
def servo_angle(Channel, angle):  # The angle range is between 0-180 .
    value = int(4096*((angle*11)+500)/2000+0.5) # Conversion angle value.
    pwm.set_pwm(Channel, 0, value)

if __name__ == "__main__": 
    
    while True:
        servo_angle(0, 0)   # Servo of port0 Rotate to 0 degrees.
        time.sleep(1)
        servo_angle(0, 90)  # Rotate to 90 degrees.
        time.sleep(1)
        servo_angle(0, 180) # Rotate to 180 degrees.
        time.sleep(1)



