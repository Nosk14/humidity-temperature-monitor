from publisher import Publisher
from sensor import DHT22
from time import sleep
import RPi.GPIO as GPIO
import logging
import os

DELAY = 3 * 60
ERROR_DELAY = 30

log_level = os.environ.get("LOG_LEVEL", 20)
logging.basicConfig(format='[%(asctime)s][%(levelname)s] %(message)s', level=int(log_level))

GPIO.setmode(GPIO.BCM)

if __name__ == '__main__':

    if not os.environ["LOCATION"]:
        raise Exception("LOCATION environment variable not specified.")

    if not os.environ["MQTT_ADDRESS"]:
        raise Exception("MQTT_ADDRESS environment variable not specified.")

    publisher = Publisher(os.environ["MQTT_ADDRESS"], os.environ["LOCATION"])
    dht = DHT22(14)

    while True:
        logging.debug("Reading values from sensor.")
        h, t, error = dht.read_data()
        if error:
            logging.warning("Error reading sensor data.")
            sleep(ERROR_DELAY)
        else:
            logging.info("Publishing values.")
            publisher.publish(humidity=h, temperature=t)
            sleep(DELAY)
