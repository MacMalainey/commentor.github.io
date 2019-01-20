import threading
import atexit
from flask import Flask

# Set number of running threads
THREAD_NUM = 5

def start_app():
    app = Flask(__name__)

    # Cancel background threads
    def interrupt():
        pass


start_app()