import socket
import json
from datetime import datetime

HOST = "127.0.0.1"
PORT = 123
CONFIG_PATH = "config.json"


def get_timeout_from_config(filename):
    with open(filename) as f:
        data = json.load(f)
        return data["timeout"]


def calculate_time(timeout):
    is_negative = False
    if timeout < 0:
        is_negative = True

    if is_negative:
        return datetime.now() - (datetime.fromtimestamp(abs(timeout)) - datetime.fromtimestamp(0))
    return datetime.now() + (datetime.fromtimestamp(timeout) - datetime.fromtimestamp(0))


def main():
    try:
        timeout = get_timeout_from_config(CONFIG_PATH)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((HOST, PORT))
        s.listen(4)
        print("Server works...")
        while True:
            conn, addr = s.accept()
            print("Connection from {0}".format(addr))
            conn.sendall(calculate_time(timeout).strftime("%H:%M:%S").encode())
            conn.shutdown(socket.SHUT_RDWR)
            conn.close()
    except Exception as err:
        print("Error: " + str(type(err)), end="")


if __name__ == "__main__":
    main()
