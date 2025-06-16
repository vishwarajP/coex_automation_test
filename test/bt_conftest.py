import pytest
from src.bt_main_module import BT
import yaml
from src.logger import *
# from pathlib import Path
# from Lib.stability_module import stability



@pytest.fixture(scope="function", autouse=True)
def setup():
    set_up = BT()
    print("iperf before running set-up")
    yield set_up
    print("iperf after running teardown")

