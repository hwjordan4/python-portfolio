__author__ = 'harrisonjordan'


from socket import socket
from Server1 import encoding, port

sock = socket()
sock2 = socket()
sock.connect(('127.0.0.1', port))

poly = {-5, 3, 0, 1}
a = 1
b = 2
tolerance = 0.001

message = 'S{} {} -5 3 0 1 {}'.format(a, b, tolerance)
print('To Server: ' + message)
bytes = message.encode(encoding)
sock.sendall(bytes)
sock.shutdown(1)

data_string = ""
bytes = sock.recv(2048)
while len(bytes) > 0:
    data_string += bytes.decode(encoding)
    bytes = sock.recv(2048)

sock.close()

print('From Server: ' + data_string)
x = float(data_string[1])
message = 'E{} -5 3 0 1'.format(x)
print('To Server: ' + message)

sock2.connect(('127.0.0.1', port))
bytes = message.encode(encoding)
sock2.sendall(bytes)
sock2.shutdown(1)

data_string = ''
bytes = sock2.recv(2048)
while len(bytes) > 0:
    data_string += bytes.decode(encoding)
    bytes = sock2.recv(2048)

print('Result: '+data_string)


sock2.close()