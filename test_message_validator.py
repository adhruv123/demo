import pytest
from simulator.message_validator import MessageValidator
from simulator.errors import InvalidMessageError

@pytest.mark.parametrize("message, expected_result", [
    ('{"id": 1, "content": "Test", "timestamp": "2025-01-01"}', True),
    ('{"id": 1, "content": "Test"}', False),
    ('invalid_json', False)
])
def test_validate_message(message, expected_result, message_validator):
    if expected_result:
        assert message_validator.validate_message(message) == True
    else:
        with pytest.raises(InvalidMessageError):
            message_validator.validate_message(message)
