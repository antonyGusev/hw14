import re

import pytest

from config import PASSWORD, SSID


def test_scan_finds_networks(device):
    networks = device.wifi.scan()

    assert any(network.ssid == SSID for network in networks)


def test_connect_success(device):
  assert device.wifi.connect(SSID, PASSWORD).connected

  status = device.wifi.status()

  assert status.connected
  assert status.ssid == SSID
  assert status.ip is not None
  assert re.fullmatch(r'\d+\.\d+\.\d+\.\d+', status.ip)

@pytest.mark.xfail(reason='wrong "connected" status after disconnection')
def test_disconnect(device):
  # Previous test leaves the DUT connected; this test verifies that transition.
  assert device.wifi.disconnect()

  status = device.wifi.status()

  assert not status.connected


def test_credentials_survive_reboot(device):
  # Previous test leaves the DUT disconnected while credentials remain stored.
  device.reboot()

  # Empty input makes the device use the stored Wi-Fi credentials.
  assert device.wifi.connect().connected

  status = device.wifi.status()

  assert status.connected
  assert status.ssid == SSID
  assert status.ip is not None
  assert re.fullmatch(r'\d+\.\d+\.\d+\.\d+', status.ip)
  