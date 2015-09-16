__author__ = 'student'

from socket import socket
from version1.server import server_port, encoding


if __name__ == "__main__":
    sock = socket()
    sock.connect(('127.0.0.1', server_port()))
    print("Connection made")

    n = 200
    m = -3

    nstr = str(n)
    nencoded = nstr.encode(encoding)  # this is a byte string
    sock.sendall(nencoded)
    sock.sendall(' '.encode(encoding))
    sock.sendall(str(m).encode(encoding))

    sock.shutdown(1)   # shutdown the sending side of the socket

    response_str = ""
    bytes = sock.recv(2048)
    while len(bytes) > 0:
        response_str += bytes.decode(encoding)
        #print("response str", response_str)
        bytes = sock.recv(2048)

    print("Response: ", response_str)

    sock.close()
