import RPi.GPIO as GPIO
import time

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Define the PIN numbers for the light sensor and the LED
LIGHT_SENSOR_PIN = 4
LED_PIN = 3

# Set up the light sensor PIN as an input
GPIO.setup(LIGHT_SENSOR_PIN, GPIO.IN)

# Set up the LED PIN as an output
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:
        # Read the state of the light sensor
        light_state = GPIO.input(LIGHT_SENSOR_PIN)

        # Control the LED based on the light sensor state
        if light_state == GPIO.LOW:
            # Light is not present, turn on the LED
            GPIO.output(LED_PIN, GPIO.HIGH)
        else:
            # Light is present, turn off the LED
            GPIO.output(LED_PIN, GPIO.LOW)

        # Small delay to avoid rapid state changes
        time.sleep(1)

except KeyboardInterrupt:
    # Clean up GPIO settings on program exit
    GPIO.cleanup()
