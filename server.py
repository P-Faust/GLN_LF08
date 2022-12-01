import computer, socket, psutil, platform

class Server(computer.Computer):
    _service = ""
    __sockIp = ""
    __sockPort = 0

    def __init__(self,power_supply, cpu, cpu_speed,ram,os,ip,service):
        super().__init__(power_supply, cpu, cpu_speed,ram,os,ip)
        self._service = service
        
    def createSocket(self, sockIP,sockPort):
        self.__sockIp = sockIP
        self.__sockPort = sockPort
        print(f"Socket IP: {(str(self.__sockIp))}\nPort: {self.__sockPort}")

    def runningServer(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.__sockIp,self.__sockPort))
            s.listen()
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    conn.sendall(data)
    
myServer = Server("750W", platform.processor(), psutil.cpu_freq().max, psutil.virtual_memory().total, platform.system(), socket.gethostbyname(socket.gethostname()), "File Server")
myServer.getInfo()
print(f"Service: {myServer._service}")
myServer.createSocket("127.0.0.1", 6420)
myServer.runningServer()