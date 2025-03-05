import signal
import sys
from types import FrameType
"""
    - Make this the single hub to emit errors for the program
    - different modules will import this to send different types of errors
    - there should be a generic exception type, a logger, and specific error types
"""
# signal.signal(signal, EOF_handler)
class FileNotFoundError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

# Signal handler
def sigint_handler(signal: int, frame: FrameType | None) -> None:
    print('Keyboard Interrupt')

def EOF_handler(signal: int, frame: FrameType | None) -> None:
    sys.exit(0)

# Register Signal
signal.signal(signal.SIGINT, sigint_handler)

class ExceptionHandler:
    def __init__(self): # include all signal handlers in here
        pass
