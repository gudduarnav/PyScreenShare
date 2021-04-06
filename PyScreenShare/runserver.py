try:
    from waitress import serve
except ImportError as exWaitress:
    print("Install waitress. Exception:", str(exWaitress))

import socket
import server as app

class Server:
    def __init__(self):
        self.app = app.app
        self.ip = "0.0.0.0"
        self.port = 8081

        self.listallurl()

        self.sockets = [
            socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ]
        self.sockets[0].bind((self.ip, self.port))
        serve(self.app, sockets=self.sockets)

    def __del__(self):
        for socket1 in self.sockets:
            socket1.close()


    def listallurl(self):
        iplist = list()
        iplist.append("127.0.0.1")

        try:
            hostname = socket.gethostname()
            print("HOSTNAME:", hostname)
            hostip = socket.gethostbyname_ex(hostname)[2]
            for hostip1 in hostip:
                iplist.append(hostip1)
        except Exception as ex:
            print("Exception looking up IP for this host:", str(ex))

        for iplist1 in iplist:
            print("URL: http://{}:{}".format(iplist1, self.port) )

def main():
    Server()


if __name__=="__main__":
    main()
