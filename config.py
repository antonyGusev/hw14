import os

from dotenv import load_dotenv

load_dotenv()

SSID = os.environ['SSID']
PASSWORD = os.environ['PASSWORD']
LED_CHAR_UUID = os.environ['LED_CHAR_UUID']
