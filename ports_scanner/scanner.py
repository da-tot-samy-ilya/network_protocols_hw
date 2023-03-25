import socket
import threading
import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("ip")
    parser.add_argument("left", type=int)
    parser.add_argument("right", type=int)
    return parser.parse_args()


def ports_scan(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((host, port))
        if result == 0:
            print(f"{port}/TCP OPEN")
        s.close()
    except Exception as e:
        print(f"ERROR: {e}")


def main():
    args = parse_args()

    for i in range(args.left, args.right + 1):
        # ports_scan(args.ip, i)
        t = threading.Thread(target=ports_scan, args=(args.ip, i))
        t.start()


if __name__ == '__main__':
    main()
