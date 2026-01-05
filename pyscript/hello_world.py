@service
def hello_world():
    """A simple PyScript service that logs a message"""
    log.info("Hello from PyScript!")
    return "Hello World from PyScript!"