from paho.mqtt.client import Client
from datetime import datetime
import logging

TOPIC = "sensors"

class Publisher:

    def __init__(self, server_address, location):
        self.client = Client()
        self.location = location
        self.address = server_address

    def publish(self, humidity, temperature):
        payload_humidity = self.__build_payload("humidity", humidity)
        payload_temperature = self.__build_payload("temperature", temperature)

        try:
            logging.debug("Connectint to MQTT...")
            self.client.connect(self.address)
            self.client.publish(TOPIC, payload_temperature)
            self.client.publish(TOPIC, payload_humidity)
            logging.info("Published values on " + TOPIC)
            self.client.disconnect()
        except Exception as ex:
            logging.error(ex)

    def __build_payload(self, prop, value):
        return '{{"timestamp":"{}", "place": "{}", "property":"{}", "value":{:.4f}}}'.format(datetime.now(), self.location, prop, value)