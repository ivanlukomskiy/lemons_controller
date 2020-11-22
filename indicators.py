import wiringpi as wp

from constants import GREEN_DIODE_PIN, YELLOW_DIODE_PIN, RED_DIODE_PIN, BUZZER_PIN

wp.wiringPiSetup()

wp.pinMode(GREEN_DIODE_PIN, 1)
wp.pinMode(YELLOW_DIODE_PIN, 1)
wp.pinMode(RED_DIODE_PIN, 1)
wp.pinMode(BUZZER_PIN, 1)


def indicate_ok():
    wp.digitalWrite(GREEN_DIODE_PIN, 1)
    wp.digitalWrite(YELLOW_DIODE_PIN, 0)
    wp.digitalWrite(RED_DIODE_PIN, 0)
    wp.digitalWrite(BUZZER_PIN, 0)


def indicate_warn():
    wp.digitalWrite(GREEN_DIODE_PIN, 1)
    wp.digitalWrite(YELLOW_DIODE_PIN, 0)
    wp.digitalWrite(RED_DIODE_PIN, 0)
    wp.digitalWrite(BUZZER_PIN, 0)


def indicate_critical():
    wp.digitalWrite(GREEN_DIODE_PIN, 1)
    wp.digitalWrite(YELLOW_DIODE_PIN, 0)
    wp.digitalWrite(RED_DIODE_PIN, 0)
    wp.digitalWrite(BUZZER_PIN, 0)
