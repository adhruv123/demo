import pyserial
from .errors import SerialPortError
import json

class SerialHandler:
    def __init__(self):
        self.port = None

    def open_port(self, port_name, baud_rate):
        try:
            self.port = pyserial.Serial(port_name, baud_rate)
        except Exception as e:
            raise SerialPortError(f"Error opening port {port_name}: {e}")

    def send_message(self, message):
        if not self.port or not self.port.is_open:
            raise SerialPortError("Port not open")
        self.port.write(message.encode())

    def receive_message(self):
        if not self.port or not self.port.is_open:
            raise SerialPortError("Port not open")
        return self.port.readline().decode()

    def close_port(self):
        if self.port:
            self.port.close()
