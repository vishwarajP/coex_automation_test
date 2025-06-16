from traceback import print_tb

import paramiko
import yaml
import subprocess

"""
we are connecting resberry PI through SSH connection,
Purpose of the SSH connect is automaticly execute the commands

"""

server_path = r"C:\Users\Vishwaraj\automation\coaex_automation\config\wlan_config_client.yaml"

with open(server_path, "r") as f:
    g = yaml.safe_load(f)
server_host = g["server"]["ip"]
server_user = g["server"]["user"]
server_password = g["server"]["password"]

# client_path = r"C:\Users\Vishwaraj\automation\WLAN Testing\.venv\config\test_config_client.yaml"
#
# with open(client_path , "r") as f1:
#     g1 = yaml.safe_load(f1)
# client_host = g1["client"]["ip"]
# client_user = g1["client"]["user"]
# client_password = g1["client"]["password"]

BT_path = r"C:\Users\Vishwaraj\automation\coaex_automation\config\BT_device_config.yaml"

with open(BT_path, "r") as f1:
    blue_config = yaml.safe_load(f1)
BT_client_host = blue_config["client"]["ip"]
BT_client_user = blue_config["client"]["user"]
BT_client_password = blue_config["client"]["password"]


def execute_command(cmd):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=server_host, username=server_user, password=server_password)

    stdin, stdout, stderr = ssh.exec_command(cmd)
    out = stdout.read().decode()
    err = stderr.read().decode()
    ssh.close()
    return out, err


def execute_command_BT(cmd):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=BT_client_host, username=BT_client_user, password=BT_client_password)

    stdin, stdout, stderr = ssh.exec_command(cmd)
    out = stdout.read().decode()
    err = stderr.read().decode()
    ssh.close()
    return out, err


# def wlan_connected(interface="wlan0"):
#     result = subprocess.run(["ifconfig" ,interface],capture_output=True)
#     return "mirafra" in result.stdout.decode()


p = execute_command("sudo iwconfig")
p2 = execute_command("iperf3 -s -p 5203")
p3 = execute_command_BT("hciconfig")

print(p3)
print("Client output:", p)
print("server output", p2)
