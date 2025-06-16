import re
import subprocess
from src.connection import execute_command
from src.logger import get_log_path
from dbm import error
# from pickletools import read_uint1
from re import findall
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


class WLAN:
    def __init__(self):
        pass

    """
    This function module will check the client and server connection and thoughput using 
    iper3 tool
    """

    # def client_server_module(self):
    #     client = execute_command("iperf3 -R -c 192.168.3.63 -t 5 i 1 -p 5203")
    #     client_str = str(client)
    #     matches = re.findall(r"\[ *\d+\] +0\.00-\d+\.\d+ +sec +[\d\.]+ +GBytes +(\d+\.\d+) +Gbits/sec" , client_str)
    #     # matches = re.findall(r"(\d+\.\d+)\s+Gbits/sec", client_str)
    #     # return obj , client
    #     if len(matches) == 2:
    #         sender_throughput = matches[0]
    #         receiver_throughput = matches[1]
    #         sender_float = float(sender_throughput)
    #         receiver_float = float(receiver_throughput)
    #         return (sender_float, receiver_float), client
    #     else:
    #         logger.error("Could not parse sender/receiver throughput from iperf3 output.")
    #         logger.debug(f"Raw iperf3 output:\n{client_str}")
    #         logger.debug(f"Regex matches found: {matches}")
    #         return (None, None), client
    # print("Could not parse sender/receiver throughput from iperf3 output:")
    # print(client_str)
    # return (None, None), client
    @staticmethod
    def client_server_module():
        config_path = r"C:\Users\Vishwaraj\automation\WLAN Testing\.venv\config\test_config.yaml"
        with open(config_path, "r") as f:
            d = yaml.safe_load(f)
            wifi_ip = d["wifi"]["ip"]
        client = execute_command(f"iperf3 -R -c {wifi_ip} -t 5 -i 1 -p 5203")
        client_str = str(client)

        logger.debug(f"Raw iperf3 output:\n{client_str}")

        matches = re.findall(r"(\d+\.\d+)\s+Gbits/sec", client_str)

        if len(matches) >= 2:
            sender_throughput = matches[-2]
            receiver_throughput = matches[-1]
            return (float(sender_throughput), float(receiver_throughput)), client
        else:
            logger.error("Could not parse sender/receiver throughput from iperf3 output.")
            logger.debug(f"Regex matches found: {matches}")
            return (None, None), client

    """
    This below function menthod will set to collect pcap logs set wlan1 down and up
    and set in monitor mode
    """
    # def set_wlan1_down(self,interface):
    #     down = execute_command(f"sudo ip link set {interface} down")
    #     return down
    #
    # def enbale_monitor_mode(self,interface):
    #     monitor=execute_command(f"sudo iw {interface} set monitor control")
    #     return monitor
    #
    # def set_wlan1_up(self,interface):
    #     up = execute_command(f"sudo ip link set {interface} up")
    #     return up
    #
    # def set_wlan1_channel(self,interface , channel):
    #     chan = execute_command(f"sudo iw {interface} set channel {channel}")
    #     return chan

    """
    start tcpdump is to collect the pcap file with time using this we parse the file
    """

    # def start_tcpdump(self, interface ,out_file , duration):
    #     execute_command(f"sudo timeout {duration} tcpdump -i {interface} -s 0 -w {out_file}")
    # #
    # def find_eapol_packets(self,pcap_file):
    #     packets = rdpcap(pcap_file)
    #     eapol_packets = [pkt for pkt in packets if pkt.haslayer(EAPOL)]
    #     return len(eapol_packets)

    """
    connectity check is the method will check the ping session and check stability of platform
    using packet loss and received packets
    """

    @staticmethod
    def check_ip():
        test_config_path = r"C:\Users\Vishwaraj\automation\WLAN Testing\.venv\config\test_config.yaml"
        with open(test_config_path, "r") as f:
            g = yaml.safe_load(f)
            ip = g["server"]["ip"]
        cmd = f"ping -c 10 -w 2 {ip}"
        ping = execute_command(cmd)
        match = re.search(r'(\d+) packets transmitted, (\d+) received, (\d+)% packet loss', str(ping))
        if match:
            packet_loss = float(match.group(3))
            return packet_loss
        else:
            return -1

    #     return match
    #
    # def udp_stream(self, interface, out_file, duration):
    #     udp = execute_command(f"sudo timeout {duration} udpdump -i {interface} -s 0 -w {out_file}")
    #     return udp

    @staticmethod
    def connect_to_wifi():
        test_config_path = r"C:\Users\Vishwaraj\automation\WLAN Testing\.venv\config\test_config.yaml"
        with open(test_config_path, "r") as f:
            g = yaml.safe_load(f)
            ssid = g["wifi"]["ssid"]
            password = g["wifi"]["password"]
        cmd = f"sudo nmcli device wifi connect {ssid} password {password}"
        f = execute_command(cmd)
        return f

    @staticmethod
    def is_connected():
        test_config_path = r"C:\Users\Vishwaraj\automation\WLAN Testing\.venv\config\test_config.yaml"
        with open(test_config_path, "r") as f:
            g = yaml.safe_load(f)
            ssid = g["wifi"]["ssid"].strip()
            expected_security = g["wifi"].get("security", "").strip().upper()
            print(expected_security)
        result = execute_command("sudo iwgetid -r")
        actual_ssid = result[0].strip() if result and result[0] else ""
        sec_result = execute_command("nmcli -f active,ssid,security dev wifi")
        security_mode = None
        for line in sec_result[0].splitlines():
            if line.strip().startswith("yes") and ssid in line:
                parts = line.strip().split()
                if len(parts) >= 3:
                    security_mode = parts[2]
                break
        print(f"Connected to: {actual_ssid} | Security: {security_mode}")
        return actual_ssid
        # print(actual_ssid)
        # return actual_ssid == ssid

    @staticmethod
    def verify_ssid():
        test_config_path = r"C:\Users\Vishwaraj\automation\WLAN Testing\.venv\config\test_config.yaml"
        with open(test_config_path, "r") as f:
            g = yaml.safe_load(f)
            ssid = g["wifi"]["ssid"].strip()
            print(ssid)
        return ssid

    @staticmethod
    def verify_security():
        test_config_path = r"C:\Users\Vishwaraj\automation\WLAN Testing\.venv\config\test_config.yaml"
        with open(test_config_path, "r") as f:
            g = yaml.safe_load(f)
            ssid = g["wifi"]["ssid"].strip()
            expected_security = g["wifi"].get("security", "").strip().upper()
        sec_result = execute_command("nmcli -f active,ssid,security dev wifi")
        security_mode = None
        for line in sec_result[0].splitlines():
            if line.strip().startswith("yes") and ssid in line:
                parts = line.strip().split()
                if len(parts) >= 3:
                    security_mode = parts[2]
                break
        print(f"Security: {security_mode}")
        if security_mode:
            return [mode.strip().lower() for mode in security_mode.split(',')]
        return []

    @staticmethod
    def verify_security_config():
        test_config_path = r"C:\Users\Vishwaraj\automation\WLAN Testing\.venv\config\test_config.yaml"
        with open(test_config_path, "r") as f:
            g = yaml.safe_load(f)
            security_modes = g["wifi"].get("security_modes", "")
            print(security_modes)
        return [mode.lower() for mode in security_modes]

    #
    # def verify_ssid_negative_scenario(self):
    #     test_config_path = r"C:\Users\Vishwaraj\automation\WLAN Testing\.venv\config\test_config.yaml"
    #     with open(test_config_path, "r") as f:
    #         g = yaml.safe_load(f)
    #         ssid = g["wifi"]["ssid"]
    #         password = g["wifiwrong_password"]["password"]
    #         cmd = f"sudo nmcli device wifi connect {ssid} password {password}"
    #         f = execute_command(cmd)
    #         d = "".join(f)
    #         r = re.findall("Error",d)
    #         return r




obj1 = WLAN()
obj1.connect_to_wifi()
obj1.is_connected()
obj1.verify_ssid()
obj1.verify_security()
obj1.verify_security_config()
(sender, receiver), raw_output = obj1.client_server_module()
if sender and receiver:
    print(f"Sender: {sender} Gbits/sec, Receiver: {receiver} Gbits/sec")
else:
    print("Throughput values not found. Check output and regex.")



# obj1.verify_ssid_negative_scenario()