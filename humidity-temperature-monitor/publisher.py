from paho.mqtt.client import Client
from datetime import datetime, timezone
import os
import logging

TOPIC = "sensors/#"

class Publisher:

    def __init__(self, location):
        self.client = Client()
        self.location = location

    def publish(self, humidity, temperature):
        payload_humidity = self.__build_payload("humidity", humidity)
        payload_temperature = self.__build_payload("temperature", temperature)

        try:
            logging.debug("Connectint to MQTT...")
            self.client.connect(os.environ["MQTT_ADDRESS"])
            self.client.publish(TOPIC, payload_temperature)
            self.client.publish(TOPIC, payload_humidity)
            logging.info("Published values on " + TOPIC)
            self.client.disconnect()
        except Exception as ex:
            logging.error(ex)

    def __build_payload(self, property, value):
        return '{"timestamp":"{}", "place": "{}", "property":"{}", "value":{:.4f}}'.format(datetime.now(), self.location, property, value)