from simulator.serial_handler import SerialHandler
from simulator.message_validator import MessageValidator
from simulator.logger import Logger
from simulator.errors import SerialPortError, InvalidMessageError
import json
import time

def run_simulation():
    # Create instances of the required classes
    serial_handler = SerialHandler()
    message_validator = MessageValidator()
    logger = Logger()

    try:
        # Open the serial port (for example, COM1 at 9600 baud)
        serial_handler.open_port("COM1", 9600)
        print("Port opened successfully.")

        # Example message to send (must be a valid JSON string)
        message = {
            "id": 1,
            "content": "Hello, this is a test message.",
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        # Convert message to JSON format
        message_json = json.dumps(message)

        # Validate the message
        if message_validator.validate_message(message_json):
            print("Message is valid.")

            # Log the sent message
            logger.log_message("send", message_json)

            # Send the message
            serial_handler.send_message(message_json)
            print("Message sent.")

            # Simulate receiving a message (for demo purposes)
            received_message = serial_handler.receive_message()
            print(f"Received message: {received_message}")

            # Log the received message
            logger.log_message("receive", received_message)
        else:
            print("Message is invalid.")

    except (SerialPortError, InvalidMessageError) as e:
        # Handle errors (either serial port or invalid message)
        print(f"Error occurred: {str(e)}")
    finally:
        # Close the port after the simulation
        serial_handler.close_port()
        print("Port closed.")

if __name__ == "__main__":
    run_simulation()
