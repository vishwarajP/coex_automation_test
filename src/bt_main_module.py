import re
import subprocess
from src.connection import execute_command_BT
from src.logger import get_log_path
from dbm import error
# from pickletools import read_uint1
from re import findall, match
import logging

# from inspect import stack
# from traceback import print_tb

import yaml
import time

# from scapy.layers.eap import EAPOL
# from scapy.utils import rdpcap
# from test.test_vish import test_iper3_throughput

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class BT:
    def __init__(self):
        bt_config_path = r"C:\Users\Vishwaraj\automation\WLAN Testing\.venv\config\BT_config.yaml"
        with open(bt_config_path, "r") as f:
            bt_load = yaml.safe_load(f)
        self.mac_address = bt_load["BT"]["MAC Address"]

    @staticmethod
    def bt_off():
        execute_command_BT("sudo rfkill block bluetooth")
        output = execute_command_BT("hciconfig")
        bt_interface_check = re.search(r"\bDOWN\b" , str(output))
        if match:
            print("interface is down")
        else:
            print("interface is up or not found")
        return output

    @staticmethod
    def bt_on():
        execute_command_BT("sudo rfkill unblock bluetooth")
        check_bt_off = execute_command_BT("hciconfig")
        bt_interface_on=re.search(r"\bUP\b", str(check_bt_off))
        if match:
            print("interface is UP")
        else:
            print("interface is Down or not found")
        return check_bt_off


    def bt_pair_device(self):
        mac = self.mac_address
        btctl_script = f"""
    power on
    agent on
    default-agent
    scan on
    trust {mac}
    pair {mac}
    connect {mac}
    exit
    """
        # Use echo to pipe into bluetoothctl
        btctl_command = f"echo '{btctl_script}' | bluetoothctl"
        result = execute_command_BT(btctl_command)
        return result , "divice is paired"


    def verify_bt_deviec(self):
        mac = self.mac_address
        execute_command_BT("exit")
        result = execute_command_BT(f"bluetoothctl info {mac}")
        if isinstance(result, tuple):  # Example: (stdout, stderr)
            output = result[0]
        else:
            output = result

        output_str = str(output).lower()
        if "connected: yes" in output_str:
            print("device is connected")
            return output_str , "device is connected"
        else:
            print("device is not connected")
            return False

    @staticmethod
    def check_A2dp():
        run_a2dp = execute_command_BT("( mplayer -slave -quiet /home/admin/bensound-sunny.mp3 )")
        return run_a2dp , "audio working fine"


# obj1 = main()
# print(obj1.client_server_module())

obj1 = BT()
time.sleep(1)
obj1.bt_off()
time.sleep(2)
obj1.bt_on()
time.sleep(2)
obj1.bt_pair_device()
time.sleep(2)
obj1.verify_bt_deviec()
time.sleep(2)
obj1.check_A2dp()
