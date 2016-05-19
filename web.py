# Python modules
import socket

# The socket module has a class called 'socket' that has several methods
# that allows many actions such as sending and receiving data

# A server must perform the sequence socket(), bind(), listen(), accept()
# (possibly repeating the accept() to service more than one client),
# while a client only needs the sequence socket(), connect().
# Also note that the server does not sendall()/recv() on the socket
# it is listening on but on the new socket returned by accept()

# create a new instance of socket
s = socket.socket()


s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


print "binding..."

# The socket gets bound to an address, in this case localhost.
# The second parameter is the port for this socket to listen on to
# accept new connections.
s.bind(('', 10000))


print "listening on port 10000"

# Listen is the socket waiting for connection requests. The argument minimum
# passed to it is 0 which is maximum of one connection to the socket.
# In this case, 5 is the maximum number of connections this socket will accept.
s.listen(5)

# Counter to keep track of number of connections made to server
count = 0

while True:
    print "accepting..."

    # Once binding is set up, a server can than began accepting connections
    # When client  connects to the server, it return a tupal consisting of (conn, address).
    # Conn is the new socket to send and receive over, and address is what
    # address is bound to the socket on the other end such as "my_ipad_ip.com"
    c = s.accept()

    print "this is c", c
    print "connected!"
    count += 1

    # Set client equal to the first arg of the clients connection request,
    # which is the hostname/ip of the client
    client = c[0]

    request = ""
    while True:
        # Recv means receive data from the socket.
        # Data is being sent to the server by the client in the form a string.
        # The maximum amount of data to be received at once is optional, but
        # in this case, 10 bytes of data from the client is allowed at a time.
        data = client.recv(10)
        request += data
        print "this is data", data

        if "\r\n\r\n" in request:
            break

    print "request: ", request.split("\n")[0]

    print "responding..."
    response = """HTTP/1.1 200 OK\r
Server: Akyya Server\r
Content-Type: text/html\r
\r
<marquee>Akyya!</marquee>"""

    response += " " + str(count)

    # Sending to a remote client
    client.send(response)

    print "closing..."
    client.close()
# Close the server. No more data will be sent.
s.close()