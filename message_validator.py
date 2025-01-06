import json
from .errors import InvalidMessageError

class MessageValidator:
    def validate_message(self, message):
        try:
            data = json.loads(message)
            if 'id' not in data or 'content' not in data or 'timestamp' not in data:
                raise InvalidMessageError("Missing required fields")
            return True
            else:
            raise InvalidMessageError("Invalid message format")
