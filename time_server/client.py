import socket
import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("host")
    parser.add_argument("port", type=int)
    return parser.parse_args()


def main():
    args = parse_args()
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((args.host, args.port))
        buf = s.recv(1024).decode("utf-8")
        print(buf, end="")
    except Exception as err:
        print("Error: " + str(type(err)), end="")


if __name__ == "__main__":
    main()
