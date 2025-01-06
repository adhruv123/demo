import pytest
from mock import Mock  # Simple mock
from simulator.serial_handler import SerialHandler
from simulator.errors import SerialPortError

# Fixture to create a mock serial port
@pytest.fixture
def mock_serial_port():
    # Create a simple mock for the serial port object
    mock_port = Mock()
    mock_port.is_open = True  # Simulate the port being open
    return mock_port

def test_open_port(mock_serial_port):
    # Create a SerialHandler instance
    serial_handler = SerialHandler()
    
    # Simulate opening the port by replacing the 'open_port' method with a mock
    SerialMock = Mock(return_value=mock_serial_port)
    
    # Open the port using the mock
    serial_handler.open_port = SerialMock
    
    # Invoke open_port and check the mock was called with the correct arguments
    serial_handler.open_port("COM1", 9600)
    
    # Verify that the mock serial port was opened with the correct parameters
    SerialMock.assert_called_once_with("COM1", 9600)
    assert serial_handler.port == mock_serial_port  # Ensure the port is set to the mock

def test_send_message(mock_serial_port):
    serial_handler = SerialHandler()
    serial_handler.port = mock_serial_port  # Use the mock port
    
    # Send a message using the mock port
    serial_handler.send_message("Test message")
    
    # Verify the mock port's write method was called with the expected data
    mock_serial_port.write.assert_called_once_with(b"Test message")

def test_receive_message(mock_serial_port):
    serial_handler = SerialHandler()
    serial_handler.port = mock_serial_port  # Use the mock port

    # Simulate receiving a message by setting the return value of readline
    mock_serial_port.readline.return_value = b"Received message"

    # Call the receive_message method and check that it returns the expected message
    message = serial_handler.receive_message()
    
    # Assert that the correct message was returned
    assert message == "Received message"
    mock_serial_port.readline.assert_called_once()

def test_close_port(mock_serial_port):
    serial_handler = SerialHandler()
    serial_handler.port = mock_serial_port  # Use the mock port
    
    # Close the port and verify that the close method was called
    serial_handler.close_port()
    mock_serial_port.close.assert_called_once()

def test_send_message_when_port_is_not_open(mock_serial_port):
    serial_handler = SerialHandler()
    
    # Simulate that the port is not open by setting it to None
    serial_handler.port = None
    
    # Test that sending a message raises an error when the port is not open
    with pytest.raises(SerialPortError):
        serial_handler.send_message("Test message")
