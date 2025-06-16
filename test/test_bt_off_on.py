import pytest
import subprocess
import time
import yaml
from bt_conftest import setup
from src.connection import execute_command_BT
from src.logger import get_log_path
import logging



def test_bt_off(setup):
    result = setup.bt_off()
    assert result

def test_bt_on(setup):
    result = setup.bt_on()
    assert result

