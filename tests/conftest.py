import pytest

from framework import StationDevice
from lib import DeviceDriver, find_device_port


@pytest.fixture(scope='session')
def device():
  # Open one serial connection for the entire pytest session.
  port = find_device_port()

  driver = DeviceDriver(port)
  driver.open()

  device = StationDevice(driver)

  try:
    yield device
  finally:
    # Always return the DUT to a known boot state after the whole test session.
    # The serial connection is closed even if the final reboot fails.
    try:
      device.reboot()
    finally:
      driver.close()


@pytest.fixture(scope='module', autouse=True)
def prepare_wifi_state(request, device):
  # Negative WiFi tests must start with the DUT disconnected.
  if request.node.name == 'test_wifi_negative.py':
    device.wifi.disconnect()
