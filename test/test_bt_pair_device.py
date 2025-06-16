import pytest
import subprocess
import time
import yaml
from bt_conftest import setup
from src.connection import execute_command_BT
from src.logger import get_log_path
import logging


def test_bt_device_paired(setup):
    setup = setup.bt_pair_device()
    logging.debug("divice is paired" in setup)


def test_bt_device_connected(setup):
    setup = setup.verify_bt_deviec()
    logging.debug("device is connected" in setup)