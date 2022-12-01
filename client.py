import computer, socket, psutil, platform
class Client(computer.Computer):
    __remoteIP = ""
    __remotePort = 0

    def createSocket(self, remoteIP, remotePort):
        self.__remoteIP = remoteIP
        self.__remotePort = remotePort
        print("")
    
    def sendData(self,msg):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.__remoteIP, self.__remotePort))
            s.sendall(b"Hallo Server")
            data = s.recv(1024)

        print(f"Received {data!r}")

myClient = Client("750W", platform.processor(), psutil.cpu_freq().max, psutil.virtual_memory().total, platform.system(), socket.gethostbyname(socket.gethostname()))
myClient.createSocket("127.0.0.1", 6420)
myClient.sendData("Nachricht kommt an")
