import pytest
import subprocess
import time
import yaml
from conftest import setup
from src.connection import execute_command
from src.logger import get_log_path
import logging

logger = logging.getLogger(__name__)


def test_iper3_throughput(setup):
    (sender, receiver), result = setup.client_server_module()

    print(f"Sender: {sender}, Receiver: {receiver}")

    if sender is None or receiver is None:
        print("Throughput parsing failed check iperf3 output")
        assert False, "Throughput parsing failed"

    assert sender > 1.0, f"Low sender throughput: {sender}"
    assert receiver > 1.0, f"Low receiver throughput: {receiver}"
