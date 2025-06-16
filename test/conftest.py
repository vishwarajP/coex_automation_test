import pytest
from src.wlan_main_module import WLAN
import yaml
from src.logger import *
# from pathlib import Path
# from Lib.stability_module import stability



@pytest.fixture(scope="function", autouse=True)
def setup():
    set_up = WLAN()
    print("iperf before running set-up")
    yield set_up
    print("iperf after running teardown")


