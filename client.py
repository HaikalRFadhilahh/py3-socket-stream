import socket

host = input("Server ipv4 Socket Server : ")
port = int(input("Port Socket Server : "))

try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    m = client.recv(1024).decode("utf-8")
    print(m)
    while True:
        m = input().encode("utf-8")
        client.sendall(m)
        o = client.recv(1024).decode("utf-8")
        if o == "OK":
            continue
        else:
            print(o)
except socket.error as e:
    print(f"Connection Socket err : {e}")
except KeyboardInterrupt:
    client.close()
finally:
    client.close()
