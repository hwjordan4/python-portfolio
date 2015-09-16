__author__ = 'student'


from socket import socket

def server_port():
    return 12345

encoding = 'UTF-8'

def binom(n,m):
    b = 1
    for i in range(0,m):
        b = b * (n-i) // (i+1)
    return b


if __name__ == "__main__":

    # setting up a listener socket
    sock = socket()   # this is how you create a new object,
    sock.bind(('', server_port()))
        #  ('', server_port())  is the socket 'address'
        # ''  is the host, which is all possible addresses
        # server_port() is the port number, 12345
    sock.listen(0)  # 0 backlog of connections




    while True:
        (conn, address) = sock.accept()
        print("connection made ", conn)
        print(address)

        # conn is a socket that will be used to communicate with the client

        # get data from client (request)
        data_string = ""
        bytes = conn.recv(2048)
        while len(bytes) > 0:
            # we actually got data from the client
            bytes_str = bytes.decode(encoding)
            print("data received: |{}|".format(bytes_str))
            data_string += bytes_str
            bytes = conn.recv(2048)

        print("all data received: " + data_string)

        #(n,m) = data_string.split(' ')
        #print("n is {} and m is {}".format(n,m))

        values = data_string.split(' ')
        print("values: ", values)
        if len(values) == 2:
            n = values[0]
            m = values[1]
        else:
            n = 0
            m = 0
            print("Invalid request syntax")
            # error condition ????

        print("n is {} and m is {}".format(n,m))

        n = int(n)   # check this for errors!
        m = int(m)   # check for errors

        ## Check that 0 <= m <= n

        # compute
        b = binom(n,m)

        # send result to client (response)
        conn.sendall(str(b).encode(encoding))
        conn.shutdown(1)  ## shutdown the sending side


        conn.close()
        print("connection closed")
