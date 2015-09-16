__author__ = 'Harrison Jordan'

from socket import socket
from polynomials import eval, bisection
#exportable resources

port = 12321
encoding = "utf-8"

if __name__ == '__main__':
    #server script

    listener = socket();
    listener.bind(('', port))
    listener.listen(1);

    while True:
        try:
            (conn, address) = listener.accept()
            ## we now have a connection
            # conn is a socket we can use to communicate
            #  address is the address of the client
            print("connection socket: ", conn)
            print("connection address: ", address)
            data_string = ""
            bytes = conn.recv(2048)
            while len(bytes) > 0:
                str = bytes.decode(encoding)
                data_string += str
                bytes = conn.recv(2048)


            print("received: |{}|".format(data_string))
            parts = []
            if data_string == '':
                messageToClient = 'Xempty request'
                print('To Client: "{}"'.format(messageToClient))
                bytes = messageToClient.encode(encoding)
                conn.sendall(bytes)
            else:
                try:
                    requestType = data_string[0]
                    data_string = data_string[1:len(data_string)]
                except Exception as e:
                    messageToClient = 'Xnot enough arguments'
                try:
                    parts = data_string.split(' ')
                    messageToClient = ''
                except Exception as e:
                    messageToClient = 'Xspacing in request wrong'

                # Evaluate Request
                if requestType == 'E':
                    if(len(parts) < 2):
                        messageToClient = 'Xnot enough arguments'
                    else:
                        try:
                            x = int(float(parts[0]))
                            parts = parts[1:]
                            poly = [int(float(x)) for x in parts]
                            evaluate = eval(x, poly)
                            messageToClient = 'E{}'.format(evaluate)
                        except Exception as e:
                            messageToClient = 'Xinvalid format numeric data'

                #Bisection Request
                if requestType == 'S':
                    if(len(parts) < 4):
                        messageToClient = 'Not enough arguments'
                    else:
                        try:
                            a = int(float(parts[0]))
                            b = int(float(parts[1]))
                            tol = float(parts[-1])
                            print('a: {} b: {} tol: {}'.format(a, b, tol))
                            poly = [int(float(x)) for x in parts[2:-1]]
                            bi = bisection(a,b,poly,tol)
                            messageToClient = 'S{}'.format(bi)
                        except Exception as e:
                           messageToClient = 'Xinvalid format numeric data'

                if requestType != 'E' and requestType != 'S' and len(data_string) > 1:
                    messageToClient = 'X unknown request'

                print('To Client: "{}"'.format(messageToClient))
                bytes = messageToClient.encode(encoding)
                conn.sendall(bytes)
        finally:
            conn.close()
