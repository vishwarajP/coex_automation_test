import pytest
from src.connection import execute_command_BT
from src.logger import get_log_path
from src.bt_main_module import BT
from bt_conftest import setup
import yaml


def test_A2dp(setup):
    setup = setup.check_A2dp()
    assert "audio working fine" in setup