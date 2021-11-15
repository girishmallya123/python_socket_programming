import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        # just send back the same data, but upper-cased
        msg = "Secret code not found"
        digits = ""
        count = 0
        if b'SECRET' in self.data:
            digits = [c for c in str(self.data) if c.isdigit()]
            msg = "Digits: {}, Count: {}".format("".join(digits), len(digits))

        self.request.sendall(bytes(msg, 'utf-8'))

if __name__ == "__main__":
    HOST, PORT = "localhost", 6666 

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()
