import socket

HOST, PORT = '', 80

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(3)
print 'Serving HTTP on port %s ...' % PORT
i=0
while True:
    print i,'Serving HTTP on port %s ...' % PORT
    client_connection, client_address = listen_socket.accept()
    try:
        request = client_connection.recv(1024)
    except:
        print "connection reset.."
    print request
    with open("output.txt","a") as file_handle:
        file_handle.write(request)
    i=i+1
    with open("inputadollarsign.txt") as file_handle:
        http_response = file_handle.read()

    try:
        client_connection.sendall(http_response+" "+str(i))
    except:
        print "sendall failed..."
    try:
        client_connection.close()
    except:
        print "cookies are for closers."
        