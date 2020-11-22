import RPi.GPIO as GPIO

from constants import GREEN_DIODE_PIN, YELLOW_DIODE_PIN, RED_DIODE_PIN, BUZZER_PIN

GPIO.setup(GREEN_DIODE_PIN, GPIO.OUT)
GPIO.setup(YELLOW_DIODE_PIN, GPIO.OUT)
GPIO.setup(RED_DIODE_PIN, GPIO.OUT)
GPIO.setup(BUZZER_PIN, GPIO.OUT)


def indicate_ok():
    GPIO.output(GREEN_DIODE_PIN, GPIO.HIGH)
    GPIO.output(YELLOW_DIODE_PIN, GPIO.LOW)
    GPIO.output(RED_DIODE_PIN, GPIO.LOW)
    GPIO.output(BUZZER_PIN, GPIO.LOW)


def indicate_warn():
    GPIO.output(GREEN_DIODE_PIN, GPIO.HIGH)
    GPIO.output(YELLOW_DIODE_PIN, GPIO.LOW)
    GPIO.output(RED_DIODE_PIN, GPIO.LOW)
    GPIO.output(BUZZER_PIN, GPIO.LOW)


def indicate_critical():
    GPIO.output(GREEN_DIODE_PIN, GPIO.HIGH)
    GPIO.output(YELLOW_DIODE_PIN, GPIO.LOW)
    GPIO.output(RED_DIODE_PIN, GPIO.LOW)
    GPIO.output(BUZZER_PIN, GPIO.LOW)
