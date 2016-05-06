import socket

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

print "binding..."
s.bind(('127.0.0.1', 10000))


print "listening..."
s.listen(0)

count = 0

while True:
    print "accepting..."
    c = s.accept()
    print "connected!"
    count += 1

    client = c[0]
    request = ""
    while True:
        data = client.recv(10)
        request += data

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
    
    client.send(response)

    print "closing..."
    client.close()
s.close()