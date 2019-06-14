from publisher import Publisher
from time import sleep
import logging
import os
import signal

DELAY = 5 * 60

log_level = os.environ.get("LOG_LEVEL", 20)
logging.basicConfig(format='[%(asctime)s][%(levelname)s] %(message)s', level=int(log_level))


if __name__ == '__main__':

    if not os.environ["LOCATION"]:
        raise Exception("LOCATION environment variable not specified.")

    publisher = Publisher(os.environ["LOCATION"])

    while True:
        logging.debug("Reading values from sensor.")
        # TODO: get sensor values
        logging.info("Publishing values.")
        # publisher publisher.publish(humidity=, temperature=)
        logging.debug("Waitting for next cycle.")
        sleep(DELAY)
