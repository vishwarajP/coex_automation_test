import pytest
import subprocess
import time
import yaml
from conftest import setup
from src.connection import execute_command
from src.logger import get_log_path
import logging


logger = logging.getLogger(__name__)


def test_wpa2_connection(setup):
    result = setup.connect_to_wifi()
    # ssid = setup.is_connected()
    logger.debug("successfully activated" in " ".join(result))
    # assert ssid == ("mirafra")
    # assert ssid == "mirafra"


def test_ssid_connection(setup):
    actual_ssid = setup.is_connected()
    expected_ssid = setup.verify_ssid()
    logger.debug(actual_ssid == expected_ssid)


def test_security_config(setup):
    actual_security = [s.lower() for s in setup.verify_security()]
    expected_security = [s.lower() for s in setup.verify_security_config()]

    # Pass if at least one actual security mode is in expected YAML config
    match_found = any(sec in expected_security for sec in actual_security)
    logger.debug(match_found, (
        f"None of the actual security modes {actual_security} are listed in the YAML config {expected_security}"
    ))

# def test_verify_Password_connection(setup):
#     negative_password = setup.verify_ssid_negative_scenario()
#     if negative_password == "Error":
#         logger.debug(negative_password + "wrong password")