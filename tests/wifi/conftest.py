import pytest

from framework import StationDevice
from lib import DeviceDriver, find_device_port


@pytest.fixture(scope='session')
def device():
  port = find_device_port()

  driver = DeviceDriver(port)
  driver.open()

  device = StationDevice(driver)

  try:
    yield device
  finally:
    try:
      device.reboot()
    finally:
      driver.close()


@pytest.fixture(scope='module', autouse=True)
def prepare_wifi_state(request, device):
  if request.node.name == 'test_wifi_negative.py':
    device.wifi.disconnect()
