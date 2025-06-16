import logging
import subprocess
import time
import yaml
import pytest


# from src.connection import execute_command
# from src.logger import get_log_path
from conftest import setup

logger = logging.getLogger(__name__)


def test_connectivity_ping(setup):
    ping = setup.check_ip()
    # logging.info(f"Packets loss: {ping:.2f}%")
    logger.debug(ping < 1.0, f"packet loss :{ping:.2f}%")

# def test_udp_steam(setup):
#     udp = setup.udp_stream()
#     assert udp<2 , f"packet loss:{upd:.2f}%"
